#/usr/local/bin/python3
#--*--coding:utf8--*--
from ftplib import FTP
import getpass

def maj_prompt():
    """
    Fonction permettant de mettre-à-jour automatiquement le prompt
    prompt = 'login@serveur-chemin_fichier: '
    """

    global ftp
    global prompt
    global login
    global serveur
    global chemin_en_cours

    #On recherche l'actuel chemin
    chemin_en_cours = ftp.pwd()

    prompt = login+'@'+serveur+'-'+chemin_en_cours+': '

def connexion_serveur(serveur, port):
    """
    Fonction permettant la connexion avec un serveur FTP, via l'adresse
    du serveur et le port FTP (21 par défaut)
    """

    global ftp

    ftp = FTP(serveur)
    ftp.connect(serveur, port)
    print(ftp.getwelcome())

def authentification(login, mdp):
    """
    Fonction permettant d'authentifier l'utilisateur via la combinaison
    login/mdp
    """

    global ftp

    ftp.login(login, mdp)

def quitter_session():
    """
    Fonction permettant de quitter une session FTP
    """

    global ftp

    print("Fermeture de la session...", end='')
    ftp.quit()
    print("OK")

if __name__ == '__main__' :

    global serveur
    global login
    global mdp
    global prompt
    global chemin_en_cours
    global ftp

    print("Bienvenue sur PyFTP")

    login = input("Veuillez entrer votre login: ")

    mdp = getpass.getpass(prompt = "Veuillez entrer votre mot-de-passe: ")

    serveur = input("Veuillez entrer l'adresse du serveur FTP: ")

    port = 21

    chemin_en_cours = "~/"

    connexion_serveur(serveur, port)

    authentification(login, mdp)

    print("\nVous êtes maintenant authentifié -- tapez [H]ELP pour afficher l'aide, [Q]UIT pour quitter\n")

    while 1:
        maj_prompt()
        ligne = input(prompt).split(' ')
        cmd = ligne[0]
        if (cmd == "Q") or (cmd == "QUIT"):
            break
        if (cmd == "H") or (cmd == "HELP"):
            print(
            "\tQ/QUIT -> Quitter\n" + \
            "\tH/HELP -> Aide\n" + \
            "\tS/STATE -> Imprime sur la sortie standard l'état du dossier dans lequel on se trouve\n" + \
            "\tCD [dossier] -> Permet de se positionner dans le dossier donné en paramètre\n" + \
            "\tR/RENAME [fichier_à_renommer] [nouveau_nom] -> Permet de modifier le nom d'un fichier/répertoire (1er paramètre) en un autre (2ème paramètre)\n" + \
            "\tRM [fichier] -> Permet de supprimer un fichier/dossier donné en paramètre" + \
            "\tDL/DOWNLOAD [fichier] -> Télécharge (récursivement) le fichier lié - ./ par défaut\n"
            )
        if (cmd == "S") or (cmd == "STATE"):
            entrees = []
            ftp.dir(entrees.append)
            for item in entrees:
                print(item)
        if (cmd == "CD"):
            if (len(ligne) == 1):
                print("ERREUR - pas de dossier donné en paramètre...")
            else:
                ftp.cwd(ligne[1])
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

    quitter_session()
