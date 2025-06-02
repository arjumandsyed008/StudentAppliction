from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
    path('dashborad/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('apply/', views.apply_course, name='apply_course'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
