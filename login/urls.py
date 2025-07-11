from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registration_page/', views.registration, name='registration'),
    path('save_candidate/', views.save_candidate, name="save_candidate"),
    path('all_candidate_details/', views.all_candidate_details, name='all_candidate_details'),
    path('candidate_login/', views.candidate_login, name='candidate_login'),
    path('edit_candidate/', views.edit_candidate, name="edit_candidate"),
    path('save_edited_candidate/', views.save_edited_candidate, name="save_edited_candidate"),
    path('delete_candidate/', views.delete_candidate, name="delete_candidate")
]