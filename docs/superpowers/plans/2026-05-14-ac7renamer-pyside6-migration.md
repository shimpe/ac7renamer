# ac7renamer PySide6 migration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate ac7renamer from PyQt5 to PySide6 and modernize the project structure (pyproject.toml, filesystem image resources, pytest suite, cross-platform build script) without changing visible app behavior.

**Architecture:** Two-phase migration on the `pyside6-migration` branch. Phase 1 is a mechanical PyQt5 → PySide6 port producing one commit. Phase 2 is a modernization pass producing a second commit on top of Phase 1.

**Tech Stack:** Python 3.10+ (this venv is 3.14), PySide6 (Qt6 binding), hatchling build backend via `pyproject.toml`, pytest for tests, pyinstaller for the standalone build, pip-tools for the optional lockfile.

**Spec:** `docs/superpowers/specs/2026-05-14-ac7renamer-pyside6-migration-design.md`.

**Working directory:** `C:\development\python\casio\ac7renamer`. The Python interpreter is `C:\development\python\casio\ac7renamer\.venv\Scripts\python.exe`. All commands below run from the repo root unless stated.

**Branch:** Already on `pyside6-migration` (created when the spec was committed).

---

## Phase 1 — Mechanical PyQt5 → PySide6 port

### Task 1: Swap PyQt5 for PySide6 in the venv

**Files:** none.

- [ ] **Step 1: Confirm current branch**

Run:
```
git branch --show-current
```
Expected: `pyside6-migration`. If anything else, run `git checkout pyside6-migration` first.

- [ ] **Step 2: Uninstall PyQt5**

Run:
```
.venv\Scripts\pip.exe uninstall -y PyQt5 PyQt5-Qt5 PyQt5_sip
```
Expected: three "Successfully uninstalled ..." lines.

- [ ] **Step 3: Install PySide6**

Run:
```
.venv\Scripts\pip.exe install "PySide6>=6.6"
```
Expected: pip resolves and installs the latest compatible PySide6 (this venv is Python 3.14, so PySide6 6.9+ will be selected). Also installs `shiboken6` as a transitive.

- [ ] **Step 4: Verify PySide6 imports**

Run:
```
.venv\Scripts\python.exe -c "from PySide6 import QtCore, QtGui, QtWidgets; print(QtCore.qVersion())"
```
Expected: prints a Qt version like `6.9.x` and exits cleanly.

- [ ] **Step 5: No commit yet** — files still reference PyQt5; the app is broken until the next tasks complete. The Phase 1 commit happens at the end of Task 11.

---

### Task 2: Regenerate `ac7renamerdlg.py` with `pyside6-uic`

**Files:**
- Modify: `ac7renamer/ac7renamerdlg.py` (regenerated, not hand-edited)

- [ ] **Step 1: Run pyside6-uic**

Run:
```
.venv\Scripts\python.exe -m PySide6.scripts.pyside_tool uic ac7renamer\ac7renamerdlg.ui -o ac7renamer\ac7renamerdlg.py
```
Expected: command exits cleanly, no output. `ac7renamer\ac7renamerdlg.py` is rewritten.

- [ ] **Step 2: Verify the regenerated file imports from PySide6**

Run:
```
.venv\Scripts\python.exe -c "import ast; src = open('ac7renamer/ac7renamerdlg.py').read(); assert 'from PySide6' in src and 'PyQt5' not in src; print('ok')"
```
Expected: prints `ok`.

- [ ] **Step 3: Verify resources import still present**

Run:
```
findstr /R "imageresources_rc" ac7renamer\ac7renamerdlg.py
```
Expected: at least one match (e.g. `from . import imageresources_rc`). The resources reference is preserved in Phase 1; Phase 2 will remove it.

---

### Task 3: Regenerate `imageresources_rc.py` with `pyside6-rcc`

**Files:**
- Modify: `ac7renamer/imageresources_rc.py` (regenerated)

- [ ] **Step 1: Run pyside6-rcc**

Run:
```
.venv\Scripts\python.exe -m PySide6.scripts.pyside_tool rcc ac7renamer\imageresources.qrc -o ac7renamer\imageresources_rc.py
```
Expected: command exits cleanly. `ac7renamer\imageresources_rc.py` is rewritten in PySide6 format.

- [ ] **Step 2: Verify it imports from PySide6**

Run:
```
.venv\Scripts\python.exe -c "src = open('ac7renamer/imageresources_rc.py').read(); assert 'from PySide6' in src and 'PyQt5' not in src; print('ok')"
```
Expected: prints `ok`.

- [ ] **Step 3: Verify the module can be imported**

Run:
```
.venv\Scripts\python.exe -c "import sys; sys.path.insert(0, '.'); from ac7renamer import imageresources_rc; print('ok')"
```
Expected: prints `ok`. (No error means the resource bytes are well-formed under PySide6 too.)

---

### Task 4: Port `ac7renamer/ac7renamer.py`

**Files:**
- Modify: `ac7renamer/ac7renamer.py`

- [ ] **Step 1: Replace imports and `exec_()`**

Edit `ac7renamer/ac7renamer.py` so it reads exactly:

```python
import sys
import ac7renamer.myrenamerdlg
from PySide6 import QtWidgets
from pathlib import Path


def main():
    app = QtWidgets.QApplication(sys.argv)
    ac7_renamer = QtWidgets.QDialog()
    ui = ac7renamer.myrenamerdlg.MyRenamerDlg()
    ui.setupUi(ac7_renamer)
    home = str(Path.home())
    ui.setup_slots(home)
    ac7_renamer.show()
    ui.flash_splash()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
```

Diff vs original: `from PyQt5 import QtWidgets` → `from PySide6 import QtWidgets`, and `app.exec_()` → `app.exec()`.

- [ ] **Step 2: Verify syntactically valid**

Run:
```
.venv\Scripts\python.exe -c "import ast; ast.parse(open('ac7renamer/ac7renamer.py').read()); print('ok')"
```
Expected: prints `ok`.

---

### Task 5: Port `ac7renamer/myrenamerdlg.py`

**Files:**
- Modify: `ac7renamer/myrenamerdlg.py`

- [ ] **Step 1: Swap imports and `exec_()` to `exec()`**

Edit `ac7renamer/myrenamerdlg.py`. The full file should read:

