from django.db import models

class Agendamento(models.Model):
    cardapio_agendado = models.ForeignKey('restaurante.CardapioRestaurante', on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)

    is_fila_espera = models.BooleanField(default=False)

    def __str__(self):
        return self.cardapio_agendado.restaurante.nome + ' - ' + self.cardapio_agendado.cardapio.refeicao.nome + ' - ' + str(self.data_agendamento)
