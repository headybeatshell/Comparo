# Comparo

Outil de comparaison A/B entre deux fichiers audio `.wav`, dans le navigateur.

## Utilisation

Ouvrir `index.html` dans un navigateur (Chrome, Firefox, Safari). Il n'y a rien à installer et aucun serveur à lancer.

1. Déposer un fichier `.wav` sur **A** et un autre sur **B**, ou cliquer sur une case pour choisir le fichier. On peut aussi déposer les deux fichiers d'un coup n'importe où sur la page.
2. Appuyer sur **▶** : les deux fichiers démarrent ensemble, parfaitement synchronisés.
3. Basculer entre A et B pendant la lecture.

| Touche | Action |
|---|---|
| `Espace` | Lecture / pause |
| `Tab`, `←`, `→` | Basculer A ⇄ B |
| `A` / `B` (ou `1` / `2`) | Choisir A ou B |

## Options

### Écouter sur (simulateur de « translation »)

Réécoute le mix comme sur un autre système de diffusion. Le traitement s'applique à A et à B, ce qui permet de continuer la comparaison :

- **Haut-parleur de téléphone** : son mono, sans basses sous ~500 Hz, médiums durs, petite pièce.
- **Écouteurs bas de gamme** : basses maigres, pic agressif vers 4–5 kHz.
- **Voiture** : basses gonflées par l'habitacle, aigus ternes, réflexions courtes.
- **Enceinte Bluetooth** : son mono, bosse de basse vers 130 Hz, limiteur, pièce moyenne.

Ce sont des filtres et une petite réverb de pièce : une approximation pour vérifier la translation, pas la mesure d'un appareil précis.

### Normalisation streaming

Chaque fichier est analysé au chargement :
- **Loudness intégré** en LUFS, selon la norme ITU-R BS.1770-4.
- **True peak** en dBTP, avec suréchantillonnage ×4.

Une crête au-dessus de −1 dBTP est signalée, car elle risque de saturer après encodage.

Choisir une plateforme applique le gain qu'elle utiliserait et affiche le niveau final de A et B :

| Plateforme | Cible | Morceaux calmes |
|---|---|---|
| Spotify (Normal) | −14 LUFS | montés, sans dépasser −1 dBTP |
| Apple Music (Sound Check) | −16 LUFS | montés dans la limite de leur marge de crête |
| YouTube | −14 LUFS | jamais montés |

## Notes

Un deuxième outil, accessible par le sélecteur **Comparo / Notes** en haut de page, ou directement avec l'adresse `#notes`.

- **Projets** : suivez vos morceaux inachevés par étape (Idée, Composition, Arrangement, Mix, Master, Terminé). Un projet non modifié depuis 14 jours est signalé comme « en pause ».
- **Versions (bounces)** : déposez un fichier audio sur la page d'un projet pour l'ajouter comme V1, V2, V3… avec un commentaire sur ce qui change.
- **Notes sur la timeline** : pendant la lecture, commencez à taper (ou appuyez sur `N`) : la note est placée à l'instant où vous avez commencé. Cliquez sur un repère ou sur l'heure d'une note pour y revenir.
- **Vers Comparo** : « Mettre en A / B » envoie une version dans Comparo pour la comparer à une autre.

Les projets et les notes sont enregistrés dans le navigateur (ou sur votre compte quand la page est ouverte sur claude.ai). Les fichiers audio ne sont jamais envoyés : la forme d'onde et les notes sont gardées, mais il faut associer à nouveau le fichier pour réécouter une version lors d'une prochaine visite.

La version précédente, sans Notes, est conservée dans `versions/comparo-v1.html`.

## Ghost

Troisième outil, accessible par le sélecteur **Comparo / Notes / Ghost**, ou directement avec l'adresse `#ghost`. C'est un détecteur de masquage : chargez deux stems (kick et basse, voix et guitare…) exportés depuis le même point de départ.

- **Spectre moyen** : les deux spectres superposés, avec les zones de conflit en corail.
- **Dans le temps** : où et quand les deux stems se masquent (cliquez pour vous placer).
- **Zones de conflit** : jusqu'à six plages de fréquences classées, avec la part du temps où elles se masquent, le stem le plus fort et une piste de correction (EQ ou sidechain si le conflit est intermittent).
- **Écouter** : isole la zone avec un filtre passe-bande pendant la lecture, avec A + B, A seul ou B seul.

L'analyse se fait en tranches de 1/6 d'octave : deux stems sont en conflit dans une tranche quand ils y sont tous deux présents au même moment, avec des niveaux proches (moins de 12 dB d'écart).

## Qualité audio

- Le contexte audio tourne à la fréquence d'échantillonnage native du fichier (lue dans l'en-tête WAV), ce qui évite tout rééchantillonnage par le navigateur.
- Avec « Studio (original) » et « Aucune » normalisation (réglages par défaut), le fichier entendu est joué à un gain d'exactement 1.0 : aucun traitement, aucune normalisation.
- Au moment du basculement, un fondu de 5 ms évite le clic. En dehors de ce fondu, le signal n'est pas modifié.
- Les fichiers restent sur votre machine : rien n'est envoyé sur Internet.

Le mixeur du système d'exploitation peut toutefois convertir le signal si la fréquence de la carte son est différente de celle du fichier. Pour une écoute bit-perfect, réglez la sortie audio du système sur la même fréquence que vos fichiers.
