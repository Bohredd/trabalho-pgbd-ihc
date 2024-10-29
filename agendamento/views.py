# agendamento/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from agendamento.models import Agendamento
from restaurante.models import CardapioRestaurante
from agendamento.forms import AgendamentoForm, RestauranteSelectForm

def selecionar_restaurante(request):
    if request.method == "POST":
        form = RestauranteSelectForm(request.POST)
        if form.is_valid():
            restaurante_id = form.cleaned_data['restaurante'].id
            print("ID REST: ", restaurante_id)
            return redirect('agendar', restaurante_id=restaurante_id)
    else:
        form = RestauranteSelectForm()

    return render(request, 'agendamento/selecionar_restaurante.html', {'form': form})


def agendar(request, restaurante_id):
    if request.method == "POST":
        form = AgendamentoForm(restaurante_id=restaurante_id, data=request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user
            agendamento.save()
            messages.success(request, 'Agendamento realizado com sucesso!')
            return redirect('ver_agendamentos')
    else:
        form = AgendamentoForm(restaurante_id=restaurante_id)

    cardapios = CardapioRestaurante.objects.filter(restaurante_id=restaurante_id)

    return render(request, 'agendamento/agendar.html', {'form': form, 'cardapios': cardapios})

def ver_agendamentos(request):
    agendamentos = Agendamento.objects.filter(usuario=request.user)
    return render(request, 'agendamento/ver_agendamentos.html', {'agendamentos': agendamentos})
