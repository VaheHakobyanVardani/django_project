from django.urls import path,include
from . import views

app_name = 'basicApp'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('user_login/', views.User_login, name='User_login'),
]
