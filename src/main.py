from ftplib import FTP

def maj_prompt():
    """
    Fonction permettant de mettre-à-jour automatiquement le prompt
    prompt = 'login@serveur-chemin_fichier: '
    """

    global prompt
    global login
    global serveur
    global chemin_en_cours

    prompt = login+'@'+serveur+'-'+chemin_en_cours+': '

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
