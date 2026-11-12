"""Build the bilingual project pages."""

from html import escape
from hashlib import sha256
from pathlib import Path


PAGES = [
    {'slug': 'pemfc-internship',
     'title': ('Stage PEMFC au GIPSA-lab', 'PEMFC internship at GIPSA-lab'),
     'eyebrow': ('Stage / Pile à combustible', 'Internship / Fuel cell'),
     'summary': ('Relier une pile à combustible aux mesures disponibles : j’ai travaillé sur son modèle et sur les '
                 'vérifications nécessaires pour distinguer ce qu’il explique de ce qui reste à confirmer.',
                 'Connect a fuel cell to the measurements available: I worked on its model and the checks needed to '
                 'distinguish what it explains from what remains uncertain.'),
     'scope': ('Stage de recherche · Avril–juillet 2026 · MATLAB / Python',
               'Research internship · April–July 2026 · MATLAB / Python'),
     'metrics': [('10', 'cellules sur le banc', 'cells on the test bench'),
                 ('7', 'cellules retenues pour l’ajustement', 'cells used for fitting'),
                 ('116', 'échantillons réservés au test chronologique', 'samples reserved for the chronological test')],
     'hero_image': ('pemfc-bench.png',
                    'Banc expérimental de la pile à combustible PEMFC',
                    'PEM fuel-cell experimental test bench',
                    'Le banc utilisé pendant le stage au GIPSA-lab.',
                    'The test bench used during the GIPSA-lab internship.'),
     'chapters': [{'id': 'problem',
                   'title': ('Le problème : construire un modèle avec des mesures incomplètes',
                             'The problem: model a system with incomplete measurements'),
                   'intro': ('Une pile PEMFC associe phénomènes électriques, circulation des gaz et gestion de l’eau. Le '
                             'travail consistait à relier ces phénomènes aux mesures disponibles sur un petit stack '
                             'pédagogique.',
                             'A PEM fuel cell combines electrical behaviour, gas flow and water management. The work was '
                             'to connect these processes to the measurements available on a small educational stack.'),
                   'paragraphs': [('J’ai réalisé ce stage dans l’équipe Infinity du GIPSA-lab, à l’Université Grenoble '
                                   'Alpes, sous la supervision d’Emmanuel Witrant. Le banc comporte dix cellules dont '
                                   'les tensions sont suivies séparément. Les cellules 3 à 9 ont été retenues pour '
                                   'l’étude du fonctionnement actif.',
                                   'I completed this internship in the Infinity team at GIPSA-lab, Université Grenoble '
                                   'Alpes, under Emmanuel Witrant’s supervision. The bench has ten cells with individual '
                                   'voltage measurements. Cells 3 to 9 were selected for the active-operation study.'),
                                  ('Le banc ne disposait pas de mesures de température ni de pression d’oxygène. Ces '
                                   'grandeurs devaient donc être supposées dans le modèle, ce qui limite '
                                   'l’identification des paramètres internes et les possibilités de commande fondées sur '
                                   'ces états.',
                                   'The bench did not provide temperature or oxygen-pressure measurements. These '
                                   'quantities therefore had to be assumed in the model, limiting identification of '
                                   'internal parameters and control based on those states.')],
                   'points': []},
                  {'id': 'method',
                   'title': ('Ajuster le modèle et vérifier ses limites', 'Fit the model and check its limits'),
                   'intro': ('Un modèle empirique de tension par cellule a été ajusté aux mesures, puis complété par une '
                             'étude analytique des dynamiques de pression et d’eau.',
                             'An empirical per-cell voltage model was fitted to measurements, alongside an analytical '
                             'study of pressure and water dynamics.'),
                   'paragraphs': [('L’ajustement initial utilise une température fixe de 343,15 K, une pression '
                                   'partielle d’oxygène de 0,21 atm et une hydratation de membrane de 14. Certains '
                                   'coefficients n’étant pas identifiables séparément, leur ajustement ne suffit pas à '
                                   'leur donner une interprétation physique unique.',
                                   'The initial fit uses a fixed temperature of 343.15 K, an oxygen partial pressure of '
                                   '0.21 atm and membrane hydration of 14. Some coefficients cannot be identified '
                                   'separately, so fitting them does not establish a unique physical interpretation.'),
                                  ('L’analyse structurelle montre que le débit d’hydrogène seul ne permet pas de '
                                   'commander tous les états du modèle étudié. La tension seule ne permet pas non plus '
                                   'de tous les observer. Ces résultats et les capteurs manquants motivent l’étude d’une '
                                   'commande à partir des grandeurs électriques accessibles.',
                                   'The structural analysis shows that hydrogen flow alone cannot control all states of '
                                   'the model studied. Voltage alone cannot observe them all either. These results and '
                                   'the missing sensors motivate control using the electrical quantities that can be '
                                   'measured.')],
                   'points': [],
                   'flow': [('Partir du banc',
                             'Start with the bench',
                             'Les tensions des cellules et les conditions disponibles définissent les données de départ.',
                             'Cell voltages and available operating conditions define the starting data.'),
                            ('Ajuster le modèle',
                             'Fit the model',
                             'Un modèle de tension est ajusté sur une première portion de l’expérience.',
                             'A voltage model is fitted on an initial portion of the experiment.'),
                            ('Tester la suite',
                             'Test the next segment',
                             'Une portion chronologique tenue à l’écart permet un contrôle dans la même expérience.',
                             'A held-back chronological segment provides a check within the same experiment.'),
                            ('Identifier les limites',
                             'Identify limits',
                             'Les capteurs manquants et le courant reconstruit bornent les conclusions et les pistes de '
                             'commande.',
                             'Missing sensors and reconstructed current limit conclusions and control proposals.')]},
                  {'id': 'evidence',
                   'title': ('Distinguer ajustement et prédiction', 'Separate fitting from prediction'),
                   'intro': ('Sur les cellules 3 à 9, l’erreur quadratique moyenne de l’ajustement initial est comprise '
                             'entre 2,0 et 11,3 mV. Un test chronologique complète ce résultat sur une partie des '
                             'mesures tenue à l’écart de l’ajustement.',
                             'For cells 3 to 9, the initial fit has a root mean square error between 2.0 and 11.3 mV. A '
                             'chronological test adds a check on measurements held back from fitting.'),
                   'paragraphs': [('Un modèle empirique à deux coefficients a été ajusté sur les 269 premiers '
                                   'échantillons de la fenêtre étudiée, puis évalué sur les 116 suivants. L’erreur de '
                                   'test est comprise entre 1,8 et 10,2 mV pour les sept cellules actives.',
                                   'A two-coefficient empirical model was fitted to the first 269 samples of the '
                                   'selected window, then evaluated on the following 116. Test error ranges from 1.8 to '
                                   '10.2 mV across the seven active cells.'),
                                  ('Ce test reste issu de la même expérience. Le courant est reconstruit à partir de la '
                                   'tension du stack et d’une résistance supposée de 25 Ω : il ne constitue donc pas une '
                                   'validation dynamique indépendante. Les essais d’un autre cycle en juillet permettent '
                                   'une comparaison dans d’autres conditions, sans établir à eux seuls la cause d’une '
                                   'dégradation.',
                                   'This test still comes from the same experiment. Current is reconstructed from stack '
                                   'voltage and an assumed 25 Ω resistance, so it does not constitute independent '
                                   'dynamic validation. A different operating cycle in July provides a comparison under '
                                   'other conditions, without establishing the cause of degradation on its own.')],
                   'points': [],
                   'image': ('pemfc-holdout.png',
                             'Résultats du test chronologique sur les tensions des cellules actives',
                             'Chronological test results for active-cell voltages',
                             'Ajustement puis test sur les échantillons suivants de la même expérience.',
                             'Fitting followed by testing on subsequent samples from the same experiment.')},
                  {'id': 'takeaway',
                   'title': ('Une piste de commande à poursuivre', 'A control approach to develop'),
                   'intro': ('La suite proposée repose sur un convertisseur boost et une régulation PI du courant du '
                             'stack, afin d’agir sur un signal électrique accessible sans dépendre de tous les états '
                             'internes de la pile.',
                             'The proposed next step uses a boost converter and PI control of stack current, acting on '
                             'an accessible electrical signal without relying on every internal fuel-cell state.'),
                   'paragraphs': [('Cette architecture reste une proposition : les gains et la boucle fermée n’ont pas '
                                   'été validés sur le banc. La calibration du courant et des mesures supplémentaires de '
                                   'température et de pression d’oxygène seraient nécessaires pour poursuivre les essais '
                                   'et améliorer le modèle.',
                                   'This architecture remains a proposal: controller gains and closed-loop behaviour '
                                   'have not been validated on the bench. Current calibration and additional temperature '
                                   'and oxygen-pressure measurements would be needed to continue testing and improve the '
                                   'model.'),
                                  ('Le rapport rassemble le modèle, les expériences et leurs limites. Le dépôt contient '
                                   'les programmes d’acquisition et de traitement, les données et les calculs utilisés '
                                   'pour vérifier les résultats présentés.',
                                   'The report brings together the model, experiments and their limits. The repository '
                                   'contains acquisition and processing programs, data and calculations used to check '
                                   'the reported results.')],
                   'points': []}],
     'reports': ('../reports/Khalil_Lagha_PEMFC_Internship_Report.pdf',
                 '../reports/Khalil_Lagha_PEMFC_Internship_Report.pdf'),
     'report_download': 'Khalil_Lagha_PEMFC_Internship_Report.pdf',
     'report_label': ('Rapport de stage', 'Internship report'),
     'repo': 'https://github.com/KhalilEllahLAGHA/PEMFC_Internship_codes'},
    {'slug': 'power-grid-analysis',
     'title': ('Analyse de réseaux électriques', 'Power grid analysis'),
     'eyebrow': ('01 / Systèmes électriques', '01 / Power systems'),
     'summary': ('J’ai construit un outil MATLAB pour comprendre le fonctionnement d’un réseau, comparer les méthodes de '
                 'calcul et examiner sa réaction après une perturbation.',
                 'I built a MATLAB tool to understand network operation, compare numerical methods and examine its '
                 'response after a disturbance.'),
     'scope': ('Projet académique individuel · MATLAB / App Designer',
               'Individual academic project · MATLAB / App Designer'),
     'metrics': [('3–118', 'nœuds dans les cas de test', 'buses across the test systems'),
                 ('3', 'solveurs de load flow comparés', 'load-flow solvers compared'),
                 ('14', 'réseaux de validation documentés', 'documented validation networks')],
     'hero_image': ('grid-interface.png',
                    'Interface de l’application MATLAB d’analyse de réseaux',
                    'MATLAB power-grid analysis application interface',
                    'L’interface rassemble matrices, load flow et stabilité.',
                    'The interface brings together matrices, load flow and stability.'),
     'chapters': [{'id': 'problem',
                   'title': ('Le problème : comprendre le comportement du réseau',
                             'The problem: understand network behaviour'),
                   'intro': ('À partir des lignes, des transformateurs et des charges, il faut retrouver les tensions et '
                             'les puissances, puis savoir ce que le réseau devient après un incident.',
                             'Starting with lines, transformers and loads, the task is to find voltages and power flows, '
                             'then examine what happens after a disturbance.'),
                   'paragraphs': [('J’ai construit ce projet en solo dans le cadre du TP d’analyse des réseaux '
                                   'électriques à l’ENP. Le parcours de calcul part des données de branche, assemble '
                                   'Ybus et Zbus, résout l’écoulement de puissance, puis utilise l’état pré-défaut pour '
                                   'une étude de stabilité transitoire.',
                                   'I built this project individually for the ENP power-system analysis lab. The '
                                   'calculation path starts with branch data, assembles Ybus and Zbus, solves power '
                                   'flow, then uses the pre-fault state for a transient-stability study.'),
                                  ('L’interface App Designer expose les trois outils sans cacher la logique numérique : '
                                   'les réseaux de test et les fonctions MATLAB restent séparés, ce qui permet aussi une '
                                   'validation sans interface graphique.',
                                   'The App Designer interface exposes all three tools without hiding the numerical '
                                   'core: test networks and MATLAB functions remain separate, allowing headless '
                                   'validation as well.')],
                   'points': [('Données',
                               'Bus PQ, PV et slack ; lignes et transformateurs à prise hors nominale.',
                               'PQ, PV and slack buses; lines and off-nominal tap transformers.'),
                              ('Matrices',
                               'Construction de Ybus et Zbus, avec comparaison à l’inverse de Ybus.',
                               'Ybus and Zbus construction, with a check against inverse Ybus.'),
                              ('Question',
                               'Que gagne-t-on en précision et en temps avec chaque solveur ?',
                               'What does each solver gain in accuracy and time?')]},
                  {'id': 'method',
                   'title': ('Trois chemins vers le load flow', 'Three routes to load flow'),
                   'intro': ('Le cœur du projet compare Gauss–Seidel, Newton–Raphson et la méthode découplée rapide BX '
                             'sur les mêmes réseaux et avec les mêmes catégories de bus.',
                             'The core of the project compares Gauss–Seidel, Newton–Raphson and BX fast-decoupled load '
                             'flow on the same networks and bus categories.'),
                   'paragraphs': [('Le constructeur Ybus additionne correctement les branches parallèles et intègre les '
                                   'transformateurs. Zbus est obtenue par construction directe ; l’écart maximal avec '
                                   'inv(Ybus) sert de contrôle sur les réseaux où cette comparaison est possible.',
                                   'The Ybus builder accumulates parallel branches and incorporates transformers. Zbus '
                                   'uses a direct building algorithm; maximum error against inv(Ybus) serves as a check '
                                   'where that comparison is defined.'),
                                  ('Gauss–Seidel et Newton–Raphson prennent en compte les contraintes de puissance '
                                   'réactive des bus PV ; la version découplée rapide BX sert à comparer une formulation '
                                   'différente sans cette gestion des limites. Leurs itérations et résultats sont '
                                   'étudiés de 3 à 118 nœuds, dont les cas IEEE 14, 30, 57 et 118.',
                                   'Gauss–Seidel and Newton–Raphson handle PV-bus reactive-power limits; the BX '
                                   'fast-decoupled version provides a different formulation for comparison without that '
                                   'limit handling. Their iterations and outputs are studied from 3 to 118 buses, '
                                   'including IEEE 14, 30, 57 and 118 cases.')],
                   'points': [('Gauss–Seidel',
                               'Itération accélérée et contrôle des limites Q des bus PV.',
                               'Accelerated iteration and PV-bus reactive-limit handling.'),
                              ('Newton–Raphson',
                               'Formulation rectangulaire pour résoudre les inconnues du réseau.',
                               'Rectangular-coordinate formulation for solving network unknowns.'),
                              ('BX',
                               'Découplage rapide pour confronter coût de calcul et résultat.',
                               'Fast-decoupled formulation for comparing computational cost and output.')],
                   'image': ('grid-loadflow-iterations.png',
                             'Comparaison du nombre d’itérations des méthodes de load flow',
                             'Load-flow iteration comparison chart',
                             'Comparer la convergence plutôt que choisir un solveur sur son nom.',
                             'Comparing convergence rather than choosing a solver by name.'),
                   'flow': [('Décrire le réseau',
                             'Describe the grid',
                             'Les branches et les rôles PQ, PV et slack précisent les données connues et les inconnues.',
                             'Branches and PQ, PV and slack roles define known data and unknowns.'),
                            ('Assembler les connexions',
                             'Assemble connections',
                             'Ybus et Zbus représentent les relations électriques entre les nœuds.',
                             'Ybus and Zbus represent electrical relationships between buses.'),
                            ('Résoudre et comparer',
                             'Solve and compare',
                             'Trois solveurs recherchent le point de fonctionnement ; je compare précision et coût de '
                             'calcul.',
                             'Three solvers find the operating point; I compare accuracy and computational cost.'),
                            ('Étudier une perturbation',
                             'Study a disturbance',
                             'La stabilité transitoire examine l’évolution des machines après le défaut et l’ouverture '
                             'de ligne.',
                             'Transient stability examines machine evolution after the fault and line opening.')]},
                  {'id': 'evidence',
                   'title': ('Du régime établi au défaut', 'From steady state to a fault'),
                   'intro': ('Après le load flow, une séquence défaut puis ouverture de ligne alimente un modèle '
                             'classique de stabilité transitoire. L’angle rotorique est intégré avec la méthode d’Euler.',
                             'After load flow, a fault and line-opening sequence feeds a classical transient-stability '
                             'model. Rotor angle is integrated with Euler’s method.'),
                   'paragraphs': [('Le test numérique documenté porte sur quatorze réseaux pour les matrices et '
                                   'solveurs, avec un cas à six nœuds pour la stabilité. Sur le cas IEEE 118, les pertes '
                                   'calculées de 131,96 MW correspondent à la référence citée dans le projet ; Zbus et '
                                   'inv(Ybus) concordent à la précision machine sur les réseaux ancrables.',
                                   'The documented numerical suite covers fourteen networks for matrices and solvers, '
                                   'plus a six-bus stability case. On IEEE 118, computed losses of 131.96 MW match the '
                                   'reference cited in the project; Zbus and inv(Ybus) agree to machine precision on '
                                   'anchorable networks.'),
                                  ('Il s’agit d’une étude de simulation et de comparaison numérique. Elle n’établit pas '
                                   'une validation sur réseau réel ; son intérêt est de relier modèle, algorithme et '
                                   'interprétation des résultats dans un même outil.',
                                   'This is a simulation and numerical-comparison study, not validation on an operating '
                                   'grid. Its value is connecting model, algorithm and interpretation within one tool.')],
                   'points': [],
                   'image': ('grid-transient-stability.png',
                             'Évolution transitoire de l’angle rotorique après défaut',
                             'Transient rotor-angle response after a fault',
                             'La réponse transitoire complète l’analyse de régime établi.',
                             'The transient response complements steady-state analysis.')},
                  {'id': 'takeaway',
                   'title': ('Ce que montre le projet', 'What this project demonstrates'),
                   'intro': ('Un même réseau peut être abordé par ses matrices, son équilibre de puissance et sa '
                             'dynamique après incident. La valeur vient de leur cohérence, vérifiée à chaque étape.',
                             'The same network can be examined through its matrices, power balance and post-disturbance '
                             'dynamics. The value lies in their consistency, checked at every step.'),
                   'paragraphs': [('La partie qui m’a le plus plu était de traduire ma compréhension des algorithmes de '
                                   'stabilité transitoire en code et de chercher à retrouver les résultats du '
                                   'professeur. C’était un défi difficile, mais plaisant, comme un problème de '
                                   'programmation.',
                                   'My favourite part was translating my understanding of transient-stability algorithms '
                                   'into code and trying to reproduce the professor’s results. It was challenging but '
                                   'enjoyable, like a programming problem.'),
                                  ('Le dépôt contient le code MATLAB, les systèmes de test et la logique de validation. '
                                   'Le rapport détaille les hypothèses, méthodes, figures et limites de l’étude.',
                                   'The repository contains MATLAB code, test systems and validation routines. The '
                                   'report documents assumptions, methods, figures and study limits.')],
                   'points': []}],
     'reports': ('../reports/power-grid-analysis-report.pdf', '../reports/power-grid-analysis-report-en.pdf'),
     'repo': 'https://github.com/KhalilEllahLAGHA/Power-grid-analysis-MATLAB'},
    {'slug': 'foc-induction-motor',
     'title': ('Commande vectorielle d’un moteur asynchrone', 'Field-oriented control of an induction motor'),
     'eyebrow': ('02 / Commande de machines', '02 / Motor drives'),
     'summary': ('Réguler la vitesse d’un moteur asynchrone de 5 kW et comparer la SPWM à deux séquences SVPWM, '
                 'à sept et à quatre segments, sur le même onduleur IGBT simulé.',
                 'Control a 5 kW induction motor and compare SPWM with seven- and four-segment SVPWM on the same '
                 'simulated IGBT inverter.'),
     'scope': ('Projet individuel · Python / MATLAB / Simulink', 'Individual project · Python / MATLAB / Simulink'),
     'metrics': [('3', 'implémentations comparables', 'comparable implementations'),
                 ('52–95 ms', 'établissement des échelons de vitesse', 'speed-step settling range'),
                  ('0,800 Wb', 'flux rotorique maintenu', 'maintained rotor flux')],
     'hero_image': ('foc-control.svg',
                    'Chaîne de commande FOC et retours de vitesse et de courant',
                    'FOC control chain with speed and current feedback',
                    'La consigne devient une demande de couple, puis des tensions et des commandes d’onduleur.',
                    'The speed target becomes torque demand, voltage references and inverter commands.'),
     'chapters': [{'id': 'problem',
                   'title': ('Le problème : garder la vitesse malgré la charge',
                             'The problem: hold speed as load changes'),
                   'intro': ('Une charge supplémentaire freine le moteur. La commande doit produire le couple nécessaire '
                             'pour retrouver la vitesse demandée, tout en gardant le flux sous contrôle.',
                             'An added load slows the motor. The controller must produce the torque needed to recover '
                             'target speed while keeping flux under control.'),
                   'paragraphs': [('J’ai étudié une machine asynchrone de 5 kW / 380 V. Dans cette machine, flux et '
                                   'couple sont liés : agir directement sur les trois courants rend leur pilotage '
                                   'difficile à lire. J’ai donc utilisé une FOC indirecte à flux rotorique orienté.',
                                   'I studied a 5 kW / 380 V induction motor. Flux and torque interact, so directly '
                                   'controlling the three phase currents makes their roles hard to separate. I used '
                                   'indirect rotor-flux-oriented control.'),
                                  ('L’idée est de regarder les courants dans un repère qui tourne avec le flux '
                                   'rotorique. Dans ce repère, id agit principalement sur l’aimantation et le flux, '
                                   'tandis que iq agit sur le couple. La boucle de vitesse ajuste la demande de couple '
                                   'lorsque la vitesse s’écarte de sa consigne.',
                                   'The idea is to express currents in a frame rotating with rotor flux. In that frame, '
                                   'id mainly controls magnetisation and flux, while iq controls torque. The speed loop '
                                   'adjusts torque demand when speed departs from its target.')],
                   'points': [('Objectif',
                               'Suivre une vitesse et rejeter une variation de charge.',
                               'Track speed and reject a load disturbance.'),
                              ('Flux',
                               'id règle principalement l’aimantation de la machine.',
                               'id mainly sets motor magnetisation.'),
                              ('Couple',
                               'iq règle le couple dans le repère correctement orienté.',
                               'iq controls torque in the correctly aligned frame.')]},
                  {'id': 'method',
                   'title': ('Comment la commande agit sur le moteur', 'How the controller drives the motor'),
                   'intro': ('Chaque bloc a un rôle précis : changer de repère, orienter les axes, régler les courants, '
                             'puis transformer une tension calculée en action de l’onduleur.',
                             'Each block has a specific role: change coordinates, align the axes, control currents, then '
                             'turn a calculated voltage into inverter action.'),
                   'paragraphs': [('Le modèle en courant estime le flux rotorique. La vitesse électrique du rotor et le '
                                   'glissement calculé donnent l’angle du repère utilisé par Park. Cet estimateur aide à '
                                   'l’orientation ; le découplage vient du repère aligné et des termes d’anticipation '
                                   'ajoutés aux régulateurs.',
                                   'A current model estimates rotor flux. Electrical rotor speed and calculated slip '
                                   'provide the reference-frame angle used by Park. The estimator supports orientation; '
                                   'the aligned frame and feed-forward terms in the controllers provide decoupling.'),
                                  ('La SPWM compare les tensions de phase à une porteuse triangulaire. La SVPWM détermine '
                                   'le secteur du vecteur de tension, calcule les durées des deux états actifs et répartit '
                                   'le temps restant entre les états nuls. La séquence à sept segments organise ces '
                                   'durées en impulsions de grille symétriques. La séquence à quatre segments applique '
                                   'chaque état actif d’un seul tenant.',
                                   'SPWM compares the phase commands with a triangle. SVPWM finds the voltage sector, '
                                   'calculates the two active dwell times and shares the remaining time between the '
                                   'zero states. The seven-segment sequence mirrors the active intervals. '
                                   'The four-segment sequence applies each active state in one interval.')],
                   'flow': [('Clarke et Park',
                             'Clarke and Park',
                             'Les trois courants deviennent deux composantes dans un repère tournant aligné sur le flux.',
                             'Three phase currents become two components in a rotating frame aligned with flux.'),
                            ('Courants id et iq',
                             'id and iq currents',
                              'Deux régulateurs suivent les consignes de courant id et iq, avec compensation de leurs '
                               'interactions.',
                               'Two controllers track id and iq current references, with feed-forward compensation of '
                               'their interaction.'),
                            ('Tensions de référence',
                             'Voltage references',
                             'Les PI calculent vd et vq. Park inverse les ramène au repère fixe pour la modulation.',
                             'The PIs calculate vd and vq. Inverse Park returns them to the stationary frame for '
                             'modulation.'),
                            ('Modulation de l’onduleur',
                             'Inverter modulation',
                             'La SPWM utilise un comparateur et la SVPWM calcule les durées de commutation.',
                             'SPWM uses a comparator and SVPWM calculates switching durations.'),
                            ('Onduleur et machine',
                             'Inverter and motor',
                             'L’onduleur synthétise les tensions triphasées. Les courants et la vitesse reviennent au '
                             'contrôleur.',
                             'The inverter synthesises three-phase voltages. Currents and speed feed back to the '
                             'controller.')],
                   'points': [],
                   'image': ('foc-simscape-scopes.png',
                             'Schéma Simscape de la commande FOC et panneau Scopes',
                             'Simscape FOC wiring and Scopes panel',
                             'Le panneau Scopes regroupe la vitesse, le couple, les courants, le flux et les '
                             'commandes de grille des IGBT. Les liaisons du modèle sont tracées à angle droit.',
                             'The Scopes panel groups speed, torque, currents, flux and IGBT gate commands. '
                             'The model wiring uses horizontal and vertical segments.'),
                   'extra_images': [
                       ('foc-simscape-carrier-slow.png',
                        'Illustration des trois commandes de grille et des sept segments avec une porteuse lente',
                        'Slow-carrier illustration of three gate commands and seven switching segments',
                        'Consignes à 50 Hz et porteuse ralentie à 150 Hz. La porteuse franchit A, C puis B à la descente et les franchit '
                        'en sens inverse à la remontée. Chaque bras reçoit une impulsion. Les trois bras '
                        'ensemble donnent les sept segments.',
                        '50 Hz phase references with a slowed 150 Hz triangle. The falling triangle crosses A, C, then B, and the rising triangle '
                        'crosses them in reverse. Each leg has one on pulse. The three legs together give seven segments.'),
                   ],
                   'references': [('FOC à flux rotorique orienté',
                                   'Rotor-field-oriented control',
                                   'https://imperix.com/doc/implementation/rotor-field-oriented-control'),
                                  ('Principe de la SVPWM',
                                   'SVPWM principle',
                                   'https://imperix.com/doc/implementation/space-vector-modulation')]},
                  {'id': 'evidence',
                   'title': ('Lire la vitesse avec la charge, le couple et le flux',
                             'Read speed alongside load, torque and flux'),
                   'intro': ('Une courbe de vitesse isolée cache la cause des écarts. Ces quatre vues partagent le même '
                             'axe temporel et proviennent d’un même calcul Python.',
                             'A speed trace alone hides the cause of deviations. These four views share one time axis '
                             'and come from the same Python simulation.'),
                   'paragraphs': [('Les changements de consigne demandent une accélération, un freinage ou une '
                                   'inversion. Le couple électromagnétique change pour produire cette évolution. '
                                   'L’application de la charge provoque, elle, un creux de vitesse que la boucle corrige '
                                   'en augmentant la demande de couple.',
                                   'Reference changes demand acceleration, braking or reversal. Electromagnetic torque '
                                   'changes to produce that motion. Applying load instead causes a speed dip, which the '
                                   'loop corrects by increasing torque demand.'),
                                  ('La référence de flux reste fixée à 0,8 Wb : sa courbe montre la montée initiale puis '
                                   'le maintien du flux, et non une consigne de défluxage. Les courants id et iq '
                                   'permettent de lire séparément l’aimantation et l’effort de couple.',
                                   'Flux reference stays at 0.8 Wb: its trace shows initial build-up and subsequent flux '
                                   'control, not a field-weakening command. The id and iq traces distinguish '
                                     'magnetisation from torque effort.'),
                                    ('À 0,55 s, la charge de +10 N·m provoque le creux de vitesse. À 1,30 s puis '
                                     '1,80 s, le couple et iq deviennent temporairement négatifs pour ralentir puis '
                                     'inverser la rotation. Leur retour à des valeurs positives à vitesse négative '
                                     'vient de la convention du scénario : la charge conserve le signe +10 N·m '
                                     'après l’inversion, et le moteur doit équilibrer cette action.',
                                     'At 0.55 s, the +10 N·m load causes the speed dip. At 1.30 s and 1.80 s, torque '
                                     'and iq briefly become negative to slow down and then reverse rotation. Their '
                                     'return to positive values at negative speed follows the scenario’s sign '
                                     'convention: load torque remains +10 N·m after reversal, and the motor must '
                                     'balance that action.')],
                   'points': [],
                   'image': ('foc-response-context.png',
                             'Simulation Python : vitesse, couple de charge et électromagnétique, courants id iq et flux '
                             'rotorique sur le même scénario',
                             'Python simulation: speed, load and electromagnetic torque, id iq currents and rotor flux '
                             'in the same scenario',
                             'Scénario Python à onduleur moyenné. Courants, charge et flux donnent le contexte des '
                             'variations de vitesse ; ce ne sont pas des mesures sur banc.',
                             'Python scenario with an averaged inverter. Currents, load and flux explain speed changes; '
                             'these are not hardware measurements.')},
                  {'id': 'takeaway',
                   'title': ('Comparer les trois modulations dans Simscape', 'Compare the three PWM variants in Simscape'),
                   'intro': ('Pourquoi les tensions de la SPWM et de la SVPWM à sept segments se ressemblent-elles ? '
                             'J’ai ajouté une séquence à quatre segments pour isoler l’effet du placement des impulsions.',
                             'Why do SPWM and seven-segment SVPWM produce such similar voltage traces? '
                             'I added a four-segment variant to see how changing the pulse placement affects the drive.'),
                   'paragraphs': [('J’ai simulé les trois modèles avec le même onduleur IGBT, un bus continu de 540 V, '
                                   'une fréquence de commutation de 10 kHz et les mêmes réglages de commande. '
                                   'J’ai comparé les tensions de phase et le couple sur six périodes, de 1,1050 à 1,1056 s, '
                                   'à la consigne de 1 400 tr/min.',
                                   'I ran the three models with the same IGBT inverter, 540 V DC bus, 10 kHz switching '
                                   'frequency and controller settings. I compared phase voltages and torque over six '
                                   'periods, from 1.1050 to 1.1056 s, at the 1,400 rpm command.')],
                   'extra_images': [
                       ('foc-simscape-voltage-7seg.png',
                        'Tensions triphasées du moteur en SPWM et en SVPWM à sept segments',
                        'Motor phase voltages for SPWM and seven-segment SVPWM',
                        'Sur la première période, les états 000 et 111 durent 14 et 8 µs en SPWM, '
                        'contre 10 µs chacun en SVPWM centrée.',
                        'In the first period, states 000 and 111 last 14 and 8 µs with SPWM '
                        'and 10 µs each with centered SVPWM.'),
                       ('foc-simscape-voltage-4seg.png',
                        'Tensions triphasées du moteur en SPWM et en SVPWM à quatre segments',
                        'Motor phase voltages for SPWM and four-segment SVPWM',
                        'Sur la première période, la tension moyenne de la phase A vaut environ 194,4 V dans les deux essais.',
                        'In the first period, phase A averages about 194.4 V in both runs.'),
                       ('foc-simscape-torque.png',
                        'Couple électromagnétique brut des trois modulations sur six périodes PWM',
                        'Raw electromagnetic torque for all three methods over six PWM periods',
                        'Sur cette fenêtre, le couple crête à crête vaut 2,14 N·m en SPWM, 1,96 N·m en SVPWM '
                        'à sept segments et 3,41 N·m en SVPWM à quatre segments.',
                        'In this window, peak-to-peak torque was 2.14 N·m for SPWM, 1.96 N·m for seven-segment SVPWM, '
                        'and 3.41 N·m for four-segment SVPWM.'),
                       ('foc-simscape-speed.png',
                        'Vitesse du rotor et consigne en SVPWM dans Simscape',
                        'Simscape SVPWM rotor speed and reference',
                        'Vitesse du rotor et consigne pendant l’essai complet en SVPWM à sept segments.',
                        'Rotor speed and its reference during the full seven-segment SVPWM run.'),
                       ('foc-simscape-drive-torque.png',
                        'Couple électromagnétique et couple de charge en SVPWM',
                        'SVPWM electromagnetic torque and applied load torque',
                        'Réponse du couple moteur aux changements de consigne et de charge en SVPWM.',
                        'Motor torque response to the reference and load changes during the SVPWM run.'),
                       ('foc-simscape-phase.png',
                        'Courants bruts des phases A, B et C en SVPWM sur une période électrique',
                        'Raw SVPWM phase A, B and C currents over one electrical cycle',
                        'Les trois courants sont superposés sur une période électrique, au pas de simulation de 1 µs. '
                        'Le courant C est reconstruit à partir de A et B.',
                        'The three currents share one set of axes over one electrical cycle at the 1 µs simulation step. '
                        'Phase C current is reconstructed from A and B.'),
                       ('foc-simscape-dq.png',
                        'Courants id et iq et consignes en SVPWM',
                        'SVPWM d- and q-axis currents and references',
                        'Suivi des consignes des courants id et iq dans le repère du flux rotorique.',
                        'Tracking of the d- and q-axis current references in the rotor-flux frame.'),
                   ],
                   'points': []}],
     'reports': ('../reports/foc-induction-motor-report.pdf', '../reports/foc-induction-motor-report-en.pdf'),
     'repo': 'https://github.com/KhalilEllahLAGHA/foc-induction-motor'},
{'slug': 'winding-flux-analysis',
 'title': ('Bobinage et analyse de flux', 'Winding and flux analysis'),
 'eyebrow': ('03 / Conception de machines', '03 / Machine design'),
 'summary': ('Du bobinage au champ magnétique : notre application Python relie une matrice de connexions signée, '
             'la force magnétomotrice et un réseau de réluctances. Les cartes 2D et la comparaison avec FEMM '
             'permettent d’interpréter le résultat et ses erreurs de discrétisation.',
             'From winding to magnetic field: our Python application connects a signed connection matrix, '
             'magnetomotive force and a reluctance network. Its 2D maps and FEMM comparison make the result '
             'and its discretisation errors visible.'),
 'stylesheet': 'winding.css',
 'chapter_labels': {'takeaway': ('FEMM', 'FEMM')},
 'scope': ('Projet d’équipe · Python / PyQt5 / FEMM', 'Team project · Python / PyQt5 / FEMM'),
 'metrics': [('3', 'espaces : bobinage, FMM, flux', 'workspaces: winding, MMF, flux'),
             ('2D', 'coupe de la machine pour lire le champ', 'machine cross-section to inspect the field'),
             ('FEMM', 'comparaison des pics et des courbes signées', 'peak and signed-curve comparison')],
 'hero_image': ('winding-parameters-app.png',
                'Interface de configuration du bobinage avec paramètres, faisabilité et dessin triphasé du stator',
                'Winding setup interface with parameters, feasibility and a three-phase stator drawing',
                'Le point de départ : choisir le bobinage et voir immédiatement ses connexions.',
                'The starting point: choose a winding and immediately see its connections.'),
 'chapters': [{'id': 'problem',
               'title': ('Le problème : passer du bobinage à son effet physique',
                         'The problem: connect a winding to its physical effect'),
               'intro': ('Un dessin de bobinage ne suffit pas à comprendre le champ qu’il produit. L’objectif du '
                         'projet est de suivre cette relation dans un même outil : configurer, calculer puis '
                         'visualiser.',
                         'A winding drawing alone does not explain the field it produces. The project follows that '
                         'relationship in one tool: configure, calculate, then visualise.'),
               'paragraphs': [('Dans ce projet d’équipe, nous avons développé une application Python/PyQt5. La '
                               'première interface permet de choisir les encoches, les paires de pôles, le pas de '
                               'bobine et le nombre de couches. Elle vérifie la faisabilité du bobinage et dessine '
                               'la répartition signée des conducteurs dans le stator. Le dessin et le calcul '
                               'utilisent la même matrice de connexions ; chaque retour de bobine porte le '
                               'courant opposé au côté aller, au pas choisi.',
                               'In this team project, we developed a Python/PyQt5 application. The first interface '
                               'sets slots, pole pairs, coil span and layers. It checks winding feasibility and '
                               'draws the signed conductor arrangement. The drawing and calculation use the same '
                               'connection matrix; each coil return carries the opposite current at the selected span.'),
                              ('L’étude se poursuit avec les dimensions de la machine : rayons, entrefer et '
                               'géométrie des encoches. Le bobinage définit où se trouvent les conducteurs ; la '
                               'géométrie définit le chemin dans lequel le flux pourra circuler.',
                               'The study continues with machine dimensions: radii, air gap and slot geometry. The '
                               'winding defines conductor placement; the geometry defines the paths through which '
                               'flux can travel.')],
               'points': [],
               'image': ('winding-machine-app.png',
                         'Écran des dimensions de la machine avec aperçu de sa coupe',
                         'Machine-dimension screen with a cross-section preview',
                         'Après le bobinage, les dimensions donnent le cadre physique du calcul.',
                         'After winding setup, the dimensions define the physical domain of the calculation.')},
              {'id': 'method',
               'title': ('La solution : de la FMM au système à résoudre',
                         'The solution: from MMF to the system to solve'),
               'intro': ('Chaque étape prépare la suivante : les courants créent l’excitation, le maillage '
                         'représente la machine et le solveur relie les deux.',
                         'Each stage prepares the next: currents create excitation, the mesh represents the machine, '
                         'and the solver connects them.'),
               'flow': [('Calculer la force magnétomotrice — FMM',
                         'Calculate magnetomotive force — MMF',
                         'La matrice signée donne les ampères-tours par encoche. Leur cumul construit une fonction '
                         'de bobinage constante dans les dents et linéaire dans les encoches. La vue instantanée '
                         'applique les courants triphasés à l’angle électrique Wt ; la résultante est leur somme. '
                         'La vue des références de crête permet de comparer les formes de chaque phase.',
                         'The signed matrix gives the ampere-turns in each slot. Their cumulative sum builds a '
                         'winding function that is constant in teeth and linear across slots. The instantaneous '
                         'view applies the three-phase currents at electrical angle Wt; the resultant is their sum. '
                         'Peak-reference mode compares the individual phase shapes.'),
                        ('Découper la machine en cellules',
                         'Divide the machine into cells',
                         'Le maillage polaire représente le rotor, l’entrefer, les dents/encoches et la culasse. '
                         'Dimensions et matériaux donnent les réluctances entre cellules : elles décrivent la '
                         'résistance au passage du flux.',
                         'The polar mesh represents the rotor, air gap, teeth/slots and yoke. Dimensions and '
                         'materials determine reluctances between cells: how strongly each path opposes magnetic '
                         'flux.'),
                        ('Assembler et résoudre Ax = b',
                         'Assemble and solve Ax = b',
                         'A assemble les conductances magnétiques entre cellules ; b contient l’excitation répartie '
                         'dans la bande dents/encoches. La conservation du flux impose la somme des flux de '
                         'branches à chaque nœud. Un potentiel de référence fixe la jauge ; le solveur creux donne '
                         'les potentiels x, puis les flux signés sur les faces.',
                         'A assembles magnetic conductances between cells; b contains excitation distributed '
                         'through the tooth/slot band. Flux conservation balances branch fluxes at each node. '
                         'One reference potential fixes the gauge; the sparse solver gives cell potentials x '
                         'and then the signed face fluxes.')],
               'flow_images': {1: [('winding-mmf-app.png',
                                    'Interface FMM avec contributions des phases A, B, C et résultante',
                                    'MMF interface with phase A, B, C contributions and their resultant',
                                    'Cas commun aux nouvelles captures : 36 encoches, 4 pôles, double couche, pas '
                                    'de 9 encoches, N = 204, I = 2,8 A crête et Wt = 90°. Dans cette application, '
                                    'chaque couche reçoit I/2 ; N multiplie le courant de chaque côté occupé.',
                                    'Common case in the updated captures: 36 slots, 4 poles, double layer, '
                                    '9-slot span, N = 204, I = 2.8 A peak and Wt = 90°. This application assigns '
                                    'I/2 to each layer; N multiplies each occupied coil-side current.')],
                               2: [('winding-mesh-app.png',
                                    'Interface de maillage polaire de la machine, avec 8 640 cellules',
                                    'Machine polar-mesh interface with 8,640 cells',
                                    'Le maillage transforme la géométrie en un réseau calculable ; le réglage '
                                    'présenté comporte 8 640 cellules.',
                                    'The mesh turns geometry into a network that can be computed; the displayed '
                                    'setting contains 8,640 cells.')]},
               'paragraphs': [('Le calcul est un réseau de réluctances sur une grille polaire. Les réluctances '
                               'intègrent les chemins radiaux et angulaires ; les sources réparties sont cohérentes '
                               'avec le courant axial homogénéisé utilisé dans FEMM. NumPy organise les données et '
                               'SciPy résout le système creux par gradient conjugué préconditionné.',
                               'The calculation uses a reluctance network on a polar grid. Reluctances integrate '
                               'radial and angular paths; the distributed sources are consistent with the '
                               'homogenised axial slot current used in FEMM. NumPy organises the data and SciPy '
                               'solves the sparse system with preconditioned conjugate gradients.'),
                              ('Le résidu relatif du système est inférieur à 10⁻⁹ dans les trois cas comparés '
                               'ci-dessous. Cela vérifie la résolution du système discret, sans mesurer à lui '
                               'seul la fidélité du champ : celle-ci se vérifie par comparaison et raffinement.',
                               'The relative system residual is below 10⁻⁹ in the three cases compared below. '
                               'This checks the discrete-system solve; field accuracy still requires comparison '
                               'and refinement.')],
               'points': []},
              {'id': 'evidence',
               'title': ('Le résultat : du flux à une lecture en 2D', 'The result: from flux to a 2D interpretation'),
               'intro': ('Une fois les potentiels connus, l’application retrouve le flux Φ, puis l’induction '
                         'magnétique B. Les deux vues aident à comprendre où passe le flux et où le champ est le '
                         'plus intense.',
                         'Once potentials are known, the application derives flux Φ and then magnetic flux density '
                         'B. Two views show where flux travels and where the field is strongest.'),
               'flow': [('Déduire les flux entre cellules',
                         'Derive fluxes between cells',
                         'Les flux de faces servent à reconstruire le potentiel vecteur plan Az, avec continuité '
                         'angulaire périodique et potentiel constant sur les frontières isolantes. Les lignes '
                         'affichées sont des contours équidistants de Az : deux contours voisins délimitent le '
                         'même flux. Le nombre de lignes règle la lecture de la carte.',
                         'The face fluxes reconstruct planar vector potential Az, with periodic angular '
                         'continuity and constant potential on insulated boundaries. Displayed lines are '
                         'equally spaced Az contours: adjacent contours enclose the same flux. The line count '
                         'controls how the map is read.'),
                        ('Calculer B et afficher la carte',
                         'Calculate B and display the map',
                         'Les observations signées des faces opposées sont moyennées et rapportées aux sections '
                         'physiques pour obtenir Br et Bθ. « Solve field » affiche directement la carte de |B| '
                         'en teslas ; un clic dans la machine donne Br, Bθ et |B| dans la cellule choisie.',
                         'Signed observations from opposite faces are averaged and divided by their physical '
                         'areas to obtain Br and Bθ. “Solve field” directly displays the |B| map in tesla; '
                         'clicking inside the machine reports Br, Bθ and |B| for the selected cell.')],
               'flow_images': {1: [('winding-flux-lines-app.png',
                                    'Application affichant les lignes de flux sur la coupe 2D de la machine',
                                    'Application displaying flux lines on the 2D machine cross-section',
                                    'Contours de Az reconstruits à partir des flux de faces. Un intervalle de '
                                    'contour correspond au même flux ; le détail près des encoches dépend du maillage.',
                                    'Az contours reconstructed from face fluxes. Each contour interval represents '
                                    'the same flux; detail near slots depends on the mesh.')],
                               2: [('winding-b-map-app.png',
                                    'Carte de |B| avec contours de flux et lecture ponctuelle du champ en teslas',
                                    '|B| map with flux contours and point-value inspection in tesla',
                                    'Carte de |B| et lecture du champ par clic. Les statistiques « Air Gap » '
                                    'couvrent toutes les cellules de l’entrefer ; le tableau de validation '
                                    'utilise une seule couronne commune aux deux modèles.',
                                    '|B| map and point-value inspection. “Air Gap” statistics cover every '
                                    'air-gap cell; the validation table uses one shared sampling ring '
                                    'for both models.')]},
               'paragraphs': [('Les captures proviennent de l’application, avec un même jeu de paramètres. Le modèle '
                               'est une coupe 2D à perméabilités imposées ; la saturation n’est pas calculée. Une '
                               'interpolation dans les cellules préserve leurs flux de faces intégrés. La '
                               'comparaison FEMM ci-dessous contrôle le champ signé, sans constituer un essai '
                               'sur machine physique.',
                               'The captures come from the application using one parameter set. The model is a 2D '
                               'cross-section with prescribed permeabilities; saturation is not calculated. '
                               'Interpolation preserves integrated face fluxes. The FEMM comparison below checks '
                               'the signed field, without constituting a physical machine test.')],
               'points': []},
              {'id': 'takeaway',
               'title': ('Vérifier le champ avec FEMM', 'Check the field against FEMM'),
               'intro': ('Un pic bien reproduit ne garantit pas une courbe correcte. L’audit du 12 novembre '
                         '2026 compare les deux composantes signées du champ dans l’entrefer et documente '
                         'l’effet du maillage.',
                         'Matching a peak does not guarantee the right curve. The 12 November 2026 audit '
                         'compares both signed air-gap field components and documents the effect of mesh resolution.'),
               'paragraphs': [('La validation construit FEMM à partir du bobinage actif, des courants, de Wt, '
                               'des dimensions, des perméabilités et de la longueur axiale. Le calcul tourne '
                               'en arrière-plan ; les résultats apparaissent dans une fenêtre et FEMM reste '
                               'ouvert sur la solution, avec légende |B|, contours de flux et lecture des valeurs '
                               'par clic.',
                               'Validation builds FEMM from the active winding, currents, Wt, dimensions, '
                               'permeabilities and axial length. The solve runs in the background; a results '
                               'window appears and FEMM remains open on the solution, with its |B| legend, flux '
                               'contours and point-value inspection.'),
                              ('Les corrections ont porté sur le signe des retours de bobine, le placement '
                               'physique des sources, les réluctances radiales et la reconstruction de B sur '
                               'les faces opposées. Ce travail relie programmation, conservation du flux et '
                               'vérification numérique ; les écarts restants sont montrés au lieu d’être '
                               'résumés par le seul maximum.',
                               'Corrections addressed coil-return signs, physical source placement, radial '
                               'reluctances and B reconstruction from opposite faces. This connects programming, '
                               'flux conservation and numerical verification; remaining differences are shown '
                               'alongside the maximum.')],
               'validation': True,
               'references': [('Audit physique et commandes de reproduction', 'Physics audit and reproduction commands',
                               'https://github.com/KhalilEllahLAGHA/Winding-and-flux-analysis-program/blob/main/femm_validation/physics-audit.md')],
               'points': []}],
 'reports': None,
 'repo': 'https://github.com/KhalilEllahLAGHA/Winding-and-flux-analysis-program'},
    {'slug': 'dc-motor-cascade-control',
     'title': ('Commande en cascade d’un moteur à courant continu', 'Cascade control of a DC motor'),
     'eyebrow': ('04 / Automatique & conversion', '04 / Control & conversion'),
     'summary': ('À l’ENP d’Alger, j’ai conçu une commande de vitesse en cascade pour un moteur à courant continu. '
                 'J’ai d’abord modélisé l’entraînement par blocs, puis simulé le pont à thyristors et la machine '
                 'avec Simscape Electrical.',
                 'At ENP Algiers, I designed a cascade speed controller for a DC motor. I first modelled the drive '
                 'with Simulink blocks, then simulated the thyristor bridge and motor in Simscape Electrical.'),
     'scope': ('ENP d’Alger · Simulink / Simscape Electrical', 'ENP Algiers · Simulink / Simscape Electrical'),
     'metrics': [('2', 'boucles de régulation imbriquées', 'nested feedback loops'),
                 ('6', 'pulses du redresseur triphasé', 'pulses in the three-phase rectifier'),
                 ('220 V', 'point nominal étudié', 'studied nominal voltage')],
     'hero_image': ('dc-motor-cascade.svg',
                    'Architecture des deux boucles de commande en cascade',
                    'Block diagram of the two cascade-control loops',
                    'La boucle externe de vitesse fixe la consigne de courant.',
                    'The outer speed loop sets the current reference.'),
     'chapters': [{'id': 'problem',
                   'title': ('Régler la vitesse en agissant sur le courant', 'Controlling speed through armature current'),
                   'intro': ('Quand la charge augmente, le moteur doit produire davantage de couple pour tenir sa '
                             'vitesse. La boucle externe demande alors plus de courant d’induit et la boucle interne '
                             'agit sur le redresseur pour atteindre cette consigne.',
                             'When load increases, the motor needs more torque to hold its speed. The outer loop '
                             'requests more armature current and the inner loop drives the rectifier to reach that target.'),
                   'paragraphs': [('J’ai réglé le PI de vitesse et le PID de courant à partir du modèle de la machine. '
                                   'La boucle de courant répond sur une échelle de temps plus courte que la boucle de '
                                   'vitesse, ce qui laisse au courant le temps de suivre la demande de couple.',
                                   'I tuned the speed PI and current PID from the motor model. The current loop responds '
                                   'on a shorter time scale than the speed loop so that armature current can follow the '
                                   'torque demand.')],
                   'points': [('Actionneur',
                               'Pont triphasé commandé à thyristors.',
                               'Three-phase controlled thyristor bridge.'),
                              ('Boucle interne',
                               'Courant et couple, réponse rapide.',
                               'Current and torque, fast response.'),
                              ('Boucle externe',
                               'Vitesse et rejet des perturbations de charge.',
                               'Speed and load-disturbance rejection.')]},
                  {'id': 'method',
                   'title': ('Du schéma-blocs à Simscape Electrical', 'From block diagram to Simscape Electrical'),
                   'intro': ('J’ai conservé les deux boucles et leurs retours de mesure. J’ai remplacé le modèle moyen '
                             'de l’entraînement par un circuit qui calcule la tension d’induit à chaque commutation. '
                             'Les deux simulations suivent leurs scénarios d’origine, avec des échelons à des instants différents.',
                             'I kept the two feedback loops and replaced the averaged drive model with a circuit that '
                             'calculates armature voltage as the thyristors switch. Each simulation uses its original '
                             'scenario, with speed steps at different times.'),
                   'paragraphs': [('Les scripts MATLAB calculent les gains à partir des paramètres du moteur et des '
                                   'temps de réponse visés. Le rapport détaille le réglage analytique par compensation '
                                   'pôle–zéro.',
                                   'The MATLAB scripts calculate gains from the motor parameters and target response '
                                   'times. The report details the analytical pole-zero cancellation method.')],
                   'flow': [('Implémentation 1 · Blocs Simulink', 'Implementation 1 · Simulink blocks',
                             'Un bloc du premier ordre représente la tension moyenne du redresseur. Le sous-système '
                             'moteur relie cette tension au courant, puis le couple et la charge à la vitesse. Les '
                             'blocs permettent de suivre le trajet du signal entre les deux correcteurs.',
                             'A first-order block represents the rectifier’s average voltage. The motor subsystem '
                             'relates voltage to current, then motor and load torque to speed. The blocks make the '
                             'signal path through both controllers visible.'),
                            ('Implémentation 2 · Circuit Simscape Electrical', 'Implementation 2 · Simscape Electrical circuit',
                             'Dans Specialized Power Systems, la commande du PID de courant fixe l’angle d’amorçage '
                             'du pont. Un générateur synchronisé au réseau produit les six impulsions. Le pont à '
                             'thyristors et l’inductance de lissage alimentent la machine. Un capteur renvoie le '
                             'courant d’induit et le bloc moteur fournit la vitesse.',
                             'In Specialized Power Systems, the current PID output sets the bridge firing angle. '
                             'A generator synchronized to the AC supply produces the six firing pulses. The thyristor '
                             'bridge and smoothing inductor supply the motor. A sensor feeds back armature current '
                             'and the motor block provides speed.')],
                   'flow_images': {1: [('dc-motor-block-diagram.png',
                                        'Modèle Simulink par blocs avec PI de vitesse, PID de courant et modèle du moteur',
                                        'Block-based Simulink model with speed PI, current PID and motor model',
                                        'Dans la version par blocs, le redresseur est représenté par sa réponse moyenne.',
                                        'In the block-based version, the rectifier is represented by its average response.'),
                                       ('dc-motor-block-diagram-response.png',
                                        'Vitesse, courant d’induit et tension moyenne dans le modèle par blocs',
                                        'Speed, armature current and average voltage in the block-based model',
                                        'Dans ce scénario de 4 s, la consigne passe à 1 000, 3 000 et 1 500 tr/min '
                                        'à 1, 2 et 3 s, respectivement.',
                                        'In this 4 s scenario, the reference steps to 1,000, 3,000 and 1,500 rpm at '
                                        '1, 2 and 3 s, respectively.')],
                                   2: [('dc-motor-simscape-diagram.png',
                                        'Circuit Simscape avec source triphasée, pont à thyristors et moteur à courant continu',
                                        'Simscape circuit with three-phase supply, thyristor bridge and DC motor',
                                        'La version Simscape détaille les impulsions d’amorçage, le pont et les capteurs.',
                                        'The Simscape version models the firing pulses, bridge and sensors explicitly.')]}},
                  {'id': 'evidence',
                   'title': ('Les résultats dans Simscape', 'The Simscape results'),
                   'intro': ('Dans le scénario Simscape de 20 s, la consigne passe à 1 000 tr/min à 1 s, à 3 000 tr/min '
                             'à 5 s, puis à 1 500 tr/min à 10 s. La vitesse simulée atteint un maximum de 3 004,42 '
                             'tr/min et termine à 1 499,95 tr/min.',
                             'In the 20 s Simscape scenario, the reference steps to 1,000 rpm at 1 s, 3,000 rpm at '
                             '5 s, and 1,500 rpm at 10 s. The simulated speed peaks at 3,004.42 rpm and ends '
                             'at 1,499.95 rpm.'),
                   'image': ('dc-motor-simscape-response.png',
                             'Vitesse, courant d’induit et couple électromagnétique simulés dans Simscape',
                             'Speed, armature current and electromagnetic torque simulated in Simscape',
                             'La consigne de courant atteint 7 A et le courant d’induit mesuré dans le modèle '
                             'culmine à 7,07 A.',
                             'The current reference reaches 7 A and the measured armature current in the model '
                             'peaks at 7.07 A.'),
                   'extra_images': [('dc-motor-simscape-rectification.png',
                                     'Tension continue du pont et courant d’induit sur une période réseau',
                                     'Bridge DC voltage and armature current over one AC supply cycle',
                                     'Zoom sur une période réseau de 20 ms à 3 000 tr/min de consigne. La tension est '
                                     'mesurée à la sortie continue du pont, en amont de l’inductance de lissage. '
                                     'Le courant d’induit varie de 0,17 A sur cette fenêtre.',
                                     'A 20 ms supply cycle at a 3,000 rpm command. Voltage is measured at the bridge’s '
                                     'DC output, upstream of the smoothing inductor. Armature current varies by '
                                     '0.17 A over this window.')]},
                  {'id': 'takeaway',
                   'title': ('Le réglage vérifié dans Python', 'Cross-checking the tuning in Python'),
                   'intro': ('J’ai aussi reproduit le calcul des gains en NumPy et SciPy. Le modèle moyen permet de '
                             'balayer les temps de réponse et de voir leur influence sur le dépassement et le temps '
                             'd’établissement.',
                             'I also reproduced the gain calculations in NumPy and SciPy. The averaged model lets '
                             'me vary the response targets and see how they affect overshoot and settling time.'),
                   'image': ('dc-motor-response.png',
                             'Réponse nominale de la cascade calculée avec le modèle moyen dans Python',
                             'Nominal cascade response calculated with the averaged model in Python',
                             'Résultat Python au point de fonctionnement étudié de 220 V et 3 000 tr/min.',
                             'Python result at the studied 220 V, 3,000 rpm operating point.')}],
     'reports': ('../reports/dc-motor-cascade-control-report.pdf', '../reports/dc-motor-cascade-control-report-en.pdf'),
     'repo': 'https://github.com/KhalilEllahLAGHA/DC-motor-cascade-control'},
    {'slug': 'mlp-backpropagation',
     'title': ('Réseau de neurones codé à la main', 'A neural network built from scratch'),
     'eyebrow': ('05 / Intelligence artificielle', '05 / Artificial intelligence'),
     'summary': ('Comprendre comment un réseau apprend : dans ce TP réalisé à deux, nous avons écrit le calcul de la '
                 'sortie et la rétropropagation sous MATLAB, sans toolbox.',
                 'Understand how a network learns: in this two-person lab, we wrote the forward calculation and '
                 'backpropagation in MATLAB without a toolbox.'),
     'scope': ('TP d’équipe de deux · MATLAB', 'Two-person academic lab · MATLAB'),
     'metrics': [('2', 'versions de la propagation', 'propagation implementations'),
                 ('1', 'couche cachée étudiée', 'hidden layer studied'),
                 ('0', 'toolbox de réseaux de neurones', 'neural-network toolboxes')],
     'hero_image': ('mlp-network.svg',
                    'Schéma du perceptron multicouche à une couche cachée',
                    'One-hidden-layer multilayer perceptron diagram',
                    'Les poids relient entrée, couche cachée et sortie.',
                    'Weights connect input, hidden layer and output.'),
     'chapters': [{'id': 'problem',
                   'title': ('Le problème : comprendre la correction des paramètres',
                             'The problem: understand parameter updates'),
                   'intro': ('Un appel à une toolbox peut entraîner un modèle sans montrer comment chaque poids est '
                             'modifié. Ce TP d’intelligence artificielle reconstruit le chemin complet de '
                             'l’apprentissage.',
                             'A toolbox call can train a model without showing how each weight changes. This AI lab '
                             'reconstructs the complete learning path.'),
                   'paragraphs': [('Le projet a été réalisé en binôme à l’ENP. Le perceptron multicouche possède une '
                                   'couche cachée et utilise une activation sigmoïde. Le programme choisit un jeu de '
                                   'données, effectue la propagation avant, calcule l’erreur de sortie et rétropropage '
                                   'le gradient jusqu’aux poids.',
                                   'This ENP project was completed by two students. The multilayer perceptron has one '
                                   'hidden layer and sigmoid activation. The program selects a data set, performs '
                                   'forward propagation, computes output error and backpropagates gradients to the '
                                   'weights.'),
                                  ('Le critère d’arrêt porte sur l’erreur de sortie ; l’exécution présente la sortie '
                                   'finale, les poids appris et le nombre d’itérations. Les petits jeux de données '
                                   'servent à comprendre le comportement de l’algorithme plutôt qu’à annoncer une '
                                   'performance industrielle.',
                                   'Stopping is based on output error; a run shows final output, learned weights and '
                                   'iteration count. Small teaching data sets help explain the algorithm rather than '
                                   'support industrial-performance claims.')],
                   'points': [('Entrée',
                               'Jeux d’apprentissage simples et classification binaire.',
                               'Small training sets and binary classification.'),
                              ('Calcul',
                               'Sigmoïde, erreur, gradient, mise à jour des poids.',
                               'Sigmoid, error, gradient and weight updates.'),
                              ('Lecture',
                               'Sortie finale, poids et nombre d’itérations.',
                               'Final output, weights and iteration count.')]},
                  {'id': 'method',
                   'title': ('Deux chemins vers le même gradient', 'Two paths to the same gradient'),
                   'intro': ('La première version privilégie des boucles pédagogiques. La seconde emploie le calcul '
                             'matriciel vectorisé et met aussi à jour les biais.',
                             'The first version favours explicit teaching loops. The second uses vectorised matrix '
                             'operations and also updates biases.'),
                   'paragraphs': [('Cette duplication volontaire aide à suivre les dimensions des vecteurs, les dérivées '
                                   'de la sigmoïde et la circulation de l’erreur d’une couche à l’autre. Elle montre '
                                   'également comment la même logique peut s’exprimer de manière plus compacte en '
                                   'MATLAB.',
                                   'This deliberate duplication helps track vector dimensions, sigmoid derivatives and '
                                   'error flow from layer to layer. It also shows how the same logic can be written more '
                                   'compactly in MATLAB.'),
                                  ('Un mode d’apprentissage en ligne conserve les poids entre exemples successifs. Les '
                                   'fichiers sont séparés entre sélection des données, boucle d’apprentissage, '
                                   'propagation et rétropropagation, afin que chaque étape puisse être étudiée '
                                   'isolément.',
                                   'An online-learning mode carries weights between successive examples. Files separate '
                                   'data selection, training loop, forward propagation and backpropagation so each stage '
                                   'can be inspected independently.')],
                   'points': [('Version 1',
                               'Boucles explicites pour suivre chaque opération.',
                               'Explicit loops for following each operation.'),
                              ('Version 2',
                               'Produits matriciels vectorisés et mise à jour des biais.',
                               'Vectorised matrix products and bias updates.'),
                              ('Organisation',
                               'Fonctions distinctes pour données, propagation et apprentissage.',
                               'Separate functions for data, propagation and learning.')],
                   'image': ('mlp-sequential-training.png',
                             'Illustration de l’apprentissage séquentiel du perceptron',
                             'Illustration of sequential perceptron training',
                             'L’apprentissage en ligne conserve l’état des poids d’un exemple à l’autre.',
                             'Online training carries the weights from one example to the next.'),
                   'flow': [('Présenter un exemple',
                             'Present an example',
                             'Les entrées et la réponse attendue définissent ce que le réseau doit apprendre.',
                             'Inputs and the expected response define what the network should learn.'),
                            ('Calculer une sortie',
                             'Calculate an output',
                             'Les couches combinent les entrées avec les poids et les biais.',
                             'The layers combine inputs with weights and biases.'),
                            ('Faire remonter l’erreur',
                             'Backpropagate error',
                             'La rétropropagation indique comment chaque paramètre contribue à l’écart.',
                             'Backpropagation indicates how each parameter contributes to the error.'),
                            ('Corriger et vérifier',
                             'Update and check',
                             'Les paramètres sont ajustés, puis les exemples sont rejoués pour observer l’apprentissage.',
                             'Parameters are updated, then examples are repeated to observe learning.')]},
                  {'id': 'evidence',
                   'title': ('Observer l’apprentissage', 'Watch learning happen'),
                   'intro': ('Le rapport présente la base d’essai, les équations et l’évolution de l’erreur. Le code a '
                             'été corrigé puis testé sous MATLAB R2024b avant publication open source.',
                             'The report presents the teaching data, equations and error evolution. The code was '
                             'corrected and tested in MATLAB R2024b before its open-source publication.'),
                   'paragraphs': [('La courbe de convergence illustre l’amélioration de l’erreur pendant l’entraînement. '
                                   'Elle documente ce jeu de données et ce paramétrage ; elle ne doit pas être lue comme '
                                   'une mesure de généralisation sur des données inconnues.',
                                   'The convergence curve illustrates training-error reduction. It documents this data '
                                   'set and configuration; it is not a generalisation measure on unseen data.'),
                                  ('Le dépôt public conserve les fonctions MATLAB et la licence MIT. Le rapport du TP '
                                   'reste la meilleure entrée pour relier équations, choix d’implémentation et figures.',
                                   'The public repository contains MATLAB functions under the MIT licence. The lab '
                                   'report is the best entry point for connecting equations, implementation choices and '
                                   'figures.')],
                   'points': [],
                   'image': ('mlp-convergence.png',
                             'Courbe de convergence de l’erreur pendant l’apprentissage',
                             'Training-error convergence chart',
                             'La convergence visualise le calcul itératif, sans prétendre mesurer la généralisation.',
                             'Convergence visualises iteration without claiming generalisation.')},
                  {'id': 'takeaway',
                   'title': ('Ce que démontre le TP', 'What the lab demonstrates'),
                   'intro': ('La rétropropagation n’est pas ici un mot-clé : chaque transformation et mise à jour est '
                             'visible dans le code.',
                             'Backpropagation is not merely a keyword here: every transform and update is visible in the '
                             'code.'),
                   'paragraphs': [('C’est une preuve de compréhension des fondements d’un MLP, dans un cadre académique. '
                                   'Le projet ne revendique ni modèle profond à grande échelle ni déploiement en '
                                   'production.',
                                   'It demonstrates understanding of MLP fundamentals in an academic setting. The '
                                   'project makes no claim of large-scale deep learning or production deployment.')],
                   'points': []}],
     'reports': ('../reports/mlp-backpropagation-report.pdf', '../reports/mlp-backpropagation-report-en.pdf'),
     'repo': 'https://github.com/KhalilEllahLAGHA/mlp-backpropagation-matlab'},
    {'slug': 'power-electronics-labs',
     'title': ('Travaux pratiques d’électronique de puissance', 'Power electronics laboratory work'),
     'eyebrow': ('06 / Conversion de puissance', '06 / Power conversion'),
     'summary': ('Comprendre ce qu’un convertisseur fait réellement : trois TP collectifs confrontent le comportement '
                 'attendu des redresseurs aux simulations et aux formes d’onde relevées sur banc.',
                 'Understand what a converter actually does: three team labs compare expected rectifier behaviour with '
                 'simulations and bench waveforms.'),
     'scope': ('Travaux pratiques académiques · ENP · rapports d’origine', 'Academic lab work · ENP · original reports'),
     'metrics': [('3', 'rapports de TP d’origine', 'original lab reports'),
                 ('AC → DC', 'conversion étudiée', 'conversion studied'),
                 ('V · A', 'tension et courant observés', 'observed voltage and current')],
     'hero_image': ('power-electronics-bridge-diodes.jpg',
                    'Schéma du redresseur triphasé à diodes tiré du compte rendu d’origine',
                    'Three-phase diode bridge diagram from the original lab report',
                    'Un schéma étudié dans les comptes rendus originaux.',
                    'A circuit studied in the original lab reports.'),
     'chapters': [{'id': 'problem',
                   'title': ('Le problème : expliquer la forme des tensions et des courants',
                             'The problem: explain voltage and current waveforms'),
                   'intro': ('Le passage du courant alternatif au continu se lit dans un schéma, une équation et une '
                             'forme d’onde mesurée. Ces TP rassemblent ces vues pour comprendre les écarts entre idéal '
                             'et réel.',
                             'AC-to-DC conversion can be read through a circuit, an equation and a measured waveform. '
                             'These labs bring those views together to understand gaps between ideal and real '
                             'behaviour.'),
                   'paragraphs': [('Les séances portent sur un redresseur triphasé à diodes, un pont mixte monophasé à '
                                   'diodes et thyristors, puis les effets du lissage et de l’empiètement de commutation. '
                                   'Les rapports d’origine documentent les montages, grandeurs attendues et '
                                   'observations.',
                                   'The sessions cover a three-phase diode rectifier, a single-phase semi-controlled '
                                   'diode/thyristor bridge, then smoothing and commutation overlap. The original reports '
                                   'document setups, expected quantities and observations.'),
                                  ('Ce sont des travaux pratiques académiques, menés avec les groupes indiqués dans les '
                                   'comptes rendus. Je présente ici ce que les rapports démontrent sans attribuer à une '
                                   'seule personne l’ensemble des mesures ou de la rédaction collective.',
                                   'These are academic labs completed with the groups named in the reports. This page '
                                   'explains what the reports demonstrate without attributing all measurements or group '
                                   'writing to one person.')],
                   'points': [('Redressement',
                               'Chemin du courant dans les topologies à diodes et thyristors.',
                               'Current paths in diode and thyristor topologies.'),
                              ('Commande',
                               'Effet de l’angle d’amorçage sur un pont mixte.',
                               'Effect of firing angle in a semi-controlled bridge.'),
                              ('Qualité',
                               'Lissage, ondulation et empiètement de commutation.',
                               'Smoothing, ripple and commutation overlap.')]},
                  {'id': 'method',
                   'title': ('Du calcul à la forme d’onde', 'From calculation to waveform'),
                   'intro': ('Les trois manipulations confrontent calculs et observations sur banc. Les deux premières '
                             'ajoutent une simulation MATLAB/Simulink pour compléter la comparaison.',
                             'All three experiments compare calculations with bench observations. The first two also use '
                             'MATLAB/Simulink simulations for a further comparison.'),
                   'paragraphs': [('Pour le pont triphasé, le schéma de conduction explique la succession des diodes '
                                   'actives et la tension redressée. Pour le pont mixte monophasé, les thyristors '
                                   'ajoutent une variable de commande : l’angle d’amorçage change la tension moyenne et '
                                   'la forme d’onde.',
                                   'For the three-phase bridge, conduction paths explain the active diode sequence and '
                                   'rectified voltage. In the single-phase semi-controlled bridge, thyristors add a '
                                   'control variable: firing angle changes average voltage and waveform.'),
                                  ('La troisième étude suit l’effet d’une inductance de lissage et de la commutation non '
                                   'instantanée. Elle relie le comportement théorique du montage aux mesures faites sur '
                                   'le banc et à l’oscilloscope.',
                                   'The third study examines smoothing inductance and non-instantaneous commutation. It '
                                   'connects theoretical circuit behaviour with bench and oscilloscope measurements.')],
                   'points': [('Prévoir',
                               'Déduire la tension et les séquences de conduction.',
                               'Derive voltage and conduction sequences.'),
                              ('Simuler',
                               'Pour les deux premiers TP, reproduire le montage dans MATLAB/Simulink.',
                               'For the first two labs, reproduce the circuit in MATLAB/Simulink.'),
                              ('Mesurer',
                               'Comparer les formes d’onde au banc de TP.',
                               'Compare waveforms at the lab bench.')],
                   'image': ('power-electronics-lab-waveform.jpg',
                             'Forme d’onde issue des mesures du TP d’électronique de puissance',
                             'Waveform from the power-electronics laboratory report',
                             'La mesure donne une lecture concrète des effets de conversion.',
                             'Measurement makes conversion effects tangible.'),
                   'flow': [('Lire la topologie',
                             'Read the topology',
                             'Identifier les composants qui conduisent à chaque instant.',
                             'Identify the devices conducting at each instant.'),
                            ('Prévoir la réponse',
                             'Predict the response',
                             'Relier la conduction à la tension moyenne et à l’ondulation attendues.',
                             'Connect conduction to expected average voltage and ripple.'),
                            ('Confronter',
                             'Compare',
                             'Pour les deux premiers TP, rapprocher calcul, simulation et relevés de banc.',
                             'For the first two labs, compare calculations, simulation and bench records.'),
                            ('Expliquer les écarts',
                             'Explain differences',
                             'Examiner le lissage, les défauts et la commutation plutôt que seulement comparer deux '
                             'courbes.',
                             'Examine smoothing, faults and commutation rather than only comparing two traces.')]},
                  {'id': 'evidence',
                   'title': ('Trois comptes rendus à parcourir', 'Three reports to explore'),
                   'intro': ('Les trois PDF publiés sont les rapports d’origine du projet. Ils sont conservés tels '
                             'quels, avec leurs schémas, simulations, relevés et conclusions.',
                             'The three published PDFs are the original project reports. They are preserved as they '
                             'were, with circuits, simulations, measurements and conclusions.'),
                   'paragraphs': [('Le premier décrit le redressement triphasé à diodes. Le deuxième traite du pont '
                                   'mixte monophasé. Le troisième analyse lissage et empiètement anodique. Ensemble, ils '
                                   'montrent comment passer d’une topologie de conversion à des grandeurs vérifiables.',
                                   'The first covers three-phase diode rectification. The second studies the '
                                   'single-phase semi-controlled bridge. The third examines smoothing and commutation '
                                   'overlap. Together they show how to move from converter topology to checkable '
                                   'quantities.'),
                                  ('Les résultats restent ceux de séances pédagogiques ; ils ne constituent ni un '
                                   'produit industriel ni une qualification d’équipement.',
                                   'The results belong to teaching labs; they are neither an industrial product nor an '
                                   'equipment qualification.')],
                   'points': [('P3 / PD3',
                               'Dans le premier TP, environ 160 V à 3 A et 31,25 % d’ondulation en simple voie, contre '
                               '310 V à 3 A et 4,83 % en double voie.',
                               'In the first lab, about 160 V at 3 A with 31.25% ripple for the single-way arrangement, '
                               'versus 310 V at 3 A with 4.83% ripple for the bridge.'),
                              ('Pont mixte',
                               'Deux thyristors et deux diodes : la tension moyenne mesurée passe d’environ 230 V à 55 V '
                               'lorsque l’angle passe de 0,07π à 2π/3.',
                               'Two thyristors and two diodes: measured average voltage falls from about 230 V to 55 V '
                               'as firing angle changes from 0.07π to 2π/3.'),
                              ('Commutation',
                               'Dans le troisième TP, la tension moyenne en simple voie passe de 156 V à 1,5 A à 151 V à '
                               '7 A. Ces valeurs restent celles du montage étudié.',
                               'In the third lab, single-way mean voltage falls from 156 V at 1.5 A to 151 V at 7 A. '
                               'These values apply to the documented setup.')],
                   'image': ('power-electronics-commutation.jpg',
                             'Tensions des ponts supérieur et inférieur mesurées à l’oscilloscope dans le troisième TP',
                             'Oscilloscope measurements of the upper and lower bridge voltages in the third lab',
                             'Troisième TP : visualisation des tensions des deux demi-ponts et de la commutation.',
                             'Third lab: measured half-bridge voltages and commutation behaviour.')},
                  {'id': 'takeaway',
                   'title': ('Pourquoi ces TP comptent', 'Why these labs matter'),
                   'intro': ('Ils donnent une base concrète pour lire les convertisseurs : suivre les composants qui '
                             'conduisent, anticiper l’effet de la commande et confronter calcul, simulation et banc.',
                             'They provide a concrete basis for reading converters: trace conducting devices, predict '
                             'control effects and compare calculation, simulation and bench data.'),
                   'paragraphs': [('Les liens ci-dessous pointent uniquement vers les trois rapports d’origine déjà '
                                   'publiés.',
                                   'The links below point only to the three original reports already published.')],
                   'points': []}],
     'reports': None,
     'extra_reports': [('../reports/tp-redressement-triphase-diodes.pdf',
                        'Redressement triphasé à diodes',
                        'Three-phase diode rectifier'),
                       ('../reports/tp-pont-mixte-monophase.pdf',
                        'Pont mixte monophasé',
                        'Single-phase semi-controlled bridge'),
                       ('../reports/tp-redressement-lissage-commutation.pdf',
                        'Lissage et commutation',
                        'Smoothing and commutation')],
     'repo': None},
]


