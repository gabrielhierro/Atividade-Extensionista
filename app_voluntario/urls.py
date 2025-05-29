from django.urls import path
from . import views

app_name = 'app_voluntario'

urlpatterns = [
    path('', views.voluntario_view, name='voluntario_view'),
]
