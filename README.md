## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirements requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Configuration

> ⚠️ **ATTENTION** : n'oubliez pas de remplir votre fichier `.env` avant de lancer l'application !
>
> Copiez `.env.example` en `.env` puis modifiez-le avec vos valeurs.

## Sentry
Pour utiliser Sentry, il faut créer un compte [Sentry](https://sentry.io/). Ensuite, créer un nouveau projet et sélectionner: Django. Suivre le guide de configuration et chercher la ligne contenant : `dsn="https://your-key@sentry.io/your-project-id"` qu'il faudra renseigner dans le `.env`.

## Github Actions
Lors d'un push sur la branche master (ou tout autre branche) :
- les tests unitaires seront lancés pour vérifier que tout fonctionne et que la couverture atteint au minimum 80 %.
- le linting sera exécuté pour s'assurer que le code respecte les normes.
Si l’une de ces actions échoue, les suivantes (celles-ci ne s’appliquent qu’à la branche master) ne seront pas exécutées.
- création d'une image docker
- l'image est taguée avec le hash du commit ainsi qu’avec latest
- push de l'image sur dockerhub
- récupération de cette image et envoie sur Render pour le déploiement

Pour que tout cela fonctionne, vous devrez renseigner les secrets suivants dans votre dépôt github:
- DOCKERHUB_TOKEN (le token permettant d'effectuer les [actions nécessaires](https://docs.docker.com/security/for-developers/access-tokens/) sur votre compte)
- DOCKERHUB_USERNAME (votre nom utilisateur sur dockerhub)
- SECRET_KEY (pour le projet Django)
- SENTRY_DSN
- RENDER_DEPLOY_HOOK (que vous pouvez trouver dans les settings de votre dashboard)
- RENDER_API_KEY (dans les settings de votre compte Render)

#### Makefile
Toutes les actions précédentes peuvent être réalisées en local grâce au Makefile:
- make build user=`yourusername` -> build une image avec le tag latest
- make push user=`yourusername` -> push l'image créée
- make run user=`yourusername` -> run l'image créée
- make full user=`yourusername` -> exécute toutes les actions précédentes

`yourusername` correspond à votre nom d'utilisateur sur dockerhub

## Docker
Récupérer la dernière image avec `docker pull yourusername/orange-county-lettings:latest`

#### Test en local
- dans votre .env local, utiliser `DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.base`
- utiliser la commande `docker run --env-file .env -p 8000:8000 yourusername/orange-county-lettings:latest` dans le répertoire où se trouve votre .env
- aller sur `http://localhost:8000`

Vous pouvez également utiliser `docker run --env-file .env -p 8000:8000 -v "$(pwd):/app" yourusername/orange-county-lettings:latest` afin de pouvoir voir les modifications sur le code en temps réel.

## Render
- Créez-vous un compte sur [Render](https://render.com/)
- Créez un nouveau WebService, sélectionner depuis une image Docker et renseigner le lien vers celle-ci
- Rendez-vous dans "Manage/Environment" et ajouter les variables DJANGO_SETTINGS_MODULE (oc_lettings_site.settings.production), SECRET_KEY et SENTRY_DSN

## Déploiement
Lorsque les tests et le lintings sont validés et que la dockerisation s'est déroulée avec succès l'image créée est récupérée et envoyé sur Render, il se chargera alors de récupérer l’image et de la déployer en mode production.

Il est également possible de redéployer l'image depuis le dashboard Render en cliquant sur le bouton `Manual Deploy`.