def clean(value):
    return escape(str(value), quote=True)


def translated(pair):
    return f'<span lang="fr">{clean(pair[0])}</span><span lang="en">{clean(pair[1])}</span>'


def asset_version(filename):
    """Refresh hosted CSS/JS when their content changes, including repeat builds."""
    content = (Path(__file__).resolve().parent / filename).read_bytes().replace(b'\r\n', b'\n')
    return sha256(content).hexdigest()[:12]


CHAPTER_LABELS = {
    "problem": ("Contexte", "Problem"),
    "method": ("Méthode", "Method"),
    "evidence": ("Résultats", "Results"),
    "takeaway": ("Bilan", "Takeaways"),
}


IMAGE_SIZES = {
    "dc-motor-cascade.svg": (1200, 500), "dc-motor-response.png": (1920, 819),
    "dc-motor-block-diagram.png": (4293, 1888), "dc-motor-simscape-diagram.png": (5521, 2050),
    "dc-motor-block-diagram-response.png": (1508, 1104),
    "dc-motor-simscape-response.png": (1515, 1104), "dc-motor-simscape-rectification.png": (1515, 770),
    "foc-control.svg": (1100, 760), "foc-speed-tracking.png": (1350, 690),
    "foc-response-context.png": (1875, 1785), "foc-simscape-scopes.png": (2133, 1258),
    "foc-simscape-speed.png": (1190, 692),
    "foc-simscape-drive-torque.png": (1168, 690),
    "foc-simscape-phase.png": (1156, 666),
    "foc-simscape-dq.png": (1168, 691),
    "foc-simscape-torque.png": (1392, 713),
    "foc-simscape-voltage-7seg.png": (1566, 1071),
    "foc-simscape-voltage-4seg.png": (1566, 1071),
    "foc-simscape-carrier-slow.png": (1819, 1445),
    "grid-interface.png": (1915, 1003), "grid-loadflow-iterations.png": (1406, 656),
    "grid-transient-stability.png": (1406, 656), "mlp-convergence.png": (1152, 640),
    "mlp-network.svg": (1200, 560), "mlp-sequential-training.png": (1152, 544),
    "power-electronics-bridge-diodes.jpg": (1076, 328),
    "power-electronics-lab-waveform.jpg": (764, 627),
    "power-electronics-commutation.jpg": (1200, 904),
    "pemfc-bench.png": (1219, 829), "pemfc-holdout.png": (4380, 2460),
    "winding-flux-heatmap.png": (1152, 720), "winding-flux-lines.png": (1152, 720),
    "winding-mmf.png": (4644, 2070),
    "winding-parameters-app.png": (1680, 1050),
    "winding-machine-app.png": (1680, 1050),
    "winding-mmf-app.png": (1680, 1050),
    "winding-mesh-app.png": (1680, 1050),
    "winding-flux-lines-app.png": (1680, 1050),
    "winding-b-map-app.png": (1680, 1050),
    "winding-femm-convergence.png": (1500, 920),
    "winding-femm-profiles.png": (1600, 1040),

}


