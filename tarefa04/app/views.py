from django.shortcuts import render
from datetime import date
from .models import Tarefa

def index(request):
    tarefas = Tarefa.objects.all()
    context = {
        "tarefas": tarefas,
        "hoje": date.today(),
    }
    return render(request, "app/index.html", context)
