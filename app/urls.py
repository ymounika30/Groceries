from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('register/', views.RegisterView.as_view(), name='register'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]