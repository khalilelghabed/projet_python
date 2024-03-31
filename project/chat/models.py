from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Conversation(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_conversations')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blocked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user1', 'user2')

    def save(self, *args, **kwargs):
        if self.pk is None:  # If it's a new conversation being saved
            # Check if a conversation already exists between the same two users
            existing_conversation = Conversation.objects.filter(
                (models.Q(user1=self.user1) & models.Q(user2=self.user2)) |
                (models.Q(user1=self.user2) & models.Q(user2=self.user1))
            ).first()
            if existing_conversation:
                raise ValidationError('Conversation already exists between these users.')
        super().save(*args, **kwargs)

    @staticmethod
    def get_or_create_conversation(user1, user2):
        conversation = Conversation.objects.filter(
            (models.Q(user1=user1) & models.Q(user2=user2)) |
            (models.Q(user1=user2) & models.Q(user2=user1))
        ).first()

        if conversation:
            return conversation
        else:
            return Conversation.objects.create(user1=user1, user2=user2)

class Message(models.Model):
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField(blank=True)  # For text content
    file = models.FileField(upload_to='message_files/', blank=True, null=True)  # For any type of file
    image = models.ImageField(upload_to='message_images/', blank=True, null=True)  # For images
    video = models.FileField(upload_to='message_videos/', blank=True, null=True)  # For videos
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)  # New field to track message seen status

    def save(self, *args, **kwargs):
        if self.sender != self.conversation.user1 and self.sender != self.conversation.user2:
            raise ValidationError('Sender must be one of the conversation users.')

        if self.receiver != self.conversation.user1 and self.receiver != self.conversation.user2:
            raise ValidationError('Receiver must be one of the conversation users.')

        super().save(*args, **kwargs)
