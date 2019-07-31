from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('user_page/', views.user_page, name= 'user_page'),
    path('logout/', views.logout, name='logout'),
    path('change_pw/', views.change_pw, name='change_pw'),
    path('profile/', views.profile, name='profile'),
]