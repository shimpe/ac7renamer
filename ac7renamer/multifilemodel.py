from PyQt5.QtGui import QStandardItemModel
from ac7parser.Ac7CommonParameters import Ac7CommonParameters

class MultiFileModel(QStandardItemModel):
    def __init__(self, rows, cols, parent):
        super().__init__(rows, cols, parent)
        self.parent = parent
        self.itemChanged.connect(self.on_change)

    def on_change(self, item: 'QStandardItem') -> None:
        txt = item.text()
        txt = Ac7CommonParameters().sanitize_stylename(txt)
        item.setText(txt)
