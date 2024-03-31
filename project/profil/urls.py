# profil/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.profil_page, name='profil_page'),
# ]


# profil/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profil_page, name='profil_page'),
    path('update_donnes/',views.update_information,name='update'),
    path('search/',views.profil_search, name='profil_search'),
    
]