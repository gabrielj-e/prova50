from django.contrib import admin
from django.urls import path, include  # 1. Importe o 'include'

urlpatterns = [
    path('admin/', admin.site.urls),

    # 2. Adicione esta linha:
    # Ela diz ao Django para enviar qualquer URL vazia (ex: 127.0.0.1:8000/)
    # para ser gerenciada pelo arquivo 'urls.py' do app 'concordancia'
    path('', include('concordancia.urls')),
]