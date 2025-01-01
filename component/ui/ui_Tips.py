# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tips.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Tips(object):
    def setupUi(self, Tips):
        if not Tips.objectName():
            Tips.setObjectName(u"Tips")
        Tips.resize(200, 60)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tips.sizePolicy().hasHeightForWidth())
        Tips.setSizePolicy(sizePolicy)
        Tips.setMinimumSize(QSize(200, 60))
        Tips.setStyleSheet(u"#TipBoard {\n"
"    border: 1px solid lightgray;\n"
"    background-color: rgb(250, 245, 245);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#TipLabel {\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font: 10pt;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: rgb(80, 80, 80);\n"
"}")
        self.verticalLayout = QVBoxLayout(Tips)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.TipBoard = QWidget(Tips)
        self.TipBoard.setObjectName(u"TipBoard")
        self.verticalLayout_2 = QVBoxLayout(self.TipBoard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TipLabel = QLabel(self.TipBoard)
        self.TipLabel.setObjectName(u"TipLabel")
        self.TipLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.TipLabel)


        self.verticalLayout.addWidget(self.TipBoard)


        self.retranslateUi(Tips)

        QMetaObject.connectSlotsByName(Tips)
    # setupUi

    def retranslateUi(self, Tips):
        Tips.setWindowTitle("")
        self.TipLabel.setText(QCoreApplication.translate("Tips", u"\u63d0\u793a", None))
    # retranslateUi

