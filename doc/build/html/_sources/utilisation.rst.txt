Guide d'utilisation
====================

Accès au site
-------------

Pour accéder à la page d'accueil du site

.. code-block:: none

   #Site déployé
   https://orange-county-lettings-l543.onrender.com/

   #Test local
   http://127.0.0.1:8000/


Accès aux profils utilisateurs
-----------------------------------------

Depuis la page d'accueil vous pouvez soit cliquez sur le bouton "Profiles" pour voir la
liste des profils
utilisateurs, soit rajouter **/profiles/** dans l'URL.

.. code-block:: none

   https://orange-county-lettings-l543.onrender.com/profiles/

Accès aux détails d'un utilisateur
-----------------------------------------

Une fois dans la page des profils cliquez sur un profil pour accéder à ses détails.

.. code-block:: none

   https://orange-county-lettings-l543.onrender.com/profiles/<nom-utilisateur>/

**Si le nom d'utilisateur n'existe pas cela vous renverra sur une page erreur 404.**


Accès aux locations
-------------------------------

Depuis la page d'accueil vous pouvez soit cliquez sur le bouton "Lettings" pour voir la
liste des locations, soit rajouter **/lettings/** dans l'URL.

.. code-block:: none

   https://orange-county-lettings-l543.onrender.com/lettings/

Accès aux détails d'une location
---------------------------------

Une fois dans la page des locations cliquez sur une location pour accéder à ses détails.

.. code-block:: none

   https://orange-county-lettings-l543.onrender.com/lettings/<id-location>/

**Si l'id de la location n'existe pas cela vous renverra sur une page erreur 404.**


Administration
---------------

Les administrateurs peuvent se rendre dans la section **admin** afin d'ajouter,
modifier ou supprimer des locations et des profiles.

.. code-block:: none

   https://orange-county-lettings-l543.onrender.com/admin/

