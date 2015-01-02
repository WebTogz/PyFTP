from session import session

class hist_session(object):

    def __init__(self):
        self.historique = []

    def __del__(self):
        for hist in self.historique:
            hist.__del__()
        print("Historique de session supprimé...")

    def ajout_session(self, session):
        self.historique.append(session)

    def ret_session(self, index):
        return self.historique[index]

    def lister_historique(self):
        for i in range(len(self.historique)):
            print(str(i)+": "+self.historique[i].__str__())

    def taille(self):
        return len(self.historique)
