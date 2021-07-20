# Cartographie

Projet de Cartographie réalisé sur les 3 fichiers Planète Solidaire se trouvant dans le dossier neo4j/ressources

## Pour commencer

Les fichiers contenant le code se trouvent dans le dossier neo4j/.
Le seul fichier à compiler est le main.py.
La visualisation des données est à voir dans une db neo4j.
Nous avons choisi de la centrer autour des projets réalisés.
Ils sont connectés aux sherpas, aux Pioupiou, et aux partenaires ainsi qu'à un noeud binôme connecté aux deux élèves d'EPITA

Les fichiers que nous avons décidé de traiter sont le .csv où sont listés les chefs de projets et leurs binômes, le .xlsx où sont listés les étudiants, les projets et les sherpas et le .xlsx avec le contact des partenaires.
Nous n'avons pas traité le .json délibérément car les informations que nous trouvons sur celui-ci peuvent sont les mêmes que dans le fichier "effectif_campus_clean.xlsx".

Dans ce même fichié, nous avons décidé de nettoyer les feuilles comme ceci :
dé-fusionner les cellules des tableaux principaux
supprimer les tableaux secondaires car les informations qu'ils comportaient étaient incomplètes et non significatives. 

### Pré-requis

- base de donnée neo4j
- neomodel
- openpyxl

### Lancement

- Lancer le fichier script.sh pour initialiser le docker avec elasticsearch
- Lancer la base de donnée Neo4j dans le Neo4j Browser
- Compiler le fichier main.py
- Admirer le résultat dans le Neo4j Browser

### Déroulé de l'algorithme

- On enlève les données résiduelles contenues dans la database
- On initialise la database avec des données non contenues dans les ressources (ex: les dirigeants Planète Solidaire)
- On parse le csv. Cela nous permet de créer une 1ere liste contenant les projets et les binômes EPITA
- On complète notre liste de projets en parsant l'excel. On ajoute donc les 2 projets ISG-only, et les informations ISG (étudiants et sherpas)
- On parse l'excel des partenaires et on ajoute leurs informations à chaque projet respectif.
- Avec cette liste de projets (classe python) on créé les noeuds Neo4J avec la structure ci-dessus ("Pour commencer")
- Le noeud PS est un noeud à part, il n'est pas connecté aux autres projets pour ne pas alourdir la lecture du graphique. Il est composé des chefs de ce projets et des consultants étant intervenus.

## Réalisé par

* Mai-Linh LANNES
* Alexandre UNG
* Rémy DOUADi


