# ac7renamer PySide6 migration — design

Date: 2026-05-14

## Goal

Migrate ac7renamer from PyQt5 to PySide6 and modernize the project structure
without changing the visible behavior of the application. The end state is a
PySide6 desktop app installable from `pyproject.toml`, with filesystem-based
images, a minimal pytest suite for non-UI logic, and a reproducible
development workflow on Windows and Linux.

## Non-goals

- No UI redesign. The .ui file's layout is unchanged.
- No new features (e.g. no new tabs, dialogs, or file format support).
- No CI setup. Tests run locally with `pytest`; CI is out of scope.
- No macOS build instructions. The README continues to say "patches welcome."
- No publishing of ac7renamer or ac7parser to PyPI. Dependencies are git URLs.

## Strategy

Two-phase migration on a `pyside6-migration` branch off `master`:

1. **Phase 1 — Mechanical port.** Smallest possible diff that makes the app
   run on PySide6 unchanged. One commit.
2. **Phase 2 — Modernize.** Filesystem resources, `pyproject.toml`, tests,
   cleanup, cross-platform build script, refreshed README. One commit, built
   on top of Phase 1.

Two commits give a clean bisect point if a regression is found after merging.

## Phase 1 — Mechanical port

### Per-file changes

- `ReStyle.py` — unchanged.
- `ac7renamer/ac7renamer.py` — swap `from PyQt5 import QtWidgets` to
  `from PySide6 import QtWidgets`. Change `app.exec_()` to `app.exec()`.
- `ac7renamer/myrenamerdlg.py` — swap PyQt5 imports to PySide6. Change
  `msg.exec_()` to `msg.exec()`. Resource paths `:/icons/images/...` stay
  unchanged (still resolved by `imageresources_rc`).
- `ac7renamer/singlefiletab.py` — swap imports. Replace `QRegExp` with
  `QRegularExpression` (from `QtCore`) and `QRegExpValidator` with
  `QRegularExpressionValidator` (from `QtGui`). Change `msg.exec_()` to
  `msg.exec()`.
- `ac7renamer/multifiletab.py` — swap imports. Change `msg.exec_()` to
  `msg.exec()`.
- `ac7renamer/multifilemodel.py` — swap imports.
- `ac7renamer/ac7renamerdlg.py` — regenerated with
  `pyside6-uic ac7renamer/ac7renamerdlg.ui -o ac7renamer/ac7renamerdlg.py`.
- `ac7renamer/imageresources_rc.py` — regenerated with
  `pyside6-rcc ac7renamer/imageresources.qrc -o ac7renamer/imageresources_rc.py`.
  (PySide6's rcc emits a different format than PyQt5's pyrcc5.)
- `ac7renamer/buildstep.sh` — update to call `pyside6-uic` and
  `pyside6-rcc`. (Will be replaced by `build.py` in Phase 2.)
- `setup.py` — temporarily change `"PyQt5"` to `"PySide6"` in
  `install_requires`. (Will be deleted in Phase 2.)
- `README.md` — temporary `pip install PySide6`/`pyside6-uic` references.
  (Will be rewritten in Phase 2.)

### Enum tightening

PySide6 still accepts un-scoped enum forms (`Qt.Checked`, `QMessageBox.Information`,
`QFileDialog.DontUseNativeDialog`, `QSizePolicy.Expanding`). Phase 1 leaves
these as-is to minimize diff. Phase 2 tightens them to Qt6 scoped form.

### Phase 1 acceptance

Manual smoke test:
- App launches.
- About dialog opens, logo image renders.
- Splash screen appears on startup, dismisses after ~1.5s.
- Single-file tab: load an .AC7 file, rename it, reorder elements, save it.
  Output file loads correctly in a fresh app run.
- Multi-file tab: load a folder, select/deselect/invert, batch rename to a
  destination folder, rhythm-split a 6-element file to two 12-element files.

## Phase 2 — Modernize

### Filesystem-based image resources

Delete `imageresources.qrc` and `imageresources_rc.py`. Add
`ac7renamer/resources.py`:

```python
from importlib.resources import files

def image_path(name: str) -> str:
    return str(files("ac7renamer").joinpath("images", name))
```

Replace `QPixmap(":/icons/images/restyle_logo.png")` and the splash logo
reference with `QPixmap(resources.image_path("restyle_logo.png"))` and
`QPixmap(resources.image_path("restyle_logo_whitebg.png"))` in
`myrenamerdlg.py`.

The window icon currently lives in the generated `ac7renamerdlg.py` via
the `.ui` file. Remove the icon attribute from `ac7renamerdlg.ui` (in Qt
Designer or by editing the XML directly), and set it in code after
`setupUi`:

