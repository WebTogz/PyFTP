from ftplib import FTP

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

    print("Bienvenue sur PyFTP")

    login = input("Veuillez entrer votre login: ")

    mdp = input("Veuillez entrer votre mot-de-passe: ")

    serveur = input("Veuillez entrer l'adresse du serveur FTP: ")

    port = 21

    chemin_en_cours = "~/"

    maj_prompt();

    connexion_serveur(serveur, port)

    authentification(login, mdp)

    while 1:
        maj_prompt()
        cmd = input(prompt)
