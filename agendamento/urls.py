from django.urls import path
from agendamento.views import ver_agendamentos, agendar, selecionar_restaurante

urlpatterns = [
    path("ver/", ver_agendamentos, name='ver_agendamentos'),
    path('selecionar_restaurante/', selecionar_restaurante, name='selecionar_restaurante'),
    path('agendar/<int:restaurante_id>/', agendar, name='agendar'),
]
