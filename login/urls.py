from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registration_page/', views.registration, name='registration'),
]
