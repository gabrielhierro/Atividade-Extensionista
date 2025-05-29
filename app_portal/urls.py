from django.urls import path
from app_portal import views

app_name = 'app_portal'


urlpatterns = [
    # A URL que o template quer acessar:
    path('comunicados/', views.comunicado, name='comunicados'),  # plural 'comunicados/' para ficar coerente

    # Outras URLs do app portal:
    path('', views.lista_comunicados, name='lista_comunicados'),
    path('novo/', views.novo_comunicado, name='novo_comunicado'),
    path('editar/<int:pk>/', views.editar_comunicado, name='editar_comunicado'),
    path('deletar/<int:pk>/', views.deletar_comunicado, name='deletar_comunicado'),
]
