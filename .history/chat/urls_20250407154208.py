from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:username>/', views.chat_room, name='chat_room'),
    path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
