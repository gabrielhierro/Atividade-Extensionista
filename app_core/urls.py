from django.urls import path
from app_core import views
from app_voluntario import views as voluntario_views  # Importe a view correta

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('voluntario/', voluntario_views.voluntario, name='voluntario'),  # Redireciona para a view no app_voluntario
    path('projetos/', views.projeto, name='projeto'),
]
