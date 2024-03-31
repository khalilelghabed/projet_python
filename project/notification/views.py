from django.shortcuts import render
from django.http import JsonResponse   
from .models import Notification
def send_notification(request):
    utilisateur = request.user.utilisateur
    notifications = Notification.objects.filter(utilisateur=utilisateur).order_by('-date_creation')
    nombre_notif_non_lues=0
    for notif in notifications:
        if notif.is_read==False:
            nombre_notif_non_lues=nombre_notif_non_lues+1
    
    notifications_json = []
    for notification in notifications:
        notification_data = {
            'id': notification.id,
            'message': notification.message,
            'date_notification': notification.date_creation.strftime('%Y-%m-%d %H:%M:%S'),  # Formatter la date
            'is_read': notification.is_read,
            'image':notification.utilisateur.photo_profil.url,
            'non_lues':nombre_notif_non_lues
        }
        notifications_json.append(notification_data)
    # Marquer toutes les notifications comme lues après les avoir récupérées
    notifications.update(is_read=True)
    print(notifications_json)
    return JsonResponse({'notifications': notifications_json})