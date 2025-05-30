from django.urls import path, include
from app_core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('projetos/', include('app_projetos.urls')),
    path('voluntario/', include('app_voluntario.urls')),
]
