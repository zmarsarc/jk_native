# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_jk_stock_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_AddJKStock(object):
    def setupUi(self, AddJKStock):
        if not AddJKStock.objectName():
            AddJKStock.setObjectName(u"AddJKStock")
        AddJKStock.resize(193, 101)
        AddJKStock.setMinimumSize(QSize(193, 101))
        AddJKStock.setMaximumSize(QSize(193, 101))
        self.gridLayout = QGridLayout(AddJKStock)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(AddJKStock)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.sel_size = QComboBox(AddJKStock)
        self.sel_size.setObjectName(u"sel_size")

        self.horizontalLayout.addWidget(self.sel_size)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(AddJKStock)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.ipt_length = QSpinBox(AddJKStock)
        self.ipt_length.setObjectName(u"ipt_length")
        self.ipt_length.setMinimum(30)
        self.ipt_length.setValue(43)

        self.horizontalLayout_2.addWidget(self.ipt_length)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(AddJKStock)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.ipt_count = QLineEdit(AddJKStock)
        self.ipt_count.setObjectName(u"ipt_count")

        self.horizontalLayout_3.addWidget(self.ipt_count)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(AddJKStock)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)


        self.retranslateUi(AddJKStock)
        self.buttonBox.accepted.connect(AddJKStock.accept)
        self.buttonBox.rejected.connect(AddJKStock.reject)

        QMetaObject.connectSlotsByName(AddJKStock)
    # setupUi

    def retranslateUi(self, AddJKStock):
        AddJKStock.setWindowTitle(QCoreApplication.translate("AddJKStock", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddJKStock", u"\u5c3a\u7801", None))
        self.label_2.setText(QCoreApplication.translate("AddJKStock", u"\u88d9\u957f", None))
        self.label_3.setText(QCoreApplication.translate("AddJKStock", u"\u5e93\u5b58", None))
    # retranslateUi

