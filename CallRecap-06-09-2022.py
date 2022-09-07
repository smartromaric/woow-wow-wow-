# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Callcenter.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, QCoreApplication, QMetaObject, QDate, QRect, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QStatusBar, QPushButton, QSpacerItem, QSizePolicy, QDateEdit, \
    QHBoxLayout, QLabel, QWidget, QFrame, QTableWidget, QAction, QComboBox
import pandas as pd
import xlsxwriter

##Gestion de l'icon de la barre des taches
basedir = os.path.dirname(__file__)
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'HallTechAfrica.CallRecap.Smart.1.5'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass
##Fin de la gestion de l'icon de la barre des taches
class CallCenter(object):
    mois, Num, dateDebut, dateFin = 0, 0, 0, 0
    ListTotal, Listexport = [], [['AppelTotal', 'AppelRepondu', 'AppelRefuse', 'MessageVocal','Date de Debut','Date de Fin']]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 571)
        MainWindow.setMaximumSize(QtCore.QSize(799, 571))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setFont(font)
        #Debut change icon
        # icon = QIcon()
        # icon.addFile(u"process.ico", QSize(), QIcon.Active, QIcon.On)
        # MainWindow.setWindowIcon(icon)
        #Fin change icon
        MainWindow.setStyleSheet("background-color: rgb(247, 249, 249)")

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
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(52, 152, 219);\n"
                                      "borser-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:5px;\n"
                                      "border-color:#fff\n;"
                                      "padding:5px\n"
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

        self.BoutonSauvegarder.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(52, 152, 219);\n"
                                      "borser-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:5px;\n"
                                      "border-color:#fff\n;"
                                      "padding:5px\n"
                                      "")

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
        # if QT_CONFIG(tooltip)
        self.EditDate.setToolTip(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>",
                                       None))
        # endif // QT_CONFIG(tooltip)
        self.labelDateEdit_2.setText(QCoreApplication.translate("MainWindow", u"Date de Fin", None))
        # if QT_CONFIG(tooltip)
        self.EditDate_2.setToolTip(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>",
                                       None))
        # endif // QT_CONFIG(tooltip)
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Horaire", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heure de Travail (08h00-16h000)", None))
        self.comboBox.setItemText(2,
                                  QCoreApplication.translate("MainWindow", u"Heure Supplementaire (16h01-07h59)", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Week-end", None))

        self.BoutonSauvegarder.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder en Excel", None))
        # retranslateUi

        #import call-phone_rc

#Debut de la logique
        #ici ces les evenements
        self.pushButton.clicked.connect(self.clicker) #le clique sur le bouton choisir fichier
        self.EditDate_2.dateChanged.connect(self.date)# quand la date du 2ieme EditDate est changer
        self.BoutonSauvegarder.clicked.connect(self.save)#le clique sur le bouton exporter
        self.comboBox.currentIndexChanged.connect(self.combo)#le combobox des horaire


    #ici c'est les action
    def clicker(self):#les actions du bouton choisir fichier
        try:
            Fichier = QFileDialog.getOpenFileName(None, 'Choisir Fichier', 'C:', 'CSV (*.csv);; Excel(*.xlsx')#ouvrir fenêtre de choix
            self.all_data = pd.read_csv(Fichier[0])
            NumRows = len(self.all_data.index)
            CallCenter.Num = NumRows
            self.TableWidgetRecapAppel.setColumnCount(len(self.all_data.columns))
            self.TableWidgetRecapAppel.setRowCount(NumRows)
            self.TableWidgetRecapAppel.setHorizontalHeaderLabels(self.all_data.columns)

            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.TableWidgetRecapAppel.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

            self.TableWidgetRecapAppel.resizeColumnsToContents()
            self.TableWidgetRecapAppel.resizeRowsToContents()
            messageVocal, pasRepondu, reponse, total = 0, 0, 0, 0
            listTemp, final = [], []
            ########
            for d in range(NumRows):

                # quand on a un 1000 ou 9999 alors c'est un appelle reussi
                if self.all_data.Destination[d][-5:-1] == "1000" or self.all_data.Destination[d][-5:-1] == "9999" and \
                        self.all_data.Conversation[d] != "non répondu":
                    if self.all_data.Destination[d][
                       :2] == "VM":  # quand on a VM au debut dans la colonne Destinataire alors c'est un message vocal
                        messageVocal += 1
                        # print(self.all_data.Date[d][3:5])
                    else:
                        reponse += 1
                else:
                    if self.all_data.Destination[d][-5:-1] == "8004" and self.all_data.Conversation[
                        d] == "non répondu":
                        # quand on a un 8004 c'est que on a tenté d'appeller
                        listTemp.append(self.all_data.Date[d])
                        if listTemp.count(self.all_data.Date[d]) == 1:
                            final.append(self.all_data.Date[d])

                    elif self.all_data.Destination[d][-5:-1] == "8004" and self.all_data.Conversation[
                        d] != "non répondu":
                        reponse += 1
            pasRepondu = len(final)
            total = reponse + pasRepondu + messageVocal
            CallCenter.ListTotal = [total, reponse, pasRepondu, messageVocal,self.all_data.Date[0][:10],self.all_data.Date[len(self.all_data)-1][:10]]
            self.LabelAppelTotal.setText(str(total))
            self.LabelAppelRepondu.setText(str(reponse))
            self.LabelAppelRefuse.setText(str(pasRepondu))
            self.LabelMessageVocal.setText(str(messageVocal))
            CallCenter.Listexport.append(CallCenter.ListTotal)


        except:
            pass

    def date(self):
        try:
            dated = self.EditDate.date()
            b = dated.toPyDate()
            CallCenter.dateDebut = b.strftime('%d-%m-%Y')
            datedf = b.strftime('%m/%d/%Y')
            datef = self.EditDate_2.date()
            b2 = datef.toPyDate()
            CallCenter.dateFin = b2.strftime('%d-%m-%Y')
            dateff = b2.strftime('%m/%d/%Y')
            a = pd.date_range(start=datedf, end=dateff)
            messageVocal, pasRepondu, reponse, total = 0, 0, 0, 0
            listTemp, final = [], []
            for d in range(CallCenter.Num):
                cr_date = self.all_data.Date[d][:10]
                cr_date = datetime.datetime.strptime(cr_date, '%d/%m/%Y')
                cr_date = cr_date.strftime("%Y/%m/%d")
                if cr_date in a:

                    # quand on a un 1000 ou 9999 alors c'est un appelle reussi
                    if self.all_data.Destination[d][-5:-1] == "1000" or self.all_data.Destination[d][
                                                                        -5:-1] == "9999" and \
                            self.all_data.Conversation[d] != "non répondu":
                        if self.all_data.Destination[d][
                           :2] == "VM":  # quand on a VM au debut dans la colonne Destinataire alors c'est un message vocal
                            messageVocal += 1
                            # print(self.all_data.Date[d][3:5])
                        else:
                            reponse += 1
                    else:
                        if self.all_data.Destination[d][-5:-1] == "8004" and self.all_data.Conversation[
                            d] == "non répondu":
                            # quand on a un 8004 c'est que on a tenté d'appeller
                            listTemp.append(self.all_data.Date[d])
                            if listTemp.count(self.all_data.Date[d]) == 1:
                                final.append(self.all_data.Date[d])

                        elif self.all_data.Destination[d][-5:-1] == "8004" and self.all_data.Conversation[
                            d] != "non répondu":
                            reponse += 1
                pasRepondu = len(final)
                total = reponse + pasRepondu + messageVocal
                self.LabelAppelTotal.setText(str(total))
                self.LabelAppelRepondu.setText(str(reponse))
                self.LabelAppelRefuse.setText(str(pasRepondu))
                self.LabelMessageVocal.setText(str(messageVocal))
            TempMonth = [total, reponse, pasRepondu, messageVocal, CallCenter.dateDebut, CallCenter.dateFin]
            CallCenter.Listexport.append(TempMonth)

        except:
            pass

    def save(self):
        try:
            # date de debut du fichier
            debut = self.all_data.Date[0][:10]
            cr_dated1 = datetime.datetime.strptime(debut, '%d/%m/%Y')
            cr_dated = cr_dated1.strftime("%d-%m-%Y")
            # fin du fichier
            fin = self.all_data.Date[CallCenter.Num - 1][:10]
            cr_datedf1 = datetime.datetime.strptime(fin, '%d/%m/%Y')
            cr_datedf = cr_datedf1.strftime("%d-%m-%Y")
            # Nommage du fichier
            if CallCenter.dateFin == 0:
                file = str(QFileDialog.getExistingDirectory(None, "Selectioner Dossier"))
                with xlsxwriter.Workbook(f'{file}/Total.xlsx') as workbook:
                    worksheet = workbook.add_worksheet()
                    for row_num, data in enumerate(CallCenter.Listexport):
                        worksheet.write_row(row_num, 0, data)
            else:
                CallCenter.Listexport.pop(1)
                print(CallCenter.Listexport)
                file = str(QFileDialog.getExistingDirectory(None, "Selectioner Dossier"))
                with xlsxwriter.Workbook(f'{file}/demo_{CallCenter.dateDebut}_{CallCenter.dateFin}.xlsx') as workbook:
                    worksheet = workbook.add_worksheet()
                    for row_num, data in enumerate(CallCenter.Listexport):
                        worksheet.write_row(row_num, 0, data)



            # if len(CallCenter.Listexport) == 1:
            #     # date de debut du fichier
            #     debut = self.all_data.Date[0][:10]
            #     cr_dated1 = datetime.datetime.strptime(debut, '%d/%m/%Y')
            #     cr_dated = cr_dated1.strftime("%d-%m-%Y")
            #     # fin du fichier
            #     fin = self.all_data.Date[CallCenter.Num - 1][:10]
            #     cr_datedf1 = datetime.datetime.strptime(fin, '%d/%m/%Y')
            #     cr_datedf = cr_datedf1.strftime("%d-%m-%Y")
            #     # Nommage du fichier
            #     file = str(QFileDialog.getExistingDirectory(None, "Selectioner Dossier"))
            #     CallCenter.Listexport.append(CallCenter.ListTotal)
            #     print(CallCenter.Listexport)
            #     with xlsxwriter.Workbook(f'{file}/Total.xlsx') as workbook:
            #         worksheet = workbook.add_worksheet()
            #         for row_num, data in enumerate(CallCenter.Listexport):
            #             worksheet.write_row(row_num, 0, data)
            #
            #
            # else:
            #     file = str(QFileDialog.getExistingDirectory(None, "Selectioner Dossier"))
            #     with xlsxwriter.Workbook(f'{file}/demo_{CallCenter.dateDebut}_{CallCenter.dateFin}.xlsx') as workbook:
            #         worksheet = workbook.add_worksheet()
            #         for row_num, data in enumerate(CallCenter.Listexport):
            #             worksheet.write_row(row_num, 0, data)


        except:
            pass


    def combo(self):
        repondu_temp=0
        def temps(Hs,Hf,Ms,Mf,Ss,Sf):
            messageVocal, pasRepondu, reponse, total = 0, 0, 0, 0
            listTemp, final = [], []
            for d in range(CallCenter.Num):
                start = datetime.time(Hs, Ms, Ss)
                end = datetime.time(Hf, Mf, Sf)
                cr_date = datetime.datetime.strptime(self.all_data.Date[d][11:19], '%H:%M:%S')
                cr_date = cr_date.time()
                if start <= cr_date <= end:

                    # quand on a un 1000 ou 9999 alors c'est un appelle reussi
                    if self.all_data.Destination[d][-5:-1] == "1000" or self.all_data.Destination[d][
                                                                        -5:-1] == "9999" and \
                            self.all_data.Conversation[d] != "non répondu":
                        if self.all_data.Destination[d][
                           :2] == "VM":  # quand on a VM au debut dans la colonne Destinataire alors c'est un message vocal
                            messageVocal += 1
                            # print(self.all_data.Date[d][3:5])
                        else:
                            reponse += 1
                    else:
                        if self.all_data.Destination[d][-5:-1] == "8004" and self.all_data.Conversation[
                            d] == "non répondu":
                            # quand on a un 8004 c'est que on a tenté d'appeller
                            listTemp.append(self.all_data.Date[d])
                            if listTemp.count(self.all_data.Date[d]) == 1:
                                final.append(self.all_data.Date[d])

                        elif self.all_data.Destination[d][-5:-1] == "8004" and self.all_data.Conversation[
                            d] != "non répondu":
                            reponse += 1
                pasRepondu = len(final)
                total = reponse + pasRepondu + messageVocal
                repondu_temp = {"total":total,"pasrepondu":pasRepondu,"reponse":reponse,"MessageVocal":messageVocal}
            return repondu_temp


        if self.comboBox.currentIndex()==1:#08h00-16h00
           b=temps(8,16,0,0,0,0)
           self.LabelAppelTotal.setText(str(b["total"]))
           self.LabelAppelRepondu.setText(str(b["reponse"]))
           self.LabelAppelRefuse.setText(str(b["pasrepondu"]))
           self.LabelMessageVocal.setText(str(b["MessageVocal"]))
        elif self.comboBox.currentIndex()==2:
            a=temps(16, 23, 1, 59, 0, 0)
            c=temps(0, 7, 0, 59, 0, 0)
            total=a["total"]+c["total"]
            reponse=a["reponse"]+c["reponse"]
            pasrepondu=a["pasrepondu"]+c["pasrepondu"]
            MessageVocal=a["MessageVocal"]+c["MessageVocal"]
            self.LabelAppelTotal.setText(str(total))
            self.LabelAppelRepondu.setText(str(reponse))
            self.LabelAppelRefuse.setText(str(pasrepondu))
            self.LabelMessageVocal.setText(str(MessageVocal))

        elif self.comboBox.currentIndex()==3:
            print(self.comboBox.currentText())





#####


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QtGui.QIcon('process.ico'))
    #gestion de l'icon de la fenetre
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'process.ico')))
    #fin de la gestion de l'icon de la fenetre
    MainWindow = QtWidgets.QMainWindow()
    ui = CallCenter()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
