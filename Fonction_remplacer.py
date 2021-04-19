
# Programme complémentaire
# Niveau 1 du projet 2
# Fonction remplacer()

# On crée un dictionnaire, où on associe quelques mots à des émojis. Il faut aussi prendre en compte les cas spéciaux par exemple les mots avec des points ou des virgules à la fin.
dic = {"princesse":"\U0001F478", "princesses":"\U0001F478" + "s", "princesse,":"\U0001F478"+",", "princesse.":"\U0001F478"+".",  "vit":"\U0001F441", "vit.":"\U0001F441"+".", "roi":"\U0001F934", "roi,":"\U0001F934"+",", "roi.":"\U0001F934"+".", "cour":"\U0001F3F0", "cour,":"\U0001F3F0"+",", "cour.":"\U0001F3F0"+".", "campagne":"\U0001F3DE", "campagne.":"\U0001F3DE"+".", "campagne,":"\U0001F3DE"+",", "passion":"\U0001F493", "passion.":"\U0001F493"+".", "passion,":"\U0001F493"+",", "passions,":"\U0001F493"+"s,"}

# On définit une fonction, qui remplace les mots du document par les émojis correspondants en utilisant le dictionnaire.
def remplacer():
    final="" # On crée une variable "final", vide.
    with open("PDC_ini.txt" , "rt" , encoding = "utf-8") as fichier : # On ouvre le document au mode de lecture (rt)
        for ligne in fichier:
            for mot in ligne.split(" "): # On parcourt chaque mot.
                for cle in dic: # On parcourt le dictionnaire.
                    if mot==cle: # On teste si le mot correspond à une clé du dictionnaire.
                        mot=dic[cle] # Si c'est le cas, on remplace le mot par la valeur correspondante.
                final+= mot + " " # On ajoute mot par mot (transformé ou non) dans la variable "final".
    return final # La variable "final" stocke tout le texte changé.