```python
from PySide6.QtGui import QIcon
ac7_renamer.setWindowIcon(QIcon(resources.image_path("restyle_icon.png")))
```

After regenerating `ac7renamerdlg.py` with `pyside6-uic`, verify it no
longer contains `from . import imageresources_rc` (it should not, since
the .qrc reference was removed from the .ui).

### pyproject.toml replaces setup.py

Delete `setup.py`. Create `pyproject.toml` at repo root:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "ac7renamer"
version = "0.1.0"
description = "Change display name of AC7 files."
authors = [{ name = "shiihs" }]
license = { text = "GPL-3.0-or-later" }
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "PySide6>=6.6",
    "ac7parser @ git+https://github.com/shimpe/ac7parser.git@7cb306b0d4b901dcf7a6ead0e4c639b4140df4cb",
]

[project.optional-dependencies]
dev = ["pytest>=7"]
build = ["pyinstaller>=6"]

[project.scripts]
ac7renamer = "ac7renamer.ac7renamer:main"

[tool.hatch.build.targets.wheel]
packages = ["ac7renamer"]

[tool.hatch.build]
include = ["ac7renamer/images/*.png", "ac7renamer/*.ui"]
```

The pinned ac7parser sha (`7cb306b0d4b901dcf7a6ead0e4c639b4140df4cb`) is the
current `HEAD` of the local `ac7parser` clone at migration time.

### Reproducible installs

Commit a `requirements.lock` file generated from `pyproject.toml` with
`pip-compile` (from pip-tools):

```
pip install pip-tools
pip-compile pyproject.toml -o requirements.lock --extra dev --extra build
```

The lock is a flat pinned `name==version` file. Users who want floating
versions run `pip install -e .[dev,build]`; users who want exact tested
versions run `pip install -r requirements.lock`. The maintainer regenerates
the lock when bumping dependencies.

### Code cleanup

- `singlefiletab.py`: collapse the 12 hardcoded `self.parent.desEl{N}`
  references into a loop:
  ```python
  self.combos_in_file_order = [
      getattr(self.parent, f"desEl{i+1}") for i in range(12)
  ]
  ```
- Delete the empty `def reject(self): pass` and its
  `Buttons.rejected.connect(self.reject)` wiring in `singlefiletab.py`.
  The generated UI already wires `Buttons.rejected.connect(Ac7Renamer.reject)`
  for the dialog itself.
- Tighten Qt6 enum usage across all modules:
  - `Qt.Checked` → `Qt.CheckState.Checked`
  - `Qt.Unchecked` → `Qt.CheckState.Unchecked`
  - `Qt.RichText` → `Qt.TextFormat.RichText`
  - `QMessageBox.Information` → `QMessageBox.Icon.Information`
  - `QMessageBox.Warning` → `QMessageBox.Icon.Warning`
  - `QMessageBox.Ok` → `QMessageBox.StandardButton.Ok`
  - `QFileDialog.DontUseNativeDialog` → `QFileDialog.Option.DontUseNativeDialog`
  - `QFileDialog.ShowDirsOnly` → `QFileDialog.Option.ShowDirsOnly`
- Add type hints to public method signatures across the modules (e.g.
  `def setup_slots(self, homefolder: str) -> None`). Internals stay
  untyped.

### Cross-platform build script

Replace `ac7renamer/buildstep.sh` with `build.py` at repo root:

```python
"""Regenerate ac7renamerdlg.py from the .ui file.

Run after editing ac7renamer/ac7renamerdlg.ui in Qt Designer.
"""
import subprocess
import sys
from pathlib import Path

PKG = Path(__file__).parent / "ac7renamer"

def main() -> None:
    subprocess.run(
        [sys.executable, "-m", "PySide6.scripts.pyside_tool", "uic",
         str(PKG / "ac7renamerdlg.ui"),
         "-o", str(PKG / "ac7renamerdlg.py")],
        check=True,
    )

if __name__ == "__main__":
    main()
```

Runs on Windows and Linux from any venv that has PySide6 installed. No
`.qrc` step (the .qrc was deleted in this phase).

### README rewrite

Rewrite `README.md` with these sections:

1. **What it is** — one short paragraph: GPLv3 charityware tool for Casio
   .AC7 rhythm display names.
2. **Development setup (Windows / Linux)** — create venv, activate,
   `pip install -e .[dev,build]`, run `python ReStyle.py`, run `pytest`.
   Requires Python 3.10+ and git.
3. **Working on ac7parser alongside ac7renamer** — explain editable install:
   `git clone https://github.com/shimpe/ac7parser.git ../ac7parser` then
   `pip install -e ../ac7parser`. Note that this shadows the installed copy
   so edits and debugger step-in target the working tree.
