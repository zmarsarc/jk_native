from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIntValidator
from gui.add_new_goods_dialog import Ui_AddNewGoodsDialog

class AddNewGoodsDialog(QDialog):

    def __init__(self, parent=None):
        super(AddNewGoodsDialog, self).__init__(parent)
        self.ui = Ui_AddNewGoodsDialog()
        self.ui.setupUi(self)