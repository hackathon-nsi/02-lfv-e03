
# Programme additionnel (pas demandé par l'énoncé, mais utile si on veut retransformer PDC.fin en texte sans émojis)
# Niveau 1 du projet 2

# Ce programme additionnel (plus court, car il utilise la fonction replace()), permet de retransformer le texte avec émojis en texte sans émojis.

dic = {"princesse":"\U0001F478", "vit":"\U0001F441", "roi":"\U0001F934", "cour":"\U0001F3F0", "campagne":"\U0001F3DE", "passion":"\U0001F493"}

with open("PDC_fin.txt" , "rt" , encoding = "utf-8") as fichier :
    d=fichier.read()
    for cle in dic:
        d=d.replace(dic[cle], cle)

with open("PDC_fin.txt" , "wt" , encoding = "utf-8") as fichier :
    fichier.write(d)