# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titlebar.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import time
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ...rc.resources_rc import *
from ..widgets.button import CButton
from ..widgets.container import CContainer

class Ui_titlebar(object):
    def setupUi(self, titlebar):
        if not titlebar.objectName():
            titlebar.setObjectName(u"titlebar")
        titlebar.resize(1014, 36)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(titlebar.sizePolicy().hasHeightForWidth())
        titlebar.setSizePolicy(sizePolicy)
        titlebar.setMinimumSize(QSize(0, 36))
        titlebar.setMaximumSize(QSize(16777215, 36))
        titlebar.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(titlebar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = CContainer(titlebar)
        self.titleWidget.setObjectName(u"titleWidget_{}".format(int(time.time() * 1000)))
        self.titleWidget.setMinimumSize(QSize(0, 36))
        self.titleWidget.setMaximumSize(QSize(16777215, 36))
        self.titleWidget.setStyleSheet(u'''
            #icon {
                border: none;
            }
            #title {
                font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";
                font: 10pt;
                background-color: transparent;
                color: rgb(60, 60, 60);
            }''')
        self.horizontalLayout = QHBoxLayout(self.titleWidget)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, 15, 0)
        self.icon = QLabel(self.titleWidget)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(24, 24))
        self.icon.setMaximumSize(QSize(24, 24))
        self.icon.setPixmap(QPixmap(u":/images/icon/icon.png"))
        self.icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon)

        self.title = QLabel(self.titleWidget)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title)

        self.titleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.titleSpacer)

        self.btnMin = CButton(self.titleWidget)
        self.btnMin.setObjectName(u"btnMin")
        self.btnMin.setMinimumSize(QSize(24, 24))
        self.btnMin.setMaximumSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u":/iamge_pack/title_bar/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMin.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnMin)

        self.btnMax = CButton(self.titleWidget)
        self.btnMax.setObjectName(u"btnMax")
        self.btnMax.setMinimumSize(QSize(24, 24))
        self.btnMax.setMaximumSize(QSize(24, 24))
        icon2 = QIcon()
        icon2.addFile(u":/iamge_pack/title_bar/maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/iamge_pack/title_bar/windowed.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnMax.setIcon(icon2)
        self.btnMax.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnMax)

        self.btnExit = CButton(self.titleWidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(24, 24))
        self.btnExit.setMaximumSize(QSize(24, 24))
        icon3 = QIcon()
        icon3.addFile(u":/iamge_pack/title_bar/shutdown.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExit.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btnExit)


        self.verticalLayout.addWidget(self.titleWidget)


        self.retranslateUi(titlebar)

        QMetaObject.connectSlotsByName(titlebar)
    # setupUi

    def retranslateUi(self, titlebar):
        titlebar.setWindowTitle("")
        self.title.setText(QCoreApplication.translate("titlebar", u"\u6807\u9898", None))
    # retranslateUi