```python
import ac7renamer.ac7renamerdlg
from PySide6.QtWidgets import QMessageBox, QSplashScreen
from ac7renamer.singlefiletab import SingleFileTab
from ac7renamer.multifiletab import MultiFileTab
from PySide6.QtCore import QSettings, Qt, QTimer
from PySide6.QtGui import QPixmap


class MyRenamerDlg(ac7renamer.ac7renamerdlg.Ui_Ac7Renamer):
    def __init__(self):
        super().__init__()
        self.home_folder = None
        self.splash = None
        self.tab_handlers = {'singlefile': SingleFileTab(self), 'multifile': MultiFileTab(self)}

    def flash_splash(self):
        self.splash = QSplashScreen(QPixmap(":/icons/images/restyle_logo_whitebg.png").scaledToWidth(500))
        self.splash.show()
        QTimer.singleShot(1500, self.splash.close)

    def setup_slots(self, homefolder):
        for tab in self.tab_handlers:
            self.tab_handlers[tab].setup_slots(homefolder)
        self.aboutButton.clicked.connect(self.about_clicked)
        settings = QSettings('Ac7Renamer', 'EulaAccepted')
        if not settings.value("Accepted", 0):
            self.about_clicked()
            settings.setValue('Accepted', 1)

    def about_clicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("About this tool...")
        msg.setTextFormat(Qt.RichText)
        msg.setInformativeText("Tool to manipulate casio .AC7 rhythm files.<br><br>"
                               "I strongly encourage you to make a donation to your favorite charity if you decide to keep using this tool.<br><br>"
                               "You can use, modify and copy the tool freely under the guarantees of the GPLv3 license.<br><br>"
                               "Complete source code can be found at <a href='https://github.com/shimpe/ac7renamer'>GitHub</a><br><br>"
                               "You may copy, distribute and modify the "
                               "software as long as you track changes/dates. Any modifications to, "
                               "or software including (via compiler) GPL-licensed code, must also be made available "
                               "under the GPL along with build & install instructions.<br><br>"
                               "I try to offer the best possible software, but cannot promise that the software will always be bug-free, available, accurate, complete, and up-to-date. "
                               "You agree that when you use this software, you do so at your own risk, and this software or affiliated persons and organizations are not in any way responsible for damage or weird behavior inflicted on your instrument. Furthermore, you also agree that you will not attempt to hold us or our data providers liable for damage or inaccuracies in the implementation.<br><br>"
                               "If you cannot agree to these terms, then under no circumstance use this software or files created with this software.")
        msg.setWindowTitle("About")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setIconPixmap(QPixmap(":/icons/images/restyle_logo.png").scaledToWidth(300))
        msg.exec()
```

Diff vs original: every `PyQt5` → `PySide6` and `msg.exec_()` → `msg.exec()`. Enums (e.g. `QMessageBox.Information`, `Qt.RichText`) are left un-scoped intentionally; Phase 2 tightens them.

- [ ] **Step 2: Verify syntactically valid**

Run:
```
.venv\Scripts\python.exe -c "import ast; ast.parse(open('ac7renamer/myrenamerdlg.py').read()); print('ok')"
```
Expected: prints `ok`.

---

### Task 6: Port `ac7renamer/singlefiletab.py`

**Files:**
- Modify: `ac7renamer/singlefiletab.py`

- [ ] **Step 1: Swap imports, replace `QRegExp` with `QRegularExpression`, swap `exec_`**

Edit `ac7renamer/singlefiletab.py`. Replace the top-of-file imports block:

```python
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QRegExpValidator
from pathlib import Path
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from ac7parser.Ac7File import Ac7File
```

with:

```python
from PySide6.QtCore import QObject
from PySide6.QtCore import QSettings
from PySide6.QtCore import QRegularExpression
from PySide6.QtCore import Qt
from PySide6.QtGui import QRegularExpressionValidator
from pathlib import Path
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QMessageBox
from ac7parser.Ac7File import Ac7File
```

In `setup_slots`, replace:

```python
        reg_ex = QRegExp(r"[A-Za-z0-9 #\(\)\.\*\+\-,\$!\"\\':;/<=&>\?@\[\]\^_{}~\|]{1,12}")
        input_validator = QRegExpValidator(reg_ex, self.parent.desiredDisplayName)
```

with:

```python
        reg_ex = QRegularExpression(r"[A-Za-z0-9 #\(\)\.\*\+\-,\$!\"\\':;/<=&>\?@\[\]\^_{}~\|]{1,12}")
        input_validator = QRegularExpressionValidator(reg_ex, self.parent.desiredDisplayName)
```

Then replace every `msg.exec_()` with `msg.exec()` (there are three occurrences).

- [ ] **Step 2: Verify file syntactically valid**

Run:
```
.venv\Scripts\python.exe -c "import ast; ast.parse(open('ac7renamer/singlefiletab.py').read()); print('ok')"
```
Expected: prints `ok`.

- [ ] **Step 3: Verify no PyQt5 / QRegExp references remain**

Run:
```
findstr /R "PyQt5 QRegExp[^a-zA-Z] exec_" ac7renamer\singlefiletab.py
```
Expected: no matches (empty output).

---

### Task 7: Port `ac7renamer/multifiletab.py`

**Files:**
- Modify: `ac7renamer/multifiletab.py`

- [ ] **Step 1: Swap imports**

Edit `ac7renamer/multifiletab.py`. Replace:

```python
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
```

with:

```python
from PySide6.QtCore import QObject, Qt
from PySide6.QtCore import QSettings
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QMessageBox
```

Replace every `msg.exec_()` with `msg.exec()` (there are two occurrences).

- [ ] **Step 2: Verify syntactically valid and clean**

Run:
```
.venv\Scripts\python.exe -c "import ast; ast.parse(open('ac7renamer/multifiletab.py').read()); print('ok')"
```
Expected: prints `ok`.

Run:
```
findstr /R "PyQt5 exec_" ac7renamer\multifiletab.py
```
Expected: no matches.

---

### Task 8: Port `ac7renamer/multifilemodel.py`

**Files:**
- Modify: `ac7renamer/multifilemodel.py`

- [ ] **Step 1: Swap import**

Edit `ac7renamer/multifilemodel.py`. Replace:

```python
from PyQt5.QtGui import QStandardItemModel, QStandardItem
```

with:

```python
from PySide6.QtGui import QStandardItemModel, QStandardItem
```

(File has no other PyQt5 references and no `exec_` calls.)

- [ ] **Step 2: Verify syntactically valid and clean**

Run:
```
.venv\Scripts\python.exe -c "import ast; ast.parse(open('ac7renamer/multifilemodel.py').read()); print('ok')"
```
Expected: prints `ok`.

Run:
```
findstr /R "PyQt5" ac7renamer\multifilemodel.py
```
Expected: no matches.

---

### Task 9: Update `buildstep.sh`, `setup.py`, and README to mention PySide6 (temporary)

**Files:**
- Modify: `ac7renamer/buildstep.sh`
- Modify: `setup.py`
- Modify: `README.md`

These changes are temporary — Phase 2 deletes `buildstep.sh` and `setup.py` and rewrites the README. They exist in Phase 1 only so a reader of the Phase 1 commit can install the right binding.

- [ ] **Step 1: Update `ac7renamer/buildstep.sh`**

Replace its contents with:

```sh
pyside6-uic ac7renamerdlg.ui -o ac7renamerdlg.py
pyside6-rcc imageresources.qrc -o imageresources_rc.py
```

- [ ] **Step 2: Update `setup.py`**

