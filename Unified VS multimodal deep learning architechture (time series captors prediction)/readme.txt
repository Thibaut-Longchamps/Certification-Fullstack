Merci de télécharger le fichier ATC_Final_notebook (1) pour consulter le code des models (La lecture ne fonctionne pas sur Github)

______________________________________________________________________________________________________________________________________________________________________________

Ressources :

• Jeux de données à télécharger : https://figshare.com/articles/dataset/MovePort_Multimodal_Dataset_of_EMG_IMU_MoCap_and_Insole_Pressure_for_Analyzing_Abnormal_Movements_and_Postures_in_Rehabilitation_Training/25202183?file=46577461

• Article lié au jeu de données :
https://ieeexplore.ieee.org/document/10601196

__________________________________________________________________________________________________________________________________________________________________________________

Structure des Données
Les données sont organisées par participant (1 à 25), et chaque participant a des enregistrements pour différentes activités/mouvements :

back : Inclinaison vers l'arrière.
forward : Inclinaison vers l'avant.
halfsquat : Demi-squat.
still : Position debout immobile.
treadmill_normal : Marche normale à trois vitesses.
treadmill_leghigh : Marche avec levée de jambe exagérée.
treadmill_dragging : Marche traînante simulant une difficulté à lever les jambes.



____________________________________________________________________________________________________________________________________________________________________________________
DATA INFORMATIONS !! :

This is the open access MovePort dataset published with our paper entitled: 
"MovePort: Multimodal Dataset of EMG, IMU, MoCap and Insole Pressure for Analyzing Abnormal Movements and Postures in Rehabilitation Training".

When using our dataset, please cite the above article.



Part 1. File Structure

The exported data is stored in the "data" folder. The file structure is as follows:
data:
├─1
│  …………
└─25
    ├─back
    ├─forward
    ├─halfsquat
    ├─still
    ├─ground_gait (only available for the subject with spastic paraplegia)
    ├─treadmill_normal
    ├─treadmill_leghigh
    └─treadmill_dragging
where 1-25 is the index of each participant.





Part 2. Introduction of Experimental Paradigm

Experiment 1: Participants are required to perform specific gaits on a treadmill.
	Normal Gait (treadmill_normal): This mode includes three speeds of normal walking.
	Low Speed: Walking at a speed of 1 km/h.
	Medium Speed: Walking at a speed of 2 km/h.
	High Speed (customizable): Walking at a speed of 3-4 km/h, with the specific speed chosen by the participants for comfortable brisk walking.

	Dragging Gait (dragging): Simulating a patient's difficulty in lifting their legs with a speed of 1 km/h, representing an abnormal gait.
	High Leg Lift Gait (leghigh): Simulating excessively high leg lifts due to overstimulation (e.g. the epidural/functional electrical stimulation used in neurorehabilitation) with a speed of 2 km/h, representing an abnormal gait.

Experiment 2: Participants are required to perform specific body postures on ground
	Standing still（still）： Standard standing without any special movements.
	Forward Lean（forward）：Participants lean their bodies forward to simulate a forward-weighted posture.
	Backward Lean (back): Participants tilt their bodies backward to simulate a backward-weighted posture.
	Half Squat (halfsquat): Participants perform a half-squat to simulate a posture with inadequate support.







Part 3.	Introduction to Data Files

The naming format of data files is: modality_SegmentIndex.csv/avi
Descriptions of different data modalities are as follows:
	Electromyography (EMG) Data
Modality Name: emg
Data Size: 16*nframe
Sampling Rate: 2000 Hz
Unit: Microvolts
Each column of data contains raw data from 8 muscles on each leg, named as: L/R_muscle_abbreviation

Muscle abbreviations are as follows:
Vlat - Vastus Lateralis
RF - Rectus Femoris
ST - Semitendinosus
TA - Tibialis Anterior
MG - Medial Gastrocnemius
LG - Lateral Gastrocnemius
SOL - Soleus
IL - Iliopsoas

	Inertial Measurement Unit (IMU) Data
Modality Name: imu
Data Size: 54*nframe
Sampling Rate: 100 Hz
Units: Acceleration (M/s²), Angular Velocity (°/s), Euler Angles (°)
Each column of data contains 9-axis data from 6 body positions of IMU, named as: Position_axis

Positions of IMU sensors are as follows:
Head, Waist (near Pelvis)
L_H - Left Hand/Wrist, R_H - Right Hand/Wrist
L_F - Left Foot, R_F - Right Foot

Axis names are as follows：
Acc_X/Y/Z - Acceleration along x, y, and z axes
Gyr_X/Y/Z - Angular velocity along x, y, and z axes
Roll, Pitch, Yaw - Euler angles along three axes

	Insole Pressure Sensors (IPS) Data
