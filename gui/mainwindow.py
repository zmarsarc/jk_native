# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resource_rc

class Ui_DressShopWindow(object):
    def setupUi(self, DressShopWindow):
        if not DressShopWindow.objectName():
            DressShopWindow.setObjectName(u"DressShopWindow")
        DressShopWindow.resize(800, 600)
        self.centralwidget = QWidget(DressShopWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.store_tab = QWidget()
        self.store_tab.setObjectName(u"store_tab")
        self.gridLayout_2 = QGridLayout(self.store_tab)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.store_tool_bar = QWidget(self.store_tab)
        self.store_tool_bar.setObjectName(u"store_tool_bar")
        self.store_tool_bar.setMaximumSize(QSize(16777215, 64))
        self.store_tool_bar.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.store_tool_bar)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_add_new_goods = QPushButton(self.store_tool_bar)
        self.btn_add_new_goods.setObjectName(u"btn_add_new_goods")
        self.btn_add_new_goods.setMinimumSize(QSize(64, 64))
        self.btn_add_new_goods.setMaximumSize(QSize(64, 64))
        self.btn_add_new_goods.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_add_new_goods, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.store_tool_bar)

        self.store_main_view = QFrame(self.store_tab)
        self.store_main_view.setObjectName(u"store_main_view")
        self.horizontalLayout = QHBoxLayout(self.store_main_view)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dockWidget_4 = QDockWidget(self.store_main_view)
        self.dockWidget_4.setObjectName(u"dockWidget_4")
        self.dockWidget_4.setFeatures(QDockWidget.DockWidgetMovable)
        self.dockWidget_4.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.gridLayout_4 = QGridLayout(self.dockWidgetContents_4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.goods_view = QTableView(self.dockWidgetContents_4)
        self.goods_view.setObjectName(u"goods_view")

        self.gridLayout_4.addWidget(self.goods_view, 0, 0, 1, 1)

        self.dockWidget_4.setWidget(self.dockWidgetContents_4)

        self.horizontalLayout.addWidget(self.dockWidget_4)

        self.dockWidget_2 = QDockWidget(self.store_main_view)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidget_2.setFeatures(QDockWidget.DockWidgetMovable)
        self.dockWidget_2.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.gridLayout_5 = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.inventory_view = QTableView(self.dockWidgetContents_2)
        self.inventory_view.setObjectName(u"inventory_view")

        self.gridLayout_5.addWidget(self.inventory_view, 0, 0, 1, 1)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)

        self.horizontalLayout.addWidget(self.dockWidget_2)


        self.verticalLayout.addWidget(self.store_main_view)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.store_tab, "")
        self.orders_tab = QWidget()
        self.orders_tab.setObjectName(u"orders_tab")
        self.tabWidget.addTab(self.orders_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        DressShopWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DressShopWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.application_menu = QMenu(self.menubar)
        self.application_menu.setObjectName(u"application_menu")
        icon = QIcon()
        icon.addFile(u":/icons/baseline_home_black_36dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.application_menu.setIcon(icon)
        self.undo_menu = QMenu(self.menubar)
        self.undo_menu.setObjectName(u"undo_menu")
        icon1 = QIcon()
        icon1.addFile(u":/icons/baseline_undo_black_36dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.undo_menu.setIcon(icon1)
        self.redo_menu = QMenu(self.menubar)
        self.redo_menu.setObjectName(u"redo_menu")
        icon2 = QIcon()
        icon2.addFile(u":/icons/baseline_redo_black_36dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.redo_menu.setIcon(icon2)
        DressShopWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DressShopWindow)
        self.statusbar.setObjectName(u"statusbar")
        DressShopWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.application_menu.menuAction())
        self.menubar.addAction(self.undo_menu.menuAction())
        self.menubar.addAction(self.redo_menu.menuAction())

        self.retranslateUi(DressShopWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DressShopWindow)
    # setupUi

    def retranslateUi(self, DressShopWindow):
        DressShopWindow.setWindowTitle(QCoreApplication.translate("DressShopWindow", u"MainWindow", None))
        self.btn_add_new_goods.setText(QCoreApplication.translate("DressShopWindow", u"\u65b0\u589e\n"
"\u5546\u54c1", None))
        self.dockWidget_4.setWindowTitle(QCoreApplication.translate("DressShopWindow", u"\u603b\u89c8", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("DressShopWindow", u"\u8be6\u60c5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.store_tab), QCoreApplication.translate("DressShopWindow", u"\u5e93\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.orders_tab), QCoreApplication.translate("DressShopWindow", u"\u8ba2\u5355", None))
        self.application_menu.setTitle(QCoreApplication.translate("DressShopWindow", u"application", None))
        self.undo_menu.setTitle(QCoreApplication.translate("DressShopWindow", u"undo", None))
        self.redo_menu.setTitle(QCoreApplication.translate("DressShopWindow", u"redo", None))
    # retranslateUi

