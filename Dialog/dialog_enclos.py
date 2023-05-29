#Jean Christ-Dawens
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_enclos
from PyQt5 import QtWidgets
from Classes.Classe_Enclos import *

#Methoes/Fonction
def verifier_enclos_liste(p_enclos):
    """
    Verifier si l'enclos est deja present dans la liste des enclos
    """
    for elt in Enclos.ls_enclos:
        if elt.Numero_enclos == p_enclos:
            return True #L'enclos existe
    return False #L'enclos existe pas

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreenclos(QtWidgets.QDialog, UI_PY.Dialog_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreenclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Enclos")
        self.label_erreur_numero_enclos_existe.setVisible(False)
        self.label_erreur_numero_enclos_existe_pas.setVisible(False)
        self.label_erreur_validation_numero_enclos.setVisible(False)
        self.label_erreur_nom_enclos.setVisible(False)
    @pyqtSlot()
    def on_pushButton_Ajouter_enclos_clicked(self):
        """
        Gestionniare d'evenement pour le bouton ajouter enclos
        """
        #Instancier les valeurs pour l'enclos
        enclos = Enclos()
        enclos.Numero_enclos = self.lineEdit_numero_enclos.text()
        enclos.Nom_enclos = self.lineEdit_nom_enclos.text()
        enclos.Taille = self.comboBox_taille_enclos.currentText()
        enclos.Type = self.comboBox_type_enclos.currentText()
        enclos.Localisation = self.comboBox_localisation.currentText()
        verifier_enclos = verifier_enclos_liste(enclos.Numero_enclos)#verifier si l'enclos existe deja
        #Validation
        if verifier_enclos is True:
            #si l'enclos existe deja on enleve les valeurs deja entrer et on ecrit un message d'erreur
            self.lineEdit_numero_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.lineEdit_nom_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.label_erreur_numero_enclos_existe.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_numero_enclos_existe.setText("Ce numeor d'ecnlos existe deja")#On ecrit un message d'erreur pour l'utilisateur

        if enclos.Numero_enclos == "":#Verifier qui l'ecriture du numero de l'enclos est respecter
            self.lineEdit_numero_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.label_erreur_validation_numero_enclos.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_validation_numero_enclos.setText("Entrez un nombre positif entier sur 5 caracteres"
                                                               "suivi de trois lettres")#On ecrit un message d'erreur pour l'utilisateur
        if enclos.Nom_enclos == "":#Verifier qui l'ecriture du nom l'enclos est respecter
            self.lineEdit_nom_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.label_erreur_nom_enclos.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_nom_enclos.setText("Alphabetique de longueur maximale egale a 25 lettres")#On ecrit un message d'erreur pour l'utilisateur

        if enclos.Numero_enclos != "" and enclos.Nom_enclos != "" and verifier_enclos is False:#si tout les valeur sont respecter on instencie l'enlcos
            Enclos.ls_enclos.append(enclos)#Ajouter l'ecnlos a la liste de l'enclos
            self.lineEdit_numero_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.lineEdit_nom_enclos.clear()#Enlever les valeur deja present dans la lineEdit
    @pyqtSlot()
    def on_pushButton_supprimer_enclos(self):
        #Instancier les valeurs pour l'enclos
        enclos = Enclos()
        enclos.Numero_enclos = self.lineEdit_numero_enclos.text()
        enclos.Nom_enclos = self.lineEdit_nom_enclos.text()
        enclos.Taille = self.comboBox_taille_enclos.currentText()
        enclos.Type = self.comboBox_type_enclos.currentText()
        enclos.Localisation = self.comboBox_localisation.currentText()
        verifier_enclos = verifier_enclos_liste(enclos.Numero_enclos)#verifier si l'enclos existe pas

        if verifier_enclos is False:
            #si l'enclos existe pas on enleve les valeurs deja entrer et on ecrit un message d'erreur
            self.lineEdit_numero_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.lineEdit_nom_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.label_erreur_numero_enclos_existe_pas.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_numero_enclos_existe_pas.setText("Ce numeor d'ecnlos existe n'existe pas")#On ecrit un message d'erreur pour l'utilisateur

        if enclos.Numero_enclos == "":#Verifier qui l'ecriture du numero de l'enclos est respecter
            self.lineEdit_numero_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.lineEdit_nom_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.label_erreur_validation_numero_enclos.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_validation_numero_enclos.setText("Entrez un nombre positif entier sur 5 caracteres"
                                                               "suivi de trois lettres")#On ecrit un message d'erreur pour l'utilisateur
        if enclos.Nom_enclos == "":#Verifier qui l'ecriture du nom l'enclos est respecter
            self.lineEdit_numero_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.lineEdit_nom_enclos.clear()#Enlever les valeur deja present dans la lineEdit
            self.label_erreur_nom_enclos.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_nom_enclos.setText("Alphabetique de longueur maximale egale a 25 lettres")#On ecrit un message d'erreur pour l'utilisateur

        if enclos.Numero_enclos != "" and enclos.Nom_enclos != "" and verifier_enclos is True:#Si tout les valeur entrez sont correct on vient supprimer l'enclos
            for elt in Enclos.ls_enclos: #On verifie chaque element de la liste enclos pour trouver celui a supprimer
                if elt.Numero_enclos == self.lineEdit_numero_enclos.text() and elt.Nom_enclos == self.lineEdit_nom_enclos.text() \
                    and elt.Taille == self.comboBox_taille_enclos.currentText() and elt.Type == self.comboBox_type_enclos.currentText() \
                    and elt.Localisation == self.comboBox_localisation.currentText():
                    Enclos.ls_enclos.remove(elt) #on supprime l'element de la liste des enclos
