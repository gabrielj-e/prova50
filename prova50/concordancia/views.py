from django.shortcuts import render, get_object_or_404
from .models import Mapeamento


# View para a página inicial (Lista - "Read")
def lista_mapeamentos(request):
    # Pega todos os objetos Mapeamento do banco
    mapeamentos = Mapeamento.objects.all()

    # Define o contexto (dados a enviar para o template)
    contexto = {
        'lista_de_mapas': mapeamentos
    }

    # Renderiza o template 'lista.html' com os dados
    return render(request, 'concordancia/lista.html', contexto)


# View para a página de detalhe (Detalhe - "Read")
def detalhe_mapeamento(request, pk):
    mapa = get_object_or_404(Mapeamento, pk=pk)

    contexto = {
        'mapa': mapa
    }
    return render(request, 'concordancia/detalhe.html', contexto)