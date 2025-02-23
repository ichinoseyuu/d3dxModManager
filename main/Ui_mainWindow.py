# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from SmodernUI import *

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(1042, 738)
        mainwindow.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(mainwindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 36, 0, 0)
        self.mainboard = QWidget(mainwindow)
        self.mainboard.setObjectName(u"mainboard")
        self.mainboard.setStyleSheet(u"/*---------------------------------title------------------------------------*/\n"
"#titleWidget {\n"
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
"/*-----------------------------------left------------------------------------*/\n"
"#leftWidget {\n"
"    border-right: 1px solid rgb(235, 235, 235);\n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"/*-----------------------------------right----------------------------------*/\n"
"#rightWidget {\n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"#currentPageTitle {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 18pt;\n"
"    font-weight: bold;\n"
"    color: rgb(80, 80, 80);\n"
"}\n"
"#stackedWidget > QWidget {\n"
"    background-color: rgb(235, 235, 235);"
                        "\n"
"}\n"
"#bottomWidget {\n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"#bottomWidget QLabel{\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(235, 235, 235);\n"
"	background-color: rgb(255, 246, 248);\n"
"    border-radius: 2px;\n"
"}\n"
"/*---------------------------------page0-------------------------------------*/\n"
"#page_0 QLabel{\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"	background-color: rgb(255, 246, 248);\n"
"    border-radius: 4px;\n"
"}\n"
"/*----------------------------------page1-----------------------------------*/\n"
"#searchWidget QLabel{\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"}\n"
"#searchWidget QLineEdit{\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"	border: 1px solid lightgray;\n"
"	bord"
                        "er-radius: 2px;\n"
"}\n"
"\n"
"#page_1 #moduleWidget QWidget > QLabel {\n"
"	background-color: rgb(255, 246, 248);\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"	border-bottom: 1px solid rgb(235, 235, 235);\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"#page_1 #moduleWidget #previewWidget_2 #preview_1 {\n"
"	background-color: rgb(255, 246, 248);\n"
"	border-bottom: 1px solid rgb(235, 235, 235);\n"
"	border-radius: 0px;\n"
"}\n"
"#page_1 #moduleWidget #previewWidget_2 #preview_2 {\n"
"	background-color: rgb(255, 246, 248);\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"/*--------------------------------page2--------------------------------------*/\n"
"#functionWidget {\n"
"    background-color: rgb(255, 246, 248);\n"
"    border-bottom"
                        ": 1px solid rgb(235, 235, 235);\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"#folderWidget {\n"
"    background-color: rgb(255, 246, 248);\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"/*-----------------------------page3--------------------------------------*/\n"
"#configBtnWidget {\n"
"	background-color: rgb(255, 246, 248);\n"
"    border-bottom: 1px solid rgb(235, 235, 235);\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"#configBtnWidget QLabel {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: rgb(60, 60, 60);\n"
"}\n"
"#configLeft {\n"
"	background-color: rgb(255, 246, 248);\n"
"	border-right: 1px solid rgb(235, 235, 23"
                        "5);\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"#configRight {\n"
"	background-color: rgb(255, 246, 248);\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#configScrollWidget QLabel{\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"}\n"
"#configScrollWidget QLineEdit{\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"	border: 1px solid lightgray;\n"
"	border-radius: 2px;\n"
"}\n"
"#configScrollWidget QComboBox {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"    border: 1px solid lightgray;\n"
"    border-radius: 2px;\n"
"}\n"
"#configScrollWidget QComboBox::drop-down {\n"
"    border: none; /* \u53bb\u6389\u4e0b"
                        "\u62c9\u6309\u94ae\u7684\u8fb9\u6846 */\n"
"    background-color: #f0f0f0; /* \u4fee\u6539\u4e0b\u62c9\u6309\u94ae\u80cc\u666f\u989c\u8272 */\n"
"    width: 20px; /* \u8c03\u6574\u4e0b\u62c9\u6309\u94ae\u7684\u5bbd\u5ea6 */\n"
"    border-top-right-radius: 2px; /* \u8bbe\u7f6e\u53f3\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-bottom-right-radius: 2px; /* \u8bbe\u7f6e\u53f3\u4e0b\u89d2\u5706\u89d2 */\n"
"}\n"
"#configScrollWidget QComboBox::down-arrow {\n"
"	image: url(:/iamge_pack/content/down_arrow.png);\n"
"    width: 16px; /* \u8bbe\u7f6e\u7bad\u5934\u7684\u5bbd\u5ea6 */\n"
"    height: 16px; /* \u8bbe\u7f6e\u7bad\u5934\u7684\u9ad8\u5ea6 */\n"
"}\n"
"/*-----------------------------------page4----------------------------------*/\n"
"#softwareInfoWidget {\n"
"    background-color: rgb(255, 246, 248);\n"
"	border-radius: 5px;\n"
"}\n"
"#softwareInfoTitle {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    color: rgb(80, 80, 80);\n"
"}\n"
"#softwareName"
                        " {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 9pt;\n"
