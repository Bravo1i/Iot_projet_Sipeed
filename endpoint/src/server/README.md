# Installation

Creer un environnement virtuel python avec le fichier requirements.txt ou installer avec pip le
fichier requirements.txt

# Lancer le server
Pour lancer le serveur, il faut etre a la racine du dossier et executer la commande suivante dans un terminal. (fonctionne sur windows, à verifier avec linux)

 `uvicorn --app-dir src main:app --reload --port 8080 --host 0.0.0.0`

Cela va demarrer un serveur dans le terminal.

# Fonctionnement du serveur
Ensuite ouvrir un navigateur et taper :
`http://localhost:8080`

C'est la page principale du serveur. C'est une page HTML où l'on peut voir combien de vehicules sont passés. 

Pour connecter la carte sur le serveur il faut aller : 
`http://localhost:8080/docs`

Sur cette page, nous avons 2 commandes. La première est get serial info. Elle permet de connaitre tous les ports série de connecter à notre ordinateur. La seconde pour se connecter à un port com en particulier.
