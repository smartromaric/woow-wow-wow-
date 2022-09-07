# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CallcenterLOTRxu.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import call-phone_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 571)
        MainWindow.setMaximumSize(QSize(799, 571))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(247, 249, 249)")


        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.actionRapport_Mensuelle = QAction(MainWindow)
        self.actionRapport_Mensuelle.setObjectName(u"actionRapport_Mensuelle")
        self.actionRechercher_une_Date = QAction(MainWindow)
        self.actionRechercher_une_Date.setObjectName(u"actionRechercher_une_Date")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TableWidgetRecapAppel = QTableWidget(self.centralwidget)
        self.TableWidgetRecapAppel.setObjectName(u"TableWidgetRecapAppel")
        self.TableWidgetRecapAppel.setGeometry(QRect(130, 130, 551, 421))
        self.FrameAppelRepondu = QFrame(self.centralwidget)
        self.FrameAppelRepondu.setObjectName(u"FrameAppelRepondu")
        self.FrameAppelRepondu.setGeometry(QRect(220, 60, 171, 61))
        self.FrameAppelRepondu.setStyleSheet(u"background-color: rgb(46, 204, 113);\n"
"color:rgb(255,255,255)")
        self.FrameAppelRepondu.setFrameShape(QFrame.StyledPanel)
        self.FrameAppelRepondu.setFrameShadow(QFrame.Raised)
        self.LabelBanierAppelRepondu = QLabel(self.FrameAppelRepondu)
        self.LabelBanierAppelRepondu.setObjectName(u"LabelBanierAppelRepondu")
        self.LabelBanierAppelRepondu.setGeometry(QRect(0, 30, 171, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.LabelBanierAppelRepondu.setFont(font1)
        self.LabelBanierAppelRepondu.setAlignment(Qt.AlignCenter)
        self.LabelAppelRepondu = QLabel(self.FrameAppelRepondu)
        self.LabelAppelRepondu.setObjectName(u"LabelAppelRepondu")
        self.LabelAppelRepondu.setGeometry(QRect(10, 0, 151, 31))
        font2 = QFont()
        font2.setPointSize(19)
        font2.setBold(True)
        font2.setWeight(75)
        self.LabelAppelRepondu.setFont(font2)
        self.LabelAppelRepondu.setAlignment(Qt.AlignCenter)
        self.FrameAppelNonRepondu = QFrame(self.centralwidget)
        self.FrameAppelNonRepondu.setObjectName(u"FrameAppelNonRepondu")
        self.FrameAppelNonRepondu.setGeometry(QRect(410, 60, 171, 61))
        self.FrameAppelNonRepondu.setStyleSheet(u"background-color: rgb(231, 76, 60);\n"
"color:rgb(255,255,255)")
        self.FrameAppelNonRepondu.setFrameShape(QFrame.StyledPanel)
        self.FrameAppelNonRepondu.setFrameShadow(QFrame.Raised)
        self.LabelAppelRefuse = QLabel(self.FrameAppelNonRepondu)
        self.LabelAppelRefuse.setObjectName(u"LabelAppelRefuse")
        self.LabelAppelRefuse.setGeometry(QRect(10, 0, 151, 31))
        self.LabelAppelRefuse.setFont(font2)
        self.LabelAppelRefuse.setAlignment(Qt.AlignCenter)
        self.LabelBanierAppelNonRepondu = QLabel(self.FrameAppelNonRepondu)
        self.LabelBanierAppelNonRepondu.setObjectName(u"LabelBanierAppelNonRepondu")
        self.LabelBanierAppelNonRepondu.setGeometry(QRect(0, 30, 171, 21))
        self.LabelBanierAppelNonRepondu.setFont(font1)
        self.LabelBanierAppelNonRepondu.setAlignment(Qt.AlignCenter)
        self.FrameAppelTotal = QFrame(self.centralwidget)
        self.FrameAppelTotal.setObjectName(u"FrameAppelTotal")
        self.FrameAppelTotal.setGeometry(QRect(30, 60, 171, 61))
        self.FrameAppelTotal.setStyleSheet(u"background-color: rgb(52, 152, 219);\n"
"color:rgb(255,255,255)")
        self.FrameAppelTotal.setFrameShape(QFrame.StyledPanel)
        self.FrameAppelTotal.setFrameShadow(QFrame.Raised)
        self.LabelBanierAppelTotal = QLabel(self.FrameAppelTotal)
        self.LabelBanierAppelTotal.setObjectName(u"LabelBanierAppelTotal")
        self.LabelBanierAppelTotal.setGeometry(QRect(0, 30, 171, 21))
        self.LabelBanierAppelTotal.setFont(font1)
        self.LabelBanierAppelTotal.setAlignment(Qt.AlignCenter)
        self.LabelAppelTotal = QLabel(self.FrameAppelTotal)
        self.LabelAppelTotal.setObjectName(u"LabelAppelTotal")
        self.LabelAppelTotal.setGeometry(QRect(10, 0, 151, 31))
        self.LabelAppelTotal.setFont(font2)
        self.LabelAppelTotal.setAlignment(Qt.AlignCenter)
        self.FrameMessageVocal = QFrame(self.centralwidget)
        self.FrameMessageVocal.setObjectName(u"FrameMessageVocal")
        self.FrameMessageVocal.setGeometry(QRect(600, 60, 171, 61))
        self.FrameMessageVocal.setStyleSheet(u"background-color: rgb(230, 126, 34);\n"
"color:rgb(255,255,255)")
        self.FrameMessageVocal.setFrameShape(QFrame.StyledPanel)
        self.FrameMessageVocal.setFrameShadow(QFrame.Raised)
        self.LabelBanierMessageVocal = QLabel(self.FrameMessageVocal)
        self.LabelBanierMessageVocal.setObjectName(u"LabelBanierMessageVocal")
        self.LabelBanierMessageVocal.setGeometry(QRect(0, 30, 171, 21))
        self.LabelBanierMessageVocal.setFont(font1)
        self.LabelBanierMessageVocal.setAlignment(Qt.AlignCenter)
        self.LabelMessageVocal = QLabel(self.FrameMessageVocal)
        self.LabelMessageVocal.setObjectName(u"LabelMessageVocal")
        self.LabelMessageVocal.setGeometry(QRect(10, 0, 151, 31))
        self.LabelMessageVocal.setFont(font2)
        self.LabelMessageVocal.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 774, 27))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(52, 152, 219);\n"
