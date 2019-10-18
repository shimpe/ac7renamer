from PyQt5.QtGui import QStandardItemModel
from ac7parser.Ac7CommonParameters import Ac7CommonParameters
from ac7renamer.columns import *
import re

class MultiFileModel(QStandardItemModel):
    def __init__(self, rows, cols, parent):
        super().__init__(rows, cols, parent)
        self.parent = parent
        self.itemChanged.connect(self.on_change)

    def sanitize_filename(self, filename):
        s = str(filename).strip().replace(' ', '_')
        s = re.sub(r'(?u)[^-\w.]', '', s)
        if s and not s.lower().endswith(".ac7"):
            s = s + ".AC7"
        return s

    def on_change(self, item: 'QStandardItem') -> None:
        idx = self.indexFromItem(item)
        if idx.column() == COL_NEWSTYLENAME:
            txt = item.text()
            txt = Ac7CommonParameters().sanitize_stylename(txt)
            item.setText(txt)
        elif idx.column() == COL_NEWFILENAME:
            txt = item.text()
            txt = self.sanitize_filename(txt)
            item.setText(txt)