def image(path, alt_fr, alt_en, *, eager=False):
    digest = sha256((Path(__file__).resolve().parent.parent / 'assets/projects' / path).read_bytes()).hexdigest()[:12]
    source = f"../assets/projects/{clean(path)}?v={digest}"
    width, height = IMAGE_SIZES[path]
    return (
        f'<a class="figure-link" href="{source}" target="_blank" rel="noopener" '
        f'aria-label="{clean(alt_fr)} — Ouvrir l’image en grand" '
        f'data-label-fr="{clean(alt_fr)} — Ouvrir l’image en grand" '
        f'data-label-en="{clean(alt_en)} — View full-size image">'
        f'<img src="{source}" alt="{clean(alt_fr)}" '
        f'data-alt-fr="{clean(alt_fr)}" data-alt-en="{clean(alt_en)}" '
        f'width="{width}" height="{height}" '
        f'loading="{"eager" if eager else "lazy"}" '
        f'{"fetchpriority=\"high\"" if eager else "decoding=\"async\""}>'
        '<span class="figure-zoom" aria-hidden="true">'
        + translated(("Toucher pour agrandir ↗", "Tap to enlarge ↗")) + '</span></a>'
    )


def figure(spec, *, hero=False):
    path, alt_fr, alt_en, caption_fr, caption_en = spec
    picture = image(path, alt_fr, alt_en, eager=hero)
    if hero:
        return (
            '<figure class="hero-art">' + picture +
            '<figcaption><span>' + translated((caption_fr, caption_en)) +
            '</span><small>FIG. 01</small></figcaption></figure>'
        )
    preserve_aspect = (path == 'foc-response-context.png'
                       or path.startswith('dc-motor-block-diagram')
                       or path.startswith('dc-motor-simscape-')
                       or path.startswith('foc-simscape-')
                       or (path.startswith('winding-') and path.endswith('-app.png'))
                       or path.startswith('winding-femm-'))
    figure_class = 'figure figure-context' if preserve_aspect else 'figure'
    return (
        f'<figure class="{figure_class}">' + picture +
        '<figcaption><strong>FIGURE</strong><span>' + translated((caption_fr, caption_en)) +
        '</span></figcaption></figure>'
    )


