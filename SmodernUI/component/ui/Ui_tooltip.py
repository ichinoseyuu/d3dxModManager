# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tooltip.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..widgets.container import CContainer

class Ui_tooltip(object):
    def setupUi(self, tooltip):
        if not tooltip.objectName():
            tooltip.setObjectName(u"tooltip")
        tooltip.resize(94, 28)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tooltip.sizePolicy().hasHeightForWidth())
        tooltip.setSizePolicy(sizePolicy)
        tooltip.setMinimumSize(QSize(0, 28))
        tooltip.setMaximumSize(QSize(16777215, 28))
        tooltip.setStyleSheet(u"#tipBoard{\n"
"    border: 1px solid rgb(230,230,230);\n"
"    border-radius: 2px;\n"
"    background-color: rgb(250, 245, 245);\n"
"}\n"
"#tipLabel {\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font: 10pt;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: rgb(80, 80, 80);\n"
"}")
        self.verticalLayout = QVBoxLayout(tooltip)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tipBoard = CContainer(tooltip)
        self.tipBoard.setObjectName(u"tipBoard")
        self.verticalLayout_2 = QVBoxLayout(self.tipBoard)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tipLabel = QLabel(self.tipBoard)
        self.tipLabel.setObjectName(u"tipLabel")
        sizePolicy.setHeightForWidth(self.tipLabel.sizePolicy().hasHeightForWidth())
        self.tipLabel.setSizePolicy(sizePolicy)
        self.tipLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.tipLabel)


        self.verticalLayout.addWidget(self.tipBoard)


        self.retranslateUi(tooltip)

        QMetaObject.connectSlotsByName(tooltip)
    # setupUi

    def retranslateUi(self, tooltip):
        tooltip.setWindowTitle("")
        self.tipLabel.setText(QCoreApplication.translate("tooltip", u"\u63d0\u793a", None))
    # retranslateUi

