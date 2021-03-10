from PySide6.QtWidgets import *
from PySide6.QtGui import *


class JKTableView(QTableView):

    def __init__(self, parent=None):
        super(JKTableView, self).__init__(parent)

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu(self)
        action = QAction(text='Remove')
        action.triggered.connect(self.remove_jk)
        menu.addAction(action)
        menu.exec_(event.globalPos())

    def remove_jk(self):
        self.model().removeRows(self.currentIndex().row(), 1)
