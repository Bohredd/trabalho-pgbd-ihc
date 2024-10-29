from django.db import models

class Refeicao(models.Model):
    nome = models.CharField(max_length=100,
                            choices=[('CAFE', 'Café da manhã'), ('ALMOCO', 'Almoço'), ('JANTA', 'Janta')])

    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()

    valor = models.DecimalField(max_digits=5, decimal_places=2)

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Restaurante(models.Model):
    nome = models.CharField(max_length=100,
                            choices=[('RU', 'Restaurante Universitário'), ('RU2', 'Restaurante Universitário 2')])

    campus = models.CharField(max_length=100,
                              choices=[('SM', 'Campus Santa Maria'), ('FW', 'Campus Frederico Westphalen'),
                                       ('PA', 'Campus Palmeira das Missões'), ('CS', 'Campus Cachoeira do Sul')])

    refeicoes_oferecidas = models.ManyToManyField(Refeicao)

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + ' - ' + self.campus

class CardapioRestaurante(models.Model):
    data_oferecida = models.DateField()
    cardapio = models.ForeignKey('cardapio.Cardapio', on_delete=models.CASCADE)
    restaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurante.nome + ' - ' + self.cardapio.refeicao.nome + ' - ' + str(self.data_oferecida)

    def get_quantia_agendamentos_diarios(self):
        """
        This method will return the quantity of agendamentos for the current cardapio
        :return: int
        """
        return self.agendamento_set.count()