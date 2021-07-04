import ac7renamer.ac7renamerdlg
from PyQt5.QtWidgets import QMessageBox
from ac7renamer.singlefiletab import SingleFileTab
from ac7renamer.multifiletab import MultiFileTab
from PyQt5.QtCore import QSettings, Qt
from PyQt5.QtGui import QPixmap


class MyRenamerDlg(ac7renamer.ac7renamerdlg.Ui_Ac7Renamer):
    def __init__(self):
        super().__init__()
        self.home_folder = None
        self.tab_handlers = {'singlefile': SingleFileTab(self), 'multifile': MultiFileTab(self)}

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
        msg.exec_()
