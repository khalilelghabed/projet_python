from django.db import models
from Utilisateurs.models import Utilisateur

class Notification(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, blank=False, null=True,related_name="notifier")
    message = models.CharField(max_length=255)
    date_creation=models.DateTimeField(auto_now_add=True,blank=False)
    
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message
