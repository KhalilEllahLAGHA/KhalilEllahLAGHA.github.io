# Rapport et visualisations de bobinages multiphasés - 14 novembre 2026

La publication présente désormais un rapport technique en français intitulé
**Génération des bobinages multiphasés et analyse du champ magnétique**, signé
**LAGHA Khalil Ellah**.
Sa structure sépare les algorithmes généraux (entrées, sorties, étapes et
contrôles) des trois applications numériques. Les attributions de méthode et
de code restent dans les références du rapport, sans apparaître dans son titre
ou ses en-têtes.

## Configuration corrigée

Le troisième cas utilise **5 phases, 45 encoches, 8 pôles et un pas de 5 encoches**,
en double couche. Le pas de 11 de la publication précédente n'est plus le cas
étudié. Le tableau, les légendes, la vidéo et l'analyse de la page correspondent
à cette configuration corrigée.

Le pas électrique vaut 160 degrés, avec un facteur de pas de 0,98481 et un
facteur de bobinage utile d'environ 0,96888. La composante à huit pôles est
dominante. L'ancienne interprétation de faible couplage à huit pôles et de
domination bipolaire a été retirée de la page actuelle. Le modèle à perméabilités
imposées ne calcule pas le rendement : les harmoniques et leurs conséquences
éventuelles ne sont pas assimilées à une mesure de pertes ou de couple.

## Rapport et vidéos

- Le rapport de 24 pages comprend les trois dessins statoriques produits par
  le composant natif de l'application, les trois FMM et les trois cartes de
  flux/densité. Il est publié sous `reports/rapport-bobinages-multiphases.pdf`.
- L'ancienne URL du rapport reste un alias contenant exactement les mêmes
  octets français pour préserver les liens existants.
- Les deux vidéos, triphasée et pentaphasée, affichent explicitement tous les
  courants A-C ou A-E, leurs déphasages et leurs valeurs instantanées avec le
  champ calculé. Elles conservent un cycle électrique complet et une échelle
  de densité fixe par vidéo.
- Le format est H.264, 1600 par 900 pixels, 30 images par seconde, 12 secondes.
  Les lecteurs proposent les commandes, l'affichage en ligne et le téléchargement,
  sans lecture automatique. Les URL de média incluent une empreinte du contenu.
- Le nombre de solutions de base du modèle linéaire ne désigne pas un nombre
  de phases : les états signés à zéro et quatre-vingt-dix degrés contiennent
  les contributions de toutes les phases du bobinage actif.

Le générateur canonique reste `projects/build_project_pages.py`. Seule la page
de bobinage est régénérée. Les fichiers CV et les différences locales des styles
et scripts partagés sont préservés hors de cette modification.

La vérification locale couvre les liens, les versions française et anglaise,
les thèmes clair et sombre, les tailles ordinateur et téléphone, ainsi que le
décodage et la lecture réelle des deux vidéos dans une instance Edge isolée.
Les preuves privées et le manifeste de copie sont conservés dans
`tmp/winding-report-fr/portfolio-qa/` du dossier de travail parent. Les résultats
de publication et de contrôle en ligne sont enregistrés dans le contexte de
travail après le déploiement.
