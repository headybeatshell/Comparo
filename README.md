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

## Qualité audio

- Le contexte audio tourne à la fréquence d'échantillonnage native du fichier (lue dans l'en-tête WAV), ce qui évite tout rééchantillonnage par le navigateur.
- Avec « Studio (original) » et « Aucune » normalisation (réglages par défaut), le fichier entendu est joué à un gain d'exactement 1.0 : aucun traitement, aucune normalisation.
- Au moment du basculement, un fondu de 5 ms évite le clic. En dehors de ce fondu, le signal n'est pas modifié.
- Les fichiers restent sur votre machine : rien n'est envoyé sur Internet.

Le mixeur du système d'exploitation peut toutefois convertir le signal si la fréquence de la carte son est différente de celle du fichier. Pour une écoute bit-perfect, réglez la sortie audio du système sur la même fréquence que vos fichiers.
