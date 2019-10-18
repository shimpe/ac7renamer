import ac7renamer.ac7renamerdlg
from pathlib import Path
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QSettings
from ac7parser.Ac7File import Ac7File
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class MyRenamerDlg(ac7renamer.ac7renamerdlg.Ui_Ac7Renamer):
    def __init__(self):
        super().__init__()
        self.home_folder = None
        self.ac7file = Ac7File()
        self.file_loaded = False
        self.filename = ""

    def setup_slots(self, homefolder):
        self.pushButton.clicked.connect(self.load_ac7_file_clicked)
        self.aboutButton.clicked.connect(self.about_clicked)
        self.saveButton.clicked.connect(self.save_clicked)
        self.home_folder = homefolder
        reg_ex = QRegExp(r"[A-Za-z0-9 #\(\)\*\+\-,\$!\"\\':;/<=>\?@\[\]\^_{}~\|]{1,12}")
        input_validator = QRegExpValidator(reg_ex, self.desiredDisplayName)
        self.desiredDisplayName.setValidator(input_validator)
        self.Buttons.rejected.connect(self.reject)
        settings = QSettings('Ac7Renamer', 'EulaAccepted')
        if not settings.value("Accepted", 0):
            self.about_clicked()
            settings.setValue('Accepted', 1)
        self.pushButton.setFocus()

    def load_ac7_file_clicked(self):
        settings = QSettings('Ac7Renamer', 'Recently Used Files')
        start_folder = "{0}".format(settings.value('recentFolder', ""))
        if not start_folder:
            start_folder = self.home_folder
        fname = QFileDialog.getOpenFileName(None, 'Open file',
                                            start_folder,
                                            "AC7 Rhythm files (*.AC7);;all files (*.*)",
                                            options=QFileDialog.DontUseNativeDialog)

        if fname and fname[0]:
            fname = fname[0]
            new_folder = Path(fname).parents[0]
            settings.setValue('recentFolder', new_folder)
            if fname:
                try:
                    self.ac7file.load_file(fname)
                    stylename = self.ac7file.properties['common_parameters'].properties['stylename']
                    binzero = stylename.find("\x00")
                    if binzero >= 0:
                        stylename = stylename[:binzero]
                    self.currentDisplayName.setText(stylename)
                    self.desiredDisplayName.setText("")
                    self.file_loaded = True
                    self.filename = Path(fname).name
                    self.desiredDisplayName.setFocus()
                except Exception as e:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Unable to load the file")
                    msg.setInformativeText(
                        "There was a problem parsing {0}. Please log a bug on https://github.com/shimpe/ac7renamer/issues and attach your .AC7 file".format(
                            fname))
                    msg.setWindowTitle("ReStyle Warning")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDetailedText(e.__repr__())
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.exec_()

    def save_clicked(self):
        if self.file_loaded:
            txt = self.desiredDisplayName.text()
            if not txt:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("No desired display name")
                msg.setInformativeText("Please type a desired name before attempting to save the file.")
                msg.setWindowTitle("ReStyle Warning")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.exec_()

            else:
                settings = QSettings('Ac7Renamer', 'Recently Used Files')
                start_folder = "{0}".format(settings.value('recentFolder', ""))
                if not start_folder:
                    start_folder = self.home_folder

                fname = QFileDialog.getSaveFileName(None, 'Save file {0} as...'.format(self.filename),
                                                    start_folder,
                                                    "AC7 Rhythm files (*.AC7);;all files (*.*)",
                                                    options=QFileDialog.DontUseNativeDialog)
                if fname and fname[0]:
                    fname = fname[0]
                    self.ac7file.properties['common_parameters'].properties['stylename'] = txt
                    try:
                        self.ac7file.write_file(fname, True, False)
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Successfully saved {0}!".format(fname))
                        msg.setWindowTitle("ReStyle Information")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.exec_()
                        self.pushButton.setFocus()
                    except Exception as e:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Unable to save the file")
                        msg.setInformativeText(
                            "There was a problem saving {0}. Please log a bug on https://github.com/shimpe/ac7renamer/issues and attach your .ac7 file".format(
                                fname))
                        msg.setWindowTitle("ReStyle Warning")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDetailedText(e.__repr__())
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("No file loaded")
            msg.setInformativeText("Please load an .AC7 file before attempting to save one.")
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()

    def reject(self):
        pass

    def about_clicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("About this tool...")
        msg.setInformativeText("Tool to change how .AC7 files are displayed by your keyboard.\n\n"
                               "I strongly encourage you to make a donation to your favorite charity if you decide to keep using this tool.\n\n"
                               "You can use, modify and copy the tool freely under the guarantees of the GPLv3 license.\n\n"
                               "Complete source code can be found at https://github.com/shimpe/ac7renamer\n\n"
                               "You may copy, distribute and modify the "
                               "software as long as you track changes/dates. Any modifications to, "
                               "or software including (via compiler) GPL-licensed code, must also be made available "
                               "under the GPL along with build & install instructions.\n\n"
                               "I try to offer the best possible software, but cannot promise that the software will always be bug-free, available, accurate, complete, and up-to-date. "
                               "You agree that when you use this software, you do so at your own risk, and this software or affiliated persons and organizations are not in any way responsible for damage or weird behavior inflicted on your instrument. Furthermore, you also agree that you will not attempt to hold us or our data providers liable for damage or inaccuracies in the implementation.\n\n"
                               "If you cannot agree to these terms, then under no circumstance use this software or files created with this software.")
        msg.setWindowTitle("About")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()