def artifact_links(page):
    links = []
    if page.get("reports"):
        fr, en = page["reports"]
        download = f' download="{clean(page["report_download"])}"' if page.get("report_download") else ''
        links.append(
            f'<a class="report-link" data-fr="{clean(fr)}" data-en="{clean(en)}" '
            f'href="{clean(fr)}" target="_blank" rel="noopener"{download}>'
            + translated(page.get("report_label", ("Lire le rapport complet · PDF", "Read the full report · PDF"))) + '</a>'
        )
    for url, label_fr, label_en in page.get("extra_reports", []):
        links.append(f'<a href="{clean(url)}" target="_blank" rel="noopener">{translated((label_fr, label_en))} · PDF</a>')
    if page.get("repo"):
        links.append(f'<a href="{clean(page["repo"])}" target="_blank" rel="noopener">{translated(("Explorer le code", "Explore the code"))} · GitHub</a>')
    return '<div class="artifact-row">' + ''.join(links) + '</div>' if links else ''


LABEL_EN = {
    "Données": "Inputs", "Matrices": "Matrices", "Question": "Question", "Machine": "Motor",
    "Orientation": "Orientation", "Alimentation": "Supply", "Bobinage": "Winding",
    "Connexions": "Connections", "Cohérence": "Consistency", "FMM": "MMF",
    "Maillage": "Mesh", "Solveur": "Solver", "Actionneur": "Actuator",
    "Boucle interne": "Inner loop", "Boucle externe": "Outer loop", "Modéliser": "Model",
    "Régler": "Tune", "Recouper": "Cross-check", "Entrée": "Inputs", "Calcul": "Calculation",
    "Lecture": "Readout", "Version 1": "Version 1", "Version 2": "Version 2",
    "Organisation": "Structure", "Redressement": "Rectification", "Commande": "Control",
    "Qualité": "Waveform quality", "Prévoir": "Predict", "Simuler": "Simulate", "Mesurer": "Measure",
    "Pont mixte": "Semi-controlled bridge",
    "Objectif": "Goal", "Flux": "Flux", "Couple": "Torque",
}


