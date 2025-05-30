from django.urls import path
from . import views

app_name = 'app_projetos'

urlpatterns = [
    path('', views.projeto_view, name='projetos'),
]
