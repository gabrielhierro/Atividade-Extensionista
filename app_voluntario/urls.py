from django.urls import path
from app_portal import views

app_name = 'app_voluntario'

urlpatterns = [
    path('', views.seja_voluntario, name='seja_voluntario'),
    path('voluntario/', views.voluntario, name='voluntario'),
]
