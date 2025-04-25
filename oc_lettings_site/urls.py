from django.contrib import admin
from django.urls import path

import lettings.views
import profiles.views
from . import views


def test(request):
    raise Exception('test')


handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'

urlpatterns = [
    path('', views.index, name='index'),
    path('error/', test, name='error'),
    path('lettings/', lettings.views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),
    path('profiles/', profiles.views.index, name='profiles_index'),
    path('profiles/<str:username>/', profiles.views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
