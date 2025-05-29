from django.urls import path, include
from app_core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    # # path('contato/', views.contato, name='contato'),
    # path('volutario/', views.voluntario, name='voluntario'),
    path('projetos/', views.projeto, name='projeto'),
    path('voluntario/', include('app_voluntario.urls')),
]