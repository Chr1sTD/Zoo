# George Pene

# Importer la classe Animal
from Classes.Classe_Animal import *


class Oiseau(Animal):
    """
    Classe Oiseau, hérité de la classe Animal
    """

    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "",
                 p_enclos: Enclos = Enclos(), p_ls_veterinaire: list = [], p_longueur_bec : float =0.0):
        """
        Contruscteur de la classe Mammifere, hérité de la classe Animal
        :param p_numero_animal: Numéro de l'animal
        :param p_surnom: Surnom de l'animal
        :param p_poids: Poids de l'animal
        :param p_famille: Famille de l'animal
        :param p_enclos: L'enclos de l'animal
        :param p_ls_veterinaire: Liste des vétérinaire qui s'occupent de l'animal
        :param p_longueur_bec: Longueur du bec de l'oieseau
        """
        Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille, p_enclos, p_ls_veterinaire)
        self._longueur_bec = p_longueur_bec  # Attribut privé

    # Propriété Longueur_bec
    @property
    def Longueur_bec(self):
        return self._longueur_bec

    @Longueur_bec.setter
    def Longueur_bec(self, p_longueur_bec):
        if p_longueur_bec > 0.0:
            self._longueur_bec = p_longueur_bec

    # Méthode spécial magique __str__
    def __str__(self):
        """
        Méthode spécial magique str de la classe Oiseau, hérité de la classe Animal
        :return: la chaine qui permet d'afficher les attributs de l'objet de la classe Mammifère instancié
        """
        return Animal.__str__(self) + f"\nLa longueur du bec de l'oiseau est de {self._longueur_bec}cm"
