from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required
def home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/home.html', {'users': users})


@login_required
def chat_room(request, username):
    other_user = User.objects.get(username=username)
    return render(request, 'chat/chat_room.html', {
        'other_user': other_user,
        'room_name': f"{min(request.user.id, other_user.id)}_{max(request.user.id, other_user.id)}"
    })
