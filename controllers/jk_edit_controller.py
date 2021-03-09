from PySide6.QtWidgets import *
from PySide6.QtCore import *


class JKSizeEditController(QItemDelegate):

    def __init__(self, parent=None):
        super(JKSizeEditController, self).__init__(parent)

    def createEditor(self, parent, option, index):
        """设置编辑器，对尺码只提供有限的选项"""
        selector = QComboBox(parent)
        return selector

    def setEditorData(self, editor: QComboBox, index: QModelIndex):
        pass

    def setModelData(self, editor, model, index):
        pass

    def updateEditorGeometry(self, editor: QComboBox, option: QStyleOptionViewItem, index):
        editor.setGeometry(option.rect)