def winding_validation():
    """Measured 2026-11-12 audit results, not acceptance thresholds.

    Presets: physics-audit-corrected-{low,mid,high}/physics_comparison.json.
    Refined reference: physics-audit-high-fine-reference/physics_comparison.json
    and physics-audit-extra-fine/convergence.json. Radial order is rotor,
    air gap, tooth/slot band, yoke; angular counts use the 5-degree slot case.
    """
    def table(rows, caption, label):
        headers = [
            ('Maillage réseau', 'Network mesh'),
            ('Couches radiales', 'Radial layers'),
            ('Grille angulaire', 'Angular grid'),
            ('Cellules', 'Cells'),
            ('Écart du pic |Br|', 'Peak |Br| error'),
            ('Erreur Br signée', 'Signed Br error'),
            ('Erreur Bθ signée', 'Signed Bθ error'),
        ]
        body = []
        for name, layers, angles, cells, peak, br, btheta in rows:
            def percent(value, places):
                number = f'{value:.{places}f}'
                return translated((number.replace('.', ',') + ' %', number + '%'))
            values = [clean(layers), clean(angles), clean(cells),
                      percent(peak, 3) if peak is not None else '—',
                      percent(br, 2), percent(btheta, 2)]
            body.append('<tr><th scope="row">' + translated(name) + '</th>'
                        + ''.join('<td>' + value + '</td>' for value in values) + '</tr>')
        return (
            '<p class="winding-table-hint">'
            + translated(('Faire défiler le tableau pour voir toutes les valeurs →',
                          'Scroll the table to see all values →')) + '</p>'
            '<div class="winding-table-scroll" role="region" tabindex="0" '
            f'aria-label="{clean(label[0])}" data-label-fr="{clean(label[0])}" '
            f'data-label-en="{clean(label[1])}"><table class="winding-table">'
            '<caption>' + translated(caption) + '</caption><thead><tr>'
            + ''.join('<th scope="col">' + translated(h) + '</th>' for h in headers)
            + '</tr></thead><tbody>' + ''.join(body) + '</tbody></table></div>'
        )

    presets = [
        (('Bas', 'Low'), '3 / 5 / 3 / 3', '72 · 5° · d=1', '1 008',
         0.2678520956779109, 14.07514663173804, 33.30397508655229),
        (('Moyen', 'Mid'), '10 / 10 / 10 / 10', '216 · 1.667° · d=3', '8 640',
         0.06732397429058047, 7.560621009583911, 43.32410848275632),
        (('Haut', 'High'), '20 / 30 / 20 / 20', '720 · 0.5° · d=10', '64 800',
         0.033006160322406226, 2.7344774684462463, 12.142890485828302),
    ]
    refined = [
        (('Haut', 'High'), '20 / 30 / 20 / 20', '720 · 0.5° · d=10', '64 800',
         0.007755132909209209, 2.685158636287719, 12.009316433074101),
        (('Raffinement supplémentaire', 'Additional refinement'),
         '40 / 60 / 40 / 40', '1 440 · 0.25° · d=20', '259 200',
         None, 0.9041802548068536, 5.322068554021697),
    ]
    case = (
        'Cas comparé : 36 encoches, 4 pôles, pas 9, double couche, 204 spires, '
        'I = 2,8 A crête, Wt = 90°, ouverture d’encoche 5°, entrefer 1 mm et longueur axiale 110 mm. '
        'Les deux modèles imposent μr = 4 000 dans le fer, un courant axial homogénéisé dans les encoches '
        'et un flux normal nul au rayon d’arbre et à la frontière externe.',
        'Compared case: 36 slots, 4 poles, span 9, double layer, 204 turns, '
        'I = 2.8 A peak, Wt = 90°, 5° slot opening, 1 mm air gap and 110 mm axial length. '
        'Both models prescribe iron μr = 4,000, homogenised axial slot current '
        'and zero normal flux at the shaft radius and outer boundary.',
    )
    definitions = (
        'Pour chaque composante B, l’erreur de courbe est le RMS de (Bréseau − BFEMM) divisé par le RMS '
        'de BFEMM, sur tous les échantillons signés. C’est la norme L2 normalisée : les signes et les '
        'écarts locaux comptent, y compris près de zéro. L’écart du pic compare seulement les maxima '
        'de |Br| ; il ne mesure pas la forme de la courbe.',
        'For each component B, curve error is RMS(Bnetwork − BFEMM) divided by RMS(BFEMM), '
        'over all signed samples. This is the normalised L2 error: polarity and local differences '
        'count, including near zero. Peak error compares only the maxima of |Br|; '
        'it does not measure curve shape.',
    )
    sampling = (
        'Dans chaque comparaison, FEMM et le réseau sont échantillonnés aux mêmes rayons et angles '
        'd’une couronne proche du milieu de l’entrefer. Le nombre de points est celui des cellules '
        'angulaires. Entre les préréglages, ces points et le rayon de la couronne peuvent changer : '
        'ce tableau documente les réglages réels de l’application, sans constituer une étude à '
        'échantillonnage fixe. Ordre des couches radiales : rotor / entrefer / dents-encoches / culasse. '
        'Grille angulaire : nombre de cellules · pas Δθ · diviseur d.',
        'Within each comparison, FEMM and the network use identical radii and angles on a ring '
        'near the middle of the air gap. The point count equals the angular cell count. '
        'Across presets, those locations and the selected ring radius can change: this table '
        'documents actual application settings rather than a fixed-sample convergence study. '
        'Radial-layer order: rotor / air gap / tooth-slot band / yoke. '
        'Angular grid: cell count · step Δθ · divider d.',
    )
    findings = (
        'Le maillage moyen reproduit le pic à 0,067 %, mais son erreur de courbe est de 7,56 % '
        'sur Br et 43,32 % sur Bθ. Le maillage haut réduit ces erreurs à 2,73 % et 12,14 %. '
        'L’erreur Bθ n’est pas monotone entre les trois préréglages ; le maximum seul masquerait '
        'les écarts locaux près des bords d’encoches.',
        'The mid mesh matches the peak within 0.067%, but its curve errors are 7.56% '
        'for Br and 43.32% for Bθ. The high mesh reduces these to 2.73% and 12.14%. '
        'Bθ error is not monotonic across the three presets; the peak alone would hide '
        'local differences near slot edges.',
    )
    refinement = (
        'La référence FEMM standard utilise des segments d’arc de 1° et une taille de maille '
        'd’entrefer égale à entrefer/4. Une référence distincte plus fine utilise 0,25° et '
        'entrefer/12. Les deux lignes ci-dessous utilisent cette référence affinée ; les '
        'valeurs du réseau à 259 200 cellules sont interpolées aux positions fixes de la '
        'référence à 720 points. L’écart du pic n’a pas été enregistré pour ce dernier calcul.',
        'The standard FEMM reference uses 1° arc segments and air-gap mesh size gap/4. '
        'A separate finer reference uses 0.25° and gap/12. Both rows below use this refined '
        'reference; the 259,200-cell network values are interpolated to its fixed 720 sample '
        'locations. Peak error was not recorded for that last calculation.',
    )
    limits = (
        'Ces résultats vérifient le modèle magnétique linéaire implémenté. La perméabilité '
        'imposée ne représente pas la saturation ; il ne s’agit pas d’une validation expérimentale. '
        'Aucune tolérance d’acceptation automatique n’est appliquée. Le raffinement réduit '
        'les écarts résiduels, en particulier la composante tangentielle près des encoches.',
        'These results check the implemented linear magnetic model. Prescribed permeability '
        'does not represent saturation; this is not experimental validation. No automatic '
        'acceptance tolerance is applied. Refinement reduces remaining discrepancies, '
        'especially the tangential component near slots.',
    )
    return (
        '<div class="winding-validation"><div class="winding-case"><h3>'
        + translated(('Un même cas physique', 'One shared physical case'))
        + '</h3><p>' + translated(case) + '</p></div>'
        '<div class="winding-error-definition"><h3>'
        + translated(('Deux mesures différentes', 'Two different measurements'))
        + '</h3><p>' + translated(definitions) + '</p>'
        '<p class="winding-formula"><span lang="fr">E<sub>courbe</sub> = 100 × '
        '√[Σ(B<sub>réseau</sub> − B<sub>FEMM</sub>)² / ΣB<sub>FEMM</sub>²]</span>'
        '<span lang="en">E<sub>curve</sub> = 100 × '
        '√[Σ(B<sub>network</sub> − B<sub>FEMM</sub>)² / ΣB<sub>FEMM</sub>²]</span></p></div>'
        + table(presets,
                ('Préréglages de l’application · référence FEMM standard',
                 'Application presets · standard FEMM reference'),
                ('Tableau des préréglages et erreurs, défilement horizontal disponible',
                 'Preset and error table, horizontal scrolling available'))
        + '<p class="winding-table-note">' + translated(sampling) + '</p>'
        + '<div class="winding-finding"><p>' + translated(findings) + '</p></div>'
        + figure(('winding-femm-convergence.png',
                  'Erreurs du champ radial et tangentiel selon le maillage du réseau, avec références FEMM distinguées',
                  'Radial and tangential field errors versus network mesh, with FEMM references distinguished',
                  'Erreurs de courbes signées : les préréglages et le contrôle avec référence affinée restent distingués.',
                  'Signed-curve errors: application presets remain separate from the refined-reference check.'))
        + '<h3 class="winding-refined-title">'
        + translated(('Contrôle avec une référence FEMM affinée', 'Check against a refined FEMM reference'))
        + '</h3><p>' + translated(refinement) + '</p>'
        + table(refined,
                ('Deux maillages réseau · même référence FEMM affinée',
                 'Two network meshes · same refined FEMM reference'),
                ('Tableau avec référence affinée, défilement horizontal disponible',
                 'Refined-reference table, horizontal scrolling available'))
        + figure(('winding-femm-profiles.png',
                  'Comparaison point par point des courbes Br et Bθ signées du réseau et de FEMM',
                  'Point-by-point comparison of signed Br and Bθ curves from the network and FEMM',
                  'Les courbes signées révèlent les différences locales que la comparaison des pics ne voit pas.',
                  'Signed curves reveal local differences that a peak comparison does not show.'))
        + '<p class="winding-limit">' + translated(limits) + '</p>'
        '<div class="artifact-row"><a href="../assets/projects/winding-femm-validation.json" '
        'download="winding-femm-validation.json">'
        + translated(('Télécharger les résultats et réglages · JSON', 'Download results and settings · JSON'))
        + '</a></div></div>'
    )


