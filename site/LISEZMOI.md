# Comparo Studio : mise en ligne

Ce dossier est un site statique complet : il n'y a ni base de données, ni PHP, ni Node.js à installer. Tout se passe dans le navigateur de l'utilisateur.

## Mettre en ligne

1. Copiez **tout le contenu** de ce dossier (y compris `fonts/` et le fichier caché `.htaccess`) à la racine de votre site, ou dans un sous-dossier, par exemple `https://votre-site.fr/comparo/`.
   - Hébergement mutualisé (OVH, o2switch, Ionos…) : par FTP/SFTP avec FileZilla, dans `www/` ou `public_html/`.
   - Netlify, Vercel, Cloudflare Pages, GitHub Pages : déposez le dossier tel quel, sans étape de build.
2. Ouvrez l'adresse dans le navigateur. C'est tout.

**HTTPS est recommandé.** Sans HTTPS, l'outil fonctionne, mais le mode hors ligne et l'installation comme application sont désactivés par les navigateurs.

## Fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | L'application complète (Comparo, Notes, Ghost) |
| `fonts/` | Polices hébergées localement (licence SIL OFL), aucun appel à Google |
| `favicon.svg` | Icône de l'onglet et de l'application installée |
| `manifest.webmanifest` | Permet d'installer Comparo comme une application |
| `sw.js` | Mode hors ligne : l'outil s'ouvre même sans connexion après une première visite |
| `.htaccess` | Réglages Apache (types de fichiers, cache). Ignoré par les autres serveurs |

### Nginx

Si votre serveur est en Nginx, le `.htaccess` n'est pas lu. Ajoutez au besoin :

```nginx
location ~* \.(woff2|svg|webmanifest)$ { add_header Cache-Control "public, max-age=2592000"; }
location ~* ^/(index\.html|sw\.js)$   { add_header Cache-Control "no-cache"; }
types { application/manifest+json webmanifest; }
```

## Données et vie privée

- Les fichiers audio ne quittent jamais l'ordinateur de l'utilisateur : rien n'est envoyé au serveur.
- Les projets de **Notes** sont enregistrés dans le navigateur de chaque utilisateur. Ils ne sont pas partagés entre appareils, et vider les données du navigateur les efface. Le bouton **Exporter mes projets**, en bas de la page Notes, crée une sauvegarde à garder, et **Importer une sauvegarde** la restaure, y compris sur un autre appareil.
- Aucune police, aucun script ni aucune statistique n'est chargé depuis un autre site.

## Mettre à jour

Remplacez les fichiers sur le serveur par la nouvelle version. Les utilisateurs reçoivent la mise à jour à leur prochaine visite.

Pour les développeurs : ce dossier est généré à partir de `index.html` à la racine du dépôt avec `python3 tools/build-site.py`.
