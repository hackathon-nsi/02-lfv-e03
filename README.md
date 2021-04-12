~ La 👸 de Clèves ~

**SUJET** : https://github.com/hackathon-nsi/h7n-nsi-02

**PROGRESSION** (*changer les - par des # | # = 5%*)<br />
niveau 1 : |####################|<br />
niveau 2 : |########------------|<br />
niveau 3 : |--------------------|<br />
niveau 4 : |--------------------|<br />

<hr />
<!-- ne pas effacer les lignes ci-dessus et mettre à jour la progression régulièrement -->

## JOURNAL DE BORD
--Plan détaillé de ce qui a été fait, quand et par qui--

Travail préparatoire:

* 01/03: création d'un compte GitHub en classe

* Semaine du 08/03: introduction à Git-Hub en classe, divers essais à remplacer des mots par des émojis sur python - collaboration Catharina et Stephanie

* 15/03: Commencement du projet: recherche d'émojis, partage du travail, planification du projet, divers essais à remplacer des mots par des émojis sur python - collaboration Catharina et Stephanie

* 17/03: Catharina et Stephanie ont rejoigné l'organisation hackathon-nsi (02-lfv-e03)

Niveau 1:

* 19/03: Essai de déposer un fichier sur Git-Hub (Test_1), divers essais à remplacer des mots par des émojis sur un fichier externe - Stephanie ; Essai de télécharger un fichier de Git-Hub, commencement du programme principal - Catharina 

* 22/03: Finalisation du projet: finalisation de la fonction remplacer sur python (Fonction_remplacer), copié le texte de la Princesse de Clèves dans un fichier txt (PDC.txt) - Stephanie; finalisation du programme principal sur python (PDC en émojis), puis mise en commun avec le document de Stephanie pour voir si tout fonctionne sans problèmes, ajustements, création d'un programme qui transforme le texte avec les émojis en texte sans émojis (PDC en texte) - Catharina  

* Ajout de tous les programmes terminés le 22/03: PDC.txt, PDC en émojis, PDC en texte et Fonction_remplacer.

Niveau 2:

* 26/03: Commencement du niveau 2: travail sur le programme principal en html - Stephanie; Recherches sur la syntaxe de JS, commencement de la fonction remplacer en JavaScript - Catharina

* 12/04: Finalisation du programme principal en HTML (PDC en HTML) - Stephanie; travail sur la fonction remplacer en JavaScript - Catharina

* Ajout du programme terminé PDC en HTML le 12/04.

## DOCUMENTATION
Document Test_1.py:
Test pour voir comment GitHub fonctionne

Document PDC.txt - Stephanie:
* comporte seulement le texte de la 1ère partie de PDC, pas modifié

Document PDC en émojis.py - le programme principal - Catharina:
* importe la fonction remplacer de Stephanie
* exécute la fonction remplacer
* "stocke" ce qui sort de cette fonction dans une variable
* ouvre le document PDC.txt
* remplace le contenu du document PDC.txt par le texte changé qui a été "stocké" dans la variable

Document Fonction_remplacer.py - Stephanie:
* création d'un dictionnaire qui associe à quelques mots des émojis
* création de la fonction:
  * ouvre PDC.txt
  * parcourt chaque mot dans le document:
    * parcourt le dictionnaire
    * si le mot se trouve dans le dictionnaire, il est remplacé par son émoji
    * chaque mot remplacé ou non est ajouté dans une variable
  * retourne la variable, qui comporte le texte modifié

Document PDC en texte.py - Catharina:
* création d'un dictionnaire qui associe à quelques mots des émojis
* ouvre le document PDC.txt
* remplace chaque émoji par son mot correspondant
* écrit les changements dans le document PDC.txt qui "retrouve" sa forme initiale (sans émojis)

Document PDC en HTML.py - Stephanie:
* affiche tout le texte de la 1ère partie de la Princesse de Clèves
* affiche un bouton "remplacer", qui déclenche après un clic la fonction "remplacer" (arrive bientôt) en JavaScript
