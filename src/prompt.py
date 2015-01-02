class prompt(object):

    """
    Classe permettant d'afficher un prompt.
    Ce prompt permettra à l'utilisateur de savoir sur quel serveur et quel dossier\
    il se trouve
    """

    def __init__(self, login, serveur, chemin = "~"):
        """
        Constructeur du prompt
        login : login de l'utilisateur
        serveur : serveur sur lequel l'utilisateur veut s'identifier
        chemin : chemin sur lequel l'utilisateur se trouve (~/ par défaut)
        """
        self.login = login
        self.serveur = serveur
        self.rep = chemin

    def __del__(self):
        """
        Destructeur du prompt
        """
        print("SUPPR: Prompt")

    def ret_prompt(self):
        """
        Méthode permettant de retourner une chaine de caractères, correspondante\
        au prompt
        """
        return self.login+'@'+self.serveur+' - '+self.rep+': '

    def change_rep(self, rep):
        """
        Méthode permettant de modifier l'attribut rep - en meme temps que l'utilisateur,\
        lors du changement de répertoire
        """
        self.rep = "~"+rep
