from django.urls import path
from app_portal import views

app_name = 'app_portal'

urlpatterns = [
    path('comunicado/', views.comunicado, name='comunicados'),
]