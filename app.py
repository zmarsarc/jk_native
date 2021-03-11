import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from models.database import Database
from models.jk_model import JKModel
from controllers.jk_edit_controller import JKEditController
from views.jk_tableview import JKTableView

class DressShop(QMainWindow):

    def __init__(self, data: Database, parent=None):
        super(DressShop, self).__init__(parent)

        self._model = JKModel(data)

        self._create_menubar()
        self._create_statusbar()
        self._create_central_widget()
        self._create_dock_tool_bar()

        self.setMinimumSize(800, 600)

    def _create_menubar(self):
        menubar = QMenuBar(self)

        application = menubar.addMenu('application')
        application.addAction('quit', self.close)

        self.setMenuBar(menubar)

    def _create_statusbar(self):
        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)

    def _create_central_widget(self):
        view = JKTableView(self)
        view.setItemDelegate(JKEditController())
        view.setModel(self._model)
        self.setCentralWidget(view)

    def _create_dock_tool_bar(self):
        toolbar = QDockWidget(self)
        
        button_container = QWidget(toolbar)
        root = QHBoxLayout(button_container)
        button_container.setLayout(root)
        root.addWidget(QPushButton('new'))
        root.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))

        toolbar.setWidget(button_container)
        
        self.addDockWidget(Qt.TopDockWidgetArea, toolbar)


if __name__ == '__main__':
    data = Database('storage.db')

    app = QApplication(sys.argv)
    shop = DressShop(data)
    shop.show()
    sys.exit(app.exec_())
