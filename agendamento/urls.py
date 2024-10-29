from django.urls import path
from agendamento.views import ver_agendamentos, agendar

urlpatterns = [
    path("ver/", ver_agendamentos),
    path("agendar/", agendar),
]
