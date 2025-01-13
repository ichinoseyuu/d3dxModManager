# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titlebar.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from resource.resources_rc import *
from ..widgets.button import CButton

class Ui_titlebar(object):
    def setupUi(self, titlebar):
        if not titlebar.objectName():
            titlebar.setObjectName(u"titlebar")
        titlebar.resize(818, 40)
        titlebar.setStyleSheet(u"#titleWidget {\n"
"    border-bottom: 1px solid rgb(235, 235, 235);\n"
"    background-color: rgb(250, 245, 245);\n"
"}\n"
"#icon{\n"
"	border: 1px solid rgb(235, 235, 235);\n"
"}\n"
"#title {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font: 10pt;\n"
"    background-color: transparent;\n"
"    color: rgb(60, 60, 60);\n"
"}\n"
"CButton {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"	border:1px solid transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"CButton::icon {\n"
"    padding-right: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(titlebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = QWidget(titlebar)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleWidget.sizePolicy().hasHeightForWidth())
        self.titleWidget.setSizePolicy(sizePolicy)
        self.titleWidget.setMinimumSize(QSize(0, 40))
        self.titleWidget.setMaximumSize(QSize(16777215, 40))
        self.hboxLayout = QHBoxLayout(self.titleWidget)
        self.hboxLayout.setSpacing(12)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(12, 0, 15, 0)
        self.icon = QLabel(self.titleWidget)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(32, 32))
        self.icon.setMaximumSize(QSize(32, 32))
        self.icon.setPixmap(QPixmap(u":/images/icon/icon.png"))
        self.icon.setScaledContents(True)

        self.hboxLayout.addWidget(self.icon)

        self.title = QLabel(self.titleWidget)
        self.title.setObjectName(u"title")

        self.hboxLayout.addWidget(self.title)

        self.titleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.titleSpacer)

        self.btnMin = CButton(self.titleWidget)
        self.btnMin.setObjectName(u"btnMin")
        self.btnMin.setMinimumSize(QSize(24, 24))
        self.btnMin.setMaximumSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u":/iamge_pack/title_bar/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMin.setIcon(icon1)

        self.hboxLayout.addWidget(self.btnMin)

        self.btnMax = CButton(self.titleWidget)
        self.btnMax.setObjectName(u"btnMax")
        self.btnMax.setMinimumSize(QSize(24, 24))
        self.btnMax.setMaximumSize(QSize(24, 24))
        icon2 = QIcon()
        icon2.addFile(u":/iamge_pack/title_bar/maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/iamge_pack/title_bar/windowed.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnMax.setIcon(icon2)
        self.btnMax.setCheckable(True)

        self.hboxLayout.addWidget(self.btnMax)

        self.btnExit = CButton(self.titleWidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(24, 24))
        self.btnExit.setMaximumSize(QSize(24, 24))
        icon3 = QIcon()
        icon3.addFile(u":/iamge_pack/title_bar/shutdown.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExit.setIcon(icon3)

        self.hboxLayout.addWidget(self.btnExit)


        self.verticalLayout.addWidget(self.titleWidget)


        self.retranslateUi(titlebar)

        QMetaObject.connectSlotsByName(titlebar)
    # setupUi

    def retranslateUi(self, titlebar):
        titlebar.setWindowTitle("")
        self.title.setText(QCoreApplication.translate("titlebar", u"d3dxModManager", None))
    # retranslateUi

