# Iot_projet_Sipeed
## Thèmes du projet  
Ce projet est un projet IOT pour Polytech IESE5 et le sujet est l'implémentation d'un compteur de véhicules utilisant la carte de développement sispeed. La carte de développement est basée sur le MaixBit de Sipeed et l'algorithme de détection des véhicules est basé sur l'algorithme de détection des objets de YOLO V2.
## Matériel de projet
Le kit de développement MaixBit, un shell conçu par Fablab, un jeu de données d'images de véhicules partagé sur CSDN.
## Comment fonctionne le programme
1. Installer Kflash et graver les fichiers sur la carte de développement (endpoint/firmware)  
2. Gravez les fichiers dans (point final/modèle) sur la carte de développement.
3. Installer MaixPy, ouvrir main.py dans (endpoint/src)
4. Connectez la carte de développement et vous êtes prêt à fonctionner.
## Résultats de la réalisation du projet
Nous pouvons compter les véhicules, mais en raison de la résolution de la caméra et du modèle supporté par la carte, nous ne pouvons compter qu'un petit nombre de véhicules à courte distance pour le moment.