def render_chapter(chapter, number, page):
    paragraphs = ''.join(f'<p>{translated(p)}</p>' for p in chapter.get("paragraphs", []))
    flow = chapter.get('flow', [])
    flow_images = chapter.get('flow_images', {})
    workflow = (
        '<ol class="flow-steps">' + ''.join(
            '<li><span class="flow-number" aria-hidden="true">' + f'{i:02d}' + '</span><div><h3>'
            + translated((title_fr, title_en)) + '</h3><p>' + translated((fr, en)) + '</p>'
            + ''.join(figure(spec) for spec in flow_images.get(i, [])) + '</div></li>'
            for i, (title_fr, title_en, fr, en) in enumerate(flow, 1)
        ) + '</ol>'
    ) if flow else ''
    prose = f'<div class="prose">{paragraphs}</div>'
    if flow and page['slug'] != 'foc-induction-motor':
        prose = '<details class="method-detail"><summary>' + translated(('Les choix de calcul', 'Calculation choices')) + '</summary>' + prose + '</details>'
    references = chapter.get('references', [])
    source_links = (
        '<p class="reference-links">' + translated(('Pour comprendre la méthode : ', 'Method background: '))
        + ' · '.join('<a href="' + clean(url) + '" target="_blank" rel="noopener">'
                     + translated((fr, en)) + '</a>' for fr, en, url in references) + '</p>'
    ) if references else ''
    points = chapter.get("points", [])
    cards = (
        '<ul class="key-points">' + ''.join(
            '<li class="key-point"><b>' + translated((label, LABEL_EN.get(label, label))) + '</b><p>' + translated((fr, en)) + '</p></li>'
            for label, fr, en in points
        ) + '</ul>'
    ) if points else ''
    visual = figure(chapter["image"]) if chapter.get("image") else ''
    visual += ''.join(figure(spec) for spec in chapter.get('extra_images', []))
    assets = artifact_links(page) if chapter["id"] == "takeaway" else ''
    validation = winding_validation() if chapter.get('validation') else ''
    return (
        f'<section class="chapter" id="{clean(chapter["id"])}" aria-labelledby="h-{clean(chapter["id"])}">'
        f'<div class="chapter-head"><span class="chapter-no">{number:02d} / 04</span></div>'
        f'<h2 id="h-{clean(chapter["id"])}">{translated(chapter["title"])}</h2>'
        f'<p class="intro">{translated(chapter["intro"])}</p>'
        f'{workflow}{prose}{cards}{visual}{validation}{source_links}{assets}</section>'
    )


