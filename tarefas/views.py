from django.shortcuts import render
from .models import *
# Create your views here.


def listar_tarefas(request):
    
    tarefas = Tarefa.objects.all().order_by('status', '-priority')
    
    contexto = {
        'tarefas': tarefas,
    }
    
    return render(request, 'tarefas/lista_tarefa.html', contexto)