Modality Name: ips
Data Size: 682*nframe
Sampling Rate: 60 Hz
Unit: psi
Each column contains a 682-length vector of feet pressure distribution (measured by two 31*11 electrode arrays, one array per feet; 1-341 dimensions: left foot; 342-682: right foot). 230 out of the 341 electrodes (each side) are active, with other electrodes giving 0 values. But we still give a 31*11 (=341) electrode array so that the data can be represented as a 2-dimensional matrix.

Modality Name: Center of Pressure (COP)
COP data are highly correlated with IPS data.
Data Size: 6*nframe
Sampling Rate: 60 Hz
Units: N, m
Each column contains total pressure values, and (in certain files) we also give the calculated pressure center coordinates of the feet, named as follows:
L/R_Force: Total pressure on the left/right foot
L/R_cop_x: X-axis coordinates of the pressure center on the left/right foot
L/R_cop_y: Y-axis coordinates of the pressure center on the left/right foot
Note: The coordinate system used for the center of pressure is consistent with the one used for the motion capture system.

	Motion Capture (MoCap) Data
Modality Name: mocap
Data Size: 78*nframe
Sampling Rate: 100 Hz
Unit: meters
Each column contains three-dimensional spatial coordinates of 26 motion capture markers, named as: marker_name_x/y/z
Specific marker names are explained as follows:


Marker Label	Location Description
IJ		Jugular Notch, located above the sternum handle, where the left and right clavicles connect
C7 		7th cervical vertebra, located at the highest protrusion behind the bent neck
RA		Right Acromion, the flat part above the right shoulder joint's front and outside
LA 		Left Acromion, the flat part above the left shoulder joint's front and outside
T8 		8th thoracic vertebra, counting up to the 8th rib, connected to it is the 8th thoracic vertebra
R_LHE 		Right Elbow Joint, outside
R_RS 		Right Wrist Joint, outside
L_LHE 		Left Elbow Joint, outside
L_RS   		Left Wrist Joint, outside
M_PSIS		Posterior Superior Iliac Spine, located at the rear end of the iliac crest
R_IAS		Right Anterior Superior Iliac Spine, located at the front of the right iliac crest
R_FTC		Right Greater Trochanter, at the junction of the right femoral neck and body on the upper outside
L_IAS		Left Anterior Superior Iliac Spine, located at the front of the left iliac crest
L_FTC		Left Greater Trochanter, at the junction of the left femoral neck and body on the upper outside
R_FLE		Right Knee Joint, outside
R_FME		Right Knee Joint, inside
R_TTC		Right Tibial Plateau
R_LM		Right Ankle Joint, outside
R_CAL		Right Heel
R_MH1		The 1st toe of the right foot
L_FlE		Left Knee Joint, outside
L_FME		Left Knee Joint, inside
L_TTC		Left Tibial Plateau
L_LM		Left Ankle Joint, outside
L_CAL		Left Heel
L_MH1		The 1st toe of the left foot






Note: Data is missing for some participants. Specific missing data is as follows:
Participants 18, 19, 20 and 24: data of the "leaning forward" body posture are not available. 
Participant 21: data of the "leaning forward" body posture and normal gait at low-speed are not available. 
Participant 22: data of the "leaning back" body posture are not available.  
Participant 23: data of the "leaning forward" and "half-squat" body postures are not available. 





Partie 2. Introduction au Paradigme Expérimental
Expérience 1 : Les participants doivent réaliser des démarches spécifiques sur un tapis roulant.

Démarche normale (treadmill_normal) : Ce mode comprend trois vitesses de marche normale.

Vitesse faible : Marche à une vitesse de 1 km/h.
Vitesse moyenne : Marche à une vitesse de 2 km/h.
Vitesse rapide (personnalisable) : Marche à une vitesse de 3-4 km/h, choisie par les participants pour un rythme de marche rapide confortable.
Démarche avec traînage (dragging) : Simule la difficulté d'un patient à lever les jambes à une vitesse de 1 km/h, représentant une démarche anormale.

Démarche avec levée de jambe élevée (leghigh) : Simule une levée de jambe excessivement haute due à une surstimulation (par ex. : stimulation épidurale/fonctionnelle électrique utilisée en neuro-rééducation) à une vitesse de 2 km/h, représentant une démarche anormale.

Expérience 2 : Les participants doivent réaliser des postures spécifiques au sol.