4. **Reproducing a known-good environment** — `pip install -r requirements.lock`
   for exact versions; instructions for regenerating the lock.
5. **Regenerating the UI** — `python build.py` after editing
   `ac7renamer/ac7renamerdlg.ui`.
6. **Building a standalone executable** — see PyInstaller section below.
7. **macOS** — "patches welcome" note unchanged.

### PyInstaller

The `pyinstaller/` directory and overall workflow stay. The build command
updates to bundle the now-plain image and .ui files:

```
# Windows
pyinstaller ..\ReStyle.py -F ^
  --add-data "..\ac7renamer\images;ac7renamer\images" ^
  --add-data "..\ac7renamer\ac7renamerdlg.ui;ac7renamer"

# Linux
pyinstaller ../ReStyle.py -F \
  --add-data "../ac7renamer/images:ac7renamer/images" \
  --add-data "../ac7renamer/ac7renamerdlg.ui:ac7renamer"
```

PySide6 hooks ship via `pyinstaller-hooks-contrib`, which pip installs as
a transitive dependency of pyinstaller — no manual hook required.

## Tests

A small pytest suite under `tests/` at repo root, run with `pytest` from
the repo root.

### tests/conftest.py

A session-scoped `QApplication` fixture, since `MultiFileModel` is a
`QStandardItemModel` subclass and any `QObject` construction needs a
`QApplication`:

```python
import sys
import pytest

@pytest.fixture(scope="session")
def qapp():
    from PySide6.QtWidgets import QApplication
    app = QApplication.instance() or QApplication(sys.argv)
    yield app
```

### tests/test_multifilemodel.py

Cover `MultiFileModel.sanitize_filename`:
- Strips whitespace, replaces spaces with underscores.
- Removes unsafe characters via the regex.
- Appends `.AC7` when missing; preserves `.ac7`/`.AC7` when present.
- Empty input returns empty string (no extension added).
- Edge cases: only unsafe characters, leading dot, mixed-case `.Ac7`.

### tests/test_singlefiletab_ordering.py

Round-trip property tests on the LUTs in `SingleFileTab`:
- `file_order_to_ui_order(ui_order_to_file_order(i)) == i` for `i` in 0..11.
- `ui_order_to_file_order(file_order_to_ui_order(i)) == i` for `i` in 0..11.
- `set(lut_in_file_order) == set(lut_in_ui_order)`.

Constructs `SingleFileTab` with a `unittest.mock.MagicMock()` parent. Pure
Python logic only — no widget access.

### tests/test_smoke_imports.py

`import` every module in the `ac7renamer` package. Catches binding swap
mistakes, missing imports, and regenerated-UI syntax errors without
exercising the GUI.

## Git workflow

- Branch: `pyside6-migration` off `master`.
- Commit 1: `Port to PySide6 (mechanical)`.
- Commit 2: `Modernize: pyproject, filesystem resources, tests, cleanup`.
- Merge to `master` once both phases pass the manual smoke test and
  `pytest` passes.

## Files added / modified / deleted (summary)

**Added:**
- `pyproject.toml`
- `requirements.lock`
- `build.py`
- `ac7renamer/resources.py`
- `tests/__init__.py`
- `tests/conftest.py`
- `tests/test_multifilemodel.py`
- `tests/test_singlefiletab_ordering.py`
- `tests/test_smoke_imports.py`
- `docs/superpowers/specs/2026-05-14-ac7renamer-pyside6-migration-design.md`

**Modified:**
- `ac7renamer/ac7renamer.py`
- `ac7renamer/myrenamerdlg.py`
- `ac7renamer/singlefiletab.py`
- `ac7renamer/multifiletab.py`
- `ac7renamer/multifilemodel.py`
- `ac7renamer/ac7renamerdlg.ui` (icon attribute removed in Phase 2)
- `ac7renamer/ac7renamerdlg.py` (regenerated, both phases)
- `README.md` (touched in Phase 1, rewritten in Phase 2)

**Deleted (Phase 2):**
- `setup.py`
- `ac7renamer/imageresources.qrc`
- `ac7renamer/imageresources_rc.py`
- `ac7renamer/buildstep.sh`

## Open questions

None. All choices were made during brainstorming:
- Resources: filesystem via `importlib.resources`.
- UI: regenerate `ac7renamerdlg.py` from the `.ui` at build time with
  `pyside6-uic`.
- Tests: pytest, non-UI logic only.
- Targets: Python 3.10+, Windows + Linux.
- ac7parser: VCS dependency in `pyproject.toml`, pinned to a commit; dev
  workflow uses `pip install -e ../ac7parser` to shadow with the working
  clone.
- Reproducibility: `requirements.lock` generated by pip-compile.
