#jean Christ-Dawens.
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
from PyQt5.QtGui import QStandardItemModel

import UI_PY.Dialog_veterinaire
from PyQt5 import QtWidgets
from Classes.Classe_Veterinaire import *
#methodes/fonctions
def verifier_veterinaires_list(p_veterinaires):
    for elt in Veterinaire.ls_veterinaire:
        if elt.Numero_emp == p_veterinaires:
            return True
    return False

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreveterinaire(QtWidgets.QDialog, UI_PY.Dialog_veterinaire.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreveterinaire, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Vétérinaire")
        self.Ajouter_enclos_combobox()#permet d'ajouter les enclos a la comboBox a l'affichage
        self.label_erreur_numero_employe_existe_pas.setVisible(False)#cache les label d'erreur au lancement du programme
        self.label_erreur_numero_employe__existe.setVisible(False)#cache les label d'erreur au lancement du programme
        self.label_erreur_numero_employe_invalide.setVisible(False)#cache les label d'erreur au lancement du programme
        self.label_erreur_nom_employe.setVisible(False)#cache les label d'erreur au lancement du programme
        self.label_erreur_date_naiss.setVisible(False)#cache les label d'erreur au lancement du programme
        self.label_erreur_prenom_employe.setVisible(False)#cache les label d'erreur au lancement du programme

    def Ajouter_enclos_combobox(self):
        """
        Perment d'ajouter les enclos instancier a la combobox enclos animla
        :return:
        """
        for elt in Enclos.ls_enclos:
            self.comboBox_enclos_animal.addItem(elt.Numero_enclos)

    @pyqtSlot()
    def on_pushButton_ajout_veterinaire_clicked(self):
        """
        Gestionnaire d'evenements pour le bouton serialiser un veterinaire
        :return:
        """
        #Intancier les valeurs veterinaires
        veterinaire = Veterinaire()
        veterinaire.Numero_emp = self.lineEdit_numero_employe.text()
        veterinaire.Nom = self.lineEdit_nom_employe.text()
        veterinaire.Prenom = self.lineEdit_prenom_employe.text()
        veterinaire.Date_naiss = self.dateEdit_datenaiss_employe
        verifier_veterinaires = verifier_veterinaires_list(veterinaire.Numero_emp)#utiliser pour verifier si le veterinaires est deja dans la liste de veterinaires

        if verifier_veterinaires is True:#verifier si le veterinaries existe deja
            self.lineEdit_numero_employe.clear()#Enlever les valeur rentrez dans la lineEdit
            self.label_erreur_numero_employe__existe.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_numero_employe__existe.setText("Le numero d'employe existe deja")#Ecrire un message d'erreur

        if veterinaire.Numero_emp == "":#verifier si l'ecriture du numero est respecter
            self.lineEdit_numero_employe.clear()#Enlever les valeur rentrez dans la lineEdit
            self.label_erreur_numero_employe_invalide.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_numero_employe_invalide.setText("Entrez les 3 premiers caracteres du nom suivis de 2 chiffres")#Ecrire un message d'erreur

        if veterinaire.Nom == "":#verifier si l'ecriture du nom est respecter
            self.lineEdit_nom_employe.clear()#Enlever les valeur rentrez dans la lineEdit
            self.label_erreur_nom_employe.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_nom_employe.setText("Alphabetique de longueur inferieure a 50 caracteres")#Ecrire un message d'erreur

        if veterinaire.Prenom == "":
            self.lineEdit_prenom_employe.clear()
            self.label_erreur_prenom_employe.setVisible(True)
            self.label_erreur_prenom_employe.setText("Alphabetique de longueur inferieure a 50 caracteres")

        if veterinaire.Date_naiss== "":
            self.dateEdit_datenaiss_employe.clear()
            self.label_erreur_date_naiss.setVisible(True)
            self.label_erreur_date_naiss.setText("L'employe doit avoir au moins 18 ans")
        #si toutes les valeurs sont respectées on instencie un veterinaires
        if veterinaire.Numero_emp != "" and veterinaire.Nom != "" and veterinaire.Prenom != "" and veterinaire.Date_naiss !="" and verifier_veterinaires is False:#si toutes les valeurs sont respectées on instencie un veterinaires
            Veterinaire.ls_veterinaire.append(veterinaire)#on ajoute le veterinaires a la liste de veterinaires
            self.serialiser(veterinaire)

    @pyqtSlot()
    def on_pushButton_ajouter_enclos_liste_clicked(self):
        #preparation de la liste view
        model = QStandardItemModel()
        self.listView_liste_enclos.setModel(model)
        model.clear()
        for elt in Enclos.ls_enclos:
            if self.comboBox_enclos_animal.currentText() == self.comboBox_enclos_animal.currentText():
                item = QStandardItemModel(elt.Numero_enclos)
                model.appendRow(item)
