from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('accounts/',include('authantification.urls')),
    path('publications/',include('publications.urls')),
    path('classe privé/',include('ClassePrive.urls')),
    path('utilisateurs/',include('Utilisateurs.urls')),
    path('profil/<int:user_id>/', include('profil.urls')),
    path('update-profile/<int:user_id>/', include('profil.urls')),
        
    path('profil/', include('profil.urls')),

    path('notificatons/',include('notification.urls')),
    path('home/',include('chat.urls')),
    path('home/',include('Utilisateurs.urls')),
    path('search/',include('search.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)