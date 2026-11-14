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

## Qualité audio

- Le contexte audio tourne à la fréquence d'échantillonnage native du fichier (lue dans l'en-tête WAV), ce qui évite tout rééchantillonnage par le navigateur.
- Le fichier entendu est joué à un gain d'exactement 1.0 : aucun traitement, aucune normalisation.
- Au moment du basculement, un fondu de 5 ms évite le clic. En dehors de ce fondu, le signal n'est pas modifié.
- Les fichiers restent sur votre machine : rien n'est envoyé sur Internet.

Le mixeur du système d'exploitation peut toutefois convertir le signal si la fréquence de la carte son est différente de celle du fichier. Pour une écoute bit-perfect, réglez la sortie audio du système sur la même fréquence que vos fichiers.
