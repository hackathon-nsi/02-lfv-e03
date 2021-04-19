
# Programme principal
# Niveau 1 du projet 2

# On importe l'autre document
from Fonction_remplacer import*

# On exécute la fonction remplacer, qui remplace chaque mot par son emoji. Le texte changé va être "stocké" dans une variable.
fichier_nv=remplacer()

# On remplace le contenu du document par le texte changé qui a été stocké dans la variable "fichier_nv" (wt = mode d'écriture)
with open("PDC.txt" , "wt" , encoding = "utf-8") as fichier :
    fichier.write(fichier_nv)














