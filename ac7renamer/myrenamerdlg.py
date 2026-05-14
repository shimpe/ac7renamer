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
