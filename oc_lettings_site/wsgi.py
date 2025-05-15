import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      os.getenv('DJANGO_SETTINGS_MODULE',
                                'oc_lettings_site.settings.production'))

application = get_wsgi_application()
