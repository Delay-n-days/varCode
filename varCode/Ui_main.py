# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 744)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBoxPage2 = QWidget()
        self.toolBoxPage2.setObjectName(u"toolBoxPage2")
        self.toolBoxPage2.setGeometry(QRect(0, 0, 1030, 692))
        self.gridLayout_2 = QGridLayout(self.toolBoxPage2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_3 = QTextEdit(self.toolBoxPage2)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.verticalLayout.addWidget(self.textEdit_3)

        self.pushButton_2 = QPushButton(self.toolBoxPage2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.textEdit_4 = QTextEdit(self.toolBoxPage2)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.verticalLayout.addWidget(self.textEdit_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.toolBoxPage2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.toolBoxPage2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit_7 = QTextEdit(self.toolBoxPage2)
        self.textEdit_7.setObjectName(u"textEdit_7")

        self.verticalLayout.addWidget(self.textEdit_7)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton = QRadioButton(self.toolBoxPage2)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.toolBoxPage2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.toolBoxPage2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.toolBoxPage2)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEdit_5 = QTextEdit(self.groupBox)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.textEdit_5)

        self.textEdit_6 = QTextEdit(self.groupBox)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.textEdit_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.toolBox.addItem(self.toolBoxPage2, u"\u53d8\u91cf\u6279\u91cf\u7ffb\u8bd1")

        self.horizontalLayout_2.addWidget(self.toolBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1+\u5904\u7406", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u9a7c\u5cf0\u547d\u540d\u6cd5", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5212\u7ebf\u547d\u540d\u6cd5", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u5904\u7406", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u66ff\u6362\u89c4\u5219", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), QCoreApplication.translate("MainWindow", u"\u53d8\u91cf\u6279\u91cf\u7ffb\u8bd1", None))
    # retranslateUi

