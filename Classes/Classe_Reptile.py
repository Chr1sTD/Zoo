# George Pene

# Importer la classe Animal
from Classes.Classe_Animal import *


class Reptile(Animal):
    """
    Classe Reptile, hérité de la classe Animal
    """

    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "",
                 p_enclos: Enclos = Enclos(), p_ls_veterinaire: list = [], p_venimeux: str=""):
        """
        Contruscteur de la classe Mammifere, hérité de la classe Animal
        :param p_numero_animal: Numéro de l'animal
        :param p_surnom: Surnom de l'animal
        :param p_poids: Poids de l'animal
        :param p_famille: Famille de l'animal
        :param p_enclos: L'enclos de l'animal
        :param p_ls_veterinaire: Liste des vétérinaire qui s'occupent de l'animal
        :param p_venimeux: Si le reptile est venimeux ou pas (booléen)
        """
        Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille, p_enclos, p_ls_veterinaire)
        self.Venimeux = p_venimeux  # Attribut public

    # Méthode spécial magique __str__
    def __str__(self):
        """
        Méthode spécial magique str de la classe Oiseau, hérité de la classe Animal
        :return: la chaine qui permet d'afficher les attributs de l'objet de la classe Mammifère instancié
        """
        return Animal.__str__(self) + f"\nLe reptile est venimeux : {self.Venimeux}"
