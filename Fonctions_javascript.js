// Programme complémentaire
// Niveau 2 du projet 2
// Fonction remplacer() 

// On crée un dictionnaire, où on associe quelques mots à des émojis. Il faut aussi prendre en compte les cas spéciaux par exemple les mots avec des points ou des virgules à la fin.

var dic = {
  "princesse": "&#x1F478", 
  "princesses":"&#x1F478" + "s",   
  "princesse,":"&#x1F478"+",", 
  "princesse.":"&#x1F478"+".",  
  "vit":"&#x1F441",   
  "vit.":"&#x1F441"+".", 
  "roi":"&#x1F934", 
  "roi,":"&#x1F934"+",",   
  "roi.":"&#x1F934"+".", 
  "cour":"&#x1F3F0", 
  "cour,":"&#x1F3F0"+",",   
  "cour.":"&#x1F3F0"+".", 
  "campagne":"&#x1F3DE", 
  "campagne.":"&#x1F3DE"+".",   
  "campagne,":"&#x1F3DE"+",", 
  "passion":"&#x1F493", 
  "passion.":"&#x1F493"+".",   
  "passion,":"&#x1F493"+",",
  "passions,":"&#x1F493"+"s,",
}

// On crée une fonction, qui remplace les mots du document par les émojis correspondants en utilisant le dictionnaire.

function remplacer() {

var final = "";       // On crée une variable "final", vide, dont on a besoin à la fin du programme.
var texte = document.querySelector("p1").innerHTML;       // On crée une variable "texte" dans laquelle on stocke tout le texte de la PDC du document html.
var mot = texte.split(" ");       // On crée une variable mot qui découpe le texte html en mots séparés.

for (var i = 0; i < mot.length; i++) {       // On crée une boucle for qui répète le contenu pour chaque mot du texte.
  for (var cle in dic) {       // On crée une autre boucle for qui parcourt le dictionnaire.
    if (mot[i]===cle) {       // On teste si le mot correspond à une clé du dictionnaire.
      mot[i]=dic[cle];       // Si le mot correspond à une clé du dictionnaire, on le remplace par la valeur de la clé.
    }
  }
  final = final + mot[i] + " ";       // On ajoute mot par mot (transformé ou non) dans la variable "final".
}

document.querySelector("p1").innerHTML = final;       // On remet le texte sur la page html.

}

