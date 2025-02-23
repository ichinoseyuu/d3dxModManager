# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ...rc.resources_rc import *
from ..widgets.button import CButton

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(370, 274)
        dialog.setStyleSheet(u"#messageWidget {\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"#messageLabel {\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font: 10pt;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"#bottomWidget {\n"
"    background-color: rgb(250, 245, 245);\n"
"}\n"
"\n"
"\n"
"CButton {\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 10pt;\n"
"	color: rgb(60, 60, 60);\n"
"    border-radius: 4px;\n"
"}\n"
"CButton::icon {\n"
"    padding-right: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 32, 0, 0)
        self.messageWidget = QWidget(dialog)
        self.messageWidget.setObjectName(u"messageWidget")
        self.messageWidget.setMinimumSize(QSize(300, 140))
        self.messageWidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_2 = QVBoxLayout(self.messageWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.messageLabel = QLabel(self.messageWidget)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.messageLabel)


        self.verticalLayout.addWidget(self.messageWidget)

        self.bottomWidget = QWidget(dialog)
        self.bottomWidget.setObjectName(u"bottomWidget")
        self.bottomWidget.setMinimumSize(QSize(300, 50))
        self.bottomWidget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.bottomWidget)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 15, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnOk = CButton(self.bottomWidget)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setMinimumSize(QSize(60, 32))
        self.btnOk.setMaximumSize(QSize(60, 32))

        self.horizontalLayout_2.addWidget(self.btnOk)

        self.btnCancel = CButton(self.bottomWidget)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(60, 32))
        self.btnCancel.setMaximumSize(QSize(60, 32))

        self.horizontalLayout_2.addWidget(self.btnCancel)


        self.verticalLayout.addWidget(self.bottomWidget)


        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle("")
        self.messageLabel.setText(QCoreApplication.translate("dialog", u"\u6d88\u606f", None))
        self.btnOk.setText(QCoreApplication.translate("dialog", u"\u786e\u5b9a", None))
        self.btnCancel.setText(QCoreApplication.translate("dialog", u"\u53d6\u6d88", None))
    # retranslateUi

