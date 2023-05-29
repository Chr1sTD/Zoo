# Jean Christ-Dawens
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets
from Classes.Classe_Animal import *
from Classes.Classe_Mammifere import *
from Classes.Classe_Oiseau import *
from Classes.Classe_Reptile import *
from Classes.Classe_Enclos import *

#Methode/Fonction
def verifier_aniaml_liste(p_animal):
    """
    Verifier si l'animal est present dans la liste animal ou non
    """
    for elt in Animal.ls_animaux:
        if elt.Numero_animal == p_animal:
            return True #l'animal existe
    return False #L'animal existe pas

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreanimal(QtWidgets.QDialog, UI_PY.Dialog_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreanimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")
        self.label_erreur_numero_animal_existe_pas.setVisible(False)#cache les label d'erreur au lancement du programme
        self.label_erreur_numero_animal_existe.setVisible(False)#cache les label d'erreur au lancement du programme
        self.label_erreur_numero_animal_invalide.setVisible(False)#cache les label d'erreur au lancement du programme
        self.label_erreur_poids_animal.setVisible(False)#cache les label d'erreur au lancement du programme
        self.label_erreur_longueur_bec.setVisible(False)#cache les label d'erreur au lancement du programme
        self.comboBox_famille_animal.currentIndexChanged.connect(self.cacher_affichage)#permet de cacher a l'affichage les controles( Mammiferes, oiseau, reptiles)
        self.Ajouter_enclos_combobox()#permet d'ajouter les enclos a la comboBox a l'affichage

    def Afficher_Mammifere(self, B):#afficher les controles pour mammiferes
        self.label_couleur_poil.setVisible(B)
        self.comboBox_couleur_poil.setVisible(B)

    def Afficher_Oiseau(self, B):#afficher les controles pour Oiseau
        self.label_longueur_bec.setVisible(B)
        self.lineEdit_longueur_bec.setVisible(B)

    def Afficher_Reptiles(self, B):#afficher les controles pour reptiles
        self.label_venimeux.setVisible(B)
        self.comboBox_venimeux.setVisible(B)

    def cacher_affichage(self):#fonctions pour cacher les affichages puis les afficher selon le choix de l'utilisateur
        if self.comboBox_famille_animal.currentText() == "Mammifères":#afficher les controles pour mammiferes
            self.Afficher_Mammifere(True)
            self.Afficher_Oiseau(False)
            self.Afficher_Reptiles(False)
        elif self.comboBox_famille_animal.currentText() == "Oiseaux":#afficher les controles pour Oiseau
            self.Afficher_Oiseau(True)
            self.Afficher_Mammifere(False)
            self.Afficher_Reptiles(False)
        elif self.comboBox_famille_animal.currentText() == "Réptiles":#afficher les controles pour reptiles
            self.Afficher_Reptiles(True)
            self.Afficher_Oiseau(False)
            self.Afficher_Mammifere(False)

    def Ajouter_enclos_combobox(self):
        """
        Permet d'ajouter les enclos istancier a la combobox enclos
        :return:
        """
        for elt in Enclos.ls_enclos:
            self.comboBox_enclos_animal.addItem(elt.Numero_enclos)

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'evenements pour le bouton ajouter un animal
        :return:
        """
        #permet d'instancier different classe dependant du choix de l'utilisateur
        animal = Animal()
        if self.comboBox_famille_animal.currentText() == "Mammiferes":
            animal = Mammifere()
        elif self.comboBox_famille_animal.currentText() == "Oiseaux":
            animal = Oiseau()
        elif self.comboBox_famille_animal.currentText() == "Reptiles":
            animal = Reptile()
        #Instancier les valeur de l'animal
        animal.Numero_animal = self.lineEdit_numero_animal.text()
        animal.Surnom = self.lineEdit_surnom_animal.text()
        animal.Poids = int(self.lineEdit_poids_animal.text())
        animal.Enclos = self.comboBox_enclos_animal.currentText()
        animal.Couleur_poil = self.comboBox_couleur_poil.currentText()
        animal.Famille = self.comboBox_famille_animal.currentText()
        animal.Longueur_bec = float(self.lineEdit_longueur_bec.text())
        animal.Venimeux = self.comboBox_venimeux.currentText()
        verifier_animal = verifier_aniaml_liste(animal.Numero_animal)#Utiliser pour verifier si le numero de l'animal est pas deja present

        #Verification des valeurs rentrez
        if verifier_animal is True:#verifier si l'animal est pas deja dans la liste d'animal
            self.lineEdit_numero_animal.clear()#Enlever les valeur rentrez dans la lineEdit
            self.lineEdit_surnom_animal.clear()#Enlever les valeur rentrez dans la lineEdit
            self.lineEdit_poids_animal.clear()#Enlever les valeur rentrez dans la lineEdit
            self.lineEdit_longueur_bec.clear()#Enlever les valeur rentrez dans la lineEdit
            self.label_erreur_numero_animal_existe.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_numero_animal_existe.setText("Le numero de"
                                                           "l'animal existe deja")#Afficher un message d'erreur

        if animal.Numero_animal == "":#Verifier si l'ecriture du numero de l'animal est respecter
            self.lineEdit_numero_animal.clear()#Enlever les valeur rentrez dans la lineEdit
            self.label_erreur_numero_animal_invalide.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_numero_animal_invalide.setText("Entrer deux lettre suivies d'un "
                                                             "tiret puis de 5 chiffes")#Afficher un message d'erreur

        if animal.Poids == 0:#verifier que l'ecriture du poids de l'animal est respecter
            self.lineEdit_poids_animal.clear()#Enlever les valeur rentrez dans la lineEdit
            self.label_erreur_poids_animal.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_poids_animal.setText("Doit etre un nombre entier "
                                                   "superieur a 15Lb")#Afficher un message d'erreur

        if animal.Longueur_bec == 0.0:#verifier si l'ecriture du bec de l'animal est respecter
            self.lineEdit_longueur_bec.clear()#Enlever les valeur rentrez dans la lineEdit
            self.label_erreur_longueur_bec.setVisible(True)#Afficher le label d'erreur
            self.label_erreur_longueur_bec.setText("Doit etre une valeur reelle"
                                                   "positive")#Afficher un message d'erreur

        if animal.Numero_animal != "" and animal.Poids != 0 and animal.Longueur_bec != 0.0 and verifier_animal is False:#si toutes les valeurs sont respectées\
            Animal.ls_animaux.append(animal)#on ajoute l'animal à la liste d'animaux                                     #on instancie un animal
            self.lineEdit_numero_animal.clear()#Enlever les valeurs rentrez dans la lineEdit
            self.lineEdit_surnom_animal.clear()#Enlever les valeurs rentrez dans la lineEdit
            self.lineEdit_poids_animal.clear()#Enlever les valeurs rentrez dans la lineEdit
            self.lineEdit_longueur_bec.clear()#Enlever les valeurs rentrez dans la lineEdit

    @pyqtSlot()
    def on_pushButton_rechercher_clicked(self):
        """
        Gestionnaire d'evenements pour le bouton rechercher un animal
        :return:
        """
        for elt in Animal.ls_animaux:#on parcourt chaques elements de la liste animal
            if elt.Numero_animal == self.lineEdit_numero_animal.text():#si le numero est egale au numero de la liste on affiche les valeurs deja existant
                self.lineEdit_numero_animal.setText(elt.Numero_animal)
                self.lineEdit_surnom_animal.setText(elt.Surnom)
                self.lineEdit_poids_animal.setText(elt.Poids)
                self.comboBox_famille_animal.setItemText(0, elt.Famille)
                self.comboBox_enclos_animal.setItemText(0, elt.Enclos)
                self.comboBox_couleur_poil.setItemText(0, elt.Couleur_poil)
                self.lineEdit_longueur_bec.setText(elt.Longueur_bec)
                self.comboBox_venimeux.setItemText(0, elt.Venimeux)
            elif elt.Numero_animal != self.lineEdit_numero_animal.text():
                self.label_erreur_numero_animal_existe_pas.setVisible(True)
                self.label_erreur_numero_animal_existe_pas.setText("Le numeoro"
                                                                   "d'animal n'existe deja")#Afficher un message d'erreur

