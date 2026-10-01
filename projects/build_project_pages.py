"""Build the six standalone, bilingual static project pages. No dependencies."""

from html import escape
from hashlib import sha256
from pathlib import Path


PAGES = [
    {
        "slug": "power-grid-analysis",
        "title": ("Analyse de réseaux électriques", "Power grid analysis"),
        "eyebrow": ("01 / Systèmes électriques", "01 / Power systems"),
        "summary": (
            "Un outil MATLAB pour passer du schéma d’un réseau à ses matrices, son load flow et sa stabilité transitoire — puis confronter les méthodes de calcul sur des cas de 3 à 118 nœuds.",
            "A MATLAB toolbox that takes a network from its one-line model to bus matrices, load flow and transient stability, then compares numerical methods on systems of 3 to 118 buses.",
        ),
        "scope": ("Projet académique individuel · MATLAB / App Designer", "Individual academic project · MATLAB / App Designer"),
        "metrics": [
            ("3–118", "nœuds dans les cas de test", "buses across the test systems"),
            ("3", "solveurs de load flow comparés", "load-flow solvers compared"),
            ("14", "réseaux de validation documentés", "documented validation networks"),
        ],
        "hero_image": ("grid-interface.png", "Interface de l’application MATLAB d’analyse de réseaux", "MATLAB power-grid analysis application interface", "L’interface rassemble matrices, load flow et stabilité.", "The interface brings together matrices, load flow and stability."),
        "chapters": [
            {
                "id": "problem", "title": ("Lire le réseau avant de le résoudre", "Understand the network before solving it"),
                "intro": ("Un réseau électrique ne se résume pas à une seule courbe. Il faut représenter ses lignes, ses transformateurs et ses nœuds avant d’interpréter tensions, pertes ou comportement après défaut.", "A power network cannot be reduced to a single plot. Lines, transformers and buses must be represented correctly before voltages, losses or post-fault behaviour can be interpreted."),
                "paragraphs": [
                    ("J’ai construit ce projet en solo dans le cadre du TP d’analyse des réseaux électriques à l’ENP. Le parcours de calcul part des données de branche, assemble Ybus et Zbus, résout l’écoulement de puissance, puis utilise l’état pré-défaut pour une étude de stabilité transitoire.", "I built this project individually for the ENP power-system analysis lab. The calculation path starts with branch data, assembles Ybus and Zbus, solves power flow, then uses the pre-fault state for a transient-stability study."),
                    ("L’interface App Designer expose les trois outils sans cacher la logique numérique : les réseaux de test et les fonctions MATLAB restent séparés, ce qui permet aussi une validation sans interface graphique.", "The App Designer interface exposes all three tools without hiding the numerical core: test networks and MATLAB functions remain separate, allowing headless validation as well."),
                ],
                "points": [
                    ("Données", "Bus PQ, PV et slack ; lignes et transformateurs à prise hors nominale.", "PQ, PV and slack buses; lines and off-nominal tap transformers."),
                    ("Matrices", "Construction de Ybus et Zbus, avec comparaison à l’inverse de Ybus.", "Ybus and Zbus construction, with a check against inverse Ybus."),
                    ("Question", "Que gagne-t-on en précision et en temps avec chaque solveur ?", "What does each solver gain in accuracy and time?"),
                ],
            },
            {
                "id": "method", "title": ("Trois chemins vers le load flow", "Three routes to load flow"),
                "intro": ("Le cœur du projet compare Gauss–Seidel, Newton–Raphson et la méthode découplée rapide BX sur les mêmes réseaux et avec les mêmes catégories de bus.", "The core of the project compares Gauss–Seidel, Newton–Raphson and BX fast-decoupled load flow on the same networks and bus categories."),
                "paragraphs": [
                    ("Le constructeur Ybus additionne correctement les branches parallèles et intègre les transformateurs. Zbus est obtenue par construction directe ; l’écart maximal avec inv(Ybus) sert de contrôle sur les réseaux où cette comparaison est possible.", "The Ybus builder accumulates parallel branches and incorporates transformers. Zbus uses a direct building algorithm; maximum error against inv(Ybus) serves as a check where that comparison is defined."),
                    ("Gauss–Seidel et Newton–Raphson prennent en compte les contraintes de puissance réactive des bus PV ; la version découplée rapide BX sert à comparer une formulation différente sans cette gestion des limites. Leurs itérations et résultats sont étudiés de 3 à 118 nœuds, dont les cas IEEE 14, 30, 57 et 118.", "Gauss–Seidel and Newton–Raphson handle PV-bus reactive-power limits; the BX fast-decoupled version provides a different formulation for comparison without that limit handling. Their iterations and outputs are studied from 3 to 118 buses, including IEEE 14, 30, 57 and 118 cases."),
                ],
                "points": [
                    ("Gauss–Seidel", "Itération accélérée et contrôle des limites Q des bus PV.", "Accelerated iteration and PV-bus reactive-limit handling."),
                    ("Newton–Raphson", "Formulation rectangulaire pour résoudre les inconnues du réseau.", "Rectangular-coordinate formulation for solving network unknowns."),
                    ("BX", "Découplage rapide pour confronter coût de calcul et résultat.", "Fast-decoupled formulation for comparing computational cost and output."),
                ],
                "image": ("grid-loadflow-iterations.png", "Comparaison du nombre d’itérations des méthodes de load flow", "Load-flow iteration comparison chart", "Comparer la convergence plutôt que choisir un solveur sur son nom.", "Comparing convergence rather than choosing a solver by name."),
            },
            {
                "id": "evidence", "title": ("Du régime établi au défaut", "From steady state to a fault"),
                "intro": ("Après le load flow, une séquence défaut puis ouverture de ligne alimente un modèle classique de stabilité transitoire. L’angle rotorique est intégré avec la méthode d’Euler.", "After load flow, a fault and line-opening sequence feeds a classical transient-stability model. Rotor angle is integrated with Euler’s method."),
                "paragraphs": [
                    ("Le test numérique documenté porte sur quatorze réseaux pour les matrices et solveurs, avec un cas à six nœuds pour la stabilité. Sur le cas IEEE 118, les pertes calculées de 131,96 MW correspondent à la référence citée dans le projet ; Zbus et inv(Ybus) concordent à la précision machine sur les réseaux ancrables.", "The documented numerical suite covers fourteen networks for matrices and solvers, plus a six-bus stability case. On IEEE 118, computed losses of 131.96 MW match the reference cited in the project; Zbus and inv(Ybus) agree to machine precision on anchorable networks."),
                    ("Il s’agit d’une étude de simulation et de comparaison numérique. Elle n’établit pas une validation sur réseau réel ; son intérêt est de relier modèle, algorithme et interprétation des résultats dans un même outil.", "This is a simulation and numerical-comparison study, not validation on an operating grid. Its value is connecting model, algorithm and interpretation within one tool."),
                ],
                "points": [],
                "image": ("grid-transient-stability.png", "Évolution transitoire de l’angle rotorique après défaut", "Transient rotor-angle response after a fault", "La réponse transitoire complète l’analyse de régime établi.", "The transient response complements steady-state analysis."),
            },
            {
                "id": "takeaway", "title": ("Ce que montre le projet", "What this project demonstrates"),
                "intro": ("Un même réseau peut être abordé par ses matrices, son équilibre de puissance et sa dynamique après incident. La valeur vient de leur cohérence, vérifiée à chaque étape.", "The same network can be examined through its matrices, power balance and post-disturbance dynamics. The value lies in their consistency, checked at every step."),
                "paragraphs": [("Le dépôt contient le code MATLAB, les systèmes de test et la logique de validation. Le rapport détaille les hypothèses, méthodes, figures et limites de l’étude.", "The repository contains MATLAB code, test systems and validation routines. The report documents assumptions, methods, figures and study limits.")],
                "points": [],
            },
        ],
        "reports": ("../reports/power-grid-analysis-report.pdf", "../reports/power-grid-analysis-report-en.pdf"),
        "repo": "https://github.com/KhalilEllahLAGHA/Power-grid-analysis-MATLAB",
    },
    {
        "slug": "foc-induction-motor",
        "title": ("Commande vectorielle d’un moteur asynchrone", "Field-oriented control of an induction motor"),
        "eyebrow": ("02 / Commande de machines", "02 / Motor drives"),
        "summary": ("Un entraînement 5 kW / 380 V commandé par FOC indirecte, reconstruit en Python puis dans deux modèles Simulink pour confronter théorie, blocs élémentaires et commutation réelle.", "A 5 kW / 380 V drive under indirect FOC, built in Python and two Simulink models to compare theory, fundamental blocks and actual switching."),
        "scope": ("Projet individuel · Python / MATLAB / Simulink", "Individual project · Python / MATLAB / Simulink"),
        "metrics": [("3", "implémentations comparables", "comparable implementations"), ("52–95 ms", "établissement des échelons de vitesse", "speed-step settling range"), ("0,800 Wb", "flux rotorique régulé", "regulated rotor flux")],
        "hero_image": ("foc-speed-tracking.png", "Courbe de suivi de vitesse de la commande vectorielle", "Field-oriented-control speed tracking plot", "Échelons, inversion du sens et perturbation de charge.", "Steps, reversal and load disturbance."),
        "chapters": [
            {
                "id": "problem", "title": ("Rendre un moteur asynchrone pilotable", "Making an induction motor controllable"),
                "intro": ("Le couple et le flux d’un moteur asynchrone interagissent. La commande vectorielle oriente un repère sur le flux rotorique pour les traiter par deux composantes de courant distinctes.", "Induction-motor torque and flux are coupled. Field-oriented control aligns a reference frame with rotor flux so two current components can govern them separately."),
                "paragraphs": [
                    ("J’ai construit un modèle dynamique de la machine 5 kW / 380 V en repère fixe, puis un contrôleur dans son propre repère estimé. Cette séparation permet d’observer une éventuelle erreur d’orientation au lieu de la supprimer par hypothèse.", "I built a dynamic model of the 5 kW / 380 V machine in the stationary frame, then a controller in its separately estimated frame. That separation reveals orientation error instead of assuming it away."),
                    ("La FOC est indirecte : l’angle vient de l’intégration de la vitesse électrique et du glissement ; le flux est estimé par un modèle en courant. Aucun capteur de flux ni filtre de Kalman n’intervient.", "The FOC is indirect: its angle comes from electrical speed and slip integration; rotor flux is estimated with a current model. No flux sensor or Kalman filter is involved."),
                ],
                "points": [("Machine", "Modèle dq, transformées de Clarke et Park.", "dq model and Clarke/Park transforms."), ("Orientation", "Calcul du glissement et estimation du flux rotorique.", "Slip calculation and rotor-flux estimation."), ("Alimentation", "Onduleur de tension à deux niveaux et SVPWM.", "Two-level voltage-source inverter and SVPWM.")],
            },
            {
                "id": "method", "title": ("Une cascade qui respecte les limites", "A cascade that respects limits"),
                "intro": ("Une boucle de vitesse produit la demande de couple ; deux boucles de courant pilotent les axes d et q. Le découplage anticipatif réduit leur interaction.", "A speed loop produces torque demand; two current loops control d and q axes. Feed-forward decoupling reduces their interaction."),
                "paragraphs": [
                    ("Les correcteurs PI sont réglés à partir des paramètres de la machine. Ils utilisent un anti-windup par back-calculation et des limites explicites de tension, courant et couple. La consigne de flux reste à 0,8 Wb et le contrôle fonctionne à 10 kHz.", "PI controllers are tuned from machine parameters. They include back-calculation anti-windup and explicit voltage, current and torque limits. Flux reference stays at 0.8 Wb and control runs at 10 kHz."),
                    ("Pour éviter qu’un seul modèle valide sa propre erreur, j’ai réalisé trois versions sur la même machine et les mêmes échelons : simulation Python, Simulink à blocs fondamentaux, puis Simscape Electrical avec pont IGBT commuté à 10 kHz.", "To avoid a single model validating its own mistakes, I built three versions around the same motor and speed steps: Python simulation, fundamental-block Simulink, then Simscape Electrical with a 10 kHz switching IGBT bridge."),
                ],
                "points": [("Python", "Modèle moteur, SVPWM et régulateurs programmés séparément.", "Motor model, SVPWM and controllers coded separately."), ("Simulink V1", "Chaîne reconstruite avec des blocs fondamentaux.", "Drive rebuilt with fundamental blocks."), ("Simulink V2", "Blocs Simscape et commutation réelle de l’onduleur.", "Simscape components and switching inverter." )],
                "image": ("foc-control.svg", "Schéma de la cascade de commande vectorielle", "FOC cascaded-control diagram", "La boucle de vitesse alimente les références de courant d et q.", "The speed loop feeds d- and q-axis current references."),
            },
            {
                "id": "evidence", "title": ("Trois modèles, un comportement cohérent", "Three models, consistent behaviour"),
                "intro": ("Le scénario associe montée du flux, échelons 800 → 1400 → 600 tr/min, inversion à −800 tr/min et application d’un couple de charge de 10 N·m.", "The scenario combines flux build-up, 800 → 1400 → 600 rpm steps, reversal to −800 rpm and a 10 N·m load-torque step."),
                "paragraphs": [
                    ("Les échelons s’établissent en 52 à 95 ms suivant la version et la transition, sans dépassement. L’échelon de charge crée un creux d’environ 69 tr/min récupéré en environ 70 ms ; les trois modèles maintiennent un flux de 0,800 Wb et un résidu d’axe q inférieur à 2 %.", "Across versions and transitions, speed steps settle in 52 to 95 ms without overshoot. The load step causes an approximately 69 rpm dip recovered in about 70 ms; all three models hold 0.800 Wb flux with q-axis flux residual below 2%."),
                    ("Les petites différences de vitesse et de courant reflètent notamment le contrôle continu ou discret et l’onduleur moyenné ou commuté. Une étude Python séparée de suivi rampe/sinus examine le principe du modèle interne ; elle n’est pas attribuée aux deux modèles MATLAB.", "Small speed and current differences reflect continuous versus discrete control and averaged versus switching inverter models. A separate Python ramp/sine study probes the internal-model principle; it is not attributed to the two MATLAB models."),
                ],
                "points": [],
            },
            {
                "id": "takeaway", "title": ("Portée et suite possible", "Scope and next steps"),
                "intro": ("Le projet relie les équations de machine à un entraînement commuté et vérifie qu’une architecture de commande conserve son comportement dans trois environnements de simulation.", "The project connects machine equations to a switching drive and checks that one control architecture retains its behaviour in three simulation environments."),
                "paragraphs": [("La consigne de flux reste constante : le défluxage au-dessus de la vitesse de base n’est pas implémenté. L’adaptation de la constante de temps rotorique et une version sans capteur de vitesse seraient des prolongements. Le rapport lié ci-dessous détaille les équations, réglages, résultats et comparaison.", "Flux reference remains constant: field weakening above base speed is not implemented. Rotor-time-constant adaptation and sensorless speed operation would be natural extensions. The linked report gives equations, tuning, results and comparison.")],
                "points": [],
            },
        ],
        "reports": ("../reports/foc-induction-motor-report.pdf", "../reports/foc-induction-motor-report-en.pdf"),
        "repo": "https://github.com/KhalilEllahLAGHA/foc-induction-motor",
    },
    {
        "slug": "winding-flux-analysis",
        "title": ("Bobinage et analyse de flux", "Winding and flux analysis"),
        "eyebrow": ("03 / Conception de machines", "03 / Machine design"),
        "summary": ("Une application PyQt d’équipe qui relie le bobinage triphasé, la force magnétomotrice, un maillage polaire et le flux calculé par réseau de réluctances, avec comparaison FEMM.", "A team-built PyQt application connecting three-phase winding, magnetomotive force, polar meshing and reluctance-network flux, with FEMM comparison."),
        "scope": ("Projet d’équipe · Python / PyQt5 / FEMM", "Team project · Python / PyQt5 / FEMM"),
        "metrics": [("3", "espaces de travail dans l’application", "workspaces in the application"), ("4", "régions dans le maillage polaire", "regions in the polar mesh"), ("FEMM", "comparaison par éléments finis", "finite-element comparison")],
        "hero_image": ("winding-flux-heatmap.png", "Carte de densité de flux magnétique dans la machine", "Magnetic flux-density heatmap in the machine", "Visualisation issue du calcul de flux de l’application.", "Flux-computation visualisation from the application."),
        "chapters": [
            {
                "id": "problem", "title": ("Du placement des bobines au champ", "From coil placement to field"),
                "intro": ("Le dimensionnement d’une machine exige de garder cohérents géométrie, connexions triphasées et grandeurs magnétiques. L’application permet d’explorer cette chaîne dans une même interface.", "Machine design requires geometry, three-phase connections and magnetic quantities to remain consistent. The application lets users explore that chain in one interface."),
                "paragraphs": [
                    ("Dans ce projet d’équipe, nous avons développé une application de bureau en Python et PyQt5. Elle commence par la configuration en encoches, pôles, couches et pas de bobinage ; elle calcule la faisabilité, les facteurs de bobinage et la matrice des connexions de phases.", "In this team project, we developed a Python/PyQt5 desktop application. It begins with slots, poles, layers and coil pitch; it computes feasibility, winding factors and the phase-connection matrix."),
                    ("Un dessin du stator et des contrôles interactifs évitent de traiter le bobinage comme une simple ligne de nombres. Les paramètres se transmettent aux vues FMM et flux pour que les calculs gardent la même machine de référence.", "A stator drawing and interactive controls keep the winding from becoming just a row of numbers. Parameters carry into MMF and flux views so the calculations use the same machine."),
                ],
                "points": [("Bobinage", "Configuration et vérification de faisabilité.", "Configuration and feasibility checks."), ("Connexions", "Matrice phase–encoche et représentation du stator.", "Phase–slot matrix and stator view."), ("Cohérence", "Paramètres synchronisés entre les trois espaces.", "Parameters shared across all three workspaces.")],
            },
            {
                "id": "method", "title": ("Voir la FMM avant de résoudre le flux", "See MMF before solving flux"),
                "intro": ("La deuxième vue calcule les profils de force magnétomotrice dent par dent pour chaque phase et leur résultante, en fonction de l’angle électrique.", "The second view computes tooth-based magnetomotive-force profiles for each phase and their resultant versus electrical angle."),
                "paragraphs": [
                    ("Le moteur de calcul sépare les profils de phase de la combinaison temporelle. L’utilisateur peut examiner la matrice de connexion, faire varier l’angle et animer la résultante ; cela rend visibles les effets du schéma de bobinage.", "The calculation engine separates phase profiles from their time-dependent combination. Users can inspect the connection matrix, vary angle and animate the resultant, making winding choices visible."),
                    ("La troisième vue guide ensuite la définition de la machine, la génération d’un maillage polaire à quatre régions et le calcul de densité de flux. Un réseau de réluctances et un solveur creux produisent des cartes de densité et des lignes de flux.", "The third view then guides machine setup, a four-region polar mesh and flux-density calculation. A reluctance network and sparse solver produce density maps and flux lines."),
                ],
                "points": [("FMM", "Profils par phase et résultante interactive.", "Per-phase profiles and interactive resultant."), ("Maillage", "Géométrie polaire organisée en quatre régions.", "Polar geometry divided into four regions."), ("Solveur", "Réseau de réluctances puis visualisation du flux.", "Reluctance network followed by flux visualisation.")],
                "image": ("winding-mmf.png", "Profils de force magnétomotrice des trois phases", "Three-phase magnetomotive-force profiles", "La FMM résultante relie connexion des bobines et excitation magnétique.", "Resultant MMF connects coil connection to magnetic excitation."),
            },
            {
                "id": "evidence", "title": ("Comparer et interpréter", "Compare and interpret"),
                "intro": ("Les cartes de densité et lignes de flux rendent le résultat inspectable. Une voie optionnelle relie l’étude au solveur éléments finis FEMM pour une comparaison indépendante.", "Density maps and flux lines make the result inspectable. An optional path links the study to FEMM finite-element analysis for independent comparison."),
                "paragraphs": [
                    ("Les figures du dépôt montrent plusieurs configurations, notamment des bobinages simple et double couche. L’interface distingue ce qui relève du calcul de bobinage, de la FMM et du flux ; cette séparation aide à localiser une incohérence.", "Repository figures show several configurations, including single- and double-layer windings. The interface separates winding, MMF and flux calculations, which helps locate inconsistencies."),
                    ("La comparaison FEMM sert de contrôle numérique, pas d’essai sur prototype physique. Le dossier fournit le code de l’application et les images de référence, avec FEMM en dépendance optionnelle pour les vérifications finies.", "FEMM comparison is a numerical check, not a physical prototype test. The repository contains application code and reference images, with FEMM optional for finite-element checks."),
                ],
                "points": [],
                "image": ("winding-flux-lines.png", "Lignes de flux simulées autour de la machine", "Simulated magnetic flux lines around the machine", "Lecture visuelle du trajet du flux dans la géométrie étudiée.", "A visual reading of flux paths in the studied geometry."),
            },
            {
                "id": "takeaway", "title": ("Ce que relie l’application", "What the application connects"),
                "intro": ("Le projet transforme une suite de calculs de machine en parcours exploratoire : saisir, visualiser, calculer, confronter.", "The project turns a sequence of machine calculations into an exploratory path: enter, visualise, calculate, compare."),
                "paragraphs": [("Il reste un outil de conception et d’analyse numérique. Les résultats doivent être interprétés dans les hypothèses du réseau de réluctances et de la géométrie choisie ; un essai expérimental demanderait un dispositif et des mesures supplémentaires.", "It remains a numerical design and analysis tool. Results must be interpreted within the chosen geometry and reluctance-network assumptions; experimental validation would require hardware and measurements.")],
                "points": [],
            },
        ],
        "reports": None,
        "repo": "https://github.com/KhalilEllahLAGHA/Winding-and-flux-analysis-program",
    },
    {
        "slug": "dc-motor-cascade-control",
        "title": ("Commande en cascade d’un moteur à courant continu", "Cascade control of a DC motor"),
        "eyebrow": ("04 / Automatique & conversion", "04 / Control & conversion"),
        "summary": ("Deux boucles imbriquées règlent courant et vitesse d’un moteur à courant continu alimenté par un redresseur triphasé à thyristors. Le réglage Simulink est recoupé par un portage Python indépendant.", "Nested current and speed loops control a DC motor fed by a three-phase thyristor rectifier. The Simulink design is cross-checked with an independent Python port."),
        "scope": ("Étude de simulation · MATLAB / Simulink / Python", "Simulation study · MATLAB / Simulink / Python"),
        "metrics": [("2", "boucles de régulation imbriquées", "nested feedback loops"), ("6", "pulses du redresseur triphasé", "pulses in the three-phase rectifier"), ("220 V", "point nominal étudié", "studied nominal voltage")],
        "hero_image": ("dc-motor-cascade.svg", "Architecture des deux boucles de commande en cascade", "Block diagram of the two cascade-control loops", "La boucle externe de vitesse fixe la consigne de courant.", "The outer speed loop sets the current reference."),
        "chapters": [
            {
                "id": "problem", "title": ("Pourquoi deux boucles ?", "Why two loops?"),
                "intro": ("Quand la charge change, la vitesse dépend du couple, donc du courant d’induit. La commande en cascade donne une réponse rapide au courant avant de demander à la vitesse de se corriger.", "When load changes, speed depends on torque and therefore armature current. Cascade control lets current respond quickly before the speed loop corrects the overall behaviour."),
                "paragraphs": [
                    ("L’étude porte sur une machine à excitation séparée alimentée en tension par un pont redresseur triphasé à six pulses. La boucle de vitesse externe calcule une consigne de courant ; la boucle interne agit sur l’angle d’amorçage des thyristors pour imposer ce courant.", "The study uses a separately excited machine supplied through a six-pulse three-phase rectifier. The outer speed loop computes a current reference; the inner loop acts on thyristor firing angle to impose that current."),
                    ("Le projet distingue le comportement électrique rapide de la dynamique mécanique plus lente. Ce découpage rend le réglage des correcteurs explicable à partir des constantes de temps de la machine.", "The project separates fast electrical behaviour from slower mechanical dynamics. That separation makes controller tuning explainable from machine time constants."),
                ],
                "points": [("Actionneur", "Pont triphasé commandé à thyristors.", "Three-phase controlled thyristor bridge."), ("Boucle interne", "Courant et couple, réponse rapide.", "Current and torque, fast response."), ("Boucle externe", "Vitesse et rejet des perturbations de charge.", "Speed and load-disturbance rejection.")],
            },
            {
                "id": "method", "title": ("Du modèle au correcteur", "From plant model to controller"),
                "intro": ("Le rapport établit le modèle du redresseur et de la machine, puis règle les correcteurs PI/PID analytiquement par compensation pôle–zéro.", "The report derives rectifier and motor models, then tunes PI/PID controllers analytically using pole-zero compensation."),
                "paragraphs": [
                    ("Les scripts MATLAB définissent les paramètres de la machine, le point de fonctionnement et les gains. Un modèle Simulink par fonctions de transfert aide à comprendre la cascade ; un modèle SimPowerSystems inclut le pont commandé et la machine détaillée.", "MATLAB scripts define machine data, the operating point and gains. A transfer-function Simulink model clarifies the cascade; a SimPowerSystems model includes the controlled bridge and detailed machine."),
                    ("Un portage NumPy/SciPy reproduit le réglage et génère des courbes de réponse. Il permet de vérifier les calculs de conception sans dépendre exclusivement du modèle Simulink ; le guide Python documente la concordance des quantités de réglage.", "A NumPy/SciPy port reproduces the tuning and generates response curves. It checks design calculations independently of the Simulink model; the Python guide documents agreement of the tuning quantities."),
                ],
                "points": [("Modéliser", "Constantes électriques et mécaniques, redresseur, fonction de transfert.", "Electrical and mechanical constants, rectifier and transfer function."), ("Régler", "PI/PID à partir des temps de réponse visés.", "PI/PID from targeted response times."), ("Recouper", "Même réglage reproduit en Python.", "Same tuning reproduced in Python.")],
                "image": ("dc-motor-response.png", "Réponse nominale du moteur à courant continu avec sa commande en cascade", "Nominal DC-motor response under cascade control", "La réponse fermée illustre le point de fonctionnement conçu.", "Closed-loop response illustrates the designed operating point."),
            },
            {
                "id": "evidence", "title": ("Explorer la forme de la réponse", "Explore the shape of the response"),
                "intro": ("Les figures ne se limitent pas à une courbe nominale : elles isolent l’effet du temps de montée de la boucle de courant, puis de l’amortissement et de la fréquence naturelle de la boucle de vitesse.", "The figures go beyond one nominal curve: they isolate the effect of current-loop rise time, then speed-loop damping and natural frequency."),
                "paragraphs": [
                    ("Le guide du portage Python indique un point de fonctionnement conçu à 220 V et 3 000 tr/min et liste les gains obtenus dans les deux environnements. Les balayages de paramètres montrent comment les objectifs de temps de réponse modifient dépassement et établissement.", "The Python-port guide records a designed 220 V, 3,000 rpm operating point and matching gains in both environments. Parameter sweeps show how response targets affect overshoot and settling."),
                    ("Ce sont des résultats de simulation et de calcul de réglage. Aucune mesure sur banc moteur n’est revendiquée ; le rapport rassemble l’architecture, les modèles et les réponses.", "These are simulation and tuning-calculation results. No motor-bench measurements are claimed; the report brings together architecture, models and responses."),
                ],
                "points": [],
            },
            {
                "id": "takeaway", "title": ("La leçon de commande", "The control lesson"),
                "intro": ("La cascade permet de concevoir chaque dynamique à sa bonne échelle : courant d’abord, vitesse ensuite. Le recoupement Python rend les calculs de gains plus faciles à auditer.", "Cascade design gives each dynamic its proper time scale: current first, speed second. Python cross-checking makes gain calculations easier to audit."),
                "paragraphs": [("L’étude reste distincte de la commande vectorielle FOC du moteur asynchrone : machine, convertisseur et stratégie de commande sont différents.", "This study is separate from the induction-motor FOC project: machine, converter and control strategy all differ.")],
                "points": [],
            },
        ],
        "reports": ("../reports/dc-motor-cascade-control-report.pdf", "../reports/dc-motor-cascade-control-report-en.pdf"),
        "repo": "https://github.com/KhalilEllahLAGHA/DC-motor-cascade-control",
    },
    {
        "slug": "mlp-backpropagation",
        "title": ("Réseau de neurones codé à la main", "A neural network built from scratch"),
        "eyebrow": ("05 / Intelligence artificielle", "05 / Artificial intelligence"),
        "summary": ("Un perceptron multicouche MATLAB à une couche cachée, entraîné par rétropropagation sans toolbox. Deux écritures du même algorithme — boucles explicites et matrices vectorisées — rendent le calcul transparent.", "A one-hidden-layer MATLAB perceptron trained by backpropagation without a toolbox. Two implementations of the same algorithm—explicit loops and vectorised matrices—make the computation transparent."),
        "scope": ("TP d’équipe de deux · MATLAB", "Two-person academic lab · MATLAB"),
        "metrics": [("2", "versions de la propagation", "propagation implementations"), ("1", "couche cachée étudiée", "hidden layer studied"), ("0", "toolbox de réseaux de neurones", "neural-network toolboxes")],
        "hero_image": ("mlp-network.svg", "Schéma du perceptron multicouche à une couche cachée", "One-hidden-layer multilayer perceptron diagram", "Les poids relient entrée, couche cachée et sortie.", "Weights connect input, hidden layer and output."),
        "chapters": [
            {
                "id": "problem", "title": ("Ouvrir la boîte noire", "Opening the black box"),
                "intro": ("Un appel à une toolbox peut entraîner un modèle sans montrer comment chaque poids est modifié. Ce TP d’intelligence artificielle reconstruit le chemin complet de l’apprentissage.", "A toolbox call can train a model without showing how each weight changes. This AI lab reconstructs the complete learning path."),
                "paragraphs": [
                    ("Le projet a été réalisé en binôme à l’ENP. Le perceptron multicouche possède une couche cachée et utilise une activation sigmoïde. Le programme choisit un jeu de données, effectue la propagation avant, calcule l’erreur de sortie et rétropropage le gradient jusqu’aux poids.", "This ENP project was completed by two students. The multilayer perceptron has one hidden layer and sigmoid activation. The program selects a data set, performs forward propagation, computes output error and backpropagates gradients to the weights."),
                    ("Le critère d’arrêt porte sur l’erreur de sortie ; l’exécution présente la sortie finale, les poids appris et le nombre d’itérations. Les petits jeux de données servent à comprendre le comportement de l’algorithme plutôt qu’à annoncer une performance industrielle.", "Stopping is based on output error; a run shows final output, learned weights and iteration count. Small teaching data sets help explain the algorithm rather than support industrial-performance claims."),
                ],
                "points": [("Entrée", "Jeux d’apprentissage simples et classification binaire.", "Small training sets and binary classification."), ("Calcul", "Sigmoïde, erreur, gradient, mise à jour des poids.", "Sigmoid, error, gradient and weight updates."), ("Lecture", "Sortie finale, poids et nombre d’itérations.", "Final output, weights and iteration count.")],
            },
            {
                "id": "method", "title": ("Deux chemins vers le même gradient", "Two paths to the same gradient"),
                "intro": ("La première version privilégie des boucles pédagogiques. La seconde emploie le calcul matriciel vectorisé et met aussi à jour les biais.", "The first version favours explicit teaching loops. The second uses vectorised matrix operations and also updates biases."),
                "paragraphs": [
                    ("Cette duplication volontaire aide à suivre les dimensions des vecteurs, les dérivées de la sigmoïde et la circulation de l’erreur d’une couche à l’autre. Elle montre également comment la même logique peut s’exprimer de manière plus compacte en MATLAB.", "This deliberate duplication helps track vector dimensions, sigmoid derivatives and error flow from layer to layer. It also shows how the same logic can be written more compactly in MATLAB."),
                    ("Un mode d’apprentissage en ligne conserve les poids entre exemples successifs. Les fichiers sont séparés entre sélection des données, boucle d’apprentissage, propagation et rétropropagation, afin que chaque étape puisse être étudiée isolément.", "An online-learning mode carries weights between successive examples. Files separate data selection, training loop, forward propagation and backpropagation so each stage can be inspected independently."),
                ],
                "points": [("Version 1", "Boucles explicites pour suivre chaque opération.", "Explicit loops for following each operation."), ("Version 2", "Produits matriciels vectorisés et mise à jour des biais.", "Vectorised matrix products and bias updates."), ("Organisation", "Fonctions distinctes pour données, propagation et apprentissage.", "Separate functions for data, propagation and learning.")],
                "image": ("mlp-sequential-training.png", "Illustration de l’apprentissage séquentiel du perceptron", "Illustration of sequential perceptron training", "L’apprentissage en ligne conserve l’état des poids d’un exemple à l’autre.", "Online training carries the weights from one example to the next."),
            },
            {
                "id": "evidence", "title": ("Observer l’apprentissage", "Watch learning happen"),
                "intro": ("Le rapport présente la base d’essai, les équations et l’évolution de l’erreur. Le code a été corrigé puis testé sous MATLAB R2024b avant publication open source.", "The report presents the teaching data, equations and error evolution. The code was corrected and tested in MATLAB R2024b before its open-source publication."),
                "paragraphs": [
                    ("La courbe de convergence illustre l’amélioration de l’erreur pendant l’entraînement. Elle documente ce jeu de données et ce paramétrage ; elle ne doit pas être lue comme une mesure de généralisation sur des données inconnues.", "The convergence curve illustrates training-error reduction. It documents this data set and configuration; it is not a generalisation measure on unseen data."),
                    ("Le dépôt public conserve les fonctions MATLAB et la licence MIT. Le rapport du TP reste la meilleure entrée pour relier équations, choix d’implémentation et figures.", "The public repository contains MATLAB functions under the MIT licence. The lab report is the best entry point for connecting equations, implementation choices and figures."),
                ],
                "points": [],
                "image": ("mlp-convergence.png", "Courbe de convergence de l’erreur pendant l’apprentissage", "Training-error convergence chart", "La convergence visualise le calcul itératif, sans prétendre mesurer la généralisation.", "Convergence visualises iteration without claiming generalisation."),
            },
            {
                "id": "takeaway", "title": ("Ce que démontre le TP", "What the lab demonstrates"),
                "intro": ("La rétropropagation n’est pas ici un mot-clé : chaque transformation et mise à jour est visible dans le code.", "Backpropagation is not merely a keyword here: every transform and update is visible in the code."),
                "paragraphs": [("C’est une preuve de compréhension des fondements d’un MLP, dans un cadre académique. Le projet ne revendique ni modèle profond à grande échelle ni déploiement en production.", "It demonstrates understanding of MLP fundamentals in an academic setting. The project makes no claim of large-scale deep learning or production deployment.")],
                "points": [],
            },
        ],
        "reports": ("../reports/mlp-backpropagation-report.pdf", "../reports/mlp-backpropagation-report-en.pdf"),
        "repo": "https://github.com/KhalilEllahLAGHA/mlp-backpropagation-matlab",
    },
    {
        "slug": "power-electronics-labs",
        "title": ("Travaux pratiques d’électronique de puissance", "Power electronics laboratory work"),
        "eyebrow": ("06 / Conversion de puissance", "06 / Power conversion"),
        "summary": ("Trois comptes rendus de TP étudient le redressement : diodes triphasées, pont mixte monophasé, puis lissage et commutation. Les rapports réunissent calcul théorique et mesures sur banc ; les deux premiers ajoutent MATLAB/Simulink.", "Three original lab reports study rectification: three-phase diodes, a single-phase semi-controlled bridge, then smoothing and commutation. All combine theory and bench measurements; the first two also use MATLAB/Simulink."),
        "scope": ("Travaux pratiques académiques · ENP · rapports d’origine", "Academic lab work · ENP · original reports"),
        "metrics": [("3", "rapports de TP d’origine", "original lab reports"), ("AC → DC", "conversion étudiée", "conversion studied"), ("V · A", "tension et courant observés", "observed voltage and current")],
        "hero_image": ("power-electronics-bridge-diodes.jpg", "Schéma du redresseur triphasé à diodes tiré du compte rendu d’origine", "Three-phase diode bridge diagram from the original lab report", "Un schéma étudié dans les comptes rendus originaux.", "A circuit studied in the original lab reports."),
        "chapters": [
            {
                "id": "problem", "title": ("Voir ce que fait vraiment un redresseur", "See what a rectifier actually does"),
                "intro": ("Le passage du courant alternatif au continu se lit dans un schéma, une équation et une forme d’onde mesurée. Ces TP rassemblent ces vues pour comprendre les écarts entre idéal et réel.", "AC-to-DC conversion can be read through a circuit, an equation and a measured waveform. These labs bring those views together to understand gaps between ideal and real behaviour."),
                "paragraphs": [
                    ("Les séances portent sur un redresseur triphasé à diodes, un pont mixte monophasé à diodes et thyristors, puis les effets du lissage et de l’empiètement de commutation. Les rapports d’origine documentent les montages, grandeurs attendues et observations.", "The sessions cover a three-phase diode rectifier, a single-phase semi-controlled diode/thyristor bridge, then smoothing and commutation overlap. The original reports document setups, expected quantities and observations."),
                    ("Ce sont des travaux pratiques académiques, menés avec les groupes indiqués dans les comptes rendus. Je présente ici ce que les rapports démontrent sans attribuer à une seule personne l’ensemble des mesures ou de la rédaction collective.", "These are academic labs completed with the groups named in the reports. This page explains what the reports demonstrate without attributing all measurements or group writing to one person."),
                ],
                "points": [("Redressement", "Chemin du courant dans les topologies à diodes et thyristors.", "Current paths in diode and thyristor topologies."), ("Commande", "Effet de l’angle d’amorçage sur un pont mixte.", "Effect of firing angle in a semi-controlled bridge."), ("Qualité", "Lissage, ondulation et empiètement de commutation.", "Smoothing, ripple and commutation overlap.")],
            },
            {
                "id": "method", "title": ("Du calcul à la forme d’onde", "From calculation to waveform"),
                "intro": ("Les trois manipulations confrontent calculs et observations sur banc. Les deux premières ajoutent une simulation MATLAB/Simulink pour compléter la comparaison.", "All three experiments compare calculations with bench observations. The first two also use MATLAB/Simulink simulations for a further comparison."),
                "paragraphs": [
                    ("Pour le pont triphasé, le schéma de conduction explique la succession des diodes actives et la tension redressée. Pour le pont mixte monophasé, les thyristors ajoutent une variable de commande : l’angle d’amorçage change la tension moyenne et la forme d’onde.", "For the three-phase bridge, conduction paths explain the active diode sequence and rectified voltage. In the single-phase semi-controlled bridge, thyristors add a control variable: firing angle changes average voltage and waveform."),
                    ("La troisième étude suit l’effet d’une inductance de lissage et de la commutation non instantanée. Elle relie le comportement théorique du montage aux mesures faites sur le banc et à l’oscilloscope.", "The third study examines smoothing inductance and non-instantaneous commutation. It connects theoretical circuit behaviour with bench and oscilloscope measurements."),
                ],
                "points": [("Prévoir", "Déduire la tension et les séquences de conduction.", "Derive voltage and conduction sequences."), ("Simuler", "Pour les deux premiers TP, reproduire le montage dans MATLAB/Simulink.", "For the first two labs, reproduce the circuit in MATLAB/Simulink."), ("Mesurer", "Comparer les formes d’onde au banc de TP.", "Compare waveforms at the lab bench.")],
                "image": ("power-electronics-lab-waveform.jpg", "Forme d’onde issue des mesures du TP d’électronique de puissance", "Waveform from the power-electronics laboratory report", "La mesure donne une lecture concrète des effets de conversion.", "Measurement makes conversion effects tangible."),
            },
            {
                "id": "evidence", "title": ("Trois comptes rendus à parcourir", "Three reports to explore"),
                "intro": ("Les trois PDF publiés sont les rapports d’origine du projet. Ils sont conservés tels quels, avec leurs schémas, simulations, relevés et conclusions.", "The three published PDFs are the original project reports. They are preserved as they were, with circuits, simulations, measurements and conclusions."),
                "paragraphs": [
                    ("Le premier décrit le redressement triphasé à diodes. Le deuxième traite du pont mixte monophasé. Le troisième analyse lissage et empiètement anodique. Ensemble, ils montrent comment passer d’une topologie de conversion à des grandeurs vérifiables.", "The first covers three-phase diode rectification. The second studies the single-phase semi-controlled bridge. The third examines smoothing and commutation overlap. Together they show how to move from converter topology to checkable quantities."),
                    ("Les résultats restent ceux de séances pédagogiques ; ils ne constituent ni un produit industriel ni une qualification d’équipement.", "The results belong to teaching labs; they are neither an industrial product nor an equipment qualification."),
                ],
                "points": [
                    ("P3 / PD3", "Dans le premier TP, environ 160 V à 3 A et 31,25 % d’ondulation en simple voie, contre 310 V à 3 A et 4,83 % en double voie.", "In the first lab, about 160 V at 3 A with 31.25% ripple for the single-way arrangement, versus 310 V at 3 A with 4.83% ripple for the bridge."),
                    ("Pont mixte", "Deux thyristors et deux diodes : la tension moyenne mesurée passe d’environ 230 V à 55 V lorsque l’angle passe de 0,07π à 2π/3.", "Two thyristors and two diodes: measured average voltage falls from about 230 V to 55 V as firing angle changes from 0.07π to 2π/3."),
                    ("Commutation", "Dans le troisième TP, la tension moyenne en simple voie passe de 156 V à 1,5 A à 151 V à 7 A. Ces valeurs restent celles du montage étudié.", "In the third lab, single-way mean voltage falls from 156 V at 1.5 A to 151 V at 7 A. These values apply to the documented setup."),
                ],
                "image": ("power-electronics-commutation.jpg", "Tensions des ponts supérieur et inférieur mesurées à l’oscilloscope dans le troisième TP", "Oscilloscope measurements of the upper and lower bridge voltages in the third lab", "Troisième TP : visualisation des tensions des deux demi-ponts et de la commutation.", "Third lab: measured half-bridge voltages and commutation behaviour."),
            },
            {
                "id": "takeaway", "title": ("Pourquoi ces TP comptent", "Why these labs matter"),
                "intro": ("Ils donnent une base concrète pour lire les convertisseurs : suivre les composants qui conduisent, anticiper l’effet de la commande et confronter calcul, simulation et banc.", "They provide a concrete basis for reading converters: trace conducting devices, predict control effects and compare calculation, simulation and bench data."),
                "paragraphs": [("Les liens ci-dessous pointent uniquement vers les trois rapports d’origine déjà publiés.", "The links below point only to the three original reports already published.")],
                "points": [],
            },
        ],
        "reports": None,
        "extra_reports": [
            ("../reports/tp-redressement-triphase-diodes.pdf", "Redressement triphasé à diodes", "Three-phase diode rectifier"),
            ("../reports/tp-pont-mixte-monophase.pdf", "Pont mixte monophasé", "Single-phase semi-controlled bridge"),
            ("../reports/tp-redressement-lissage-commutation.pdf", "Lissage et commutation", "Smoothing and commutation"),
        ],
        "repo": None,
    },
]