Change line 12 from:

```python
    install_requires=[ "https://github.com/shimpe/ac7parser", "PyQt5" ],
```

to:

```python
    install_requires=[ "https://github.com/shimpe/ac7parser", "PySide6" ],
```

- [ ] **Step 3: Update `README.md`**

In `README.md`, replace every occurrence of `pip3 install PyQt5` with `pip3 install PySide6`. (There are two — one each in the Windows and Linux sections.)

No other README edits in Phase 1.

- [ ] **Step 4: Sanity-check no PyQt5 mentions remain anywhere**

Run:
```
findstr /S /R "PyQt5" .
```
Expected: no matches — except possibly inside `.venv\`, `.git\`, or other build artefacts. If anything outside those directories matches, fix it before moving on.

---

### Task 10: Phase 1 smoke test (manual)

**Files:** none.

- [ ] **Step 1: Launch the app**

Run:
```
.venv\Scripts\python.exe ReStyle.py
```

Expected: app window appears titled "Restyles piles of files!". The cyan info banner is visible at the top. The splash screen flashes briefly on launch. The About dialog opens on first run (since `EulaAccepted/Accepted` is set after the first time, this may or may not happen depending on test history — manually click "About this tool" if it doesn't auto-open).

- [ ] **Step 2: Verify the About dialog**

Click "About this tool". Expected: dialog shows the logo on the left, the GPLv3 text on the right, an "OK" button. Click OK to dismiss.

- [ ] **Step 3: Verify single-file load/save**

Pick any `.AC7` file from `C:\development\python\casio\ac7parser\testfiles\` (e.g. one of the smaller ones). On the "Single file" tab:
1. Click "Load Ac7 File", browse to a file, open it.
2. Verify "Current display name" is populated and the desired-ordering combo boxes get items.
3. Type a short new name into "Desired display name" (max 12 chars).
4. Click "Save AC7 File", save to a temp location, confirm success dialog.

- [ ] **Step 4: Verify multi-file flow**

Switch to "Many files" tab:
1. Click "Load folder", pick `C:\development\python\casio\ac7parser\testfiles\` (or any folder with .AC7 files).
2. Verify the table populates with one row per file.
3. Type a desired display name in one row. Type a desired filename in another row.
4. Click Select All / Deselect All / Invert Selection — verify checkboxes update.
5. Click "Rename!", pick a destination folder, verify "Success!" appears in the error column for the processed rows.
6. Click "4 Variation Rhythm Split" — pick a destination folder, verify it produces `_12.AC7` and `_34.AC7` outputs.

- [ ] **Step 5: Close the app**

Click the dialog's Close button or the window's X. Expected: app exits cleanly.

If any step fails, **do not commit**. Investigate the failure first and update earlier tasks as needed.

---

### Task 11: Commit Phase 1

**Files:** none (commit step).

- [ ] **Step 1: Stage Phase 1 changes**

Run:
```
git add ac7renamer\ac7renamer.py ac7renamer\myrenamerdlg.py ac7renamer\singlefiletab.py ac7renamer\multifiletab.py ac7renamer\multifilemodel.py ac7renamer\ac7renamerdlg.py ac7renamer\imageresources_rc.py ac7renamer\buildstep.sh setup.py README.md
```

- [ ] **Step 2: Verify staged contents**

Run:
```
git diff --staged --stat
```

Expected: roughly 10 files changed, no surprising additions, no `.venv/` or `.idea/` paths.

- [ ] **Step 3: Commit**

Run:
```
git commit -m "Port to PySide6 (mechanical)

Swap PyQt5 imports for PySide6 across all modules. Change exec_() to exec().
Replace QRegExp/QRegExpValidator with QRegularExpression/QRegularExpressionValidator.
Regenerate ac7renamerdlg.py with pyside6-uic and imageresources_rc.py with pyside6-rcc.

Behavior unchanged. Enum tightening and modernization happen in the next commit."
```

Expected: one new commit on `pyside6-migration`.

---

## Phase 2 — Modernize

### Task 12: Create `pyproject.toml`

**Files:**
- Create: `pyproject.toml`

- [ ] **Step 1: Write `pyproject.toml` at repo root**

Create `C:\development\python\casio\ac7renamer\pyproject.toml` with this exact content:

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

- [ ] **Step 2: Validate the TOML parses**

Run:
```
.venv\Scripts\python.exe -c "import tomllib; tomllib.load(open('pyproject.toml','rb')); print('ok')"
```
Expected: prints `ok`.

---

### Task 13: Delete `setup.py`

**Files:**
- Delete: `setup.py`

- [ ] **Step 1: Remove the file**

Run:
```
git rm setup.py
```
Expected: `rm 'setup.py'`. Don't commit yet — Phase 2 commits at the end.

---

### Task 14: Install the project as editable, with `dev` and `build` extras

**Files:** none.

- [ ] **Step 1: Install via pyproject**

Run:
```
.venv\Scripts\pip.exe install -e ".[dev,build]"
```

Expected:
- pip resolves PySide6 (already satisfied), pytest (newly installed), pyinstaller (already satisfied).
- pip fetches `ac7parser` from `git+https://github.com/shimpe/ac7parser.git@7cb306b0d4b901dcf7a6ead0e4c639b4140df4cb` and installs it (this may replace the existing source-installed copy).
- Final line: `Successfully installed ac7renamer-0.1.0 ...` plus any transitives.

This requires `git` to be on PATH and HTTPS access to GitHub. If it fails with "git not found", install git for Windows first; if it fails with a network error, retry on a working connection.

- [ ] **Step 2: Verify pytest is on PATH**

Run:
```
.venv\Scripts\pytest.exe --version
```
Expected: pytest version string (e.g. `pytest 8.x.x`).

- [ ] **Step 3: Verify ac7parser is still importable**

Run:
```
.venv\Scripts\python.exe -c "from ac7parser.Ac7File import Ac7File; print('ok')"
```
Expected: prints `ok`.

---

### Task 15: Add tests scaffolding (`tests/__init__.py`, `tests/conftest.py`)

**Files:**
- Create: `tests/__init__.py`
- Create: `tests/conftest.py`

- [ ] **Step 1: Create empty `tests/__init__.py`**

Create `C:\development\python\casio\ac7renamer\tests\__init__.py` with no content (zero bytes).

- [ ] **Step 2: Create `tests/conftest.py`**

Create `C:\development\python\casio\ac7renamer\tests\conftest.py` with this exact content:

```python
import sys

import pytest


@pytest.fixture(scope="session")
def qapp():
    from PySide6.QtWidgets import QApplication

    app = QApplication.instance() or QApplication(sys.argv)
    yield app
```

The fixture is session-scoped because Qt only supports one `QApplication` per process. Any test that needs Qt object construction takes `qapp` as a fixture.

---

### Task 16: Write `tests/test_smoke_imports.py`

**Files:**
- Create: `tests/test_smoke_imports.py`

