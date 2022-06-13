import datetime
from datetime import timedelta

from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QTableWidget,QFrame,QComboBox,QDateEdit,QStatusBar,QFileDialog,QPushButton,QTableWidgetItem
from PyQt5 import uic, QtWidgets
import sys
import pandas as pd
import xlsxwriter
import test

class CallCenter(QMainWindow):
    mois,Num,dateDebut,dateFin=0,0,0,0
    ListTotal,Listexport=[],[['AppelTotal','AppelRepondu','AppelRefuse','MessageVocal','Date de Debut','Date de Fin']]
    def __init__(self):
        super(CallCenter,self).__init__()

        #charger le fichie Callcenter
        uic.loadUi("Callcenter.ui",self)

        #efinir les element

        self.AppelReponse =self.findChild(QLabel,"LabelAppelRepondu")
        self.AppelRefuse=self.findChild(QLabel,"LabelAppelRefuse")
        self.TotalAppel=self.findChild(QLabel,"LabelAppelTotal")
        self.MessageVocal=self.findChild(QLabel,"LabelMessageVocal")
        self.button=self.findChild(QPushButton,"pushButton")
        self.sauvegarder = self.findChild(QPushButton, "BoutonSauvegarder")
        self.Date = self.findChild(QDateEdit, "EditDate")
        self.Date_2 = self.findChild(QDateEdit, "EditDate_2")
        self.tableWidget=self.findChild(QTableWidget,"TableWidgetRecapAppel")
        #action clique

        self.button.clicked.connect(self.clicker)
        self.Date_2.dateChanged.connect(self.date)
        self.sauvegarder.clicked.connect(self.save)

        #afficher l'application

        self.show()



    def clicker(self):
        try:
            Fichier = QFileDialog.getOpenFileName(self, 'Choisir Fichier', 'C:', 'CSV (*.csv);; Excel(*.xlsx')
            self.all_data = pd.read_csv(Fichier[0])
            NumRows = len(self.all_data.index)
            CallCenter.Num = NumRows
            self.tableWidget.setColumnCount(len(self.all_data.columns))
            self.tableWidget.setRowCount(NumRows)
            self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
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
            CallCenter.ListTotal = [total, reponse, pasRepondu, messageVocal]
            self.TotalAppel.setText(str(total))
            self.AppelReponse.setText(str(reponse))
            self.AppelRefuse.setText(str(pasRepondu))
            self.MessageVocal.setText(str(messageVocal))
            print(CallCenter.ListTotal)

        except:
            pass





    def date(self):
        try:
            dated = self.Date.date()
            b = dated.toPyDate()
            CallCenter.dateDebut = b.strftime('%d-%m-%Y')
            datedf = b.strftime('%m/%d/%Y')
            datef = self.Date_2.date()
            b2 = datef.toPyDate()
            CallCenter.dateFin = b2.strftime('%d-%m-%Y')
            dateff = b2.strftime('%m/%d/%Y')
            a = pd.date_range(start=datedf, end=dateff)
            messageVocal, pasRepondu, reponse, total = 0, 0, 0, 0
            l,c=0,0
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
                self.TotalAppel.setText(str(total))
                self.AppelReponse.setText(str(reponse))
                self.AppelRefuse.setText(str(pasRepondu))
                self.MessageVocal.setText(str(messageVocal))
            TempMonth = [total, reponse, pasRepondu, messageVocal, CallCenter.dateDebut, CallCenter.dateFin]
            CallCenter.Listexport.append(TempMonth)

        except:
            pass

    def save(self):
        try:
            if len(CallCenter.Listexport) == 1:
                # date de debut du fichier
                debut = self.all_data.Date[0][:10]
                cr_dated1 = datetime.datetime.strptime(debut, '%d/%m/%Y')
                cr_dated = cr_dated1.strftime("%d-%m-%Y")
                # fin du fichier
                fin = self.all_data.Date[CallCenter.Num - 1][:10]
                cr_datedf1 = datetime.datetime.strptime(fin, '%d/%m/%Y')
                cr_datedf = cr_datedf1.strftime("%d-%m-%Y")
                # Nommage du fichier
                file = str(QFileDialog.getExistingDirectory(self, "Selectioner Dossier"))
                CallCenter.Listexport.append(CallCenter.ListTotal)
                print( CallCenter.Listexport)
                with xlsxwriter.Workbook(f'{file}/Total.xlsx') as workbook:
                    worksheet = workbook.add_worksheet()
                    for row_num, data in enumerate(CallCenter.Listexport):
                        worksheet.write_row(row_num, 0, data)


            else:
                file = str(QFileDialog.getExistingDirectory(self, "Selectioner Dossier"))
                with xlsxwriter.Workbook(f'{file}/demo_{CallCenter.dateDebut}_{CallCenter.dateFin}.xlsx') as workbook:
                    worksheet = workbook.add_worksheet()
                    for row_num, data in enumerate(CallCenter.Listexport):
                        worksheet.write_row(row_num, 0, data)

        except:
            pass






# initialisation de l'application

app=QApplication(sys.argv)
UIwindow = CallCenter()
app.exec_()