def clean(value):
    return escape(str(value), quote=True)


def translated(pair):
    return f'<span lang="fr">{clean(pair[0])}</span><span lang="en">{clean(pair[1])}</span>'


def asset_version(filename):
    """Refresh hosted CSS/JS when their content changes, including repeat builds."""
    return sha256((Path(__file__).resolve().parent / filename).read_bytes()).hexdigest()[:12]


CHAPTER_LABELS = {
    "problem": ("Contexte", "Problem"),
    "method": ("Méthode", "Method"),
    "evidence": ("Résultats", "Results"),
    "takeaway": ("Bilan", "Takeaways"),
}


IMAGE_SIZES = {
    "dc-motor-cascade.svg": (1200, 500), "dc-motor-response.png": (1920, 819),
    "foc-control.svg": (1200, 560), "foc-speed-tracking.png": (1350, 690),
    "grid-interface.png": (1915, 1003), "grid-loadflow-iterations.png": (1406, 656),
    "grid-transient-stability.png": (1406, 656), "mlp-convergence.png": (1152, 640),
    "mlp-network.svg": (1200, 560), "mlp-sequential-training.png": (1152, 544),
    "power-electronics-bridge-diodes.jpg": (1076, 328),
    "power-electronics-lab-waveform.jpg": (764, 627),
    "power-electronics-commutation.jpg": (1200, 904),
    "winding-flux-heatmap.png": (1152, 720), "winding-flux-lines.png": (1152, 720),
    "winding-mmf.png": (4644, 2070),
}


