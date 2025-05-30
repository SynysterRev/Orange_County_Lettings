## Résumé

Site web d'Orange County Lettings

Pour une documentation plus détaillée
[ReadTheDocs](https://docholidayhomes.readthedocs.io/fr/latest/)

## Installation

### Clonage du dépôt

Clonez le dépôt de code avec la commande ```git clone https://github.com/SynysterRev/Orange_County_Lettings/```

### Créer l'environnement virtuel

#### Windows
```python -m venv venv```

#### MacOS ou Linux
```python3 -m venv venv```

### Activation de l'environnement virtuel

#### Windows
```.\venv\Scripts\activate```

#### MacOS ou Linux
```source venv/bin/activate```

### Installation des dépendances
```pip install -r requirements.txt```

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
