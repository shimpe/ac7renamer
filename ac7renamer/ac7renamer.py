import sys
import ac7renamer.myrenamerdlg
from PyQt5 import QtWidgets
from pathlib import Path

def main():
    app = QtWidgets.QApplication(sys.argv)
    Ac7Ren = QtWidgets.QDialog()
    ui = ac7renamer.myrenamerdlg.MyRenamerDlg()
    ui.setupUi(Ac7Ren)
    home = str(Path.home())
    ui.setup_slots(home)
    Ac7Ren.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
