Interfaces de programmation
****************************

Models
============

.. automodule:: lettings.models
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: profiles.models
   :members:
   :undoc-members:
   :show-inheritance:


Views
==========

.. automodule:: lettings.views
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: profiles.views
   :members:
   :undoc-members:
   :show-inheritance:


URLs
==========

Page d'accueil
----------------
**URL:** ``/``

**Vue:** ``oc_lettings_site.views.index``

**Nom:** ``index``

**Description:** Page d'accueil principale du site.

Test d'erreur 500
-------------------
**URL:** ``/error/``

**Vue:** ``test_error_500``

**Nom:** ``error``

**Description:** Point d'entrée qui génère volontairement une exception pour tester la gestion des erreurs 500.

Lettings - Index
-------------------
**URL:** ``/lettings/``

**Vue:** ``lettings.views.index``

**Nom:** ``lettings_index``

**Description:** Liste de toutes les locations disponibles.

Letting - Détail
-------------------
**URL:** ``/lettings/<int:letting_id>/``

**Vue:** ``lettings.views.letting``

**Nom:** ``letting``

**Description:** Détails d'une location spécifique identifiée par son ID.

Profiles - Index
-------------------
**URL:** ``/profiles/``

**Vue:** ``profiles.views.index``

**Nom:** ``profiles_index``

**Description:** Liste de tous les profils utilisateurs.

Profile - Détail
-------------------
**URL:** ``/profiles/<str:username>/``

**Vue:** ``profiles.views.profile``

**Nom:** ``profile``

**Description:** Détails d'un profil utilisateur spécifique identifié par son nom d'utilisateur.

Administration
-------------------
**URL:** ``/admin/``

**Vue:** ``admin.site.urls``

**Description:** Interface d'administration Django.

Gestion des erreurs
-------------------
**404 Not Found Handler:** ``oc_lettings_site.views.custom_404``

**500 Server Error Handler:** ``oc_lettings_site.views.custom_500``

