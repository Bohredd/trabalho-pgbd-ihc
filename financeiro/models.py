from django.db import models

class Carteira(models.Model):
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    saldo = models.FloatField(default=0)

    def levantamento_entradas_saidas(self):
        entradas = Transacao.objects.filter(carteira=self, is_entrada=True)
        saidas = Transacao.objects.filter(carteira=self, is_entrada=False)
        return entradas, saidas

class Transacao(models.Model):
    carteira = models.ForeignKey('financeiro.Carteira', on_delete=models.CASCADE)
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)
    is_entrada = models.BooleanField(default=False)

    def __str__(self):
        return self.carteira.usuario.nome + ' - ' + str(self.valor) + ' - ' + str(self.data)

    def save(self, *args, **kwargs):
        self.carteira.saldo += self.valor if self.is_entrada else -self.valor
        self.carteira.save()
        super(Transacao, self).save(*args, **kwargs)