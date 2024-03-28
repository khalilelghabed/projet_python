from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[

    path('chat/', views.users, name='users'),
    path('conversation_messages/<int:profile_user_id>/', views.conversation_messages, name='conversation_messages')

]