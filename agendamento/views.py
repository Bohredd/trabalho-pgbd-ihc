from django.shortcuts import render
from agendamento.models import Agendamento


def agendar(request, restaurante_id, refeicao_rest_id):

    Agendamento.objects.create(
        usuario=request.user,
        restaurante_id=restaurante_id,
        refeicao_rest_id=refeicao_rest_id
    )


def ver_agendamentos(request):
    agendamentos = Agendamento.objects.filter(
        usuario=request.user)

    return render('agendamento/ver_agendamentos.html', {'agendamentos' : agendamentos})