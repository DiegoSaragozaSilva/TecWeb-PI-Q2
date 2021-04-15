from django.shortcuts import render
from .models import Anotacao

def index(request):
    all_anotacoes = Anotacao.objects.all()
    last_anotacao = all_anotacoes[len(all_anotacoes) - 1]
    if request.method == 'POST':

        new_anotacao = Anotacao(content = request.POST.get('content'))
        new_anotacao.save()
        last_anotacao = new_anotacao
        return render(request, 'anotacoes/index.html', {'anotacao': last_anotacao})
        
    return render(request, 'anotacoes/index.html', {'anotacao': last_anotacao})