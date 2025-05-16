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

## Github Actions
Lors d'un push sur la branche master (ou tout autre branche) :
- les tests unitaires seront lancés pour voir si tout fonctionne et que la couverture atteint au minimum 80%.
- le linting sera lancé pour voir si le code correspond aux normes
Si une de ces actions échoue les suivantes (celles si ne s'appliquent que pour la branche master) ne s'exécuteront pas.
- créer d'une image docker
- tag cette image avec le hash du commit ainsi que latest
- push de l'image sur dockerhub

Pour que tout cela fonctionne il faudra remplir les secrets suivants sur votre github:
- DJANGO_SETTINGS_MODULE
- DOCKERHUB_TOKEN (le token permettant d'effectuer les [actions nécessaires](https://docs.docker.com/security/for-developers/access-tokens/) sur votre compte)
- DOCKERHUB_USERNAME (votre nom utilisateur sur dockerhub)
- SECRET_KEY (pour le projet Django)
- SENTRY_DSN

## Docker
Récupérer la dernière image avec `docker pull yourusername/orange-county-lettings:latest`

`yourusername` correspond à votre nom d'utilisateur sur dockerhub

#### Test en local
- dans votre .env local, utiliser `DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.base`
- utiliser la commande `docker run --env-file .env -p 8000:8000 yourusername/orange-county-lettings:latest` dans le répertoire où se trouve votre .env
- aller sur `http://localhost:8000`
