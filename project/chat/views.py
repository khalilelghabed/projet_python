from django.db.models import Q
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Conversation
from Utilisateurs.models import Utilisateur
from notification.models import Notification
from .models import Message, Conversation
from django.db.models import Max



def users(request):
    # Retrieve all utilisateur objects
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'home/chat.html', {'utilisateurs': utilisateurs})


@login_required
def conversation_messages(request, profile_user_id):
    # Fetch current user's ID
    user_id = request.user.id

    # Fetch or create conversation between the users
    user1 = request.user
    user2 = get_object_or_404(User, pk=profile_user_id)
    conversation = Conversation.objects.filter(Q(user1=user1, user2=user2) | Q(user1=user2, user2=user1)).first()
    if not conversation:
        conversation = Conversation.objects.create(user1=user1, user2=user2)

    # Fetch messages for the conversation
    messages = conversation.messages.all().order_by('timestamp')

    # Pass user_id and profile_user_id to the template context
    context = {
        'conversation': conversation,
        'user_id': user_id,
        'profile_user_id': profile_user_id,
        'messages': messages
    }

    return render(request, 'chat/conversation_messages.html', context)
