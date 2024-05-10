from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [

    path('register/', views.registerView, name='register'),
    # Include
    path('login/', views.LoginView, name='login'),
      path('logout/', views.Logout, name='logout')
    ] 