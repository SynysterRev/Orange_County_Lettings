Déploiement
===========

Le déploiement de l'application est automatisé avec les GitHub Actions et Render.
Tout est configuré dans le fichier **ci.yml** qui se trouve dans **github/workflows/**.

Création d'une application avec Render
--------------------------------------

1. Connectez-vous sur Render en cliquant sur **Get Started for Free**
2. Ajouter un nouveau **Web Service**
3. Choissisez **Existing Image** et renseignez le lien vers l'image docker que vous
   souhaitez utiliser.
4. Configurez les **Environment Variables** pour y ajouter :

   - DJANGO_SETTINGS_MODULE (oc_lettings_site.settings.production)
   - SECRET_KEY
   - SENTRY_DSN

Docker
------

Commencez par créer un compte sur Docker Hub et installez l'application. Puis créer
un repository **orange-county-lettings** sur Docker Hub. Une fois
cela fait vous pourrez utilisez les commandes suivantes pour tester en local :

.. note::
   Pensez à mettre votre variable DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.base
   dans votre .env pour des tests en local.

Pour créer l'image :

.. code-block:: bash

   docker build -t dockerusername/orange-county-lettings:latest .

Pour faire lancer l'image (à utiliser dans le répertoire où se trouve votre .env) :

.. code-block:: bash

   docker run --env-file .env -p 8000:8000 dockerusername/orange-county-lettings:latest


Configuration des GitHub Actions
---------------------------------

Dans votre repository GitHub, configurez les secrets suivants :

* ``DOCKER_USERNAME`` : Votre nom d'utilisateur Docker Hub
* ``DOCKERHUB_TOKEN`` : Votre token a récupéré sur Docker Hub
* ``RENDER_DEPLOY_HOOK`` : A récupérer dans les paramètres de votre dashboard
* ``RENDER_API_KEY`` : Votre clé API Render
* ``SECRET_KEY`` : La clé secrète Django
* ``SENTRY_DSN`` : Le DSN sentry afin de gérer la journalisation

Le projet utilise GitHub Actions pour automatiser le déploiement. Seuls les commits
sur la branche master déclencheront le déploiment. Les autres branches ne
déclencheront que les tests et le linting.

Le workflow est le suivant :

1. **Tests** : Exécute les tests pour vérifier si la couverture est d'au moins 80% et
le linting
2. **Build** : Construit l'image Docker et pousse l'image vers Docker Hub
3. **Deploy** : Déploie l'application sur Render en utilisant la dernière image