# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ac7renamerdlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ac7Renamer(object):
    def setupUi(self, Ac7Renamer):
        Ac7Renamer.setObjectName("Ac7Renamer")
        Ac7Renamer.resize(393, 336)
        Ac7Renamer.setAutoFillBackground(False)
        Ac7Renamer.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Ac7Renamer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Ac7Renamer)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:rgb(127,227,255)")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Ac7Renamer)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.aboutButton = QtWidgets.QPushButton(Ac7Renamer)
        self.aboutButton.setObjectName("aboutButton")
        self.horizontalLayout.addWidget(self.aboutButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(Ac7Renamer)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.currentDisplayName = QtWidgets.QLineEdit(Ac7Renamer)
        self.currentDisplayName.setReadOnly(True)
        self.currentDisplayName.setObjectName("currentDisplayName")
        self.verticalLayout.addWidget(self.currentDisplayName)
        self.label = QtWidgets.QLabel(Ac7Renamer)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.desiredDisplayName = QtWidgets.QLineEdit(Ac7Renamer)
        self.desiredDisplayName.setText("")
        self.desiredDisplayName.setReadOnly(False)
        self.desiredDisplayName.setObjectName("desiredDisplayName")
        self.verticalLayout.addWidget(self.desiredDisplayName)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.saveButton = QtWidgets.QPushButton(Ac7Renamer)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Buttons = QtWidgets.QDialogButtonBox(Ac7Renamer)
        self.Buttons.setOrientation(QtCore.Qt.Horizontal)
        self.Buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.Buttons.setObjectName("Buttons")
        self.verticalLayout_2.addWidget(self.Buttons)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_2.setBuddy(self.currentDisplayName)
        self.label.setBuddy(self.desiredDisplayName)

        self.retranslateUi(Ac7Renamer)
        self.Buttons.accepted.connect(Ac7Renamer.accept)
        self.Buttons.rejected.connect(Ac7Renamer.reject)
        QtCore.QMetaObject.connectSlotsByName(Ac7Renamer)

    def retranslateUi(self, Ac7Renamer):
        _translate = QtCore.QCoreApplication.translate
        Ac7Renamer.setWindowTitle(_translate("Ac7Renamer", "Restyles piles of files!"))
        self.textBrowser.setHtml(_translate("Ac7Renamer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">This tool is GPLv3 charityware. Use and copy it freely,</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">but if you keep using it, please consider</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">making a donation to a charity of your choice.</span></p></body></html>"))
        self.pushButton.setText(_translate("Ac7Renamer", "Load Ac7 File"))
        self.aboutButton.setText(_translate("Ac7Renamer", "About this tool"))
        self.label_2.setText(_translate("Ac7Renamer", "Current display name"))
        self.currentDisplayName.setPlaceholderText(_translate("Ac7Renamer", "(will be loaded from file)"))
        self.label.setText(_translate("Ac7Renamer", "Desired display name (max 12 chars)"))
        self.desiredDisplayName.setPlaceholderText(_translate("Ac7Renamer", "(type here)"))
        self.saveButton.setText(_translate("Ac7Renamer", "Save AC7 File"))
        self.Buttons.setToolTip(_translate("Ac7Renamer", "Save as a new filename"))
