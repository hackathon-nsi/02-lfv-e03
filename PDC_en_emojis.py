
# Programme principal
# Niveau 1 du projet 2

# On importe la fonction
from Fonction_remplacer import*

# On exécute la fonction remplacer, qui remplace chaque mot par son emoji. Le texte changé va être "stocké" dans une variable.
fichier_nv=remplacer()

# On remplace le contenu du texte de sortie (PDC_fin.txt) par le texte changé qui a été stocké dans la variable "fichier_nv" (wt = mode d'écriture)
with open("PDC_fin.txt" , "wt" , encoding = "utf-8") as fichier :
    fichier.write(fichier_nv)














