from django.urls import path
from . import views

urlpatterns = [
    #path('chat/', views.users, name='users'),
    path('chat/conversation/<int:profile_user_id>', views.conversation_messages, name='conversation_messages'),
    path('chat/conversation/1', views.conversation_messages, name='users'),
    path('send-message/<int:profile_user_id>/', views.send_message, name='send_message'),
]