def render(page, next_page):
    slug = page["slug"]
    title_fr, title_en = page["title"]
    canonical = f"https://khalilellahlagha.github.io/projects/{slug}.html"
    hero_image = f"https://khalilellahlagha.github.io/assets/projects/{page['hero_image'][0]}"
    extra_stylesheet = (
        f'<link rel="stylesheet" href="{clean(page["stylesheet"])}?v={asset_version(page["stylesheet"])}">'
    ) if page.get('stylesheet') else ''
    metrics = ''.join(
        f'<div class="metric"><strong>{clean(value)}</strong><span>{translated((fr, en))}</span></div>'
        for value, fr, en in page["metrics"]
    )
    chapter_nav = ''.join(
        f'<li><a href="#{clean(chapter["id"])}" aria-label="{clean(chapter["title"][0])}" '
        f'data-label-fr="{clean(chapter["title"][0])}" data-label-en="{clean(chapter["title"][1])}">'
        f'<span class="chapter-label-full">{translated(chapter["title"])}</span>'
        f'<span class="chapter-label-short" aria-hidden="true">{translated(page.get("chapter_labels", {}).get(chapter["id"], CHAPTER_LABELS[chapter["id"]]))}</span>'
        '</a></li>'
        for chapter in page["chapters"]
    )
    chapters = ''.join(render_chapter(chapter, n, page) for n, chapter in enumerate(page["chapters"], 1))
    next_link = f'{clean(next_page["slug"])}.html'
    report_action = ''
    if page.get("reports"):
        fr, en = page["reports"]
        download = f' download="{clean(page["report_download"])}"' if page.get("report_download") else ''
        report_action = (
            f'<a class="button ghost report-link" data-fr="{clean(fr)}" data-en="{clean(en)}" '
            f'href="{clean(fr)}" target="_blank" rel="noopener"{download}>'
            + translated(page.get("report_label", ("Rapport PDF ↗", "PDF report ↗"))) + '</a>'
        )
    elif page.get("extra_reports"):
        report_action = '<a class="button ghost" href="#takeaway">' + translated(("Voir les rapports ↓", "See the reports ↓")) + '</a>'
    elif page.get("repo"):
        report_action = '<a class="button ghost" href="' + clean(page["repo"]) + '" target="_blank" rel="noopener">' + translated(("Code GitHub ↗", "GitHub code ↗")) + '</a>'
    return f'''<!doctype html>
<html lang="fr" data-theme="dark">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>{clean(title_fr)} — Lagha Khalil</title>
  <meta name="description" content="{clean(page['summary'][0])}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="article"><meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{clean(title_fr)} — Lagha Khalil">
  <meta property="og:description" content="{clean(page['summary'][0])}">
  <meta property="og:image" content="{clean(hero_image)}">
  <meta property="og:locale" content="fr_FR"><meta property="og:locale:alternate" content="en_US">
  <meta name="theme-color" content="#090e1c">
  <link rel="stylesheet" href="project.css?v={asset_version('project.css')}"><script src="project.js?v={asset_version('project.js')}" defer></script>{extra_stylesheet}
</head>
<body>
  <div class="progress" aria-hidden="true"></div>
  <a class="skip" href="#main">{translated(('Aller au contenu','Skip to content'))}</a>
  <header class="topbar"><div class="topbar-inner">
    <a class="brand" href="../index.html#projets"><span class="mark" aria-hidden="true">KL</span><span>{translated(('Lagha Khalil','Khalil Lagha'))}</span></a>
    <span class="topbar-title">{translated(('Carnet de projet','Project story'))}</span>
    <div class="top-actions"><button class="icon-btn lang-toggle" type="button" aria-label="Switch to English">EN</button><button class="icon-btn theme-toggle" type="button" aria-label="Passer au thème clair" aria-pressed="true">◐</button></div>
  </div></header>
  <main id="main">
    <section class="hero" aria-labelledby="page-title"><div class="container">
      <div class="hero-grid"><div>
        <p class="eyebrow">{translated(page['eyebrow'])}</p>
        <h1 id="page-title">{translated(page['title'])}</h1>
        <p class="lede">{translated(page['summary'])}</p>
        <div class="hero-actions"><a class="button primary" href="#problem">{translated(('Découvrir le projet ↓','Explore the project ↓'))}</a>{report_action}</div>
        <div class="hero-index"><span>{translated(page['scope'])}</span></div>
      </div>{figure(page['hero_image'], hero=True)}</div>
    </div></section>
    <section class="metric-band" aria-label="Repères du projet" data-label-fr="Repères du projet" data-label-en="Project highlights"><div class="container metrics">{metrics}</div></section>
    <div class="container story-shell">
      <nav class="chapter-nav" aria-label="Chapitres" data-label-fr="Chapitres" data-label-en="Chapters"><p>{translated(('Dans ce projet','In this project'))}</p><ol>{chapter_nav}</ol></nav>
      <div class="story">{chapters}</div>
    </div>
    <section class="next"><div class="container next-inner"><div><p class="next-kicker">{translated(('Projet suivant','Next project'))}</p><h2>{translated(next_page['title'])}</h2></div><a class="button primary" href="{next_link}">{translated(('Continuer →','Continue →'))}</a></div></section>
  </main>
  <footer class="footer"><div class="container footer-inner"><span>{translated(('Lagha Khalil · Portfolio CSEE','Khalil Lagha · CSEE portfolio'))}</span><a href="../index.html#projets">{translated(('Tous les projets ↑','All projects ↑'))}</a></div></footer>
</body></html>
'''


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    for index, page in enumerate(PAGES):
        destination = here / f"{page['slug']}.html"
        destination.write_text(render(page, PAGES[(index + 1) % len(PAGES)]), encoding="utf-8")
        print(destination)
