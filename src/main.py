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
    global sess

    ftp = FTP(sess.serveur)
    ftp.connect(sess.serveur, sess.port)
    print(ftp.getwelcome())

def authentification():
    """
    Fonction permettant de se logger sur le serveur FTP
    """

    global ftp
    global sess

    ftp.login(sess.login, sess.mdp)

def demande_reconnexion():
    """
    Fonction permettant de se reconnecter sur une session déjà utilisée
    """

    global sess

    print("Demande de reconnexion sur "+sess.serveur)
    connexion()
    authentification()
    print("Reconnexion effectuée...")

def quitter():
    """
    Fonction permettant de se déconnecter sur le serveur FTP
    """

    global ftp
    global sess

    ftp.quit()
    print("Déconnexion sur "+sess.serveur+" effectuée...")


if __name__ == '__main__' :

    global ftp
    global sess

    hist_rep = []

    hist_session = hist_session()

    port = 21

    choix = "N"

    print("Bienvenue sur PyFTP")

    while 1:

        if (choix == "N"):

            login = input("Veuillez entrer votre login: ")

            mdp = getpass.getpass(prompt = "Veuillez entrer votre mot-de-passe: ")

            serveur = input("Veuillez entrer l'adresse du serveur FTP: ")

            if (input("Utilisez-vous le port "+str(port)+"? <O>UI/<N>ON") == "N"):
                port = int(input("Port = "))

            sess = session(login, mdp, serveur, port)

            connexion()

            authentification()

            print("\nVous êtes maintenant authentifié -- tapez [H]ELP pour afficher l'aide, [Q]UIT pour quitter\n")

            prm = prompt(sess.login, sess.serveur)

        while 1:
            prm.change_rep(ftp.pwd())
            ligne = input(prm.ret_prompt()).split(' ')
            cmd = ligne[0]
            if (cmd == "Q") or (cmd == "QUIT"):
                break
            if (cmd == "H") or (cmd == "HELP"):
                print(
                "\tQ/QUIT -> Quitter\n" + \
                "\tH/HELP -> Aide\n" + \
                "\tS/STATE -> Imprime sur la sortie standard l'état du dossier dans lequel on se trouve\n" + \
                "\tM/MOVE [dossier] -> Permet de se positionner dans le dossier donné en paramètre\n" + \
                "\tL/LOOKING [fichier] -> Permet de visualiser un fichier dans la console\n" + \
                "\tCD/CREATE DIRECTORY [dossier] -> Permet de créer un dossier dans ./\n" + \
                "\tR/RENAME [fichier_à_renommer] [nouveau_nom] -> Permet de modifier le nom d'un fichier/répertoire (1er paramètre) en un autre (2ème paramètre)\n" + \
                "\tRM [fichier] -> Permet de supprimer un fichier/dossier donné en paramètre\n" + \
                "\tDL/DOWNLOAD [fichier] -> Télécharge le fichier NON BINAIRE lié - ./ par défaut dans le cas récursif\n" + \
                "\tDLB/DOWNLOAD BINARY [binaire] -> Télécharge le BINAIRE lié\n"
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
            if (cmd == "L") or (cmd == "LOOKING"):
                if (len(ligne) == 1):
                    print("ERREUR - pas de fichier donné en paramètre...")
                else:
                    try:
                        ftp.retrlines('RETR %s' %ligne[1])
                    except:
                        print("Visualisation du fichier impossible...")
            if (cmd == "CD") or (cmd == "CREATE DIRECTORY"):
                print("Pas encore implémenté...")
            if (cmd == "R") or (cmd == "RENAME"):
                if (len(ligne) <= 2):
                    print("ERREUR - vous n'avez pas entré les paramètres demandés...")
                else:
                    ftp.rename(ligne[1], ligne[2])
            if (cmd == "RM"):
                if (len(ligne) == 1):
                    print("ERREUR - pas de fichier/dossier donné en paramètre...")
                else:
                    try:
                        ftp.delete(ligne[1])
                    except error_perm as e_perm:
                        print("ERREUR - Vous n'avez pas la permission de supprimer le fichier/dossier donné en paramètre")
                    except error_reply as e_reply:
                        print("ERREUR lors de la suppression du fichier/dossier: ", e_reply)
            if (cmd == "DL") or (cmd == "DOWNLOAD"):
                if (len(ligne) == 1):
                    print("Le téléchargement récursif sur ./ n'a pas encore implémenté...")
                else:
                    try:
                        fichier = open(ligne[1], 'wt')
                        ftp.retrlines('RETR %s' %ligne[1], lambda data: fichier.write(data+'\n'))
                    except:
                        print("Téléchargement du fichier impossible...")
            if (cmd == "DLB") or (cmd == "DOWNLOAD BINARY"):
                if (len(ligne) == 1):
                    print("ERREUR - absence du nom du binaire en paramètre")
                else:
                    try:
                        fichier = open(ligne[1], 'wb')
                        ftp.retrbinary('RETR %s' %ligne[1], fichier.write)
                    except:
                        print("Téléchargement du binaire impossible...")

        quitter()

        if choix == "N":
            hist_session.ajout_session(sess)

        choix = input("Voulez-vous créer une nouvelle session? <N>OUVELLE / <E>XISTANTE / <Q>UITTER")

        if choix == "N":
            print("\n")
            print("**********")
            print("\n")
            continue
        if choix == "E":
            hist_session.lister_historique()
            ind = int(input("Choisissez une session: "))
            if (ind >= 0) and (ind < hist_session.taille()):
                #Nouvelle date de demande de connexion
                hist_session.ret_session(ind).nvelle_date()
                sess = hist_session.ret_session(ind)
                demande_reconnexion()
            else:
                print("ERREUR - choix incorrect...")
                break
        else:
            break

    print("Au revoir!")
