import os
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path
from ac7parser.Ac7File import Ac7File
from ac7renamer.multifilemodel import MultiFileModel

class MultiFileTab(QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.file_loaded = False
        self.filename = ""
        self.home_folder = ""
        self.multi_file_model = MultiFileModel(0, 4, self)

    def setup_slots(self, homefolder):
        self.parent.loadFolderContent.clicked.connect(self.load_folder)
        self.home_folder = homefolder
        self.parent.fileListing.setModel(self.multi_file_model)
        self.setupTableHeader()

    def setupTableHeader(self):
        self.multi_file_model.setHorizontalHeaderLabels(
            ["Current filename", "Current Display name", "Desired Display name", "New filename"])
        self.parent.fileListing.resizeColumnsToContents()

    def collect_ac7files(self, location):
        return [filename for filename in Path(location).glob('*.AC7')]

    def load_folder(self):
        settings = QSettings('Ac7Renamer', 'Recently Used Files')
        start_folder = "{0}".format(settings.value('recentFolder', ""))
        if not start_folder:
            start_folder = self.home_folder

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
                self.multi_file_model.setItem(row, 0, QStandardItem(n))
                stylename = ""
                try:
                    ac7file = Ac7File()
                    ac7file.load_file(os.path.join(new_folder, n))
                    stylename = ac7file.properties['common_parameters'].properties['stylename']
                    binzero = stylename.find("\x00")
                    if binzero >= 0:
                        stylename = stylename[:binzero]
                except Exception as e:
                    stylename = "(Couldn't load)"
                self.multi_file_model.setItem(row, 1, QStandardItem(stylename))
                self.multi_file_model.setItem(row, 2, QStandardItem(""))
                self.multi_file_model.setItem(row, 3, QStandardItem(""))
            self.multi_file_model.blockSignals(False)
            self.setupTableHeader()