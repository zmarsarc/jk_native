from typing import List
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QStringListModel
from .ui_add_jk_stock_dialog import Ui_AddJKStock
from models import inventory

class AddJKStock(QDialog):

    def __init__(self, sizes: List[inventory.JKSize.Size] = [], parent=None):
        super(AddJKStock, self).__init__(parent)
        
        self.ui = Ui_AddJKStock()
        self.ui.setupUi(self)

        self._sizes = sizes
        self.ui.sel_size.setModel(QStringListModel([x.name for x in self._sizes]))

    def jk_data(self):
        return (self._sizes[self.ui.sel_size.currentIndex()], self.ui.ipt_length.value(),
            int(self.ui.ipt_count.text()))
