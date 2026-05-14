"""Regenerate ac7renamerdlg.py from the .ui file.

Run after editing ac7renamer/ac7renamerdlg.ui in Qt Designer:

    python build.py

Works on Windows and Linux from any venv that has PySide6 installed.
The --from-imports flag tells uic to emit package-relative imports
for the .qrc-generated resource module (when one is present).
"""
import shutil
import subprocess
import sys
from pathlib import Path

PKG = Path(__file__).parent / "ac7renamer"


def main() -> None:
    uic = shutil.which("pyside6-uic")
    if uic is None:
        sys.exit(
            "pyside6-uic not found on PATH. Activate the venv first, or install PySide6."
        )
    subprocess.run(
        [
            uic,
            "--from-imports",
            str(PKG / "ac7renamerdlg.ui"),
            "-o",
            str(PKG / "ac7renamerdlg.py"),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
