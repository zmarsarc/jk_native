from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QStringListModel
from .ui_add_new_goods_dialog import Ui_AddNewGoodsDialog

class AddNewGoodsDialog(QDialog):

    def __init__(self, goods_types=[], parent=None):
        super(AddNewGoodsDialog, self).__init__(parent)
        self.ui = Ui_AddNewGoodsDialog()
        self.ui.setupUi(self)
        self._goods_types = goods_types
        self.ui.sel_goods_type.setModel(QStringListModel([x.name for x in goods_types]))

    def goods_data(self):
        return (
            self.ui.ipt_goods_name.text(), self._goods_types[self.ui.sel_goods_type.currentIndex()],
            self.ui.txt_comment.document().toPlainText())