"    font-weight: bold;\n"
"    color: rgb(80, 80, 80);\n"
"}\n"
"#softwareVersion {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 9pt;\n"
"    color: dimgray;\n"
"}\n"
"#developerName {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 9pt;\n"
"    font-weight: bold;\n"
"    color: rgb(80, 80, 80);\n"
"}\n"
"#developerInfo {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 9pt;\n"
"    color: dimgray;\n"
"}\n"
"#copyrightLabel {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 9pt;\n"
"    color: dimgray\n"
"}\n"
"/*-----------------------------------btn----------------------------------*/\n"
"CButton {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"	border:1px solid transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"CButton::icon {\n"
"    padding-right: 10px;\n"
"}\n"
"/*"
                        "-----------------------------------ScrollArea----------------------------------*/\n"
"QScrollArea{\n"
"	border:none;\n"
"}\n"
"QScrollArea QScrollBar:vertical {\n"
"    width: 6px;\n"
"    margin: 0px 0px 0px 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background: rgb(215,215,215);\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"    width: 6px;\n"
"}\n"
"QScrollArea QScrollBar::add-line:vertical {\n"
"    background: transparent;\n"
"    border: none;\n"
"    height: 0px;\n"
"}\n"
"QScrollArea QScrollBar::sub-line:vertical {\n"
"    background: transparent;\n"
"    border: none;\n"
"    height: 0px;\n"
"}\n"
"QScrollArea QScrollBar::up-arrow:vertical,\n"
"QScrollArea QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"QComboBox {\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 10pt;\n"
"    color: rgb(60, 60, 60);\n"
"    border: 1px solid lightgray;\n"
"    border-radius: 2px;\n"
"}\n"
"QCo"
                        "mboBox::drop-down {\n"
"    border: none; \n"
"    background-color: #f0f0f0; \n"
"    width: 20px; \n"
"    border-top-right-radius: 2px; \n"
"    border-bottom-right-radius: 2px; \n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/iamge_pack/content/down_arrow.png);\n"
"    width: 16px; \n"
"    height: 16px; \n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.mainboard)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftWidget = QWidget(self.mainboard)
        self.leftWidget.setObjectName(u"leftWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.leftWidget.setMinimumSize(QSize(56, 0))
        self.leftWidget.setMaximumSize(QSize(56, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftWidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(7, -1, 7, -1)
        self.btnHome = CButton(self.leftWidget)
        self.btnHome.setTipText("")
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(42, 42))
        self.btnHome.setMaximumSize(QSize(42, 42))
        icon = QIcon()
        icon.addFile(u":/iamge_pack/tab/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHome.setIcon(icon)
        self.btnHome.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btnHome)

        self.btnModule = CButton(self.leftWidget)
        self.btnModule.setTipText("")
        self.btnModule.setObjectName(u"btnModule")
        self.btnModule.setMinimumSize(QSize(42, 42))
        self.btnModule.setMaximumSize(QSize(42, 42))
        icon1 = QIcon()
        icon1.addFile(u":/iamge_pack/tab/module_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnModule.setIcon(icon1)
        self.btnModule.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btnModule)

        self.btnFolder = CButton(self.leftWidget)
        self.btnFolder.setTipText("")
        self.btnFolder.setObjectName(u"btnFolder")
        self.btnFolder.setMinimumSize(QSize(42, 42))
        self.btnFolder.setMaximumSize(QSize(42, 42))
        icon2 = QIcon()
        icon2.addFile(u":/iamge_pack/tab/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFolder.setIcon(icon2)
        self.btnFolder.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btnFolder)

        self.btnConfig = CButton(self.leftWidget)
        self.btnConfig.setTipText("")
        self.btnConfig.setObjectName(u"btnConfig")
        self.btnConfig.setMinimumSize(QSize(42, 42))
        self.btnConfig.setMaximumSize(QSize(42, 42))
        icon3 = QIcon()
        icon3.addFile(u":/iamge_pack/tab/Settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnConfig.setIcon(icon3)
        self.btnConfig.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btnConfig)

        self.btnAbout = CButton(self.leftWidget)
        self.btnAbout.setTipText("")
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setMinimumSize(QSize(42, 42))
        self.btnAbout.setMaximumSize(QSize(42, 42))
        icon4 = QIcon()
        icon4.addFile(u":/iamge_pack/tab/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAbout.setIcon(icon4)
        self.btnAbout.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btnAbout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btnTheme = CButton(self.leftWidget)
        self.btnTheme.setTipText("")
        self.btnTheme.setObjectName(u"btnTheme")
        self.btnTheme.setMinimumSize(QSize(42, 42))
        self.btnTheme.setMaximumSize(QSize(42, 42))
        icon5 = QIcon()
        icon5.addFile(u":/iamge_pack/tab/dark_theme.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/iamge_pack/tab/light_theme.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnTheme.setIcon(icon5)
        self.btnTheme.setIconSize(QSize(24, 24))
        self.btnTheme.setCheckable(True)
        self.btnTheme.setChecked(False)

        self.verticalLayout_2.addWidget(self.btnTheme)


        self.horizontalLayout.addWidget(self.leftWidget)

        self.rightWidget = QWidget(self.mainboard)
        self.rightWidget.setObjectName(u"rightWidget")
        self.verticalLayout_9 = QVBoxLayout(self.rightWidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.currentPageTitle = QLabel(self.rightWidget)
        self.currentPageTitle.setObjectName(u"currentPageTitle")
        self.currentPageTitle.setMinimumSize(QSize(0, 50))
        self.currentPageTitle.setMaximumSize(QSize(16777215, 50))
        self.currentPageTitle.setIndent(10)

        self.verticalLayout_9.addWidget(self.currentPageTitle)

        self.stackedWidget = QStackedWidget(self.rightWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.verticalLayout_8 = QVBoxLayout(self.page_0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 0, 9, 9)
        self.widget = QWidget(self.page_0)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_26 = QVBoxLayout(self.widget)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.wallpaper = QLabel(self.widget)
        self.wallpaper.setObjectName(u"wallpaper")
        self.wallpaper.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.wallpaper)


        self.verticalLayout_8.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.searchWidget = QWidget(self.page_1)
        self.searchWidget.setObjectName(u"searchWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.searchWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.searchWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 24))
        self.lineEdit.setMaximumSize(QSize(300, 24))

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.searchWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(80, 24))
        self.comboBox.setMaximumSize(QSize(80, 24))

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.btnSearch = CButton(self.searchWidget)
        self.btnSearch.setTipText("")
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setMinimumSize(QSize(30, 24))
        self.btnSearch.setMaximumSize(QSize(30, 24))
        icon6 = QIcon()
        icon6.addFile(u":/iamge_pack/content/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSearch.setIcon(icon6)
        self.btnSearch.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btnSearch)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addWidget(self.searchWidget)

        self.moduleWidget = QWidget(self.page_1)
        self.moduleWidget.setObjectName(u"moduleWidget")
        self.gridLayout_3 = QGridLayout(self.moduleWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.classifiWidget = QWidget(self.moduleWidget)
        self.classifiWidget.setObjectName(u"classifiWidget")
        self.verticalLayout_13 = QVBoxLayout(self.classifiWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.classifiLabel = QLabel(self.classifiWidget)
        self.classifiLabel.setObjectName(u"classifiLabel")
        self.classifiLabel.setMinimumSize(QSize(0, 26))
        self.classifiLabel.setMaximumSize(QSize(16777215, 26))
        self.classifiLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.classifiLabel)


        self.gridLayout_3.addWidget(self.classifiWidget, 0, 0, 1, 1)

        self.partWidget = QWidget(self.moduleWidget)
        self.partWidget.setObjectName(u"partWidget")
        self.verticalLayout_16 = QVBoxLayout(self.partWidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.partLabel = QLabel(self.partWidget)
        self.partLabel.setObjectName(u"partLabel")
        self.partLabel.setMinimumSize(QSize(0, 26))
        self.partLabel.setMaximumSize(QSize(16777215, 26))
        self.partLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.partLabel)


        self.gridLayout_3.addWidget(self.partWidget, 0, 1, 1, 1)

        self.modWidget = QWidget(self.moduleWidget)
        self.modWidget.setObjectName(u"modWidget")
        self.verticalLayout_25 = QVBoxLayout(self.modWidget)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.modLabel = QLabel(self.modWidget)
        self.modLabel.setObjectName(u"modLabel")
        self.modLabel.setMinimumSize(QSize(0, 26))
        self.modLabel.setMaximumSize(QSize(16777215, 26))
        self.modLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.modLabel)


        self.gridLayout_3.addWidget(self.modWidget, 0, 2, 1, 1)

        self.previewWidget_1 = QWidget(self.moduleWidget)
        self.previewWidget_1.setObjectName(u"previewWidget_1")
        self.verticalLayout_14 = QVBoxLayout(self.previewWidget_1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.previewLabel = QLabel(self.previewWidget_1)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setMinimumSize(QSize(0, 26))
        self.previewLabel.setMaximumSize(QSize(16777215, 26))
        self.previewLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.previewLabel)


        self.gridLayout_3.addWidget(self.previewWidget_1, 0, 3, 1, 1)

        self.classifiScrollArea = QScrollArea(self.moduleWidget)
        self.classifiScrollArea.setObjectName(u"classifiScrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.classifiScrollArea.sizePolicy().hasHeightForWidth())
        self.classifiScrollArea.setSizePolicy(sizePolicy1)
        self.classifiScrollArea.setMinimumSize(QSize(200, 0))
        self.classifiScrollArea.setMaximumSize(QSize(200, 16777215))
        self.classifiScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.classifiScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.classifiScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.classifiScrollArea.setWidgetResizable(True)
        self.roleScrollWidget = QWidget()
        self.roleScrollWidget.setObjectName(u"roleScrollWidget")
        self.roleScrollWidget.setGeometry(QRect(0, 0, 200, 30))
        self.verticalLayout_11 = QVBoxLayout(self.roleScrollWidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.classifiScrollArea.setWidget(self.roleScrollWidget)

        self.gridLayout_3.addWidget(self.classifiScrollArea, 1, 0, 1, 1)

        self.modScrollArea = QScrollArea(self.moduleWidget)
        self.modScrollArea.setObjectName(u"modScrollArea")
        sizePolicy1.setHeightForWidth(self.modScrollArea.sizePolicy().hasHeightForWidth())
        self.modScrollArea.setSizePolicy(sizePolicy1)
        self.modScrollArea.setMinimumSize(QSize(200, 0))
        self.modScrollArea.setMaximumSize(QSize(200, 16777215))
        self.modScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.modScrollArea.setWidgetResizable(True)
        self.modScrollWidget = QWidget()
        self.modScrollWidget.setObjectName(u"modScrollWidget")
        self.modScrollWidget.setGeometry(QRect(0, 0, 200, 30))
        self.verticalLayout_15 = QVBoxLayout(self.modScrollWidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.modScrollArea.setWidget(self.modScrollWidget)

        self.gridLayout_3.addWidget(self.modScrollArea, 1, 1, 1, 1)

        self.partScrollArea = QScrollArea(self.moduleWidget)
        self.partScrollArea.setObjectName(u"partScrollArea")
        sizePolicy1.setHeightForWidth(self.partScrollArea.sizePolicy().hasHeightForWidth())
        self.partScrollArea.setSizePolicy(sizePolicy1)
        self.partScrollArea.setMinimumSize(QSize(200, 0))
        self.partScrollArea.setMaximumSize(QSize(200, 16777215))
        self.partScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.partScrollArea.setWidgetResizable(True)
        self.partScrollWidget = QWidget()
        self.partScrollWidget.setObjectName(u"partScrollWidget")
        self.partScrollWidget.setGeometry(QRect(0, 0, 200, 30))
        self.verticalLayout_12 = QVBoxLayout(self.partScrollWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.partScrollArea.setWidget(self.partScrollWidget)

        self.gridLayout_3.addWidget(self.partScrollArea, 1, 2, 1, 1)

        self.previewWidget_2 = QWidget(self.moduleWidget)
        self.previewWidget_2.setObjectName(u"previewWidget_2")
        self.verticalLayout_10 = QVBoxLayout(self.previewWidget_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.preview_1 = QLabel(self.previewWidget_2)
        self.preview_1.setObjectName(u"preview_1")

        self.verticalLayout_10.addWidget(self.preview_1)

        self.preview_2 = QLabel(self.previewWidget_2)
        self.preview_2.setObjectName(u"preview_2")

        self.verticalLayout_10.addWidget(self.preview_2)


        self.gridLayout_3.addWidget(self.previewWidget_2, 1, 3, 1, 1)


        self.verticalLayout_7.addWidget(self.moduleWidget)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 9)
        self.functionWidget = QWidget(self.page_2)
        self.functionWidget.setObjectName(u"functionWidget")
        self.functionWidget.setMinimumSize(QSize(0, 40))
        self.functionWidget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.functionWidget)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btnDelFolder = CButton(self.functionWidget)
        self.btnDelFolder.setTipText("")
        self.btnDelFolder.setObjectName(u"btnDelFolder")
        self.btnDelFolder.setMinimumSize(QSize(32, 32))
        self.btnDelFolder.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u":/iamge_pack/content/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelFolder.setIcon(icon7)
        self.btnDelFolder.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btnDelFolder)

        self.btnSelectAll = CButton(self.functionWidget)
        self.btnSelectAll.setTipText("")
        self.btnSelectAll.setObjectName(u"btnSelectAll")
        self.btnSelectAll.setMinimumSize(QSize(32, 32))
        self.btnSelectAll.setMaximumSize(QSize(32, 32))
        icon8 = QIcon()
        icon8.addFile(u":/iamge_pack/content/select_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/iamge_pack/content/unselect_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnSelectAll.setIcon(icon8)
        self.btnSelectAll.setIconSize(QSize(24, 24))
        self.btnSelectAll.setCheckable(True)
        self.btnSelectAll.setChecked(False)

        self.horizontalLayout_2.addWidget(self.btnSelectAll)

        self.btnAddFolder = CButton(self.functionWidget)
        self.btnAddFolder.setTipText("")
        self.btnAddFolder.setObjectName(u"btnAddFolder")
        self.btnAddFolder.setMinimumSize(QSize(32, 32))
        self.btnAddFolder.setMaximumSize(QSize(32, 32))
        icon9 = QIcon()
        icon9.addFile(u":/iamge_pack/content/increase.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddFolder.setIcon(icon9)
        self.btnAddFolder.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btnAddFolder)

        self.btnEditFolder = CButton(self.functionWidget)
        self.btnEditFolder.setTipText("")
        self.btnEditFolder.setObjectName(u"btnEditFolder")
        self.btnEditFolder.setMinimumSize(QSize(32, 32))
        self.btnEditFolder.setMaximumSize(QSize(32, 32))
        icon10 = QIcon()
        icon10.addFile(u":/iamge_pack/content/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/btn/main_widget/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnEditFolder.setIcon(icon10)
        self.btnEditFolder.setIconSize(QSize(24, 24))
        self.btnEditFolder.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btnEditFolder)


        self.verticalLayout_4.addWidget(self.functionWidget)

        self.startPageScrollArea = QScrollArea(self.page_2)
        self.startPageScrollArea.setObjectName(u"startPageScrollArea")
        self.startPageScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.startPageScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.startPageScrollArea.setWidgetResizable(True)
        self.startPageScrollWidget = QWidget()
        self.startPageScrollWidget.setObjectName(u"startPageScrollWidget")
        self.startPageScrollWidget.setGeometry(QRect(0, 0, 100, 30))
        self.startPageScrollWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.startPageScrollWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.folderWidget = QWidget(self.startPageScrollWidget)
        self.folderWidget.setObjectName(u"folderWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.folderWidget.sizePolicy().hasHeightForWidth())
        self.folderWidget.setSizePolicy(sizePolicy2)
        self.FolderGridLayout = QGridLayout(self.folderWidget)
        self.FolderGridLayout.setSpacing(9)
        self.FolderGridLayout.setObjectName(u"FolderGridLayout")
        self.FolderGridLayout.setContentsMargins(14, 9, 14, 9)

        self.verticalLayout_5.addWidget(self.folderWidget)

        self.startPageScrollArea.setWidget(self.startPageScrollWidget)

        self.verticalLayout_4.addWidget(self.startPageScrollArea)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 9, 9)
        self.configBtnWidget = QWidget(self.page_3)
        self.configBtnWidget.setObjectName(u"configBtnWidget")
        self.configBtnWidget.setMinimumSize(QSize(0, 40))
        self.configBtnWidget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.configBtnWidget)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.homeTitle = QLabel(self.configBtnWidget)
        self.homeTitle.setObjectName(u"homeTitle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(22)
        sizePolicy3.setHeightForWidth(self.homeTitle.sizePolicy().hasHeightForWidth())
        self.homeTitle.setSizePolicy(sizePolicy3)
        self.homeTitle.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_3.addWidget(self.homeTitle)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btnClearGameData = CButton(self.configBtnWidget)
        self.btnClearGameData.setTipText("")
        self.btnClearGameData.setObjectName(u"btnClearGameData")
        self.btnClearGameData.setMinimumSize(QSize(28, 28))
        self.btnClearGameData.setMaximumSize(QSize(28, 28))
        icon11 = QIcon()
        icon11.addFile(u":/iamge_pack/content/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClearGameData.setIcon(icon11)
        self.btnClearGameData.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btnClearGameData)

        self.btnNext = CButton(self.configBtnWidget)
        self.btnNext.setTipText("")
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setMinimumSize(QSize(28, 28))
        self.btnNext.setMaximumSize(QSize(28, 28))
        icon12 = QIcon()
        icon12.addFile(u":/iamge_pack/content/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNext.setIcon(icon12)

        self.horizontalLayout_3.addWidget(self.btnNext)


        self.verticalLayout_3.addWidget(self.configBtnWidget)

        self.configScrollArea = QScrollArea(self.page_3)
        self.configScrollArea.setObjectName(u"configScrollArea")
        self.configScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.configScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.configScrollArea.setWidgetResizable(True)
        self.configScrollWidget = QWidget()
        self.configScrollWidget.setObjectName(u"configScrollWidget")
        self.configScrollWidget.setGeometry(QRect(0, 0, 937, 102))
        self.horizontalLayout_5 = QHBoxLayout(self.configScrollWidget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.configLeft = QWidget(self.configScrollWidget)
        self.configLeft.setObjectName(u"configLeft")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.configLeft.sizePolicy().hasHeightForWidth())
        self.configLeft.setSizePolicy(sizePolicy4)
        self.configLeft.setMinimumSize(QSize(256, 0))
        self.configLeft.setMaximumSize(QSize(512, 16777215))
        self.gridLayout_2 = QGridLayout(self.configLeft)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_L_2 = QLabel(self.configLeft)
        self.label_L_2.setObjectName(u"label_L_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(22)
        sizePolicy5.setHeightForWidth(self.label_L_2.sizePolicy().hasHeightForWidth())
        self.label_L_2.setSizePolicy(sizePolicy5)
        self.label_L_2.setMinimumSize(QSize(0, 22))

        self.gridLayout_2.addWidget(self.label_L_2, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 6, 4, 1, 1)

        self.lomboBox_L_2 = QComboBox(self.configLeft)
        self.lomboBox_L_2.setObjectName(u"lomboBox_L_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lomboBox_L_2.sizePolicy().hasHeightForWidth())
        self.lomboBox_L_2.setSizePolicy(sizePolicy6)
        self.lomboBox_L_2.setMinimumSize(QSize(0, 22))
        self.lomboBox_L_2.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_2.addWidget(self.lomboBox_L_2, 2, 4, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 6, 0, 1, 1)

        self.lomboBox_L_1 = QComboBox(self.configLeft)
        self.lomboBox_L_1.setObjectName(u"lomboBox_L_1")
        sizePolicy6.setHeightForWidth(self.lomboBox_L_1.sizePolicy().hasHeightForWidth())
        self.lomboBox_L_1.setSizePolicy(sizePolicy6)
        self.lomboBox_L_1.setMinimumSize(QSize(0, 22))
        self.lomboBox_L_1.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_2.addWidget(self.lomboBox_L_1, 4, 4, 1, 1)

        self.label_L_1 = QLabel(self.configLeft)
        self.label_L_1.setObjectName(u"label_L_1")
        sizePolicy5.setHeightForWidth(self.label_L_1.sizePolicy().hasHeightForWidth())
        self.label_L_1.setSizePolicy(sizePolicy5)
        self.label_L_1.setMinimumSize(QSize(0, 22))

        self.gridLayout_2.addWidget(self.label_L_1, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.configLeft)

        self.configRight = QWidget(self.configScrollWidget)
        self.configRight.setObjectName(u"configRight")
        self.configRight.setMinimumSize(QSize(681, 0))
        self.gridLayout = QGridLayout(self.configRight)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 3, 1, 1)

        self.label_R_3 = QLabel(self.configRight)
        self.label_R_3.setObjectName(u"label_R_3")
        self.label_R_3.setMinimumSize(QSize(0, 22))
        self.label_R_3.setMaximumSize(QSize(16777215, 22))

        self.gridLayout.addWidget(self.label_R_3, 1, 2, 1, 1)

        self.label_R_1 = QLabel(self.configRight)
        self.label_R_1.setObjectName(u"label_R_1")
        sizePolicy5.setHeightForWidth(self.label_R_1.sizePolicy().hasHeightForWidth())
        self.label_R_1.setSizePolicy(sizePolicy5)
        self.label_R_1.setMinimumSize(QSize(0, 22))

        self.gridLayout.addWidget(self.label_R_1, 3, 2, 1, 1)

        self.comboBox_R_1 = QComboBox(self.configRight)
        self.comboBox_R_1.setObjectName(u"comboBox_R_1")
        sizePolicy6.setHeightForWidth(self.comboBox_R_1.sizePolicy().hasHeightForWidth())
        self.comboBox_R_1.setSizePolicy(sizePolicy6)
        self.comboBox_R_1.setMinimumSize(QSize(0, 22))
        self.comboBox_R_1.setMaximumSize(QSize(16777215, 22))

        self.gridLayout.addWidget(self.comboBox_R_1, 1, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 2, 1, 1)

        self.lineEdit_R_2 = QLineEdit(self.configRight)
        self.lineEdit_R_2.setObjectName(u"lineEdit_R_2")
        self.lineEdit_R_2.setMinimumSize(QSize(0, 22))
        self.lineEdit_R_2.setMaximumSize(QSize(16777215, 22))

        self.gridLayout.addWidget(self.lineEdit_R_2, 3, 3, 1, 1)

        self.lineEdit_R_1 = QLineEdit(self.configRight)
        self.lineEdit_R_1.setObjectName(u"lineEdit_R_1")
        self.lineEdit_R_1.setMinimumSize(QSize(0, 22))
        self.lineEdit_R_1.setMaximumSize(QSize(16777215, 22))

        self.gridLayout.addWidget(self.lineEdit_R_1, 2, 3, 1, 1)

        self.label_R_2 = QLabel(self.configRight)
        self.label_R_2.setObjectName(u"label_R_2")
        self.label_R_2.setMinimumSize(QSize(0, 22))
        self.label_R_2.setMaximumSize(QSize(16777215, 22))

        self.gridLayout.addWidget(self.label_R_2, 2, 2, 1, 1)

        self.btnSelect_1 = CButton(self.configRight)
        self.btnSelect_1.setTipText("")
        self.btnSelect_1.setObjectName(u"btnSelect_1")
        self.btnSelect_1.setMinimumSize(QSize(22, 22))
        self.btnSelect_1.setMaximumSize(QSize(22, 22))
        icon13 = QIcon()
        icon13.addFile(u":/iamge_pack/content/more.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSelect_1.setIcon(icon13)

        self.gridLayout.addWidget(self.btnSelect_1, 2, 4, 1, 1)

        self.btnSelect_2 = CButton(self.configRight)
        self.btnSelect_2.setTipText("")
        self.btnSelect_2.setObjectName(u"btnSelect_2")
        self.btnSelect_2.setMinimumSize(QSize(22, 22))
        self.btnSelect_2.setMaximumSize(QSize(22, 22))
        self.btnSelect_2.setIcon(icon13)

        self.gridLayout.addWidget(self.btnSelect_2, 3, 4, 1, 1)


        self.horizontalLayout_5.addWidget(self.configRight)

        self.configScrollArea.setWidget(self.configScrollWidget)

        self.verticalLayout_3.addWidget(self.configScrollArea)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 0, 9, 9)
        self.softwareInfoWidget = QWidget(self.page_4)
        self.softwareInfoWidget.setObjectName(u"softwareInfoWidget")
        self.softwareInfoTitle = QLabel(self.softwareInfoWidget)
        self.softwareInfoTitle.setObjectName(u"softwareInfoTitle")
        self.softwareInfoTitle.setGeometry(QRect(20, 20, 171, 40))
        self.softwareInfoTitle.setMinimumSize(QSize(0, 40))
        self.softwareInfoTitle.setMaximumSize(QSize(16777215, 40))
        self.softwarePic = QLabel(self.softwareInfoWidget)
        self.softwarePic.setObjectName(u"softwarePic")
        self.softwarePic.setGeometry(QRect(20, 70, 64, 64))
        self.softwarePic.setMinimumSize(QSize(64, 64))
        self.softwarePic.setMaximumSize(QSize(64, 64))
        self.softwarePic.setPixmap(QPixmap(u":/images/icon/icon.png"))
        self.softwarePic.setScaledContents(True)
        self.softwareName = QLabel(self.softwareInfoWidget)
        self.softwareName.setObjectName(u"softwareName")
        self.softwareName.setGeometry(QRect(90, 70, 125, 32))
        self.softwareName.setMinimumSize(QSize(125, 32))
        self.softwareName.setMaximumSize(QSize(125, 32))
        self.softwareVersion = QLabel(self.softwareInfoWidget)
        self.softwareVersion.setObjectName(u"softwareVersion")
        self.softwareVersion.setGeometry(QRect(90, 110, 125, 32))
        self.softwareVersion.setMinimumSize(QSize(125, 32))
        self.softwareVersion.setMaximumSize(QSize(125, 32))
        self.developerPic = QLabel(self.softwareInfoWidget)
        self.developerPic.setObjectName(u"developerPic")
        self.developerPic.setGeometry(QRect(290, 70, 64, 64))
        self.developerPic.setMinimumSize(QSize(64, 64))
        self.developerPic.setMaximumSize(QSize(64, 64))
        self.developerPic.setPixmap(QPixmap(u":/iamge_pack/touxiang.png"))
        self.developerPic.setScaledContents(True)
        self.developerName = QLabel(self.softwareInfoWidget)
        self.developerName.setObjectName(u"developerName")
        self.developerName.setGeometry(QRect(360, 70, 125, 32))
        self.developerName.setMinimumSize(QSize(125, 32))
        self.developerName.setMaximumSize(QSize(125, 32))
        self.developerInfo = QLabel(self.softwareInfoWidget)
        self.developerInfo.setObjectName(u"developerInfo")
        self.developerInfo.setGeometry(QRect(360, 110, 161, 32))
        self.developerInfo.setMinimumSize(QSize(125, 32))
        self.developerInfo.setMaximumSize(QSize(16777215, 32))
        self.btnGitHub = CButton(self.softwareInfoWidget)
        self.btnGitHub.setTipText("")
        self.btnGitHub.setObjectName(u"btnGitHub")
        self.btnGitHub.setGeometry(QRect(280, 160, 151, 32))
        self.btnGitHub.setMinimumSize(QSize(120, 32))
        self.btnGitHub.setMaximumSize(QSize(16777215, 32))
        icon14 = QIcon()
        icon14.addFile(u":/iamge_pack/content/github.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGitHub.setIcon(icon14)
        self.btnGitHub.setIconSize(QSize(24, 24))
        self.btnCheckUpdate = CButton(self.softwareInfoWidget)
        self.btnCheckUpdate.setTipText("")
        self.btnCheckUpdate.setObjectName(u"btnCheckUpdate")
        self.btnCheckUpdate.setGeometry(QRect(20, 160, 100, 32))
        self.btnCheckUpdate.setMinimumSize(QSize(100, 32))
        self.btnCheckUpdate.setMaximumSize(QSize(16777215, 32))
        icon15 = QIcon()
        icon15.addFile(u":/iamge_pack/content/update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCheckUpdate.setIcon(icon15)
        self.btnCheckUpdate.setIconSize(QSize(24, 24))
        self.btnRemoveUerdata = CButton(self.softwareInfoWidget)
        self.btnRemoveUerdata.setTipText("")
        self.btnRemoveUerdata.setObjectName(u"btnRemoveUerdata")
        self.btnRemoveUerdata.setGeometry(QRect(150, 160, 100, 32))
        self.btnRemoveUerdata.setMinimumSize(QSize(100, 32))
        self.btnRemoveUerdata.setMaximumSize(QSize(16777215, 32))
        self.btnRemoveUerdata.setIcon(icon11)
        self.btnRemoveUerdata.setIconSize(QSize(24, 24))
        self.copyrightLabel = QLabel(self.softwareInfoWidget)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setGeometry(QRect(20, 210, 361, 32))
        self.copyrightLabel.setMinimumSize(QSize(0, 32))
        self.copyrightLabel.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout_6.addWidget(self.softwareInfoWidget)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_9.addWidget(self.stackedWidget)

        self.bottomWidget = QWidget(self.rightWidget)
        self.bottomWidget.setObjectName(u"bottomWidget")
        sizePolicy.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.bottomWidget)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.currentGamePic = QLabel(self.bottomWidget)
        self.currentGamePic.setObjectName(u"currentGamePic")
        self.currentGamePic.setMinimumSize(QSize(42, 42))
        self.currentGamePic.setMaximumSize(QSize(42, 42))

        self.horizontalLayout_4.addWidget(self.currentGamePic)

        self.btnPlay = CButton(self.bottomWidget)
        self.btnPlay.setTipText("")
        self.btnPlay.setObjectName(u"btnPlay")
        self.btnPlay.setMinimumSize(QSize(110, 42))
        self.btnPlay.setMaximumSize(QSize(110, 42))
        icon16 = QIcon()
        icon16.addFile(u":/iamge_pack/content/run_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPlay.setIcon(icon16)
        self.btnPlay.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.btnPlay)


        self.verticalLayout_9.addWidget(self.bottomWidget)


        self.horizontalLayout.addWidget(self.rightWidget)


        self.verticalLayout.addWidget(self.mainboard)


        self.retranslateUi(mainwindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle("")
        self.currentPageTitle.setText(QCoreApplication.translate("mainwindow", u"\u9996\u9875", None))
        self.wallpaper.setText("")
        self.btnSearch.setText("")
        self.classifiLabel.setText(QCoreApplication.translate("mainwindow", u"\u5206\u7c7b", None))
        self.partLabel.setText(QCoreApplication.translate("mainwindow", u"\u90e8\u4ef6", None))
        self.modLabel.setText(QCoreApplication.translate("mainwindow", u"mod", None))
        self.previewLabel.setText(QCoreApplication.translate("mainwindow", u"\u9884\u89c8", None))
        self.preview_1.setText("")
        self.preview_2.setText("")
        self.btnDelFolder.setText("")
        self.btnSelectAll.setText("")
        self.btnAddFolder.setText("")
        self.btnEditFolder.setText("")
        self.homeTitle.setText(QCoreApplication.translate("mainwindow", u"\u57fa\u7840\u914d\u7f6e\uff1a", None))
        self.btnClearGameData.setText("")
        self.label_L_2.setText(QCoreApplication.translate("mainwindow", u"\u5207\u6362mod\u65f6\u5220\u9664\u7f13\u5b58:", None))
        self.label_L_1.setText(QCoreApplication.translate("mainwindow", u"\u81ea\u52a8\u6dfb\u52a0\u9884\u89c8\u56fe:", None))
        self.label_R_3.setText(QCoreApplication.translate("mainwindow", u"\u5f53\u524d\u6e38\u620f:", None))
        self.label_R_1.setText(QCoreApplication.translate("mainwindow", u"\u6a21\u7ec4\u52a0\u8f7d\u5668\u8def\u5f84:", None))
        self.label_R_2.setText(QCoreApplication.translate("mainwindow", u"\u6e38\u620f\u8def\u5f84:", None))
        self.btnSelect_1.setText("")
        self.btnSelect_2.setText("")
        self.softwareInfoTitle.setText(QCoreApplication.translate("mainwindow", u"\u8f6f\u4ef6\u4fe1\u606f", None))
        self.softwarePic.setText("")
        self.softwareName.setText(QCoreApplication.translate("mainwindow", u"d3dxModManager", None))
        self.softwareVersion.setText(QCoreApplication.translate("mainwindow", u"Version\uff1a1.0.0", None))
        self.developerPic.setText("")
        self.developerName.setText(QCoreApplication.translate("mainwindow", u"ichinoseyuu", None))
        self.developerInfo.setText(QCoreApplication.translate("mainwindow", u"d3dxModManager\u7684\u5f00\u53d1\u8005", None))
        self.btnGitHub.setText(QCoreApplication.translate("mainwindow", u" \u53bb\u6211\u7684github\u4e3b\u9875", None))
        self.btnCheckUpdate.setText(QCoreApplication.translate("mainwindow", u" \u68c0\u67e5\u66f4\u65b0", None))
        self.btnRemoveUerdata.setText(QCoreApplication.translate("mainwindow", u" \u6e05\u9664\u6570\u636e", None))
        self.copyrightLabel.setText(QCoreApplication.translate("mainwindow", u"Copyright \u00a9 ichinoseyuu 2023-2025. All Rights Reserved.", None))
        self.currentGamePic.setText("")
        self.btnPlay.setText(QCoreApplication.translate("mainwindow", u" \u542f\u52a8", None))
    # retranslateUi

