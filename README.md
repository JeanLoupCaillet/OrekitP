# OrekitPython
---------------
Ce projet a pour but de créér un utilitaire graphique facile d'utilisation pour les applications de mécanique spatiale. 

_Utilisation avec Anaconda Python-3.7_

## Etapes d'installation :

### Télécharger et installer Anaconda & Pycharm: 
-----------------------------------------------
Ouvrir un terminal Anaconda et executer: 
* 'conda create -m env python=3.7 anaconda'
* 'conda activate env'
* 'conda install -m env -c conda-forge orekit'


### Télécharger le projet gitlab de Petrus Hyvönen : 
---------------------------------------------------
_Pré-requis:_ Avoir un compte gitlab. Et générer une clé rsa :'ssh-keygen -o -t rsa -b "4096" -C "email@adress" 
* Suivre les consignes indiquées à l'écran et taper un mot de passe. 
* Rajouter le contenue de la clé générée (~/.ssh/id_rsa.pub) sur votre compte gitlab. (Settings -> SSH), vous pouvez alors cloner le répertoire.
* 'git clone https://gitlab.orekit.org/orekit-labs/python-wrapper.git'


### Créer les variables d'environnement utilisateur :
----------------------------------------------------
_Pré-requis:_ Avoir un environnement java adéquat : JRE v8 ou JDK v13
* set JCC_JDK=C:\Program Files (x86)\Java\jdk1.6.0_35
* set PATH=%JCC_JDK%\jre\bin\client;%JCC_JDK%\bin;%JCC_JDK%\lib;%PATH%


### Tester son environnement:
---------------------------- 

* Exécuter le fichier test.py
* Voud devriez avoir en sortie _Keplerian parameters: {a: 2.446456E7; e: 0.7311; i: 6.997991918168848; pa: 178.00996553801494; raan: 57.68596377156641; v: 25.421887733782746;}_

Tout devrait bien se passer. Si jamais un problème persiste ouvrir une issues :) 

### Quelques commandes git :
----------------------------

* git config --global user.name "UserName"
* git config --global user.email "user@email.com"
* git config --global alias.st "status"
* git config --global alias.lg "log --oneline --graph --color=tty"
* git config --global alias.br "branch -vaa"
* git pull (récupérer le repository)
* git br (connaitre toutes les branches existante et celle sur laquelle on travaille)
* git remote -vv (s'assurer que les pulls et push sont bien connectées à la même adresse)
* git status (permet de connaitre l'état de son répertoire local par rapport au remote)
* git add . (permet d'ajouter toutes les modifications en local afin de préparer son commit)
* git commit -m "message" (ajout un commentaire sur le commit pour expliquer les modifications)
* git push (permet d'envoyer les modifications sur le remote)
* git reset --soft HEAD (permet d'annuler les préparations de commit et de se baser sur la version du remote)
* git fetch (récupère les données du remote sans merger avec les modifications locales)
* git merge (permet de rassembler les modifications, utile quand on travail sur des branches)
* NB: git pull ( git fetch + git merge)
* git stash (sauve l'état courant local, afin de ne pas perdre les données avec un pull)
* git stash pop (remet l'état courant après un pull)


