import re

from PySide6.QtGui import QStandardItem, QStandardItemModel

from ac7parser.Ac7CommonParameters import Ac7CommonParameters
from ac7renamer.columns import COL_NEWFILENAME, COL_NEWSTYLENAME


class MultiFileModel(QStandardItemModel):
    def __init__(self, rows: int, cols: int, parent) -> None:
        # Do not store parent as self.parent — that shadows QObject.parent()
        # and breaks PySide6 signal delivery.
        super().__init__(rows, cols, parent)
        self.itemChanged.connect(self.on_change)

    def sanitize_filename(self, filename: str) -> str:
        s = str(filename).strip().replace(" ", "_")
        s = re.sub(r"(?u)[^-\w.]", "", s)
        if s and not s.lower().endswith(".ac7"):
            s = s + ".AC7"
        return s

    def on_change(self, item: QStandardItem) -> None:
        idx = self.indexFromItem(item)
        if idx.column() == COL_NEWSTYLENAME:
            item.setText(Ac7CommonParameters().sanitize_stylename(item.text()))
        elif idx.column() == COL_NEWFILENAME:
            item.setText(self.sanitize_filename(item.text()))
