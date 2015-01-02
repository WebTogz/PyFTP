from session import session

class hist_session(object):

    """
    Classe permettant de sauver dans une liste toutes les sessions utilisées
    """

    def __init__(self):
        """
        Constructeur de l'objet hist_session
        """
        self.historique = []

    def __del__(self):
        """
        Destructeur - suppression des sessions sauvées avant la destruction de l'objet
        """
        for hist in self.historique:
            hist.__del__()
        print("Historique de session supprimé...")

    def ajout_session(self, session):
        """
        Méthode permettant d'ajouter une session dans la liste de sessions de l'objet
        """
        self.historique.append(session)

    def ret_session(self, index):
        """
        Méthode permettant de retourner l'objet session contenue à l'index donné en paramètre, issu de l'objet sur lequel on invoque la méthode
        """
        return self.historique[index]

    def lister_historique(self):
        """
        Méthode permettant de lister les sessions sauvées dans l'objet
        """
        for i in range(len(self.historique)):
            print(str(i)+": "+self.historique[i].__str__())

    def taille(self):
        """
        Méthode permettant de retourner la taille de la liste de sessions
        """
        return len(self.historique)
