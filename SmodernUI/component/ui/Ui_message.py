# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'message.ui'
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

class Ui_message(object):
    def setupUi(self, message):
        if not message.objectName():
            message.setObjectName(u"message")
        message.resize(318, 228)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(message.sizePolicy().hasHeightForWidth())
        message.setSizePolicy(sizePolicy)
        message.setMinimumSize(QSize(318, 0))
        message.setStyleSheet(u"#titleWidget {\n"
"    border-bottom: 1px solid rgb(235, 235, 235);\n"
"    background-color: rgb(250, 245, 245);\n"
"}\n"
"\n"
"#title {\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font: 11pt;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"#messageWidget {\n"
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
        self.verticalLayout_3 = QVBoxLayout(message)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.titleWidget = QWidget(message)
        self.titleWidget.setObjectName(u"titleWidget")
        self.titleWidget.setMinimumSize(QSize(300, 40))
        self.titleWidget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.titleWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.titleWidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnExit = CButton(self.titleWidget)
        self.btnExit.setTipText("")
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(24, 24))
        self.btnExit.setMaximumSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u":/iamge_pack/title_bar/shutdown.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExit.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnExit)


        self.verticalLayout_3.addWidget(self.titleWidget)

        self.messageWidget = QWidget(message)
        self.messageWidget.setObjectName(u"messageWidget")
        self.messageWidget.setMinimumSize(QSize(300, 120))
        self.messageWidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_2 = QVBoxLayout(self.messageWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.messageLabel = QLabel(self.messageWidget)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.messageLabel)


        self.verticalLayout_3.addWidget(self.messageWidget)

        self.bottomWidget = QWidget(message)
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
        self.btnOk.setTipText("")
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setMinimumSize(QSize(60, 32))
        self.btnOk.setMaximumSize(QSize(60, 32))

        self.horizontalLayout_2.addWidget(self.btnOk)

        self.btnCancel = CButton(self.bottomWidget)
        self.btnCancel.setTipText("")
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(60, 32))
        self.btnCancel.setMaximumSize(QSize(60, 32))

        self.horizontalLayout_2.addWidget(self.btnCancel)


        self.verticalLayout_3.addWidget(self.bottomWidget)


        self.retranslateUi(message)

        QMetaObject.connectSlotsByName(message)
    # setupUi

    def retranslateUi(self, message):
        self.title.setText(QCoreApplication.translate("message", u"\u6807\u9898", None))
        self.messageLabel.setText(QCoreApplication.translate("message", u"\u6d88\u606f", None))
        self.btnOk.setText(QCoreApplication.translate("message", u"\u786e\u5b9a", None))
        self.btnCancel.setText(QCoreApplication.translate("message", u"\u53d6\u6d88", None))
        pass
    # retranslateUi

