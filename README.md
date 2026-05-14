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