def image(path, alt_fr, alt_en, *, eager=False):
    source = f"../assets/projects/{clean(path)}"
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
    return (
        '<figure class="figure">' + picture +
        '<figcaption><strong>FIGURE</strong><span>' + translated((caption_fr, caption_en)) +
        '</span></figcaption></figure>'
    )


def artifact_links(page):
    links = []
    if page.get("reports"):
        fr, en = page["reports"]
        links.append(
            f'<a class="report-link" data-fr="{clean(fr)}" data-en="{clean(en)}" '
            f'href="{clean(fr)}" target="_blank" rel="noopener">'
            + translated(("Lire le rapport complet · PDF", "Read the full report · PDF")) + '</a>'
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
}


def render_chapter(chapter, number, page):
    paragraphs = ''.join(f'<p>{translated(p)}</p>' for p in chapter.get("paragraphs", []))
    points = chapter.get("points", [])
    cards = (
        '<ul class="key-points">' + ''.join(
            '<li class="key-point"><b>' + translated((label, LABEL_EN.get(label, label))) + '</b><p>' + translated((fr, en)) + '</p></li>'
            for label, fr, en in points
        ) + '</ul>'
    ) if points else ''
    visual = figure(chapter["image"]) if chapter.get("image") else ''
    assets = artifact_links(page) if chapter["id"] == "takeaway" else ''
    return (
        f'<section class="chapter" id="{clean(chapter["id"])}" aria-labelledby="h-{clean(chapter["id"])}">'
        f'<div class="chapter-head"><span class="chapter-no">{number:02d} / 04</span></div>'
        f'<h2 id="h-{clean(chapter["id"])}">{translated(chapter["title"])}</h2>'
        f'<p class="intro">{translated(chapter["intro"])}</p>'
        f'<div class="prose">{paragraphs}</div>{cards}{visual}{assets}</section>'
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
        report_action = (
            f'<a class="button ghost report-link" data-fr="{clean(fr)}" data-en="{clean(en)}" '
            f'href="{clean(fr)}" target="_blank" rel="noopener">'
            + translated(("Rapport PDF ↗", "PDF report ↗")) + '</a>'
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
