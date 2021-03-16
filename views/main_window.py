from PySide6.QtWidgets import QMainWindow
from gui.mainwindow import Ui_DressShopWindow
from .add_new_goods import AddNewGoodsDialog

class DressShopMainWindow(QMainWindow):

    def __init__(self):
        super(DressShopMainWindow, self).__init__()
        self.ui = Ui_DressShopWindow()
        self.ui.setupUi(self)

        self.ui.btn_add_new_goods.clicked.connect(self.add_new_goods)

    def add_new_goods(self):
        dialog = AddNewGoodsDialog(self)
        dialog.exec_()
