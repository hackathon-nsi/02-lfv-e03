
# Programme complémentaire
# Niveau 1 du projet 2
# Fonction remplacer()

# On crée un dictionnaire, où on associe quelques mots à des émojis. Il faut aussi prendre en compte les cas spéciaux par exemple les mots avec des points ou des virgules à la fin.
dic = {"princesse":"\U0001F478", "princesses":"\U0001F478" + "s", "princesse,":"\U0001F478"+",", "princesse.":"\U0001F478"+".",  "vit":"\U0001F441", "vit.":"\U0001F441"+".", "roi":"\U0001F934", "roi,":"\U0001F934"+",", "roi.":"\U0001F934"+".", "cour":"\U0001F3F0", "cour,":"\U0001F3F0"+",", "cour.":"\U0001F3F0"+".", "campagne":"\U0001F3DE", "campagne.":"\U0001F3DE"+".", "campagne,":"\U0001F3DE"+",", "passion":"\U0001F493", "passion.":"\U0001F493"+".", "passion,":"\U0001F493"+","}

# On définit une fonction, qui remplace les mots du document par les émojis correspondants en utilisant le dictionnaire.
def remplacer():
    d="" # On crée une variable d, vide.
    with open("PDC.txt" , "rt" , encoding = "utf-8") as fichier : # On ouvre le document au mode de lecture (rt)
        for ligne in fichier:
            for mot in ligne.split(" "): # On parcourt chaque mot
                for cle in dic: # On parcourt le dictionnaire
                    if mot==cle:
                        mot=dic[cle] # On associe les valeurs correspondantes au mot
                d+= mot + " " # On ajoute mot par mot (transformé ou non) dans la variable d
    return d # La variable d stocke tout le texte changé