- [ ] **Step 1: Write the test**

Create `C:\development\python\casio\ac7renamer\tests\test_smoke_imports.py` with this exact content:

```python
"""Smoke test: every module in the package imports cleanly."""


def test_imports_ac7renamer():
    import ac7renamer.ac7renamer  # noqa: F401


def test_imports_myrenamerdlg(qapp):
    import ac7renamer.myrenamerdlg  # noqa: F401


def test_imports_singlefiletab(qapp):
    import ac7renamer.singlefiletab  # noqa: F401


def test_imports_multifiletab(qapp):
    import ac7renamer.multifiletab  # noqa: F401


def test_imports_multifilemodel(qapp):
    import ac7renamer.multifilemodel  # noqa: F401


def test_imports_columns():
    import ac7renamer.columns  # noqa: F401
```

The `qapp` fixture is requested for any module that defines `QObject` subclasses at import time (`SingleFileTab`, `MultiFileTab` instantiate `QObject` only at call time, but importing `myrenamerdlg` triggers loading them, and the regenerated `ac7renamerdlg` references PySide6 enums at import — easier to just require `qapp` everywhere).

- [ ] **Step 2: Run the test, expect pass**

Run:
```
.venv\Scripts\pytest.exe tests/test_smoke_imports.py -v
```
Expected: all 6 tests PASS.

If any fail, the Phase 1 port has a missed binding somewhere — fix the underlying source file rather than the test.

---

### Task 17: Write `tests/test_multifilemodel.py`

**Files:**
- Create: `tests/test_multifilemodel.py`

- [ ] **Step 1: Write the test**

Create `C:\development\python\casio\ac7renamer\tests\test_multifilemodel.py` with this exact content:

```python
"""Tests for MultiFileModel.sanitize_filename behavior."""
import pytest


@pytest.fixture
def model(qapp):
    from ac7renamer.multifilemodel import MultiFileModel

    return MultiFileModel(0, 6, parent=None)


def test_appends_ac7_when_missing(model):
    assert model.sanitize_filename("MyStyle") == "MyStyle.AC7"


def test_preserves_uppercase_ac7(model):
    assert model.sanitize_filename("MyStyle.AC7") == "MyStyle.AC7"


def test_preserves_lowercase_ac7(model):
    # The endswith check is case-insensitive, so .ac7 is left alone.
    assert model.sanitize_filename("mystyle.ac7") == "mystyle.ac7"


def test_replaces_spaces_with_underscores(model):
    assert model.sanitize_filename("my style") == "my_style.AC7"


def test_strips_surrounding_whitespace(model):
    assert model.sanitize_filename("   trimmed   ") == "trimmed.AC7"


def test_strips_unsafe_characters(model):
    assert model.sanitize_filename("a!b@c#d") == "abcd.AC7"


def test_keeps_dot_and_hyphen_and_underscore(model):
    assert model.sanitize_filename("a-b_c.d") == "a-b_c.d.AC7"


def test_empty_input_returns_empty(model):
    # No characters means no .AC7 is appended.
    assert model.sanitize_filename("") == ""


def test_only_unsafe_chars_returns_empty(model):
    # After sanitization the result is empty; nothing gets the .AC7 suffix.
    assert model.sanitize_filename("!@#$%") == ""
```

- [ ] **Step 2: Run the test, expect pass**

Run:
```
.venv\Scripts\pytest.exe tests/test_multifilemodel.py -v
```
Expected: all 9 tests PASS.

If any fail, **stop** and re-read `MultiFileModel.sanitize_filename` — the test characterizes the existing behavior, so a failure means either the test misreads the code or the code has changed. Fix the test (not the code) unless you have a reason to change behavior.

---

### Task 18: Write `tests/test_singlefiletab_ordering.py`

**Files:**
- Create: `tests/test_singlefiletab_ordering.py`

- [ ] **Step 1: Write the test**

Create `C:\development\python\casio\ac7renamer\tests\test_singlefiletab_ordering.py` with this exact content:

```python
"""Tests for the file-order <-> UI-order LUT round-trip in SingleFileTab."""
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def tab(qapp):
    from ac7renamer.singlefiletab import SingleFileTab

    return SingleFileTab(parent=MagicMock())


def test_luts_contain_the_same_elements(tab):
    assert set(tab.lut_in_file_order) == set(tab.lut_in_ui_order)
    assert len(tab.lut_in_file_order) == 12
    assert len(tab.lut_in_ui_order) == 12


@pytest.mark.parametrize("i", list(range(12)))
def test_file_to_ui_to_file_round_trip(tab, i):
    assert tab.ui_order_to_file_order(tab.file_order_to_ui_order(i)) == i


@pytest.mark.parametrize("i", list(range(12)))
def test_ui_to_file_to_ui_round_trip(tab, i):
    assert tab.file_order_to_ui_order(tab.ui_order_to_file_order(i)) == i
```

- [ ] **Step 2: Run the test, expect pass**

Run:
```
.venv\Scripts\pytest.exe tests/test_singlefiletab_ordering.py -v
```
Expected: all 25 tests PASS (1 + 12 + 12).

- [ ] **Step 3: Run the whole suite for a baseline**

Run:
```
.venv\Scripts\pytest.exe -v
```
Expected: all tests PASS (6 + 9 + 25 = 40).

---

### Task 19: Create `ac7renamer/resources.py` for filesystem image paths

**Files:**
- Create: `ac7renamer/resources.py`

- [ ] **Step 1: Write the helper**

Create `C:\development\python\casio\ac7renamer\ac7renamer\resources.py` with this exact content:

```python
from importlib.resources import files


def image_path(name: str) -> str:
    return str(files("ac7renamer").joinpath("images", name))
```

- [ ] **Step 2: Verify it resolves the three image files**

Run:
```
.venv\Scripts\python.exe -c "from ac7renamer.resources import image_path; import os; [print(name, os.path.exists(image_path(name))) for name in ('restyle_icon.png','restyle_logo.png','restyle_logo_whitebg.png')]"
```
Expected: three lines, each ending in `True`.

---

### Task 20: Edit `ac7renamerdlg.ui` to drop the .qrc references

**Files:**
- Modify: `ac7renamer/ac7renamerdlg.ui`

- [ ] **Step 1: Remove the `windowIcon` property**

Open `ac7renamer/ac7renamerdlg.ui`. Delete lines 16–19, which contain exactly:

```xml
  <property name="windowIcon">
   <iconset resource="imageresources.qrc">
    <normaloff>:/icons/images/restyle_icon.png</normaloff>:/icons/images/restyle_icon.png</iconset>
  </property>
```

- [ ] **Step 2: Remove the `<resources>` block near the end of the file**

In the same file, delete the three lines previously at 616–618, which contain exactly:

```xml
 <resources>
  <include location="imageresources.qrc"/>
 </resources>
```

- [ ] **Step 3: Sanity-check no .qrc references remain in the file**

