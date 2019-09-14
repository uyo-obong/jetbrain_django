from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', user_views.registration, name='registration'),
    path('accounts/login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
    path('profile/', user_views.profile, name='profile')

]
