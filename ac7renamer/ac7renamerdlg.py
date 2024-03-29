# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ac7renamerdlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ac7Renamer(object):
    def setupUi(self, Ac7Renamer):
        Ac7Renamer.setObjectName("Ac7Renamer")
        Ac7Renamer.resize(1286, 642)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/restyle_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ac7Renamer.setWindowIcon(icon)
        Ac7Renamer.setAutoFillBackground(False)
        Ac7Renamer.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Ac7Renamer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Ac7Renamer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 75))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:rgb(127,227,255)")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.aboutButton = QtWidgets.QPushButton(Ac7Renamer)
        self.aboutButton.setObjectName("aboutButton")
        self.horizontalLayout_5.addWidget(self.aboutButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Ac7Renamer)
        self.tabWidget.setObjectName("tabWidget")
        self.singleFileTab = QtWidgets.QWidget()
        self.singleFileTab.setObjectName("singleFileTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.singleFileTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.singleFileTab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.singleFileTab)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.currentDisplayName = QtWidgets.QLineEdit(self.singleFileTab)
        self.currentDisplayName.setReadOnly(True)
        self.currentDisplayName.setObjectName("currentDisplayName")
        self.verticalLayout_3.addWidget(self.currentDisplayName)
        self.label = QtWidgets.QLabel(self.singleFileTab)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.desiredDisplayName = QtWidgets.QLineEdit(self.singleFileTab)
        self.desiredDisplayName.setText("")
        self.desiredDisplayName.setReadOnly(False)
        self.desiredDisplayName.setObjectName("desiredDisplayName")
        self.verticalLayout_3.addWidget(self.desiredDisplayName)
        self.label_5 = QtWidgets.QLabel(self.singleFileTab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.singleFileTab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.firstRow = QtWidgets.QHBoxLayout()
        self.firstRow.setObjectName("firstRow")
        self.curEl1 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curEl1.sizePolicy().hasHeightForWidth())
        self.curEl1.setSizePolicy(sizePolicy)
        self.curEl1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.curEl1.setObjectName("curEl1")
        self.curEl1.addItem("")
        self.firstRow.addWidget(self.curEl1)
        self.curEl2 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl2.setEnabled(False)
        self.curEl2.setObjectName("curEl2")
        self.curEl2.addItem("")
        self.firstRow.addWidget(self.curEl2)
        self.curEl4 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl4.setEnabled(False)
        self.curEl4.setObjectName("curEl4")
        self.curEl4.addItem("")
        self.firstRow.addWidget(self.curEl4)
        self.curEl3 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl3.setEnabled(False)
        self.curEl3.setObjectName("curEl3")
        self.curEl3.addItem("")
        self.firstRow.addWidget(self.curEl3)
        self.curEl5 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl5.setEnabled(False)
        self.curEl5.setObjectName("curEl5")
        self.curEl5.addItem("")
        self.firstRow.addWidget(self.curEl5)
        self.curEl6 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl6.setEnabled(False)
        self.curEl6.setObjectName("curEl6")
        self.curEl6.addItem("")
        self.firstRow.addWidget(self.curEl6)
        self.curEl8 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl8.setEnabled(False)
        self.curEl8.setEditable(False)
        self.curEl8.setObjectName("curEl8")
        self.curEl8.addItem("")
        self.firstRow.addWidget(self.curEl8)
        self.curEl10 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl10.setEnabled(False)
        self.curEl10.setObjectName("curEl10")
        self.curEl10.addItem("")
        self.firstRow.addWidget(self.curEl10)
        self.curEl9 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl9.setEnabled(False)
        self.curEl9.setObjectName("curEl9")
        self.curEl9.addItem("")
        self.firstRow.addWidget(self.curEl9)
        self.curEl11 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl11.setEnabled(False)
        self.curEl11.setObjectName("curEl11")
        self.curEl11.addItem("")
        self.firstRow.addWidget(self.curEl11)
        self.curEl7 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl7.setEnabled(False)
        self.curEl7.setObjectName("curEl7")
        self.curEl7.addItem("")
        self.firstRow.addWidget(self.curEl7)
        self.curEl12 = QtWidgets.QComboBox(self.singleFileTab)
        self.curEl12.setEnabled(False)
        self.curEl12.setObjectName("curEl12")
        self.curEl12.addItem("")
        self.firstRow.addWidget(self.curEl12)
        self.verticalLayout_3.addLayout(self.firstRow)
        self.label_4 = QtWidgets.QLabel(self.singleFileTab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.secRow = QtWidgets.QHBoxLayout()
        self.secRow.setObjectName("secRow")
        self.desEl1 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl1.setObjectName("desEl1")
        self.secRow.addWidget(self.desEl1)
        self.desEl2 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl2.setObjectName("desEl2")
        self.secRow.addWidget(self.desEl2)
        self.desEl4 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl4.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl4.setObjectName("desEl4")
        self.secRow.addWidget(self.desEl4)
        self.desEl3 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl3.setObjectName("desEl3")
        self.secRow.addWidget(self.desEl3)
        self.desEl5 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl5.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl5.setObjectName("desEl5")
        self.secRow.addWidget(self.desEl5)
        self.desEl6 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl6.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl6.setObjectName("desEl6")
        self.secRow.addWidget(self.desEl6)
        self.desEl8 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl8.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl8.setObjectName("desEl8")
        self.secRow.addWidget(self.desEl8)
        self.desEl10 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl10.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl10.setObjectName("desEl10")
        self.secRow.addWidget(self.desEl10)
        self.desEl9 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl9.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.desEl9.setObjectName("desEl9")
        self.secRow.addWidget(self.desEl9)
        self.desEl11 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl11.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl11.setObjectName("desEl11")
        self.secRow.addWidget(self.desEl11)
        self.desEl7 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl7.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl7.setObjectName("desEl7")
        self.secRow.addWidget(self.desEl7)
        self.desEl12 = QtWidgets.QComboBox(self.singleFileTab)
        self.desEl12.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.desEl12.setObjectName("desEl12")
        self.secRow.addWidget(self.desEl12)
        self.verticalLayout_3.addLayout(self.secRow)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.saveButton = QtWidgets.QPushButton(self.singleFileTab)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.singleFileTab, "")
        self.multiFileTab = QtWidgets.QWidget()
        self.multiFileTab.setObjectName("multiFileTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.multiFileTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loadFolderContent = QtWidgets.QPushButton(self.multiFileTab)
        self.loadFolderContent.setObjectName("loadFolderContent")
        self.horizontalLayout_3.addWidget(self.loadFolderContent)
        self.selectAll = QtWidgets.QPushButton(self.multiFileTab)
        self.selectAll.setObjectName("selectAll")
        self.horizontalLayout_3.addWidget(self.selectAll)
        self.deselectAll = QtWidgets.QPushButton(self.multiFileTab)
        self.deselectAll.setObjectName("deselectAll")
        self.horizontalLayout_3.addWidget(self.deselectAll)
        self.invertSelection = QtWidgets.QPushButton(self.multiFileTab)
        self.invertSelection.setObjectName("invertSelection")
        self.horizontalLayout_3.addWidget(self.invertSelection)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.fileListing = QtWidgets.QTableView(self.multiFileTab)
        self.fileListing.setObjectName("fileListing")
        self.verticalLayout_4.addWidget(self.fileListing)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.renameFolderContent = QtWidgets.QPushButton(self.multiFileTab)
        self.renameFolderContent.setObjectName("renameFolderContent")
        self.horizontalLayout_4.addWidget(self.renameFolderContent)
        self.rhythmSplit = QtWidgets.QPushButton(self.multiFileTab)
        self.rhythmSplit.setObjectName("rhythmSplit")
        self.horizontalLayout_4.addWidget(self.rhythmSplit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.multiFileTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.Buttons = QtWidgets.QDialogButtonBox(Ac7Renamer)
        self.Buttons.setOrientation(QtCore.Qt.Horizontal)
        self.Buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.Buttons.setObjectName("Buttons")
        self.verticalLayout_2.addWidget(self.Buttons)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_2.setBuddy(self.currentDisplayName)
        self.label.setBuddy(self.desiredDisplayName)

        self.retranslateUi(Ac7Renamer)
        self.tabWidget.setCurrentIndex(0)
        self.Buttons.accepted.connect(Ac7Renamer.accept)
        self.Buttons.rejected.connect(Ac7Renamer.reject)
        QtCore.QMetaObject.connectSlotsByName(Ac7Renamer)
        Ac7Renamer.setTabOrder(self.textBrowser, self.aboutButton)
        Ac7Renamer.setTabOrder(self.aboutButton, self.tabWidget)
        Ac7Renamer.setTabOrder(self.tabWidget, self.pushButton)
        Ac7Renamer.setTabOrder(self.pushButton, self.currentDisplayName)
        Ac7Renamer.setTabOrder(self.currentDisplayName, self.desiredDisplayName)
        Ac7Renamer.setTabOrder(self.desiredDisplayName, self.curEl1)
        Ac7Renamer.setTabOrder(self.curEl1, self.desEl1)
        Ac7Renamer.setTabOrder(self.desEl1, self.curEl2)
        Ac7Renamer.setTabOrder(self.curEl2, self.desEl2)
        Ac7Renamer.setTabOrder(self.desEl2, self.curEl4)
        Ac7Renamer.setTabOrder(self.curEl4, self.desEl4)
        Ac7Renamer.setTabOrder(self.desEl4, self.curEl3)
        Ac7Renamer.setTabOrder(self.curEl3, self.desEl3)
        Ac7Renamer.setTabOrder(self.desEl3, self.curEl5)
        Ac7Renamer.setTabOrder(self.curEl5, self.desEl5)
        Ac7Renamer.setTabOrder(self.desEl5, self.curEl6)
        Ac7Renamer.setTabOrder(self.curEl6, self.desEl6)
        Ac7Renamer.setTabOrder(self.desEl6, self.curEl8)
        Ac7Renamer.setTabOrder(self.curEl8, self.desEl8)
        Ac7Renamer.setTabOrder(self.desEl8, self.curEl10)
        Ac7Renamer.setTabOrder(self.curEl10, self.desEl10)
        Ac7Renamer.setTabOrder(self.desEl10, self.curEl9)
        Ac7Renamer.setTabOrder(self.curEl9, self.desEl9)
        Ac7Renamer.setTabOrder(self.desEl9, self.curEl11)
        Ac7Renamer.setTabOrder(self.curEl11, self.desEl11)
        Ac7Renamer.setTabOrder(self.desEl11, self.curEl7)
        Ac7Renamer.setTabOrder(self.curEl7, self.desEl7)
        Ac7Renamer.setTabOrder(self.desEl7, self.curEl12)
        Ac7Renamer.setTabOrder(self.curEl12, self.desEl12)
        Ac7Renamer.setTabOrder(self.desEl12, self.saveButton)
        Ac7Renamer.setTabOrder(self.saveButton, self.loadFolderContent)
        Ac7Renamer.setTabOrder(self.loadFolderContent, self.selectAll)
        Ac7Renamer.setTabOrder(self.selectAll, self.deselectAll)
        Ac7Renamer.setTabOrder(self.deselectAll, self.invertSelection)
        Ac7Renamer.setTabOrder(self.invertSelection, self.fileListing)
        Ac7Renamer.setTabOrder(self.fileListing, self.renameFolderContent)
        Ac7Renamer.setTabOrder(self.renameFolderContent, self.rhythmSplit)

    def retranslateUi(self, Ac7Renamer):
        _translate = QtCore.QCoreApplication.translate
        Ac7Renamer.setWindowTitle(_translate("Ac7Renamer", "Restyles piles of files!"))
        self.textBrowser.setHtml(_translate("Ac7Renamer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool is GPLv3 charityware. Use and copy it freely,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">but if you keep using it, please consider</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">making a donation to a charity of your choice.</p></body></html>"))
        self.aboutButton.setText(_translate("Ac7Renamer", "About this tool"))
        self.pushButton.setText(_translate("Ac7Renamer", "Load Ac7 File"))
        self.label_2.setText(_translate("Ac7Renamer", "Current display name"))
        self.currentDisplayName.setPlaceholderText(_translate("Ac7Renamer", "(will be loaded from file)"))
        self.label.setText(_translate("Ac7Renamer", "Desired display name (max 12 chars)"))
        self.desiredDisplayName.setPlaceholderText(_translate("Ac7Renamer", "(type here)"))
        self.label_5.setText(_translate("Ac7Renamer", "[Optionally] Reorder elements"))
        self.label_3.setText(_translate("Ac7Renamer", "Current ordering"))
        self.curEl1.setItemText(0, _translate("Ac7Renamer", "intro (1)"))
        self.curEl2.setItemText(0, _translate("Ac7Renamer", "normal (1)"))
        self.curEl4.setItemText(0, _translate("Ac7Renamer", "fill-in (1)"))
        self.curEl3.setItemText(0, _translate("Ac7Renamer", "var (2)"))
        self.curEl5.setItemText(0, _translate("Ac7Renamer", "fill-in (2)"))
        self.curEl6.setItemText(0, _translate("Ac7Renamer", "end (1)"))
        self.curEl8.setCurrentText(_translate("Ac7Renamer", "var (3)"))
        self.curEl8.setItemText(0, _translate("Ac7Renamer", "var (3)"))
        self.curEl10.setItemText(0, _translate("Ac7Renamer", "fill-in (3)"))
        self.curEl9.setItemText(0, _translate("Ac7Renamer", "var (4)"))
        self.curEl11.setItemText(0, _translate("Ac7Renamer", "fill-in (4)"))
        self.curEl7.setItemText(0, _translate("Ac7Renamer", "intro (2)"))
        self.curEl12.setItemText(0, _translate("Ac7Renamer", "end (2)"))
        self.label_4.setText(_translate("Ac7Renamer", "Desired ordering"))
        self.saveButton.setText(_translate("Ac7Renamer", "Save AC7 File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.singleFileTab), _translate("Ac7Renamer", "Single file"))
        self.loadFolderContent.setText(_translate("Ac7Renamer", "Load folder"))
        self.selectAll.setText(_translate("Ac7Renamer", "Select All"))
        self.deselectAll.setText(_translate("Ac7Renamer", "Deselect All"))
        self.invertSelection.setText(_translate("Ac7Renamer", "Invert Selection"))
        self.renameFolderContent.setText(_translate("Ac7Renamer", "Rename!"))
        self.rhythmSplit.setText(_translate("Ac7Renamer", "4 Variation Rhythm Split"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multiFileTab), _translate("Ac7Renamer", "Many files"))
        self.Buttons.setToolTip(_translate("Ac7Renamer", "Save as a new filename"))
from . import imageresources_rc
