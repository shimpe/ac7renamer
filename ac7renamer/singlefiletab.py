from PyQt5.QtCore import QObject
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QRegExpValidator
from pathlib import Path
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from ac7parser.Ac7File import Ac7File


class SingleFileTab(QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ac7file = Ac7File()
        self.file_loaded = False
        self.filename = ""
        self.home_folder = ""
        self.no_of_el = 0
        # lut is ordered as in the .ac7 file
        # do not change the order in lut
        # rather, change the ordering in the .ui file if needed
        # if you do, make sure to swap both the current and corresponding destination fields
        self.lut_in_file_order = ["intro (1)",
                    "normal (1)",
                    "var (2)",
                    "fill-in (1)",
                    "fill-in (2)",
                    "end (1)",
                    "intro (2)",
                    "var (3)",
                    "var (4)",
                    "fill-in (3)",
                    "fill-in (4)",
                   "end (2)"]
        self.lut_in_ui_order = ["intro (1)",
                    "normal (1)",
                    "fill-in (1)",
                    "var (2)",
                    "fill-in (2)",
                    "end (1)",
                    "var (3)",
                    "fill-in (3)",
                    "var (4)",
                    "fill-in (4)",
                    "intro (2)",
                    "end (2)"]
        self.ordering = []
        self.combos_in_file_order = []

    def file_order_to_ui_order(self, file_order_index):
        txt = self.lut_in_file_order[file_order_index]
        return self.lut_in_ui_order.index(txt)

    def ui_order_to_file_order(self, ui_order_index):
        txt = self.lut_in_ui_order[ui_order_index]
        return self.lut_in_file_order.index(txt)

    def setup_slots(self, homefolder):
        self.parent.pushButton.clicked.connect(self.load_ac7_file_clicked)
        self.parent.saveButton.clicked.connect(self.save_clicked)
        self.home_folder = homefolder
        reg_ex = QRegExp(r"[A-Za-z0-9 #\(\)\.\*\+\-,\$!\"\\':;/<=&>\?@\[\]\^_{}~\|]{1,12}")
        input_validator = QRegExpValidator(reg_ex, self.parent.desiredDisplayName)
        self.parent.desiredDisplayName.setValidator(input_validator)
        self.parent.Buttons.rejected.connect(self.reject)
        self.combos_in_file_order = [
            self.parent.desEl1,
            self.parent.desEl2,
            self.parent.desEl3,
            self.parent.desEl4,
            self.parent.desEl5,
            self.parent.desEl6,
            self.parent.desEl7,
            self.parent.desEl8,
            self.parent.desEl9,
            self.parent.desEl10,
            self.parent.desEl11,
            self.parent.desEl12]
        self.parent.pushButton.setFocus()

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
                    self.parent.currentDisplayName.setText(stylename)
                    self.parent.desiredDisplayName.setText("")
                    self.file_loaded = True
                    self.filename = Path(fname).name
                    self.parent.desiredDisplayName.setFocus()
                    self.set_number_of_elements(len(self.ac7file.properties['common_parameters'].properties['overall_parameters']['elements']))
                except Exception as e:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Unable to load the file")
                    msg.setTextFormat(Qt.RichText)
                    msg.setInformativeText(
                        "There was a problem parsing {0}. Please log a bug in <href a='https://github.com/shimpe/ac7renamer/issues'>the bug database</href> and attach your .AC7 file".format(
                            fname))
                    msg.setWindowTitle("ReStyle Warning")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDetailedText(e.__repr__())
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.exec_()

    def save_clicked(self):
        self.ordering = []
        for index_in_file_order in range(self.no_of_el):
            self.ordering.append(self.ui_order_to_file_order(self.combos_in_file_order[index_in_file_order].currentIndex()))

        if self.file_loaded:
            txt = self.parent.desiredDisplayName.text()
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
                    if not fname.lower().endswith(".ac7"):
                        fname = fname + ".AC7"
                    self.ac7file.properties['common_parameters'].properties['stylename'] = txt
                    try:
                        self.ac7file.set_custom_element_ordering(self.ordering)
                        self.ac7file.prepare_for_save()
                        self.ac7file.write_file(fname, True, False)
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Successfully saved {0}!".format(fname))
                        msg.setWindowTitle("ReStyle Information")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.exec_()
                        self.parent.pushButton.setFocus()
                    except Exception as e:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Unable to save the file")
                        msg.setTextFormat(Qt.RichText)
                        msg.setInformativeText(
                            "There was a problem saving {0}. Please log a bug in <href a='https://github.com/shimpe/ac7renamer/issues'>the bug database</href> and attach your .ac7 file".format(
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

    def set_number_of_elements(self, no_of_el):
        self.no_of_el = no_of_el
        for index_in_file_order, c in enumerate(self.combos_in_file_order):
            c.clear()
            if index_in_file_order >= no_of_el:
                c.setEnabled(False)
            else:
                c.setEnabled(True)
            for index_in_ui_order, l in enumerate(self.lut_in_ui_order):
                inner_index_in_file_order = self.ui_order_to_file_order(index_in_ui_order)
                if inner_index_in_file_order < no_of_el:
                    c.addItem(l)
            c.setCurrentIndex(self.file_order_to_ui_order(index_in_file_order))
