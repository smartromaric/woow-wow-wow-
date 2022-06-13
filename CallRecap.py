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
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TableWidgetRecapAppel = QtWidgets.QTableWidget(self.centralwidget)
        self.TableWidgetRecapAppel.setGeometry(QtCore.QRect(130, 130, 551, 421))
        self.TableWidgetRecapAppel.setObjectName("TableWidgetRecapAppel")
        self.TableWidgetRecapAppel.setColumnCount(0)
        self.TableWidgetRecapAppel.setRowCount(0)
        self.FrameAppelRepondu = QtWidgets.QFrame(self.centralwidget)
        self.FrameAppelRepondu.setGeometry(QtCore.QRect(220, 60, 171, 61))
        self.FrameAppelRepondu.setStyleSheet("background-color: rgb(46, 204, 113);\n"
"color:rgb(255,255,255)")
        self.FrameAppelRepondu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameAppelRepondu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameAppelRepondu.setObjectName("FrameAppelRepondu")
        self.LabelBanierAppelRepondu = QtWidgets.QLabel(self.FrameAppelRepondu)
        self.LabelBanierAppelRepondu.setGeometry(QtCore.QRect(0, 30, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelBanierAppelRepondu.setFont(font)
        self.LabelBanierAppelRepondu.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelBanierAppelRepondu.setObjectName("LabelBanierAppelRepondu")
        self.LabelAppelRepondu = QtWidgets.QLabel(self.FrameAppelRepondu)
        self.LabelAppelRepondu.setGeometry(QtCore.QRect(10, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.LabelAppelRepondu.setFont(font)
        self.LabelAppelRepondu.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelAppelRepondu.setObjectName("LabelAppelRepondu")
        self.FrameAppelNonRepondu = QtWidgets.QFrame(self.centralwidget)
        self.FrameAppelNonRepondu.setGeometry(QtCore.QRect(410, 60, 171, 61))
        self.FrameAppelNonRepondu.setStyleSheet("background-color: rgb(231, 76, 60);\n"
"color:rgb(255,255,255)")
        self.FrameAppelNonRepondu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameAppelNonRepondu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameAppelNonRepondu.setObjectName("FrameAppelNonRepondu")
        self.LabelAppelRefuse = QtWidgets.QLabel(self.FrameAppelNonRepondu)
        self.LabelAppelRefuse.setGeometry(QtCore.QRect(10, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.LabelAppelRefuse.setFont(font)
        self.LabelAppelRefuse.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelAppelRefuse.setObjectName("LabelAppelRefuse")
        self.LabelBanierAppelNonRepondu = QtWidgets.QLabel(self.FrameAppelNonRepondu)
        self.LabelBanierAppelNonRepondu.setGeometry(QtCore.QRect(0, 30, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelBanierAppelNonRepondu.setFont(font)
        self.LabelBanierAppelNonRepondu.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelBanierAppelNonRepondu.setObjectName("LabelBanierAppelNonRepondu")
        self.FrameAppelTotal = QtWidgets.QFrame(self.centralwidget)
        self.FrameAppelTotal.setGeometry(QtCore.QRect(30, 60, 171, 61))
        self.FrameAppelTotal.setStyleSheet("background-color: rgb(52, 152, 219);\n"
"color:rgb(255,255,255)")
        self.FrameAppelTotal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameAppelTotal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameAppelTotal.setObjectName("FrameAppelTotal")
        self.LabelBanierAppelTotal = QtWidgets.QLabel(self.FrameAppelTotal)
        self.LabelBanierAppelTotal.setGeometry(QtCore.QRect(0, 30, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelBanierAppelTotal.setFont(font)
        self.LabelBanierAppelTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelBanierAppelTotal.setObjectName("LabelBanierAppelTotal")
        self.LabelAppelTotal = QtWidgets.QLabel(self.FrameAppelTotal)
        self.LabelAppelTotal.setGeometry(QtCore.QRect(10, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.LabelAppelTotal.setFont(font)
        self.LabelAppelTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelAppelTotal.setObjectName("LabelAppelTotal")
        self.FrameMessageVocal = QtWidgets.QFrame(self.centralwidget)
        self.FrameMessageVocal.setGeometry(QtCore.QRect(600, 60, 171, 61))
        self.FrameMessageVocal.setStyleSheet("background-color: rgb(230, 126, 34);\n"
"color:rgb(255,255,255)")
        self.FrameMessageVocal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameMessageVocal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameMessageVocal.setObjectName("FrameMessageVocal")
        self.LabelBanierMessageVocal = QtWidgets.QLabel(self.FrameMessageVocal)
        self.LabelBanierMessageVocal.setGeometry(QtCore.QRect(0, 30, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LabelBanierMessageVocal.setFont(font)
        self.LabelBanierMessageVocal.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelBanierMessageVocal.setObjectName("LabelBanierMessageVocal")
        self.LabelMessageVocal = QtWidgets.QLabel(self.FrameMessageVocal)
        self.LabelMessageVocal.setGeometry(QtCore.QRect(10, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.LabelMessageVocal.setFont(font)
        self.LabelMessageVocal.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelMessageVocal.setObjectName("LabelMessageVocal")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 632, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(52, 152, 219);\n"
"borser-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"border-color:#fff\n;"
"padding:5px\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LabelDateEdit = QtWidgets.QLabel(self.widget)
        self.LabelDateEdit.setObjectName("LabelDateEdit")
        self.horizontalLayout.addWidget(self.LabelDateEdit)
        self.EditDate = QtWidgets.QDateEdit(self.widget)
        self.EditDate.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 152, 219);\n"
"borser-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"border-color:#fff")
        self.EditDate.setCalendarPopup(True)
        self.EditDate.setDate(QtCore.QDate(2022, 1, 1))
        self.EditDate.setObjectName("EditDate")
        self.horizontalLayout.addWidget(self.EditDate)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelDateEdit_2 = QtWidgets.QLabel(self.widget)
        self.labelDateEdit_2.setObjectName("labelDateEdit_2")
        self.horizontalLayout_2.addWidget(self.labelDateEdit_2)
        self.EditDate_2 = QtWidgets.QDateEdit(self.widget)
        self.EditDate_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 152, 219);\n"
"borser-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"border-color:#fff")
        self.EditDate_2.setCalendarPopup(True)
        self.EditDate_2.setDate(QtCore.QDate(2022, 1, 1))
        self.EditDate_2.setObjectName("EditDate_2")
        self.horizontalLayout_2.addWidget(self.EditDate_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.BoutonSauvegarder = QtWidgets.QPushButton(self.widget)
        self.BoutonSauvegarder.setObjectName("BoutonSauvegarder")
        self.horizontalLayout_3.addWidget(self.BoutonSauvegarder)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actionRapport_Mensuelle = QtWidgets.QAction(MainWindow)
        self.actionRapport_Mensuelle.setObjectName("actionRapport_Mensuelle")
        self.actionRechercher_une_Date = QtWidgets.QAction(MainWindow)
        self.actionRechercher_une_Date.setObjectName("actionRechercher_une_Date")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CallRecap"))#nom de la fenetre
        self.LabelBanierAppelRepondu.setText(_translate("MainWindow", " Appel Repondu"))
        self.LabelAppelRepondu.setText(_translate("MainWindow", "0"))
        self.LabelAppelRefuse.setText(_translate("MainWindow", "0"))
        self.LabelBanierAppelNonRepondu.setText(_translate("MainWindow", " Appel non Repondu"))
        self.LabelBanierAppelTotal.setText(_translate("MainWindow", "Total Appel"))
        self.LabelAppelTotal.setText(_translate("MainWindow", "0"))
        self.LabelBanierMessageVocal.setText(_translate("MainWindow", " Message Vocal"))
        self.LabelMessageVocal.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Choisir Fichier"))
        self.LabelDateEdit.setText(_translate("MainWindow", "Date de Debut"))
        self.EditDate.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.labelDateEdit_2.setText(_translate("MainWindow", "Date de Fin"))
        self.EditDate_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.BoutonSauvegarder.setText(_translate("MainWindow", "Sauvegarder en Excel"))
        self.BoutonSauvegarder.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(52, 152, 219);\n"
                                      "borser-style:outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:5px;\n"
                                      "border-color:#fff;\n"
                                      "padding:5px\n"
                                      "")
        self.action_2.setText(_translate("MainWindow", "Choisir Fichier"))
        self.actionRapport_Mensuelle.setText(_translate("MainWindow", "Rapport Mensuelle"))
        self.actionRechercher_une_Date.setText(_translate("MainWindow", "Rechercher une Date"))
#import call-phone_rc

#Debut de la logique
        #ici ces les evenements
        self.pushButton.clicked.connect(self.clicker) #le clique sur le bouton choisir fichier
        self.EditDate_2.dateChanged.connect(self.date)# quand la date du 2ieme EditDate est changer
        self.BoutonSauvegarder.clicked.connect(self.save)#le clique sur le bouton exporter


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