Run:
```
findstr /R "qrc resource" ac7renamer\ac7renamerdlg.ui
```
Expected: no matches.

---

### Task 21: Regenerate `ac7renamerdlg.py` with `pyside6-uic` (no resources reference now)

**Files:**
- Modify: `ac7renamer/ac7renamerdlg.py` (regenerated)

- [ ] **Step 1: Regenerate**

Run:
```
.venv\Scripts\python.exe -m PySide6.scripts.pyside_tool uic ac7renamer\ac7renamerdlg.ui -o ac7renamer\ac7renamerdlg.py
```

- [ ] **Step 2: Verify the resource import is gone**

Run:
```
findstr /R "imageresources_rc" ac7renamer\ac7renamerdlg.py
```
Expected: no matches.

---

### Task 22: Update `myrenamerdlg.py` — filesystem image paths, scoped enums, set window icon in code

**Files:**
- Modify: `ac7renamer/myrenamerdlg.py`

- [ ] **Step 1: Rewrite the file**

Replace the entire contents of `ac7renamer/myrenamerdlg.py` with:

```python
import ac7renamer.ac7renamerdlg
from PySide6.QtWidgets import QMessageBox, QSplashScreen
from PySide6.QtCore import QSettings, Qt, QTimer
from PySide6.QtGui import QIcon, QPixmap

from ac7renamer import resources
from ac7renamer.singlefiletab import SingleFileTab
from ac7renamer.multifiletab import MultiFileTab


class MyRenamerDlg(ac7renamer.ac7renamerdlg.Ui_Ac7Renamer):
    def __init__(self) -> None:
        super().__init__()
        self.home_folder: str | None = None
        self.splash: QSplashScreen | None = None
        self.tab_handlers = {
            "singlefile": SingleFileTab(self),
            "multifile": MultiFileTab(self),
        }

    def setupUi(self, dialog) -> None:
        super().setupUi(dialog)
        dialog.setWindowIcon(QIcon(resources.image_path("restyle_icon.png")))

    def flash_splash(self) -> None:
        pixmap = QPixmap(resources.image_path("restyle_logo_whitebg.png")).scaledToWidth(500)
        self.splash = QSplashScreen(pixmap)
        self.splash.show()
        QTimer.singleShot(1500, self.splash.close)

    def setup_slots(self, homefolder: str) -> None:
        for tab in self.tab_handlers:
            self.tab_handlers[tab].setup_slots(homefolder)
        self.aboutButton.clicked.connect(self.about_clicked)
        settings = QSettings("Ac7Renamer", "EulaAccepted")
        if not settings.value("Accepted", 0):
            self.about_clicked()
            settings.setValue("Accepted", 1)

    def about_clicked(self) -> None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("About this tool...")
        msg.setTextFormat(Qt.TextFormat.RichText)
        msg.setInformativeText(
            "Tool to manipulate casio .AC7 rhythm files.<br><br>"
            "I strongly encourage you to make a donation to your favorite charity if you decide to keep using this tool.<br><br>"
            "You can use, modify and copy the tool freely under the guarantees of the GPLv3 license.<br><br>"
            "Complete source code can be found at <a href='https://github.com/shimpe/ac7renamer'>GitHub</a><br><br>"
            "You may copy, distribute and modify the "
            "software as long as you track changes/dates. Any modifications to, "
            "or software including (via compiler) GPL-licensed code, must also be made available "
            "under the GPL along with build & install instructions.<br><br>"
            "I try to offer the best possible software, but cannot promise that the software will always be bug-free, available, accurate, complete, and up-to-date. "
            "You agree that when you use this software, you do so at your own risk, and this software or affiliated persons and organizations are not in any way responsible for damage or weird behavior inflicted on your instrument. Furthermore, you also agree that you will not attempt to hold us or our data providers liable for damage or inaccuracies in the implementation.<br><br>"
            "If you cannot agree to these terms, then under no circumstance use this software or files created with this software."
        )
        msg.setWindowTitle("About")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.setIconPixmap(QPixmap(resources.image_path("restyle_logo.png")).scaledToWidth(300))
        msg.exec()
```

Notes on the diff vs Phase 1:
- `from ac7renamer import resources` (new) replaces the implicit `:/icons/...` resource references.
- A `setupUi` override sets the window icon in code (since the .ui no longer carries it).
- All `QPixmap(":/icons/images/...")` calls become `QPixmap(resources.image_path("..."))`.
- Enum forms tightened: `QMessageBox.Icon.Information`, `Qt.TextFormat.RichText`, `QMessageBox.StandardButton.Ok`.
- Type hints added on signatures.

- [ ] **Step 2: Verify syntactically valid**

Run:
```
.venv\Scripts\python.exe -c "import ast; ast.parse(open('ac7renamer/myrenamerdlg.py').read()); print('ok')"
```
Expected: prints `ok`.

- [ ] **Step 3: Run pytest**

Run:
```
.venv\Scripts\pytest.exe -v
```
Expected: all tests still PASS. The smoke import test exercises this file.

---

### Task 23: Delete `imageresources.qrc` and `imageresources_rc.py`

**Files:**
- Delete: `ac7renamer/imageresources.qrc`
- Delete: `ac7renamer/imageresources_rc.py`

- [ ] **Step 1: Remove both files**

Run:
```
git rm ac7renamer\imageresources.qrc ac7renamer\imageresources_rc.py
```
Expected: `rm 'ac7renamer/imageresources.qrc'` and `rm 'ac7renamer/imageresources_rc.py'`.

- [ ] **Step 2: Verify nothing else imports `imageresources_rc`**

Run:
```
findstr /S /R "imageresources_rc" ac7renamer
```
Expected: no matches (the regenerated `ac7renamerdlg.py` from Task 21 no longer references it).

- [ ] **Step 3: Run pytest**

Run:
```
.venv\Scripts\pytest.exe -v
```
Expected: all tests still PASS.

---

### Task 24: Clean up `singlefiletab.py` — combo loop, scoped enums, drop no-op `reject`

**Files:**
- Modify: `ac7renamer/singlefiletab.py`

- [ ] **Step 1: Rewrite the file**

Replace the entire contents of `ac7renamer/singlefiletab.py` with:

