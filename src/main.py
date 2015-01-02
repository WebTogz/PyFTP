#/usr/local/bin/python3
#--*--coding:utf8--*--
from ftplib import FTP
import getpass
from prompt import prompt
from hist_session import hist_session
from session import session

def connexion():
    """
    Fonction permettant de se connecter sur le serveur FTP
    """

    global ftp
    global session

    ftp = FTP(session.serveur)
    ftp.connect(session.serveur, session.port)
    print(str(ftp.getwelcome(), 'UTF-8'))

def authentification():
    """
    Fonction permettant de se logger sur le serveur FTP
    """

    global ftp
    global session

    ftp.login(session.login, session.mdp)

def demande_reconnexion():
    """
    Fonction permettant de se reconnecter sur une session déjà utilisée
    """

    global session

    print("Demande de reconnexion sur "+session.serveur)
    connexion()
    authentification()
    print("Reconnexion effectuée...")

def quitter():
    """
    Fonction permettant de se déconnecter sur le serveur FTP
    """

    global ftp
    global session

    ftp.quit()
    print("Déconnexion sur "+session.serveur+" effectuée...")


if __name__ == '__main__' :

    global ftp
    global session

    hist_rep = []

    print("Bienvenue sur PyFTP")

    hist_session = hist_session()

    login = input("Veuillez entrer votre login: ")

    mdp = getpass.getpass(prompt = "Veuillez entrer votre mot-de-passe: ")

    serveur = input("Veuillez entrer l'adresse du serveur FTP: ")

    port = 21

    session = session(login, mdp, serveur, port)

    connexion()

    authentification()

    print("\nVous êtes maintenant authentifié -- tapez [H]ELP pour afficher l'aide, [Q]UIT pour quitter\n")

    prompt = prompt(session.login, session.serveur)

    hist_session.ajout_session(session)

    while 1:
        prompt.change_rep(ftp.pwd())
        ligne = input(prompt.ret_prompt()).split(' ')
        cmd = ligne[0]
        if (cmd == "Q") or (cmd == "QUIT"):
            break
        if (cmd == "H") or (cmd == "HELP"):
            print(
            "\tQ/QUIT -> Quitter\n" + \
            "\tH/HELP -> Aide\n" + \
            "\tS/STATE -> Imprime sur la sortie standard l'état du dossier dans lequel on se trouve\n" + \
            "\tM/MOVE [dossier] -> Permet de se positionner dans le dossier donné en paramètre\n" + \
            "\tCD/CREATE DIRECTORY [dossier] -> Permet de créer un dossier dans ./\n" + \
            "\tR/RENAME [fichier_à_renommer] [nouveau_nom] -> Permet de modifier le nom d'un fichier/répertoire (1er paramètre) en un autre (2ème paramètre)\n" + \
            "\tRM [fichier] -> Permet de supprimer un fichier/dossier donné en paramètre\n" + \
            "\tDL/DOWNLOAD [fichier] -> Télécharge (récursivement) le fichier lié - ./ par défaut\n" + \
            "\tDS/DISPLAY SESSIONS -> Affiche sur la sortie standard la liste des sessions enregistrées\n" + \
            "\tCS/CONNECT SESSION -> Nouvelle connexion sur une session pré-enregistrée\n"
            )
        if (cmd == "S") or (cmd == "STATE"):
            entrees = []
            ftp.dir(entrees.append)
            for item in entrees:
                print(item)
        if (cmd == "M") or (cmd == "MOVE"):
            if (len(ligne) == 1):
                print("ERREUR - pas de dossier donné en paramètre...")
            else:
                ftp.cwd(ligne[1])
                hist_rep.append(ligne[1])
        if (cmd == "CD") or (cmd == "CREATE DIRECTORY"):
            print("Pas encore implémenté...")
        if (cmd == "R") or (cmd == "RENAME"):
            if (len(ligne) <= 2):
                print("ERREUR - vous n'avez pas entré les paramètres demandés...")
            else:
                ftp.rename(ligne[1], ligne[2])
        if (cmd == "RM"):
            if (len(ligne) == 1):
                print("ERREUR - pas de fichier/dossier donné en paramètre")
            else:
                try:
                    ftp.delete(ligne[1])
                except error_perm as e_perm:
                    print("ERREUR - Vous n'avez pas la permission de supprimer le fichier/dossier donné en paramètre")
                except error_reply as e_reply:
                    print("ERREUR lors de la suppression du fichier/dossier: ", e_reply)
        if (cmd == "DL") or (cmd == "DOWNLOAD"):
            print("Pas encore implémenté...")
        if (cmd == "DS") or (cmd == "DISPLAY SESSIONS"):
            hist_session.lister_historique()
        if (cmd == "CS") or (cmd == "CONNECT SESSION"):
            hist_session.lister_historique()
            ind = int(input("Choisissez une session: "))
            if (ind >= 0) and (ind < hist_session.taille()):
                quitter()
                session = hist_session.ret_session(ind)
                demande_reconnexion()

    quitter()
