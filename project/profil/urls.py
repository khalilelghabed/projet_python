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
    path('<int:user_id>/update_etu/', views.update_information_etu, name='update_etu'),
    path('<int:user_id>/update_ens/', views.update_information_ens, name='update_ens'),
    path('<int:user_id>/update_ent/', views.update_information_ent, name='update_ent'),
    
]