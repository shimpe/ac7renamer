from pathlib import Path

from PySide6.QtCore import QObject, QRegularExpression, QSettings, Qt
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QFileDialog, QMessageBox

from ac7parser.Ac7File import Ac7File


class SingleFileTab(QObject):
    # lut is ordered as in the .ac7 file
    # do not change the order in lut_in_file_order
    # rather, change the ordering in the .ui file if needed
    # if you do, make sure to swap both the current and corresponding destination fields
    lut_in_file_order = [
        "intro (1)", "normal (1)", "var (2)", "fill-in (1)", "fill-in (2)", "end (1)",
        "intro (2)", "var (3)", "var (4)", "fill-in (3)", "fill-in (4)", "end (2)",
    ]
    lut_in_ui_order = [
        "intro (1)", "normal (1)", "fill-in (1)", "var (2)", "fill-in (2)", "end (1)",
        "var (3)", "fill-in (3)", "var (4)", "fill-in (4)", "intro (2)", "end (2)",
    ]

    def __init__(self, parent) -> None:
        # Stored as self.dlg, not self.parent — assigning self.parent would
        # shadow QObject.parent() and break PySide6 signal delivery.
        super().__init__()
        self.dlg = parent
        self.ac7file = Ac7File()
        self.file_loaded = False
        self.filename = ""
        self.home_folder = ""
        self.no_of_el = 0
        self.ordering: list[int] = []
        self.combos_in_file_order: list = []

    def file_order_to_ui_order(self, file_order_index: int) -> int:
        return self.lut_in_ui_order.index(self.lut_in_file_order[file_order_index])

    def ui_order_to_file_order(self, ui_order_index: int) -> int:
        return self.lut_in_file_order.index(self.lut_in_ui_order[ui_order_index])

    def setup_slots(self, homefolder: str) -> None:
        self.dlg.pushButton.clicked.connect(self.load_ac7_file_clicked)
        self.dlg.saveButton.clicked.connect(self.save_clicked)
        self.home_folder = homefolder
        reg_ex = QRegularExpression(
            r"[A-Za-z0-9 #\(\)\.\*\+\-,\$!\"\\':;/<=&>\?@\[\]\^_{}~\|]{1,12}"
        )
        input_validator = QRegularExpressionValidator(reg_ex, self.dlg.desiredDisplayName)
        self.dlg.desiredDisplayName.setValidator(input_validator)
        self.combos_in_file_order = [
            getattr(self.dlg, f"desEl{i + 1}") for i in range(12)
        ]
        self.dlg.pushButton.setFocus()

    def load_ac7_file_clicked(self) -> None:
        settings = QSettings("Ac7Renamer", "Recently Used Files")
        start_folder = "{0}".format(settings.value("recentFolder", "")) or self.home_folder
        fname = QFileDialog.getOpenFileName(
            None,
            "Open file",
            start_folder,
            "AC7 Rhythm files (*.AC7);;all files (*.*)",
            options=QFileDialog.Option.DontUseNativeDialog,
        )
        if not (fname and fname[0]):
            return
        fname = fname[0]
        settings.setValue("recentFolder", Path(fname).parents[0])
        try:
            self.ac7file.load_file(fname)
            stylename = self.ac7file.properties["common_parameters"].properties["stylename"]
            binzero = stylename.find("\x00")
            if binzero >= 0:
                stylename = stylename[:binzero]
            self.dlg.currentDisplayName.setText(stylename)
            self.dlg.desiredDisplayName.setText("")
            self.file_loaded = True
            self.filename = Path(fname).name
            self.dlg.desiredDisplayName.setFocus()
            self.set_number_of_elements(
                len(self.ac7file.properties["common_parameters"].properties["overall_parameters"]["elements"])
            )
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Unable to load the file")
            msg.setTextFormat(Qt.TextFormat.RichText)
            msg.setInformativeText(
                "There was a problem parsing {0}. Please log a bug in <href a='https://github.com/shimpe/ac7renamer/issues'>the bug database</href> and attach your .AC7 file".format(fname)
            )
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDetailedText(e.__repr__())
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()

    def save_clicked(self) -> None:
        self.ordering = [
            self.ui_order_to_file_order(self.combos_in_file_order[i].currentIndex())
            for i in range(self.no_of_el)
        ]

        if not self.file_loaded:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("No file loaded")
            msg.setInformativeText("Please load an .AC7 file before attempting to save one.")
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        txt = self.dlg.desiredDisplayName.text()
        if not txt:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("No desired display name")
            msg.setInformativeText("Please type a desired name before attempting to save the file.")
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        settings = QSettings("Ac7Renamer", "Recently Used Files")
        start_folder = "{0}".format(settings.value("recentFolder", "")) or self.home_folder
        fname = QFileDialog.getSaveFileName(
            None,
            "Save file {0} as...".format(self.filename),
            start_folder,
            "AC7 Rhythm files (*.AC7);;all files (*.*)",
            options=QFileDialog.Option.DontUseNativeDialog,
        )
        if not (fname and fname[0]):
            return
        fname = fname[0]
        if not fname.lower().endswith(".ac7"):
            fname = fname + ".AC7"
        self.ac7file.properties["common_parameters"].properties["stylename"] = txt
        try:
            self.ac7file.set_custom_element_ordering(self.ordering)
            self.ac7file.prepare_for_save()
            self.ac7file.write_file(fname, True, False)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Successfully saved {0}!".format(fname))
            msg.setWindowTitle("ReStyle Information")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()
            self.dlg.pushButton.setFocus()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Unable to save the file")
            msg.setTextFormat(Qt.TextFormat.RichText)
            msg.setInformativeText(
                "There was a problem saving {0}. Please log a bug in <href a='https://github.com/shimpe/ac7renamer/issues'>the bug database</href> and attach your .ac7 file".format(fname)
            )
            msg.setWindowTitle("ReStyle Warning")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDetailedText(e.__repr__())
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()

    def set_number_of_elements(self, no_of_el: int) -> None:
        self.no_of_el = no_of_el
        for index_in_file_order, c in enumerate(self.combos_in_file_order):
            c.clear()
            c.setEnabled(index_in_file_order < no_of_el)
            for index_in_ui_order, label in enumerate(self.lut_in_ui_order):
                if self.ui_order_to_file_order(index_in_ui_order) < no_of_el:
                    c.addItem(label)
            c.setCurrentIndex(self.file_order_to_ui_order(index_in_file_order))
