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
]
