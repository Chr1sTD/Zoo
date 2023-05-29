# George Pene

class Enclos:
    """
    Class Enclos
    """
    # Attribut de classe
    ls_enclos =[]
    # Méthode constructeur
    def __init__(self, p_numero_enclos: str = "", p_nom_enclos: str = "", p_type: str = "", p_taille: str = "", p_localisation: str = ""):
        """
        Constructeur de la classe Enclos
        :param p_numero_enclos: Numéro de l'enclos
        :param p_nom_enclos: Nom de l'enclos
        :param p_type: Type de l'enclos
        :param p_taille: Taille de l'enclos
        :param p_localisation: Localisation de l'enclos
        """
        # Attributs d'instances
        self._numero_enclos = p_numero_enclos  # attribut privé
        self._nom_enclos = p_nom_enclos  # attribut privé
        self.Taille = p_taille  # attribut public
        self.Type = p_type  # attribut public
        self.Localisation = p_localisation  # attribut public

    # Propriété Numero_enclos
    @property
    def Numero_enclos(self):
        return self._numero_enclos

    @Numero_enclos.setter
    def Numero_enclos(self, p_numero_enclos):
        if len(p_numero_enclos) == 8 and p_numero_enclos[0:5].isnumeric() and p_numero_enclos[5:8].isalpha():
            self._numero_enclos = p_numero_enclos

    # Propriété Nom_enclos
    @property
    def Nom_enclos(self):
        return self._nom_enclos

    @Nom_enclos.setter
    def Nom_enclos(self, p_nom_enclos):
        if len(p_nom_enclos) <= 25 and p_nom_enclos.isalpha():
            self._nom_enclos = p_nom_enclos

    # Méthode spécial magique __str__
    def __str__(self):
        """
        Méthode spécial magique str de la classe Enclos
        :return: chaine
        """
        chaine = f"Le numéro de l'enclos est : {self._numero_enclos}\nLe nom de l'enclos est : {self._nom_enclos}\n" \
                 f"La taille de l'enclos est : {self.Taille}\nLe type de l'enclos est : {self.Taille}\n" \
                 f"La localisation de l'enclos est : {self.Localisation}"
        return chaine
