from PySide6.QtWidgets import QTableView
from PySide6.QtCore import QItemSelection, Signal, Qt

class GoodsView(QTableView):

    selectedGoodsChanged = Signal(object)

    def __init__(self, parent=None):
        super(GoodsView, self).__init__(parent)

    def selectionChanged(self, sel: QItemSelection, desel: QItemSelection):
        super(GoodsView, self).selectionChanged(sel, desel)

        indexes = sel.indexes()
        if len(indexes) == 0:
            return

        goods = self.model().data(indexes[0], Qt.EditRole)
        self.selectedGoodsChanged.emit(goods)