Debout immobile (still) : Position debout standard sans mouvements particuliers.
Inclinaison vers l'avant (forward) : Les participants inclinent leur corps vers l'avant pour simuler une posture en appui vers l'avant.
Inclinaison vers l'arrière (back) : Les participants penchent leur corps vers l'arrière pour simuler une posture en appui vers l'arrière.
Demi-squat (halfsquat) : Les participants effectuent un demi-squat pour simuler une posture avec un soutien insuffisant.
Partie 3. Introduction aux Fichiers de Données
Le format de nommage des fichiers de données est le suivant : modality_SegmentIndex.csv/avi Les descriptions des différentes modalités de données sont les suivantes :




Données d'Électromyographie (EMG)

Nom de la Modalité : emg
Taille des Données : 16*nframe
Fréquence d'Échantillonnage : 2000 Hz
Unité : Microvolts
Chaque colonne de données contient les données brutes de 8 muscles sur chaque jambe, nommées comme suit : L/R_abbréviation_muscle
Les abréviations musculaires sont les suivantes :

Vlat : Vaste Latéral
RF : Droit Fémoral
ST : Semi-tendineux
TA : Tibial Antérieur
MG : Gastrocnémien Médial
LG : Gastrocnémien Latéral
SOL : Soléaire
IL : Ilio-psoas
Données d'Unités de Mesure Inertielle (IMU)




Nom de la Modalité : imu
Taille des Données : 54*nframe
Fréquence d'Échantillonnage : 100 Hz
Unités : Accélération (M/s²), Vitesse Angulaire (°/s), Angles d'Euler (°)
Chaque colonne de données contient des données 9 axes de 6 positions corporelles de l'IMU, nommées comme suit : Position_axe
Positions des capteurs IMU :

Head : Tête, Waist : Taille (près du Bassin)
L_H : Main/Poignet Gauche, R_H : Main/Poignet Droit
L_F : Pied Gauche, R_F : Pied Droit
Noms des axes :

Acc_X/Y/Z : Accélération selon les axes x, y, et z
Gyr_X/Y/Z : Vitesse angulaire selon les axes x, y, et z
Roll, Pitch, Yaw : Angles d'Euler selon les trois axes
Données des Capteurs de Pression Plantaire (IPS)





Nom de la Modalité : ips
Taille des Données : 682*nframe
Fréquence d'Échantillonnage : 60 Hz
Unité : psi
Chaque colonne contient un vecteur de longueur 682 de la distribution de pression sous les pieds (mesuré par deux matrices de 31x11 électrodes, une par pied ; dimensions 1-341 : pied gauche ; 342-682 : pied droit). 230 des 341 électrodes (chaque côté) sont actives, les autres affichent une valeur de 0. Cependant, les données sont présentées sous forme de matrice 31x11 (=341) pour une représentation en 2D.
Nom de la Modalité : Centre de Pression (COP)

Les données COP sont fortement corrélées aux données IPS.
Taille des Données : 6*nframe
Fréquence d'Échantillonnage : 60 Hz
Unités : N, m
Chaque colonne contient les valeurs de pression totale, et (dans certains fichiers) les coordonnées du centre de pression des pieds, nommées comme suit :
L/R_Force : Pression totale sur le pied gauche/droit
L/R_cop_x : Coordonnées sur l'axe X du centre de pression pour le pied gauche/droit
L/R_cop_y : Coordonnées sur l'axe Y du centre de pression pour le pied gauche/droit
Remarque : Le système de coordonnées utilisé pour le centre de pression est compatible avec celui du système de capture de mouvement.
Données de Capture de Mouvement (MoCap)





Nom de la Modalité : mocap
Taille des Données : 78*nframe
Fréquence d'Échantillonnage : 100 Hz
Unité : mètres
Chaque colonne contient les coordonnées spatiales en trois dimensions de 26 marqueurs de capture de mouvement, nommées comme suit : nom_marqueur_x/y/z
Descriptions des Marqueurs :

IJ : Incisure Jugulaire, au-dessus du sternum, où les clavicules se rejoignent
C7 : 7ème vertèbre cervicale, située à la plus haute proéminence derrière le cou
RA : Acromion Droit, partie plate au-dessus de l'articulation de l'épaule droite
LA : Acromion Gauche, partie plate au-dessus de l'articulation de l'épaule gauche
T8 : 8ème vertèbre thoracique, attachée à la 8ème côte
Et autres positions spécifiques pour chaque articulation et zone du corps.
Remarque : Certaines données manquent pour certains participants. Les données spécifiques manquantes sont les suivantes :




Participants 18, 19, 20 et 24 : données de la posture "inclinaison vers l'avant" non disponibles.
Participant 21 : données de la posture "inclinaison vers l'avant" et de la démarche normale à basse vitesse non disponibles.
Participant 22 : données de la posture "inclinaison vers l'arrière" non disponibles.
Participant 23 : données des postures "inclinaison vers l'avant" et "demi-squat" non disponibles.
