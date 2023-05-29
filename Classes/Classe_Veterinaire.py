# George Pene

# import date
import datetime
from datetime import date

# import Classe_Enclos
from Classes.Classe_Enclos import *

class Veterinaire:
    """
    Classe Vétérinaire
    """
    # attribut de classe
    ls_veterinaire = []
    def __init__(self, p_numero_emp: str = "", p_nom: str = "", p_prenom: str = "", p_date_naiss: date = "",
                 p_list_enclos: list = []):
        """
        Contstructeur de la classe Vétérinaire
        :param p_numero_emp: Numéro de l'employé
        :param p_nom: Nom du vétérinaire
        :param p_prenom: Prénom du vétérinaire
        :param p_date_naiss: Date de naissance du vétérinaire
        :param p_list_enclos: Liste qui contient les enclos assignés au vétérinaire
        """
        self._numero_emp = p_numero_emp  # Attribut privé
        self._nom = p_nom  # Attribut privé
        self._prenom = p_prenom  # Attribut privé
        self._date_naiss = p_date_naiss  # Attribut privé
        self.list_enclos = p_list_enclos  # Attribut publique


    # Propriété Numero_emp
    @property
    def Numero_emp(self):
        return self._numero_emp

    @Numero_emp.setter
    def Numero_emp(self, p_num_emp):
        if p_num_emp[0:3].isalpha() and p_num_emp[3:5].isnumeric():
            self._numero_emp = p_num_emp

    # Propriété Nom
    @property
    def Nom(self):
        return self._nom

    @Nom.setter
    def Nom(self, p_nom):
        if len(p_nom) <= 50 and p_nom.isalpah():
            self._nom = p_nom

    # Propriété Prenom
    @property
    def Prenom(self):
        return self._prenom

    @Prenom.setter
    def Prenom(self, p_prenom):
        if p_prenom <= 50 and p_prenom.isalpha():
            self._prenom = p_prenom

    # Propriété Date_naiss
    @property
    def Date_naiss(self):
        return self._date_naiss

    @Date_naiss.setter
    def Date_naiss(self, p_date_naiss):
        if p_date_naiss < datetime.date.today():
            self._date_naiss = p_date_naiss

    # Méthode d'instance privéé calculerAge
    def _calculerAge(self, p_date_naiss):
        today = datetime.date.today()
        return today.year - p_date_naiss.year() - ((today.month, today.day) < (p_date_naiss.month, p_date_naiss.day))

    # Methode d'instance publique prendreRetraite
    def prendreRetraite(self):
        if self._calculerAge(self._date_naiss) >= 60:
            return True
        else:
            return False

    # Méthode d'instance publique afficherEnclos
    def afficherEnclos(self):
        """
        Affiche de façon professionelle les informations des enclos assignés au vétérinaire
        :return: chaine
        """
        chaine = ""
        for elt in self.list_enclos:
            chaine += elt.__str__()
        print(chaine)

    # Méthode d'instance publique ajouterEnclos
    def ajouterEnclos(self, p_objet_Enclos: Enclos):
        """
        Ajoute un enclos à la liste des enclos assignés au vértérinaire
        :param p_objet_Enclos: L'objet Enclos concérné
        """
        self.list_enclos.append(p_objet_Enclos)

    # Méthode d'instance publique supprimerEnclos
    def supprimerEnclos(self, p_objet_Enclos: Enclos):
        """
        Ajoute un enclos à la liste des enclos assignés au vértérinaire
        :param p_objet_Enclos: L'objet Enclos concérné
        """
        self.list_enclos.remove(p_objet_Enclos)

    def serialiser(self):
        pass

    # Méthode spécial magique __str__
    def __str__(self):
        """
        Méthode spécial magique str de la classe Vétérinaire
        :return: chaine
        """
        chaine = f"Le numéro de l'empoyé est : {self._numero_emp}\nLe nom du vétérinaire est : {self._nom}\n" \
                 f"Le prénom du vétérinaire est : {self._prenom}\n" \
                 f"La date de naissance du vétérinaire est : {self._date_naiss}\n"

        return chaine

