from django.urls import path
from .views import user_login, user_logout, user_profile, dashboard, user_register

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', user_register, name='register'),
]