"borser-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"border-color:#fff\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LabelDateEdit = QLabel(self.widget)
        self.LabelDateEdit.setObjectName(u"LabelDateEdit")

        self.horizontalLayout.addWidget(self.LabelDateEdit)

        self.EditDate = QDateEdit(self.widget)
        self.EditDate.setObjectName(u"EditDate")
        self.EditDate.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 152, 219);\n"
"borser-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"border-color:#fff")
        self.EditDate.setCalendarPopup(True)
        self.EditDate.setDate(QDate(2022, 1, 1))

        self.horizontalLayout.addWidget(self.EditDate)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelDateEdit_2 = QLabel(self.widget)
        self.labelDateEdit_2.setObjectName(u"labelDateEdit_2")

        self.horizontalLayout_2.addWidget(self.labelDateEdit_2)

        self.EditDate_2 = QDateEdit(self.widget)
        self.EditDate_2.setObjectName(u"EditDate_2")
        self.EditDate_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 152, 219);\n"
"borser-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"border-color:#fff")
        self.EditDate_2.setCalendarPopup(True)
        self.EditDate_2.setDate(QDate(2022, 1, 1))

        self.horizontalLayout_2.addWidget(self.EditDate_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 152, 219);\n"
"borser-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"border-color:#fff")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.BoutonSauvegarder = QPushButton(self.widget)
        self.BoutonSauvegarder.setObjectName(u"BoutonSauvegarder")

        self.horizontalLayout_3.addWidget(self.BoutonSauvegarder)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"Choisir Fichier", None))
        self.actionRapport_Mensuelle.setText(QCoreApplication.translate("MainWindow", u"Rapport Mensuelle", None))
        self.actionRechercher_une_Date.setText(QCoreApplication.translate("MainWindow", u"Rechercher une Date", None))
        self.LabelBanierAppelRepondu.setText(QCoreApplication.translate("MainWindow", u" Appel Repondu", None))
        self.LabelAppelRepondu.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.LabelAppelRefuse.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.LabelBanierAppelNonRepondu.setText(QCoreApplication.translate("MainWindow", u" Appel non Repondu", None))
        self.LabelBanierAppelTotal.setText(QCoreApplication.translate("MainWindow", u"Total Appel", None))
        self.LabelAppelTotal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.LabelBanierMessageVocal.setText(QCoreApplication.translate("MainWindow", u" Message Vocal", None))
        self.LabelMessageVocal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Choisir Fichier", None))
        self.LabelDateEdit.setText(QCoreApplication.translate("MainWindow", u"Date de Debut", None))
#if QT_CONFIG(tooltip)
        self.EditDate.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelDateEdit_2.setText(QCoreApplication.translate("MainWindow", u"Date de Fin", None))
#if QT_CONFIG(tooltip)
        self.EditDate_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Heure de Travail (08h00-16h000)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heure Supplementaire (16h01-07h59)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Week-end", None))

        self.BoutonSauvegarder.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder en Excel", None))
    # retranslateUi

