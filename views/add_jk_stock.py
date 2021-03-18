from PySide6.QtWidgets import QDialog
from .ui_add_jk_stock_dialog import Ui_AddJKStock


class AddJKStock(QDialog):

    def __init__(self, parent=None):
        super(AddJKStock, self).__init__(parent)
        self.ui = Ui_AddJKStock()
        self.ui.setupUi(self)
