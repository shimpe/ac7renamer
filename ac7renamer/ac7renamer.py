import sys
import ac7renamer.myrenamerdlg
from PyQt5 import QtWidgets
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
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
