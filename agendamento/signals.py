
from django.db.models.signals import post_save

from agendamento.models import Agendamento
# from agendamento.utils import send_email_agendamento

def alterar_saldo_usuario(sender, instance, created, **kwargs):
    if created:

        if instance.usuario.saldo >= instance.cardapio_agendado.cardapio.refeicao.valor:
            instance.usuario.saldo -= instance.cardapio_agendado.cardapio.refeicao.valor
            instance.usuario.save()
            # send_email_agendamento(instance.usuario.email, instance.cardapio_agendado)
        else:
            raise "Saldo insuficiente. Por favor, realize uma recarga."