# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_goods_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_AddNewGoodsDialog(object):
    def setupUi(self, AddNewGoodsDialog):
        if not AddNewGoodsDialog.objectName():
            AddNewGoodsDialog.setObjectName(u"AddNewGoodsDialog")
        AddNewGoodsDialog.resize(400, 378)
        AddNewGoodsDialog.setModal(False)
        self.gridLayout_2 = QGridLayout(AddNewGoodsDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(AddNewGoodsDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.ipt_goods_name = QLineEdit(AddNewGoodsDialog)
        self.ipt_goods_name.setObjectName(u"ipt_goods_name")

        self.horizontalLayout.addWidget(self.ipt_goods_name)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(AddNewGoodsDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.sel_goods_type = QComboBox(AddNewGoodsDialog)
        self.sel_goods_type.setObjectName(u"sel_goods_type")

        self.horizontalLayout_2.addWidget(self.sel_goods_type)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(AddNewGoodsDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.ipt_cost = QLineEdit(AddNewGoodsDialog)
        self.ipt_cost.setObjectName(u"ipt_cost")

        self.horizontalLayout_3.addWidget(self.ipt_cost)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(AddNewGoodsDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.txt_comment = QPlainTextEdit(AddNewGoodsDialog)
        self.txt_comment.setObjectName(u"txt_comment")

        self.verticalLayout.addWidget(self.txt_comment)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(AddNewGoodsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(AddNewGoodsDialog)
        self.buttonBox.accepted.connect(AddNewGoodsDialog.accept)
        self.buttonBox.rejected.connect(AddNewGoodsDialog.reject)

        QMetaObject.connectSlotsByName(AddNewGoodsDialog)
    # setupUi

    def retranslateUi(self, AddNewGoodsDialog):
        AddNewGoodsDialog.setWindowTitle(QCoreApplication.translate("AddNewGoodsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddNewGoodsDialog", u"\u5546\u54c1\u540d", None))
        self.label_2.setText(QCoreApplication.translate("AddNewGoodsDialog", u"\u7c7b\u578b", None))
        self.label_3.setText(QCoreApplication.translate("AddNewGoodsDialog", u"\u6210\u672c", None))
        self.label_4.setText(QCoreApplication.translate("AddNewGoodsDialog", u"\u5907\u6ce8", None))
    # retranslateUi

