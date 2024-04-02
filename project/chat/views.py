from django.db.models import Q
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest

from django.contrib.auth.decorators import login_required

from Utilisateurs.models import Utilisateur
from notification.models import Notification
from .models import Message, Conversation
from .forms import MessageForm
from django.utils import timezone


from django.db.models import Q

def users(request):
    current_user = request.user
    search_query = request.GET.get('q')  # Get the search query from the request
    
    # Retrieve the current user's followers and following
    followers = current_user.utilisateur.followers.all()
    following = current_user.utilisateur.following.all()

    # Retrieve users that are following the current user and are being followed by the current user
    mutual_users = followers.filter(pk__in=following)
    
    # Filter mutual_users based on the search query
    if search_query:
        mutual_users = mutual_users.filter(Q(nom__icontains=search_query) | Q(prenom__icontains=search_query))

    # Create a dictionary to store the last message with each user
    last_messages = {}

    for utilisateur in mutual_users:
        # Get the conversation between the current user and the current utilisateur
        conversation = Conversation.objects.filter(
            Q(user1=current_user, user2=utilisateur.user) | Q(user1=utilisateur.user, user2=current_user)
        ).first()
        
        # Get the last message in this conversation
        last_message = conversation.messages.last() if conversation else None
        
        # Store the last message with the user
        last_messages[utilisateur.user_id] = {
            'user': utilisateur,
            'last_message': last_message
        }
    
    return render(request, 'home/chat.html', {'last_messages': last_messages})

@login_required
def conversation_messages(request, profile_user_id):
    # Retrieve all utilisateur objects
    utilisateurs = Utilisateur.objects.all()
    
    # Create a dictionary to store the last message with each user
    last_messages = {}
    current_user = request.user
    selected_user = get_object_or_404(Utilisateur, pk=profile_user_id)  # Fetch user by primary key
    for utilisateur in utilisateurs:
        # Get the conversation between the current user and the current utilisateur
        conversation = Conversation.objects.filter(
            Q(user1=current_user, user2=utilisateur.user) | Q(user1=utilisateur.user, user2=current_user)
        ).first()
        
        # Get the last message in this conversation
        last_message = conversation.messages.last() if conversation else None
        
        # Store the last message with the user
        last_messages[utilisateur.user_id] = {
            'user': utilisateur,
            'last_message': last_message
        }
    
    # Fetch messages for the selected user
    selected_user = get_object_or_404(Utilisateur, pk=profile_user_id)  # Fetch user by primary key
    conversation = Conversation.objects.filter(
        Q(user1=current_user, user2=selected_user.user) | Q(user1=selected_user.user, user2=current_user)
    ).first()
    
    if conversation is None:
        # If conversation doesn't exist, render conversation_not_found.html template
        conversation = Conversation.objects.create(user1=current_user, user2=selected_user.user)

    selected_user_messages = conversation.messages.all().order_by('timestamp')
    
    return render(request, 'home/conversation.html', {'last_messages': last_messages, 'messages': selected_user_messages, 'selected_user': selected_user})


@login_required
def send_message(request, profile_user_id):
    selected_user = get_object_or_404(Utilisateur, pk=profile_user_id)
    current_user = request.user
    
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message_content = form.cleaned_data.get('content', '').strip()  # Get message content and remove leading/trailing whitespace
            if message_content:  # Check if message content is not empty
                conversation = Conversation.objects.filter(
                    Q(user1=current_user, user2=selected_user.user) | Q(user1=selected_user.user, user2=current_user)
                ).first()
                if conversation is None:
                    # If conversation doesn't exist, create a new conversation
                    conversation = Conversation.objects.create(user1=current_user, user2=selected_user.user)
                message = form.save(commit=False)
                message.sender = current_user
                message.receiver = selected_user.user
                message.conversation = conversation
                message.timestamp = timezone.now()
                message.save()
                return redirect('conversation_messages', profile_user_id=profile_user_id)
            else:
                 # Return a JavaScript alert if message content is empty
                return redirect('conversation_messages', profile_user_id=profile_user_id)

        else:
            return HttpResponseBadRequest("Invalid form data.")
    else:
        return HttpResponseBadRequest("Invalid request method.")
