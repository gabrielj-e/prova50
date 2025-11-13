from django.urls import path
from . import views

urlpatterns = [
    # Ex: http://127.0.0.1:8000/
    path('', views.lista_mapeamentos, name='lista'),
    # Ex: http://127.0.0.1:8000/mapeamento/1/
    path('mapeamento/<int:pk>/', views.detalhe_mapeamento, name='detalhe'),
]