```python
from pathlib import Path

from PySide6.QtCore import QObject, QRegularExpression, QSettings, Qt
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QFileDialog, QMessageBox

from ac7parser.Ac7File import Ac7File


class SingleFileTab(QObject):
    # lut is ordered as in the .ac7 file
    # do not change the order in lut_in_file_order
    # rather, change the ordering in the .ui file if needed
    # if you do, make sure to swap both the current and corresponding destination fields
    lut_in_file_order = [
        "intro (1)", "normal (1)", "var (2)", "fill-in (1)", "fill-in (2)", "end (1)",
        "intro (2)", "var (3)", "var (4)", "fill-in (3)", "fill-in (4)", "end (2)",
    ]
    lut_in_ui_order = [
        "intro (1)", "normal (1)", "fill-in (1)", "var (2)", "fill-in (2)", "end (1)",
        "var (3)", "fill-in (3)", "var (4)", "fill-in (4)", "intro (2)", "end (2)",
    ]

    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.ac7file = Ac7File()
        self.file_loaded = False
        self.filename = ""
        self.home_folder = ""
        self.no_of_el = 0
        self.ordering: list[int] = []
        self.combos_in_file_order: list = []

    def file_order_to_ui_order(self, file_order_index: int) -> int:
        return self.lut_in_ui_order.index(self.lut_in_file_order[file_order_index])

    def ui_order_to_file_order(self, ui_order_index: int) -> int:
        return self.lut_in_file_order.index(self.lut_in_ui_order[ui_order_index])

    def setup_slots(self, homefolder: str) -> None:
        self.parent.pushButton.clicked.connect(self.load_ac7_file_clicked)
        self.parent.saveButton.clicked.connect(self.save_clicked)
        self.home_folder = homefolder
        reg_ex = QRegularExpression(
            r"[A-Za-z0-9 #\(\)\.\*\+\-,\$!\"\\':;/<=&>\?@\[\]\^_{}~\|]{1,12}"
        )
        input_validator = QRegularExpressionValidator(reg_ex, self.parent.desiredDisplayName)
        self.parent.desiredDisplayName.setValidator(input_validator)
        self.combos_in_file_order = [
            getattr(self.parent, f"desEl{i + 1}") for i in range(12)
        ]
        self.parent.pushButton.setFocus()

    def load_ac7_file_clicked(self) -> None:
        settings = QSettings("Ac7Renamer", "Recently Used Files")
        start_folder = "{0}".format(settings.value("recentFolder", "")) or self.home_folder
        fname = QFileDialog.getOpenFileName(
            None,
            "Open file",
            start_folder,
            "AC7 Rhythm files (*.AC7);;all files (*.*)",
            options=QFileDialog.Option.DontUseNativeDialog,
        )
        if not (fname and fname[0]):
            return
        fname = fname[0]
        settings.setValue("recentFolder", Path(fname).parents[0])
        try:
            self.ac7file.load_file(fname)
            stylename = self.ac7file.properties["common_parameters"].properties["stylename"]
            binzero = stylename.find("\x00")
            if binzero >= 0:
                stylename = stylename[:binzero]
            self.parent.currentDisplayName.setText(stylename)
            self.parent.desiredDisplayName.setText("")
            self.file_loaded = True
            self.filename = Path(fname).name
            self.parent.desiredDisplayName.setFocus()
            self.set_number_of_elements(
                len(self.ac7file.properties["common_parameters"].properties["overall_parameters"]["elements"])
            )
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Unable to load the file")
            msg.setTextFormat(Qt.TextFormat.RichText)
            msg.setInformativeText(
                "There was a problem parsing {0}. Please log a bug in <href a='https://github.com/shimpe/ac7renamer/issues'>the bug database</href> and attach your .AC7 file".format(fname)
            )
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDetailedText(e.__repr__())
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()

    def save_clicked(self) -> None:
        self.ordering = [
            self.ui_order_to_file_order(self.combos_in_file_order[i].currentIndex())
            for i in range(self.no_of_el)
        ]

        if not self.file_loaded:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("No file loaded")
            msg.setInformativeText("Please load an .AC7 file before attempting to save one.")
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        txt = self.parent.desiredDisplayName.text()
        if not txt:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("No desired display name")
            msg.setInformativeText("Please type a desired name before attempting to save the file.")
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        settings = QSettings("Ac7Renamer", "Recently Used Files")
        start_folder = "{0}".format(settings.value("recentFolder", "")) or self.home_folder
        fname = QFileDialog.getSaveFileName(
            None,
            "Save file {0} as...".format(self.filename),
            start_folder,
            "AC7 Rhythm files (*.AC7);;all files (*.*)",
            options=QFileDialog.Option.DontUseNativeDialog,
        )
        if not (fname and fname[0]):
            return
        fname = fname[0]
        if not fname.lower().endswith(".ac7"):
            fname = fname + ".AC7"
        self.ac7file.properties["common_parameters"].properties["stylename"] = txt
        try:
            self.ac7file.set_custom_element_ordering(self.ordering)
            self.ac7file.prepare_for_save()
            self.ac7file.write_file(fname, True, False)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Successfully saved {0}!".format(fname))
            msg.setWindowTitle("ReStyle Information")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()
            self.parent.pushButton.setFocus()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Unable to save the file")
            msg.setTextFormat(Qt.TextFormat.RichText)
            msg.setInformativeText(
                "There was a problem saving {0}. Please log a bug in <href a='https://github.com/shimpe/ac7renamer/issues'>the bug database</href> and attach your .ac7 file".format(fname)
            )
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDetailedText(e.__repr__())
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()

    def set_number_of_elements(self, no_of_el: int) -> None:
        self.no_of_el = no_of_el
        for index_in_file_order, c in enumerate(self.combos_in_file_order):
            c.clear()
            c.setEnabled(index_in_file_order < no_of_el)
            for index_in_ui_order, label in enumerate(self.lut_in_ui_order):
                if self.ui_order_to_file_order(index_in_ui_order) < no_of_el:
                    c.addItem(label)
            c.setCurrentIndex(self.file_order_to_ui_order(index_in_file_order))
```

