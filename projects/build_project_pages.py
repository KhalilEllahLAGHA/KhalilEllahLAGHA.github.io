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
     'summary': ('Réguler la vitesse d’un moteur asynchrone de 5 kW et comparer la SPWM et la SVPWM à sept segments '
                 'sur le même onduleur IGBT simulé.',
                 'Control a 5 kW induction motor and compare SPWM with seven-segment SVPWM on the same simulated '
                 'IGBT inverter.'),
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
                                   'durées en impulsions de grille symétriques.',
                                   'SPWM compares the phase commands with a triangle. SVPWM finds the voltage sector, '
                                   'calculates the two active dwell times and shares the remaining time between the '
                                   'zero states. The seven-segment sequence arranges those times into symmetric gate pulses.')],
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
                   'title': ('Résultats Simscape', 'Simscape results'),
                   'intro': ('Les courbes de vitesse, de couple et de courant sur l’essai complet proviennent de la SVPWM '
                             'à sept segments. Le détail des trois courants de phase couvre une période électrique au palier de 1 400 tr/min.',
                             'The drive-response plots use the seven-segment SVPWM run. The three phase currents are '
                             'shown over one electrical cycle on the 1,400 rpm plateau.'),
                   'paragraphs': [('Pour comparer les modulations, j’ai relevé le couple électromagnétique '
                                   'sur les mêmes six périodes PWM, de 1,1050 à 1,1056 s. Les deux essais utilisent un bus '
                                   'continu de 540 V, une fréquence de commutation de 10 kHz et les mêmes réglages de commande.',
                                   'I compared electromagnetic torque over the same six PWM periods, '
                                   'from 1.1050 to 1.1056 s. Both runs use a 540 V DC bus, a 10 kHz switching frequency, '
                                   'and the same controller settings.')],
                   'extra_images': [
                       ('foc-simscape-speed.png',
                        'Vitesse du rotor et consigne en SVPWM dans Simscape',
                        'Simscape SVPWM rotor speed and reference',
                        'Vitesse du rotor et consigne pendant l’essai en SVPWM.',
                        'Rotor speed and its reference during the SVPWM run.'),
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
                       ('foc-simscape-torque.png',
                        'Couple électromagnétique brut sur six périodes PWM en SPWM et en SVPWM',
                        'Raw electromagnetic torque over six PWM periods for SPWM and SVPWM',
                        'Sur ces six périodes, le couple électromagnétique moyen est de 9,87 N·m en SPWM et de 10,69 N·m en SVPWM.',
                        'Over these six periods, mean electromagnetic torque was 9.87 N·m with SPWM and 10.69 N·m with SVPWM.'),
                   ],
                   'points': []}],
     'reports': ('../reports/foc-induction-motor-report.pdf', '../reports/foc-induction-motor-report-en.pdf'),
     'repo': 'https://github.com/KhalilEllahLAGHA/foc-induction-motor'},
{'slug': 'winding-flux-analysis',
 'title': ('Bobinage et analyse de flux', 'Winding and flux analysis'),
 'eyebrow': ('03 / Conception de machines', '03 / Machine design'),
 'summary': ('Comment un choix de bobinage se traduit-il dans le champ magnétique ? Notre application Python relie '
             'les paramètres saisis, la force magnétomotrice et le calcul du flux à une lecture de la machine en 2D.',
             'How does a winding choice affect the magnetic field? Our Python application connects input parameters, '
             'magnetomotive force and flux calculation to a 2D view of the machine.'),
 'scope': ('Projet d’équipe · Python / PyQt5 / FEMM', 'Team project · Python / PyQt5 / FEMM'),
 'metrics': [('3', 'espaces : bobinage, FMM, flux', 'workspaces: winding, MMF, flux'),
             ('2D', 'coupe de la machine pour lire le champ', 'machine cross-section to inspect the field'),
             ('Python', 'interface et chaîne de calcul', 'interface and calculation pipeline')],
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
                               'la répartition des phases dans le stator.',
                               'In this team project, we developed a Python/PyQt5 application. The first interface '
                               'sets slots, pole pairs, coil span and layers. It checks winding feasibility and '
                               'draws the phase arrangement in the stator.'),
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
                         'La disposition des bobines, le nombre de spires et les courants donnent la contribution de '
                         'chaque phase. Leur somme produit une FMM résultante : l’excitation magnétique appliquée '
                         'aux dents de la machine.',
                         'Coil placement, turns and currents determine each phase contribution. Their sum gives the '
                         'resultant MMF: the magnetic excitation applied to the machine teeth.'),
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
                         'A décrit les liaisons du réseau de réluctances ; b contient l’excitation issue de la FMM. '
                         'La résolution donne x, les potentiels magnétiques des cellules. Ces valeurs permettent '
                         'ensuite de calculer les flux entre cellules.',
                         'A describes connections in the reluctance network; b contains the excitation derived from '
                         'MMF. Solving gives x, the cell magnetic potentials. These values then allow fluxes between '
                         'cells to be calculated.')],
               'flow_images': {1: [('winding-mmf-app.png',
                                    'Interface FMM avec contributions des phases A, B, C et résultante',
                                    'MMF interface with phase A, B, C contributions and their resultant',
                                    'Cas illustratif commun aux captures : 36 encoches, 2 paires de pôles, double '
                                    'couche, 204 spires, courant de phase réglé à 0,5 A et angle électrique de 90°.',
                                    'Illustrative case used throughout these captures: 36 slots, 2 pole pairs, '
                                    'double layer, 204 turns, phase-current setting 0.5 A and electrical angle '
                                    '90°.')],
                               2: [('winding-mesh-app.png',
                                    'Interface de maillage polaire de la machine, avec 8 640 cellules',
                                    'Machine polar-mesh interface with 8,640 cells',
                                    'Le maillage transforme la géométrie en un réseau calculable ; le réglage '
                                    'présenté comporte 8 640 cellules.',
                                    'The mesh turns geometry into a network that can be computed; the displayed '
                                    'setting contains 8,640 cells.')]},
               'paragraphs': [('La discrétisation utilisée ici est un réseau de réluctances sur une grille polaire. '
                               'La FMM calculée par dent est reportée sur ce réseau. NumPy organise les données et '
                               'SciPy résout le système creux par gradient conjugué préconditionné.',
                               'The discretisation used here is a reluctance network on a polar grid. Tooth MMF is '
                               'mapped onto that network. NumPy organises the data and SciPy solves the sparse '
                               'system with preconditioned conjugate gradients.')],
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
                         'Les différences de potentiel magnétique, les sources de FMM et les réluctances donnent le '
                         'flux de chaque branche. Les lignes reconstruites rendent son trajet lisible dans la coupe '
                         'de la machine.',
                         'Magnetic-potential differences, MMF sources and reluctances give the flux in each branch. '
                         'Reconstructed lines make its path visible in the machine cross-section.'),
                        ('Calculer B et afficher la carte',
                         'Calculate B and display the map',
                         'Le flux rapporté aux sections traversées donne les composantes de B. La carte de couleurs '
                         'affiche son intensité dans la géométrie : on relie ainsi un choix de bobinage à un '
                         'résultat physique visible.',
                         'Flux divided by the traversed cross-sectional areas gives the components of B. The colour '
                         'map shows its magnitude within the geometry, connecting a winding choice to a visible '
                         'physical result.')],
               'flow_images': {1: [('winding-flux-lines-app.png',
                                    'Application affichant les lignes de flux sur la coupe 2D de la machine',
                                    'Application displaying flux lines on the 2D machine cross-section',
                                    'Lignes de flux : lire le trajet du flux dans la machine. Elles sont '
                                    'reconstruites et lissées pour l’affichage.',
                                    'Flux lines: inspect flux paths through the machine. The lines are reconstructed '
                                    'and smoothed for display.')],
                               2: [('winding-b-map-app.png',
                                    'Application affichant la carte de la norme de B en teslas',
                                    'Application displaying the magnitude of B in teslas',
                                    'Carte de |B| : lire la répartition de l’induction magnétique pour le même cas '
                                    'de calcul.',
                                    'Map of |B|: inspect the magnetic flux-density distribution for the same '
                                    'calculation case.')]},
               'paragraphs': [('Les captures proviennent de l’application, avec un même jeu de paramètres. Le modèle '
                               'est une coupe 2D à perméabilités imposées ; la saturation n’est pas calculée. Une '
                               'comparaison avec FEMM peut compléter l’étude, sans constituer un essai sur machine '
                               'physique.',
                               'The captures come from the application using one parameter set. The model is a 2D '
                               'cross-section with prescribed permeabilities; saturation is not calculated. A FEMM '
                               'comparison can complement the study, without constituting a physical machine test.')],
               'points': []},
              {'id': 'takeaway',
               'title': ('Ce que ce projet démontre', 'What this project demonstrates'),
               'intro': ('Relier une question d’électrotechnique à un outil Python utilisable : des entrées '
                         'compréhensibles, une chaîne de calcul cohérente et des résultats que l’on peut '
                         'interpréter.',
                         'Connect an electrical-engineering question to a usable Python tool: clear inputs, a '
                         'consistent calculation pipeline and results that can be interpreted.'),
               'paragraphs': [('Ce travail d’équipe met en pratique la programmation orientée objet et la séparation '
                               'entre interface, calcul et visualisation. C’est cette continuité — du paramètre '
                               'saisi au résultat expliqué — qui donne sa valeur à l’application.',
                               'This team project applies object-oriented programming and separates the interface, '
                               'calculation and visualisation. That continuity, from an input parameter to an '
                               'explained result, gives the application its value.')],
               'points': []}],
 'reports': None,
 'repo': 'https://github.com/KhalilEllahLAGHA/Winding-and-flux-analysis-program'},
    {'slug': 'dc-motor-cascade-control',
     'title': ('Commande en cascade d’un moteur à courant continu', 'Cascade control of a DC motor'),
     'eyebrow': ('04 / Automatique & conversion', '04 / Control & conversion'),
     'summary': ('Maintenir une vitesse quand la charge change : une boucle de vitesse demande le courant nécessaire, '
                 'puis une boucle plus rapide commande le pont à thyristors pour agir sur le moteur.',
                 'Hold speed as load changes: a speed loop requests the necessary current, then a faster loop controls '
                 'the thyristor bridge to act on the motor.'),
     'scope': ('Étude de simulation · MATLAB / Simulink / Python', 'Simulation study · MATLAB / Simulink / Python'),
     'metrics': [('2', 'boucles de régulation imbriquées', 'nested feedback loops'),
                 ('6', 'pulses du redresseur triphasé', 'pulses in the three-phase rectifier'),
                 ('220 V', 'point nominal étudié', 'studied nominal voltage')],
     'hero_image': ('dc-motor-cascade.svg',
                    'Architecture des deux boucles de commande en cascade',
                    'Block diagram of the two cascade-control loops',
                    'La boucle externe de vitesse fixe la consigne de courant.',
                    'The outer speed loop sets the current reference.'),
     'chapters': [{'id': 'problem',
                   'title': ('Le problème : corriger la vitesse sans perdre le courant de vue',
                             'The problem: correct speed while controlling current'),
                   'intro': ('Quand la charge change, la vitesse dépend du couple, donc du courant d’induit. La commande '
                             'en cascade donne une réponse rapide au courant avant de demander à la vitesse de se '
                             'corriger.',
                             'When load changes, speed depends on torque and therefore armature current. Cascade control '
                             'lets current respond quickly before the speed loop corrects the overall behaviour.'),
                   'paragraphs': [('L’étude porte sur une machine à excitation séparée alimentée en tension par un pont '
                                   'redresseur triphasé à six pulses. La boucle de vitesse externe calcule une consigne '
                                   'de courant ; la boucle interne agit sur l’angle d’amorçage des thyristors pour '
                                   'imposer ce courant.',
                                   'The study uses a separately excited machine supplied through a six-pulse three-phase '
                                   'rectifier. The outer speed loop computes a current reference; the inner loop acts on '
                                   'thyristor firing angle to impose that current.'),
                                  ('Le projet distingue le comportement électrique rapide de la dynamique mécanique plus '
                                   'lente. Ce découpage rend le réglage des correcteurs explicable à partir des '
                                   'constantes de temps de la machine.',
                                   'The project separates fast electrical behaviour from slower mechanical dynamics. '
                                   'That separation makes controller tuning explainable from machine time constants.')],
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
                   'title': ('Du modèle au correcteur', 'From plant model to controller'),
                   'intro': ('Le rapport établit le modèle du redresseur et de la machine, puis règle les correcteurs '
                             'PI/PID analytiquement par compensation pôle–zéro.',
                             'The report derives rectifier and motor models, then tunes PI/PID controllers analytically '
                             'using pole-zero compensation.'),
                   'paragraphs': [('Les scripts MATLAB définissent les paramètres de la machine, le point de '
                                   'fonctionnement et les gains. Un modèle Simulink par fonctions de transfert aide à '
                                   'comprendre la cascade ; un modèle SimPowerSystems inclut le pont commandé et la '
                                   'machine détaillée.',
                                   'MATLAB scripts define machine data, the operating point and gains. A '
                                   'transfer-function Simulink model clarifies the cascade; a SimPowerSystems model '
                                   'includes the controlled bridge and detailed machine.'),
                                  ('Un portage NumPy/SciPy reproduit le réglage et génère des courbes de réponse. Il '
                                   'permet de vérifier les calculs de conception sans dépendre exclusivement du modèle '
                                   'Simulink ; le guide Python documente la concordance des quantités de réglage.',
                                   'A NumPy/SciPy port reproduces the tuning and generates response curves. It checks '
                                   'design calculations independently of the Simulink model; the Python guide documents '
                                   'agreement of the tuning quantities.')],
                   'points': [('Modéliser',
                               'Constantes électriques et mécaniques, redresseur, fonction de transfert.',
                               'Electrical and mechanical constants, rectifier and transfer function.'),
                              ('Régler',
                               'PI/PID à partir des temps de réponse visés.',
                               'PI/PID from targeted response times.'),
                              ('Recouper', 'Même réglage reproduit en Python.', 'Same tuning reproduced in Python.')],
                   'image': ('dc-motor-response.png',
                             'Réponse nominale du moteur à courant continu avec sa commande en cascade',
                             'Nominal DC-motor response under cascade control',
                             'La réponse fermée illustre le point de fonctionnement conçu.',
                             'Closed-loop response illustrates the designed operating point.'),
                   'flow': [('Demande de vitesse',
                             'Speed request',
                             'La boucle externe compare la vitesse réelle à la consigne et demande le courant '
                             'nécessaire.',
                             'The outer loop compares actual speed with its target and requests the required current.'),
                            ('Réglage du courant',
                             'Current control',
                             'La boucle interne corrige rapidement l’écart de courant.',
                             'The inner loop rapidly corrects current error.'),
                            ('Pont à thyristors',
                             'Thyristor bridge',
                             'L’angle d’amorçage règle la tension moyenne appliquée à l’induit.',
                             'The firing angle sets the average voltage applied to the armature.'),
                            ('Retour du moteur',
                             'Motor feedback',
                             'Courant et vitesse ferment les deux boucles ; leurs échelles de temps sont différentes.',
                             'Current and speed close the two loops, which operate on different time scales.')]},
                  {'id': 'evidence',
                   'title': ('Explorer la forme de la réponse', 'Explore the shape of the response'),
                   'intro': ('Les figures ne se limitent pas à une courbe nominale : elles isolent l’effet du temps de '
                             'montée de la boucle de courant, puis de l’amortissement et de la fréquence naturelle de la '
                             'boucle de vitesse.',
                             'The figures go beyond one nominal curve: they isolate the effect of current-loop rise '
                             'time, then speed-loop damping and natural frequency.'),
                   'paragraphs': [('Le guide du portage Python indique un point de fonctionnement conçu à 220 V et 3 000 '
                                   'tr/min et liste les gains obtenus dans les deux environnements. Les balayages de '
                                   'paramètres montrent comment les objectifs de temps de réponse modifient dépassement '
                                   'et établissement.',
                                   'The Python-port guide records a designed 220 V, 3,000 rpm operating point and '
                                   'matching gains in both environments. Parameter sweeps show how response targets '
                                   'affect overshoot and settling.'),
                                  ('Ce sont des résultats de simulation et de calcul de réglage. Aucune mesure sur banc '
                                   'moteur n’est revendiquée ; le rapport rassemble l’architecture, les modèles et les '
                                   'réponses.',
                                   'These are simulation and tuning-calculation results. No motor-bench measurements are '
                                   'claimed; the report brings together architecture, models and responses.')],
                   'points': []},
                  {'id': 'takeaway',
                   'title': ('La leçon de commande', 'The control lesson'),
                   'intro': ('La cascade permet de concevoir chaque dynamique à sa bonne échelle : courant d’abord, '
                             'vitesse ensuite. Le recoupement Python rend les calculs de gains plus faciles à auditer.',
                             'Cascade design gives each dynamic its proper time scale: current first, speed second. '
                             'Python cross-checking makes gain calculations easier to audit.'),
                   'paragraphs': [('L’étude reste distincte de la commande vectorielle FOC du moteur asynchrone : '
                                   'machine, convertisseur et stratégie de commande sont différents.',
                                   'This study is separate from the induction-motor FOC project: machine, converter and '
                                   'control strategy all differ.')],
                   'points': []}],
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
    "foc-control.svg": (1100, 760), "foc-speed-tracking.png": (1350, 690),
    "foc-response-context.png": (1875, 1785), "foc-simscape-scopes.png": (2133, 1258),
    "foc-simscape-speed.png": (1190, 692),
    "foc-simscape-drive-torque.png": (1168, 690),
    "foc-simscape-phase.png": (1156, 666),
    "foc-simscape-dq.png": (1168, 691),
    "foc-simscape-torque.png": (1473, 513),
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
                       or path.startswith('foc-simscape-')
                       or (path.startswith('winding-') and path.endswith('-app.png')))
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
    return (
        f'<section class="chapter" id="{clean(chapter["id"])}" aria-labelledby="h-{clean(chapter["id"])}">'
        f'<div class="chapter-head"><span class="chapter-no">{number:02d} / 04</span></div>'
        f'<h2 id="h-{clean(chapter["id"])}">{translated(chapter["title"])}</h2>'
        f'<p class="intro">{translated(chapter["intro"])}</p>'
        f'{workflow}{prose}{cards}{visual}{source_links}{assets}</section>'
    )


def render(page, next_page):
    slug = page["slug"]
    title_fr, title_en = page["title"]
    canonical = f"https://khalilellahlagha.github.io/projects/{slug}.html"
    hero_image = f"https://khalilellahlagha.github.io/assets/projects/{page['hero_image'][0]}"
    metrics = ''.join(
        f'<div class="metric"><strong>{clean(value)}</strong><span>{translated((fr, en))}</span></div>'
        for value, fr, en in page["metrics"]
    )
    chapter_nav = ''.join(
        f'<li><a href="#{clean(chapter["id"])}" aria-label="{clean(chapter["title"][0])}" '
        f'data-label-fr="{clean(chapter["title"][0])}" data-label-en="{clean(chapter["title"][1])}">'
        f'<span class="chapter-label-full">{translated(chapter["title"])}</span>'
        f'<span class="chapter-label-short" aria-hidden="true">{translated(CHAPTER_LABELS[chapter["id"]])}</span>'
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
  <link rel="stylesheet" href="project.css?v={asset_version('project.css')}"><script src="project.js?v={asset_version('project.js')}" defer></script>
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
