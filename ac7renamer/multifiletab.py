import os
import shutil
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from pathlib import Path
from ac7parser.Ac7File import Ac7File
from ac7renamer.multifilemodel import MultiFileModel
from ac7renamer.columns import *

class MultiFileTab(QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.file_loaded = False
        self.filename = ""
        self.home_folder = ""
        self.folder = ""
        self.multi_file_model = MultiFileModel(0, 5, self)

    def setup_slots(self, homefolder):
        self.parent.loadFolderContent.clicked.connect(self.load_folder)
        self.parent.renameFolderContent.clicked.connect(self.rename_folder)
        self.home_folder = homefolder
        self.parent.fileListing.setModel(self.multi_file_model)
        self.setupTableHeader()

    def setupTableHeader(self):
        self.multi_file_model.setHorizontalHeaderLabels(
            ["Current filename", "Current Display name", "Desired Display name", "New filename", "Error msg"])
        self.parent.fileListing.resizeColumnsToContents()

    def collect_ac7files(self, location):
        return [filename for filename in Path(location).glob('*.AC7')]

    def load_folder(self):
        settings = QSettings('Ac7Renamer', 'Recently Used Files')
        start_folder = "{0}".format(settings.value('recentFolder', ""))
        if not start_folder:
            start_folder = self.home_folder
        self.folder = start_folder
        fname = QFileDialog.getExistingDirectory(None, 'Open folder',
                                                 start_folder,
                                                 options=QFileDialog.DontUseNativeDialog|QFileDialog.ShowDirsOnly)
        if fname:
            new_folder = fname
            settings.setValue('recentFolder', new_folder)
            files = self.collect_ac7files(new_folder)
            basenames = [f.name for f in files]
            self.multi_file_model.blockSignals(True)
            self.multi_file_model.clear()
            for row, n in enumerate(basenames):
                self.multi_file_model.setItem(row, COL_FILENAME, QStandardItem(n))
                stylename = ""
                errormsg = ""
                try:
                    ac7file = Ac7File()
                    ac7file.load_file(os.path.join(new_folder, n))
                    stylename = ac7file.properties['common_parameters'].properties['stylename']
                    binzero = stylename.find("\x00")
                    if binzero >= 0:
                        stylename = stylename[:binzero]
                except Exception as e:
                    errormsg = "Couldn't load"
                self.multi_file_model.setItem(row, COL_STYLENAME, QStandardItem(stylename))
                self.multi_file_model.setItem(row, COL_NEWSTYLENAME, QStandardItem(""))
                self.multi_file_model.setItem(row, COL_NEWFILENAME, QStandardItem(""))
                self.multi_file_model.setItem(row, COL_ERROR, QStandardItem(errormsg))
            self.multi_file_model.blockSignals(False)
            self.setupTableHeader()
            self.file_loaded = True

    def rename_folder(self):

        if not self.file_loaded or self.multi_file_model.rowCount() < 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("No files loaded")
            msg.setInformativeText("Please load a folder with .AC7 files before attempting to save.")
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
            return

        settings = QSettings('Ac7Renamer', 'Recently Used Files')
        start_folder = "{0}".format(settings.value('recentFolder', ""))
        if not start_folder:
            start_folder = self.home_folder
        fname = QFileDialog.getExistingDirectory(None, 'Open folder',
                                                 start_folder,
                                                 options=QFileDialog.DontUseNativeDialog|QFileDialog.ShowDirsOnly)
        if fname:
            self.multi_file_model.blockSignals(True)
            new_folder = fname
            settings.setValue('recentFolder', new_folder)
            rows = self.multi_file_model.rowCount()
            for r in range(rows):
                errormsg = ""
                old_filename = self.multi_file_model.item(r, COL_FILENAME).text()
                desired_stylename = self.multi_file_model.item(r, COL_NEWSTYLENAME).text()
                desired_filename = self.multi_file_model.item(r, COL_NEWFILENAME).text()
                need_backup = False
                if desired_stylename.strip():
                    if not desired_filename.strip():
                        desired_filename = old_filename
                    full_desired_filename = os.path.join(new_folder, desired_filename)
                    if os.path.exists(full_desired_filename):
                        backup_filename = full_desired_filename + "_bak"
                        i = 0
                        found = False
                        while i < 1000 and not found:
                            if os.path.exists(backup_filename):
                                backup_filename = full_desired_filename+"_backup_{0}".format(i)
                                i = i + 1
                            else:
                                found = True
                        try:
                            shutil.copyfile(full_desired_filename, backup_filename)
                        except Exception as e:
                            errormsg = e.__repr__()
                    ac7file = Ac7File()
                    try:
                        ac7file.load_file(os.path.join(self.folder, old_filename))
                        ac7file.properties["common_parameters"].properties["stylename"] = desired_stylename
                        ac7file.write_file(full_desired_filename, True, False)
                        errormsg = "Success!"
                    except Exception as e:
                        errormsg = e.__repr__()
                    self.multi_file_model.setItem(r, COL_ERROR, QStandardItem(errormsg))
            self.multi_file_model.blockSignals(False)