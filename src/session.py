from datetime import datetime

class session(object):

    """
    Classe permettant d'initialiser une session FTP
    """

    def __init__(self, login, mdp, serveur, port = 21):
        """
        Constructeur de la session
        login : login de l'utilisateur
        mdp : mot-de-passe de la session utilisateur
        serveur : serveur de la session
        port : port pour la connexion FTP - par défaut 21
        """
        self.login = login
        self.mdp = mdp
        self.serveur = serveur
        self.port = port
        self.date = datetime.now()

    def __del__(self):
        """
        Destructeur de la session
        """
        print("Session "+self.serveur+" détruite...")

    def __str__(self):
        """
        Impression de l'objet
        """
        return self.ret_date()+" :: Session "+self.serveur+" - initialisée par "+self.login

    def nvelle_date(self):
        """
        Fonction permettant de modifier l'attribut date de l'objet
        """
        self.date = datetime.now()

    def ret_date(self):
        """
        Fonction permettant de retourner la date d'après l'attribut homonyme
        """
        return str(self.date.year)+"/"+str(self.date.month)+"/"+str(self.date.day)+"-"+str(self.date.hour)+":"+str(self.date.minute)+":"+str(self.date.second)
