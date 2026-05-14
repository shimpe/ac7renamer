# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ac7renamerdlg.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QTextBrowser, QVBoxLayout,
    QWidget)
from . import imageresources_rc

class Ui_Ac7Renamer(object):
    def setupUi(self, Ac7Renamer):
        if not Ac7Renamer.objectName():
            Ac7Renamer.setObjectName(u"Ac7Renamer")
        Ac7Renamer.resize(1286, 642)
        icon = QIcon()
        icon.addFile(u":/icons/images/restyle_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Ac7Renamer.setWindowIcon(icon)
        Ac7Renamer.setAutoFillBackground(False)
        Ac7Renamer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Ac7Renamer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Ac7Renamer)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QSize(0, 75))
        self.textBrowser.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setBold(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"background-color:rgb(127,227,255)")

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.aboutButton = QPushButton(Ac7Renamer)
        self.aboutButton.setObjectName(u"aboutButton")

        self.horizontalLayout_5.addWidget(self.aboutButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Ac7Renamer)
        self.tabWidget.setObjectName(u"tabWidget")
        self.singleFileTab = QWidget()
        self.singleFileTab.setObjectName(u"singleFileTab")
        self.verticalLayout_3 = QVBoxLayout(self.singleFileTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.singleFileTab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.singleFileTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_2)

        self.currentDisplayName = QLineEdit(self.singleFileTab)
        self.currentDisplayName.setObjectName(u"currentDisplayName")
        self.currentDisplayName.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.currentDisplayName)

        self.label = QLabel(self.singleFileTab)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.desiredDisplayName = QLineEdit(self.singleFileTab)
        self.desiredDisplayName.setObjectName(u"desiredDisplayName")
        self.desiredDisplayName.setReadOnly(False)

        self.verticalLayout_3.addWidget(self.desiredDisplayName)

        self.label_5 = QLabel(self.singleFileTab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_3 = QLabel(self.singleFileTab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.firstRow = QHBoxLayout()
        self.firstRow.setObjectName(u"firstRow")
        self.curEl1 = QComboBox(self.singleFileTab)
        self.curEl1.addItem("")
        self.curEl1.setObjectName(u"curEl1")
        self.curEl1.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.curEl1.sizePolicy().hasHeightForWidth())
        self.curEl1.setSizePolicy(sizePolicy1)
        self.curEl1.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.firstRow.addWidget(self.curEl1)

        self.curEl2 = QComboBox(self.singleFileTab)
        self.curEl2.addItem("")
        self.curEl2.setObjectName(u"curEl2")
        self.curEl2.setEnabled(False)

        self.firstRow.addWidget(self.curEl2)

        self.curEl4 = QComboBox(self.singleFileTab)
        self.curEl4.addItem("")
        self.curEl4.setObjectName(u"curEl4")
        self.curEl4.setEnabled(False)

        self.firstRow.addWidget(self.curEl4)

        self.curEl3 = QComboBox(self.singleFileTab)
        self.curEl3.addItem("")
        self.curEl3.setObjectName(u"curEl3")
        self.curEl3.setEnabled(False)

        self.firstRow.addWidget(self.curEl3)

        self.curEl5 = QComboBox(self.singleFileTab)
        self.curEl5.addItem("")
        self.curEl5.setObjectName(u"curEl5")
        self.curEl5.setEnabled(False)

        self.firstRow.addWidget(self.curEl5)

        self.curEl6 = QComboBox(self.singleFileTab)
        self.curEl6.addItem("")
        self.curEl6.setObjectName(u"curEl6")
        self.curEl6.setEnabled(False)

        self.firstRow.addWidget(self.curEl6)

        self.curEl8 = QComboBox(self.singleFileTab)
        self.curEl8.addItem("")
        self.curEl8.setObjectName(u"curEl8")
        self.curEl8.setEnabled(False)
        self.curEl8.setEditable(False)

        self.firstRow.addWidget(self.curEl8)

        self.curEl10 = QComboBox(self.singleFileTab)
        self.curEl10.addItem("")
        self.curEl10.setObjectName(u"curEl10")
        self.curEl10.setEnabled(False)

        self.firstRow.addWidget(self.curEl10)

        self.curEl9 = QComboBox(self.singleFileTab)
        self.curEl9.addItem("")
        self.curEl9.setObjectName(u"curEl9")
        self.curEl9.setEnabled(False)

        self.firstRow.addWidget(self.curEl9)

        self.curEl11 = QComboBox(self.singleFileTab)
        self.curEl11.addItem("")
        self.curEl11.setObjectName(u"curEl11")
        self.curEl11.setEnabled(False)

        self.firstRow.addWidget(self.curEl11)

        self.curEl7 = QComboBox(self.singleFileTab)
        self.curEl7.addItem("")
        self.curEl7.setObjectName(u"curEl7")
        self.curEl7.setEnabled(False)

        self.firstRow.addWidget(self.curEl7)

        self.curEl12 = QComboBox(self.singleFileTab)
        self.curEl12.addItem("")
        self.curEl12.setObjectName(u"curEl12")
        self.curEl12.setEnabled(False)

        self.firstRow.addWidget(self.curEl12)


        self.verticalLayout_3.addLayout(self.firstRow)

        self.label_4 = QLabel(self.singleFileTab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.secRow = QHBoxLayout()
        self.secRow.setObjectName(u"secRow")
        self.desEl1 = QComboBox(self.singleFileTab)
        self.desEl1.setObjectName(u"desEl1")
        self.desEl1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl1)

        self.desEl2 = QComboBox(self.singleFileTab)
        self.desEl2.setObjectName(u"desEl2")
        self.desEl2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl2)

        self.desEl4 = QComboBox(self.singleFileTab)
        self.desEl4.setObjectName(u"desEl4")
        self.desEl4.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl4)

        self.desEl3 = QComboBox(self.singleFileTab)
        self.desEl3.setObjectName(u"desEl3")
        self.desEl3.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl3)

        self.desEl5 = QComboBox(self.singleFileTab)
        self.desEl5.setObjectName(u"desEl5")
        self.desEl5.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl5)

        self.desEl6 = QComboBox(self.singleFileTab)
        self.desEl6.setObjectName(u"desEl6")
        self.desEl6.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl6)

        self.desEl8 = QComboBox(self.singleFileTab)
        self.desEl8.setObjectName(u"desEl8")
        self.desEl8.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl8)

        self.desEl10 = QComboBox(self.singleFileTab)
        self.desEl10.setObjectName(u"desEl10")
        self.desEl10.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl10)

        self.desEl9 = QComboBox(self.singleFileTab)
        self.desEl9.setObjectName(u"desEl9")
        self.desEl9.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.secRow.addWidget(self.desEl9)

        self.desEl11 = QComboBox(self.singleFileTab)
        self.desEl11.setObjectName(u"desEl11")
        self.desEl11.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl11)

        self.desEl7 = QComboBox(self.singleFileTab)
        self.desEl7.setObjectName(u"desEl7")
        self.desEl7.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl7)

        self.desEl12 = QComboBox(self.singleFileTab)
        self.desEl12.setObjectName(u"desEl12")
        self.desEl12.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.secRow.addWidget(self.desEl12)


        self.verticalLayout_3.addLayout(self.secRow)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.saveButton = QPushButton(self.singleFileTab)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.singleFileTab, "")
        self.multiFileTab = QWidget()
        self.multiFileTab.setObjectName(u"multiFileTab")
        self.verticalLayout_4 = QVBoxLayout(self.multiFileTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.loadFolderContent = QPushButton(self.multiFileTab)
        self.loadFolderContent.setObjectName(u"loadFolderContent")

        self.horizontalLayout_3.addWidget(self.loadFolderContent)

        self.selectAll = QPushButton(self.multiFileTab)
        self.selectAll.setObjectName(u"selectAll")

        self.horizontalLayout_3.addWidget(self.selectAll)

        self.deselectAll = QPushButton(self.multiFileTab)
        self.deselectAll.setObjectName(u"deselectAll")

        self.horizontalLayout_3.addWidget(self.deselectAll)

        self.invertSelection = QPushButton(self.multiFileTab)
        self.invertSelection.setObjectName(u"invertSelection")

        self.horizontalLayout_3.addWidget(self.invertSelection)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.fileListing = QTableView(self.multiFileTab)
        self.fileListing.setObjectName(u"fileListing")

        self.verticalLayout_4.addWidget(self.fileListing)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.renameFolderContent = QPushButton(self.multiFileTab)
        self.renameFolderContent.setObjectName(u"renameFolderContent")

        self.horizontalLayout_4.addWidget(self.renameFolderContent)

        self.rhythmSplit = QPushButton(self.multiFileTab)
        self.rhythmSplit.setObjectName(u"rhythmSplit")

        self.horizontalLayout_4.addWidget(self.rhythmSplit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.multiFileTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.Buttons = QDialogButtonBox(Ac7Renamer)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setOrientation(Qt.Horizontal)
        self.Buttons.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout_2.addWidget(self.Buttons)


        self.verticalLayout.addLayout(self.verticalLayout_2)

#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.currentDisplayName)
        self.label.setBuddy(self.desiredDisplayName)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.textBrowser, self.aboutButton)
        QWidget.setTabOrder(self.aboutButton, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.currentDisplayName)
        QWidget.setTabOrder(self.currentDisplayName, self.desiredDisplayName)
        QWidget.setTabOrder(self.desiredDisplayName, self.curEl1)
        QWidget.setTabOrder(self.curEl1, self.desEl1)
        QWidget.setTabOrder(self.desEl1, self.curEl2)
        QWidget.setTabOrder(self.curEl2, self.desEl2)
        QWidget.setTabOrder(self.desEl2, self.curEl4)
        QWidget.setTabOrder(self.curEl4, self.desEl4)
        QWidget.setTabOrder(self.desEl4, self.curEl3)
        QWidget.setTabOrder(self.curEl3, self.desEl3)
        QWidget.setTabOrder(self.desEl3, self.curEl5)
        QWidget.setTabOrder(self.curEl5, self.desEl5)
        QWidget.setTabOrder(self.desEl5, self.curEl6)
        QWidget.setTabOrder(self.curEl6, self.desEl6)
        QWidget.setTabOrder(self.desEl6, self.curEl8)
        QWidget.setTabOrder(self.curEl8, self.desEl8)
        QWidget.setTabOrder(self.desEl8, self.curEl10)
        QWidget.setTabOrder(self.curEl10, self.desEl10)
        QWidget.setTabOrder(self.desEl10, self.curEl9)
        QWidget.setTabOrder(self.curEl9, self.desEl9)
        QWidget.setTabOrder(self.desEl9, self.curEl11)
        QWidget.setTabOrder(self.curEl11, self.desEl11)
        QWidget.setTabOrder(self.desEl11, self.curEl7)
        QWidget.setTabOrder(self.curEl7, self.desEl7)
        QWidget.setTabOrder(self.desEl7, self.curEl12)
        QWidget.setTabOrder(self.curEl12, self.desEl12)
        QWidget.setTabOrder(self.desEl12, self.saveButton)
        QWidget.setTabOrder(self.saveButton, self.loadFolderContent)
        QWidget.setTabOrder(self.loadFolderContent, self.selectAll)
        QWidget.setTabOrder(self.selectAll, self.deselectAll)
        QWidget.setTabOrder(self.deselectAll, self.invertSelection)
        QWidget.setTabOrder(self.invertSelection, self.fileListing)
        QWidget.setTabOrder(self.fileListing, self.renameFolderContent)
        QWidget.setTabOrder(self.renameFolderContent, self.rhythmSplit)

        self.retranslateUi(Ac7Renamer)
        self.Buttons.accepted.connect(Ac7Renamer.accept)
        self.Buttons.rejected.connect(Ac7Renamer.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Ac7Renamer)
    # setupUi

    def retranslateUi(self, Ac7Renamer):
        Ac7Renamer.setWindowTitle(QCoreApplication.translate("Ac7Renamer", u"Restyles piles of files!", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Ac7Renamer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool is GPLv3 charityware. Use and copy it freely,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">but if you keep using it, please consider</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">making a donation to a charity of your choice.</p></body></html>", None))
        self.aboutButton.setText(QCoreApplication.translate("Ac7Renamer", u"About this tool", None))
        self.pushButton.setText(QCoreApplication.translate("Ac7Renamer", u"Load Ac7 File", None))
        self.label_2.setText(QCoreApplication.translate("Ac7Renamer", u"Current display name", None))
        self.currentDisplayName.setPlaceholderText(QCoreApplication.translate("Ac7Renamer", u"(will be loaded from file)", None))
        self.label.setText(QCoreApplication.translate("Ac7Renamer", u"Desired display name (max 12 chars)", None))
        self.desiredDisplayName.setText("")
        self.desiredDisplayName.setPlaceholderText(QCoreApplication.translate("Ac7Renamer", u"(type here)", None))
        self.label_5.setText(QCoreApplication.translate("Ac7Renamer", u"[Optionally] Reorder elements", None))
        self.label_3.setText(QCoreApplication.translate("Ac7Renamer", u"Current ordering", None))
        self.curEl1.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"intro (1)", None))

        self.curEl2.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"normal (1)", None))

        self.curEl4.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"fill-in (1)", None))

        self.curEl3.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"var (2)", None))

        self.curEl5.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"fill-in (2)", None))

        self.curEl6.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"end (1)", None))

        self.curEl8.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"var (3)", None))

        self.curEl8.setCurrentText(QCoreApplication.translate("Ac7Renamer", u"var (3)", None))
        self.curEl10.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"fill-in (3)", None))

        self.curEl9.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"var (4)", None))

        self.curEl11.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"fill-in (4)", None))

        self.curEl7.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"intro (2)", None))

        self.curEl12.setItemText(0, QCoreApplication.translate("Ac7Renamer", u"end (2)", None))

        self.label_4.setText(QCoreApplication.translate("Ac7Renamer", u"Desired ordering", None))
        self.saveButton.setText(QCoreApplication.translate("Ac7Renamer", u"Save AC7 File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.singleFileTab), QCoreApplication.translate("Ac7Renamer", u"Single file", None))
        self.loadFolderContent.setText(QCoreApplication.translate("Ac7Renamer", u"Load folder", None))
        self.selectAll.setText(QCoreApplication.translate("Ac7Renamer", u"Select All", None))
        self.deselectAll.setText(QCoreApplication.translate("Ac7Renamer", u"Deselect All", None))
        self.invertSelection.setText(QCoreApplication.translate("Ac7Renamer", u"Invert Selection", None))
        self.renameFolderContent.setText(QCoreApplication.translate("Ac7Renamer", u"Rename!", None))
        self.rhythmSplit.setText(QCoreApplication.translate("Ac7Renamer", u"4 Variation Rhythm Split", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multiFileTab), QCoreApplication.translate("Ac7Renamer", u"Many files", None))
#if QT_CONFIG(tooltip)
        self.Buttons.setToolTip(QCoreApplication.translate("Ac7Renamer", u"Save as a new filename", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

