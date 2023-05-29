# George Pene

# Importer la classe Enclos
from Classes.Classe_Enclos import *

# Importer la classe Veterinaire
from Classes.Classe_Veterinaire import *

# importer json
import jsonpickle

class Animal:
    """
    Classe Animal
    """
    # Attributs de classe
    nb_animaux = 0
    ls_animaux = []

    # Méthode constructeur
    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "",
                 p_enclos: Enclos = Enclos(), p_ls_veterinaire: list = [] ):
        """
        Constructeur de la classe Animal
        :param p_numero_animal: Numéro de l'animal
        :param p_surnom: Surnom de l'animal
        :param p_poids: Poids de l'animal
        :param p_famille: Famille de l'animal
        :param p_enclos: L'enclos de l'animal
        :param p_ls_veterinaire: Liste des vétérinaire qui s'occupent de l'animal
        """
        if p_ls_veterinaire is None:
            p_ls_veterinaire = []
        self._numero_animal = p_numero_animal  # attribut privé
        self.Surnom = p_surnom  # attribut public
        self._poids = p_poids  # attribut privé
        self.Famille = p_famille  # attribut public
        self.Enclos = p_enclos  # attribut public
        self.ls_veterinaire = p_ls_veterinaire  # attribut public

        Animal.nb_animaux += 1  # Calcul le nbr d'animaux instanciés


    # Propriété Numero_animal
    @property
    def Numero_animal(self):
        return self._numero_animal

    @Numero_animal.setter
    def Numero_animal(self, p_numero_animal):
        if len(p_numero_animal) == 8 and p_numero_animal[0:2].isalpha() and p_numero_animal[2] == "-" and p_numero_animal[3:8].isnumeric():
            self._numero_animal = p_numero_animal

    # Propriété Poids
    @property
    def Poids(self):
        return self._poids

    @Poids.setter
    def Poids(self, p_poids):
        if p_poids > 15:
            self._poids = p_poids

    # Méthode d'instance sérialisé jsonpickle
    def serialiserAnimal(self, p_nom_fichier):
        """
        Méthode permettant de sérialiser un objet de la classe Animal avec jsonpickle
        :param p_nom_fichier: Le nom du fichier qui contiendra l'objet sérialiser
        """
        json_string = jsonpickle.encode(self)
        with open(p_nom_fichier, "w") as file:
            file.write(json_string)

    # Méthode d'instance désérialiser jsonpickle
    def deserialiserAnimal(self, p_nom_fichier):
        """
        Méthode permettant de désérialiser un objet de la classe Animal avec jspnpickle
        :param p_nom_fichier: Le nom du fichier qui contiendra l'objet sérialiser
        """
        with open(p_nom_fichier, "r") as file:
            json_string = file.readline()
            return jsonpickle.decode(json_string)

    # Méthode d'instance ajouter un enclos au vétérinaire
    def ajouterEnclosVeterinaire(self, p_numero_emp, p_objet_Enclos: Enclos):
        for elt in self.ls_veterinaire:
            if elt.Numero_emp == p_numero_emp:
                elt.list_enclos.append(p_objet_Enclos)

    # Méthode de classe
    @classmethod
    def afficherLstAnimal(cls):
        chaine = ""
        for elt in cls.ls_animaux:
            chaine += elt.__str__()
        print(chaine)

    # Méthode spéciale magique __str__
    def __str__(self):
        """
        Méthode spécial magique str de la classe Animal
        :return: chaine
        """
        chaine = f"Le numéro de l'animal est : {self._numero_animal}\nLe surnom de l'animal est : {self.Surnom}\n" \
                 f"Le poids de l'animal est de : {self._poids} lb\nLa famille de l'animal est : {self.Famille}\n" \
                 f"Les caractéristiques de l'enclos de l'animal sont : {self.Enclos.__str__()}\n"
        return chaine
