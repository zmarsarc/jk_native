from PySide6.QtWidgets import QMainWindow, QDialog
from gui.mainwindow import Ui_DressShopWindow
from .add_new_goods import AddNewGoodsDialog
from models import Goods

class DressShopMainWindow(QMainWindow):

    def __init__(self, goodsdata):
        super(DressShopMainWindow, self).__init__()
        self.ui = Ui_DressShopWindow()
        self.ui.setupUi(self)

        self.ui.btn_add_new_goods.clicked.connect(self.add_new_goods)

        self._goods_model = Goods(goodsdata, self)
        self.ui.goods_view.setModel(self._goods_model)

    def add_new_goods(self):
        dialog = AddNewGoodsDialog(self._goods_model.types(), self)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            data = dialog.goods_data()
            self._goods_model.add_new_goods({
                'name': data[0],
                'goods_type': data[1],
                'comment': data[2] if data[2] != '' else None
            })
