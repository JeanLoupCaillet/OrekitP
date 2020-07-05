# OrekitPython
---------------

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