Notes on the diff vs Phase 1:
- LUTs are now class attributes (still mutable lists, but they don't need to be re-bound per instance).
- The 12 hardcoded `self.parent.desEl{N}` references collapse into a `getattr` loop.
- No-op `def reject(self): pass` and its `Buttons.rejected.connect(self.reject)` wiring removed. (The generated UI already wires `Buttons.rejected` → `Ac7Renamer.reject` on the dialog.)
- All enums tightened to scoped Qt6 forms (`QMessageBox.Icon.Warning`, `Qt.TextFormat.RichText`, `QFileDialog.Option.DontUseNativeDialog`, etc.).
- Early-return guards replace nested `if/else` in `save_clicked` and `load_ac7_file_clicked`.
- Type hints added on public methods.

- [ ] **Step 2: Run pytest**

Run:
```
.venv\Scripts\pytest.exe -v
```
Expected: all tests still PASS. `test_singlefiletab_ordering.py` exercises this file directly — if its assertions fail, the LUTs got reordered by mistake. Revert and re-check.

---

### Task 25: Clean up `multifiletab.py` — scoped enums

**Files:**
- Modify: `ac7renamer/multifiletab.py`

- [ ] **Step 1: Replace un-scoped enums with scoped forms**

In `ac7renamer/multifiletab.py`, make these substitutions across the whole file:
- `Qt.Checked` → `Qt.CheckState.Checked` (3 occurrences in `select_all`, `invert_selection`, and the two `... == Qt.Checked` checks)
- `Qt.Unchecked` → `Qt.CheckState.Unchecked` (2 occurrences in `deselect_all` and `invert_selection`)
- `QMessageBox.Warning` → `QMessageBox.Icon.Warning` (2 occurrences)
- `QMessageBox.Ok` → `QMessageBox.StandardButton.Ok` (4 occurrences across the two warning dialogs)
- `QFileDialog.DontUseNativeDialog` → `QFileDialog.Option.DontUseNativeDialog` (3 occurrences)
- `QFileDialog.ShowDirsOnly` → `QFileDialog.Option.ShowDirsOnly` (3 occurrences)

If your editor's "replace all" treats each as a literal substring, that's the safest approach for each token individually — no rewriting needed beyond these substitutions.

- [ ] **Step 2: Verify no un-scoped enums remain in this file**

Run:
```
findstr /R "Qt\.Checked Qt\.Unchecked QMessageBox\.Warning QMessageBox\.Ok QFileDialog\.DontUseNativeDialog QFileDialog\.ShowDirsOnly" ac7renamer\multifiletab.py
```
Expected: no matches. (The scoped forms — e.g. `Qt.CheckState.Checked` — would still match `Qt\.Checked` as a prefix in some regex flavors, but `findstr /R` is line-anchored only at the boundaries; if any matches are scoped forms, that's OK. Inspect any output to be sure.)

- [ ] **Step 3: Run pytest**

Run:
```
.venv\Scripts\pytest.exe -v
```
Expected: all tests still PASS.

---

### Task 26: Clean up `multifilemodel.py` — type hints, no enum changes needed

**Files:**
- Modify: `ac7renamer/multifilemodel.py`

- [ ] **Step 1: Replace the file**

Replace the entire contents of `ac7renamer/multifilemodel.py` with:

```python
import re

from PySide6.QtGui import QStandardItem, QStandardItemModel

from ac7parser.Ac7CommonParameters import Ac7CommonParameters
from ac7renamer.columns import COL_NEWFILENAME, COL_NEWSTYLENAME


class MultiFileModel(QStandardItemModel):
    def __init__(self, rows: int, cols: int, parent) -> None:
        super().__init__(rows, cols, parent)
        self.parent = parent
        self.itemChanged.connect(self.on_change)

    def sanitize_filename(self, filename: str) -> str:
        s = str(filename).strip().replace(" ", "_")
        s = re.sub(r"(?u)[^-\w.]", "", s)
        if s and not s.lower().endswith(".ac7"):
            s = s + ".AC7"
        return s

    def on_change(self, item: QStandardItem) -> None:
        idx = self.indexFromItem(item)
        if idx.column() == COL_NEWSTYLENAME:
            item.setText(Ac7CommonParameters().sanitize_stylename(item.text()))
        elif idx.column() == COL_NEWFILENAME:
            item.setText(self.sanitize_filename(item.text()))
```

Notes: explicit import names replace the wildcard `from ac7renamer.columns import *`, type hints added, `'QStandardItem'` string forward reference replaced with the imported class.

- [ ] **Step 2: Run pytest**

Run:
```
.venv\Scripts\pytest.exe -v
```
Expected: all tests still PASS. `test_multifilemodel.py` exercises this file directly.

---

### Task 27: Add a type hint to `ac7renamer.py`

**Files:**
- Modify: `ac7renamer/ac7renamer.py`

- [ ] **Step 1: Add `-> None` to `main`**

In `ac7renamer/ac7renamer.py`, change the line `def main():` to `def main() -> None:`. No other changes.

- [ ] **Step 2: Run pytest**

Run:
```
.venv\Scripts\pytest.exe -v
```
Expected: all tests still PASS.

---

### Task 28: Create cross-platform `build.py`

**Files:**
- Create: `build.py`

- [ ] **Step 1: Write `build.py` at repo root**

Create `C:\development\python\casio\ac7renamer\build.py` with this exact content:

```python
"""Regenerate ac7renamerdlg.py from the .ui file.

Run after editing ac7renamer/ac7renamerdlg.ui in Qt Designer:

    python build.py

Works on Windows and Linux from any venv that has PySide6 installed.
"""
import subprocess
import sys
from pathlib import Path

PKG = Path(__file__).parent / "ac7renamer"


def main() -> None:
    subprocess.run(
        [
            sys.executable,
            "-m",
            "PySide6.scripts.pyside_tool",
            "uic",
            str(PKG / "ac7renamerdlg.ui"),
            "-o",
            str(PKG / "ac7renamerdlg.py"),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it to confirm it works**

Run:
```
.venv\Scripts\python.exe build.py
```
Expected: command exits cleanly. `ac7renamer\ac7renamerdlg.py` is regenerated (idempotent — should be byte-identical to what's already there since the .ui file hasn't changed since Task 21).

- [ ] **Step 3: Confirm pytest still passes**

Run:
```
.venv\Scripts\pytest.exe -v
```
Expected: all tests still PASS.

---

### Task 29: Delete `buildstep.sh`

**Files:**
- Delete: `ac7renamer/buildstep.sh`

- [ ] **Step 1: Remove the file**

Run:
```
git rm ac7renamer\buildstep.sh
```
Expected: `rm 'ac7renamer/buildstep.sh'`.

---

### Task 30: Generate `requirements.lock` with pip-tools

**Files:**
- Create: `requirements.lock`

- [ ] **Step 1: Install pip-tools (only needed by the maintainer)**

Run:
```
.venv\Scripts\pip.exe install pip-tools
```

- [ ] **Step 2: Generate the lockfile**

Run:
```
.venv\Scripts\python.exe -m piptools compile pyproject.toml -o requirements.lock --extra dev --extra build --no-header --resolver=backtracking
```
Expected: writes `requirements.lock` at repo root with pinned versions of PySide6, ac7parser, pytest, pyinstaller, and all transitives.

- [ ] **Step 3: Sanity-check the lockfile**

Run:
```
findstr /R "pyside6 ac7parser pytest pyinstaller" requirements.lock
```
Expected: at least one line per package, each pinned to an exact version (with `==`).

- [ ] **Step 4: Uninstall pip-tools again (optional)**

It's not part of the declared dependencies; the maintainer only needs it when regenerating the lock. Either uninstall or leave it — it doesn't affect anything downstream.

---

### Task 31: Rewrite `README.md`

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace the entire file**

Replace the contents of `README.md` with:

```markdown
# ac7renamer

GPLv3 charityware tool for renaming Casio AC7 rhythm files and editing their
display names. Built with PySide6.

## Development setup (Windows / Linux)

Requires Python 3.10+ and git on PATH.

    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Linux:
    source .venv/bin/activate

    pip install -e ".[dev,build]"

That installs ac7renamer, ac7parser (pulled from GitHub at the pinned commit),
PySide6, pytest, and pyinstaller into the venv.

Run the app:

    python ReStyle.py

Run the tests:

    pytest

## Working on ac7parser alongside ac7renamer

If you want to step into and edit ac7parser source while debugging ac7renamer,
shadow the installed copy with an editable install pointing at your local clone:

    git clone https://github.com/shimpe/ac7parser.git ../ac7parser
    pip install -e ../ac7parser

After that, edits to `../ac7parser/ac7parser/*.py` take effect immediately
(no reinstall) and the debugger steps into your working tree, not into
`site-packages`.

## Reproducing a known-good environment

The exact tested versions are pinned in `requirements.lock` (generated from
`pyproject.toml` with pip-tools). To install those specific versions:

    pip install -r requirements.lock

Regenerate the lock after changing dependencies in `pyproject.toml`:

    pip install pip-tools
    python -m piptools compile pyproject.toml -o requirements.lock \
        --extra dev --extra build --no-header --resolver=backtracking

## Regenerating the UI

After editing `ac7renamer/ac7renamerdlg.ui` (e.g. in Qt Designer):

    python build.py

That runs `pyside6-uic` to rewrite `ac7renamer/ac7renamerdlg.py`. The script
works on Windows and Linux out of any venv that has PySide6 installed.

## Building a standalone executable with PyInstaller

### Windows

    mkdir pyinstaller
    cd pyinstaller
    pyinstaller ..\ReStyle.py -F ^
      --add-data "..\ac7renamer\images;ac7renamer\images" ^
      --add-data "..\ac7renamer\ac7renamerdlg.ui;ac7renamer"

The standalone `ReStyle.exe` ends up in `pyinstaller\dist\`.

### Linux

    mkdir pyinstaller
    cd pyinstaller
    pyinstaller ../ReStyle.py -F \
      --add-data "../ac7renamer/images:ac7renamer/images" \
      --add-data "../ac7renamer/ac7renamerdlg.ui:ac7renamer"

The standalone `ReStyle` binary ends up in `pyinstaller/dist/`.

PySide6 PyInstaller hooks are installed automatically via
`pyinstaller-hooks-contrib` (a transitive dependency of pyinstaller); no
manual hook is needed.

## macOS

No build instructions yet. Patches with macOS build steps welcome.
```

- [ ] **Step 2: Final sanity check**

Run:
```
findstr /S /R "PyQt5" .
```
Expected: no matches anywhere in the repo (outside `.venv\`, `.git\`, `.idea\`, `pyinstaller\` build artifacts, and the historical `docs\superpowers\specs\` and `docs\superpowers\plans\` files which mention PyQt5 in context — those are fine).

---

### Task 32: Phase 2 smoke test (manual + pytest)

**Files:** none.

- [ ] **Step 1: Full pytest run**

Run:
```
.venv\Scripts\pytest.exe -v
```
Expected: all tests PASS (40 of them — 6 smoke + 9 sanitize + 25 ordering).

- [ ] **Step 2: Launch the app**

Run:
```
.venv\Scripts\python.exe ReStyle.py
```

Repeat the same manual smoke test as Phase 1 (Task 10 steps 1–5): window opens, About dialog renders with logo, splash flashes, single-file load/rename/save works, multi-file load/select/rename/rhythm-split works, app exits cleanly.

Additional Phase 2 checks:
- Window icon visible in the title bar (set in code via `setupUi` override in `myrenamerdlg.py`).
- Splash screen renders the logo (loaded from filesystem now, not from .qrc).
- About dialog renders the logo (same).

If any step fails, **do not commit**. Investigate, fix the underlying file, re-run pytest and the manual test.

---

### Task 33: Commit Phase 2

**Files:** none (commit step).

- [ ] **Step 1: Review staged + unstaged changes**

Run:
```
git status
git diff --stat
```
Expected (working tree changes since the Phase 1 commit, before staging):

```
A  pyproject.toml
A  requirements.lock
A  build.py
A  ac7renamer/resources.py
A  tests/__init__.py
A  tests/conftest.py
A  tests/test_smoke_imports.py
A  tests/test_multifilemodel.py
A  tests/test_singlefiletab_ordering.py
M  ac7renamer/ac7renamer.py
M  ac7renamer/myrenamerdlg.py
M  ac7renamer/singlefiletab.py
M  ac7renamer/multifiletab.py
M  ac7renamer/multifilemodel.py
M  ac7renamer/ac7renamerdlg.py
M  ac7renamer/ac7renamerdlg.ui
M  README.md
D  setup.py                            (from git rm)
D  ac7renamer/imageresources.qrc       (from git rm)
D  ac7renamer/imageresources_rc.py     (from git rm)
D  ac7renamer/buildstep.sh             (from git rm)
```

- [ ] **Step 2: Stage everything explicitly**

Run:
```
git add pyproject.toml requirements.lock build.py ac7renamer\resources.py tests\__init__.py tests\conftest.py tests\test_smoke_imports.py tests\test_multifilemodel.py tests\test_singlefiletab_ordering.py ac7renamer\ac7renamer.py ac7renamer\myrenamerdlg.py ac7renamer\singlefiletab.py ac7renamer\multifiletab.py ac7renamer\multifilemodel.py ac7renamer\ac7renamerdlg.py ac7renamer\ac7renamerdlg.ui README.md
```

The four deletions were already staged by `git rm` in earlier tasks. Don't run `git add -A` — it would sweep in `.idea\workspace.xml` and similar local IDE state.

- [ ] **Step 3: Verify staged contents**

Run:
```
git diff --staged --stat
```
Expected: 21 files, no `.venv\`, no `.idea\`, no surprising additions.

- [ ] **Step 4: Commit**

Run:
```
git commit -m "Modernize: pyproject, filesystem resources, tests, cleanup

- Replace setup.py with pyproject.toml (hatchling build backend).
- Drop .qrc resource workflow; load images from the package via importlib.resources.
- Add pytest suite for non-UI logic (sanitize_filename, LUT round-trip, smoke imports).
- Tighten enums to Qt6 scoped form across all modules.
- Collapse hardcoded 12-combo references in SingleFileTab into a loop.
- Remove no-op Buttons.rejected slot in SingleFileTab.
- Replace buildstep.sh with cross-platform build.py.
- Add requirements.lock (generated via pip-tools) for reproducible installs.
- Rewrite README with new dev-setup, editable-install, build, and pyinstaller instructions.

ac7parser is now pulled from GitHub at a pinned commit via the pyproject.toml
VCS dependency; the README documents the editable-install workflow for
developers who want to debug into ac7parser from a local clone."
```

Expected: one new commit on `pyside6-migration`.

- [ ] **Step 5: Verify two-commit branch state**

Run:
```
git log --oneline master..pyside6-migration
```
Expected: three commits ahead of master — the design-spec commit, the Phase 1 mechanical port, the Phase 2 modernization.

---

## Done

The branch `pyside6-migration` now contains the design spec, a working PySide6 port, and a modernized project structure. Merging to `master` and any post-merge cleanup are out of scope for this plan — handle them via the `superpowers:finishing-a-development-branch` skill when ready.
