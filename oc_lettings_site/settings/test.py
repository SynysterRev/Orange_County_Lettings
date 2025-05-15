from .base import *  # noqa: F401, F403

# Désactivation des paramètres de sécurité pour les tests
DEBUG = True

SECRET_KEY = 'test_secret_key'

# Désactivation des redirections SSL pour les tests
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Utiliser une base de données en mémoire pour les tests rapides
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Configuration de mot de passe simplifiée pour accélérer les tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
