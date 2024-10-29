from django.db import models

class Cardapio(models.Model):
    refeicao = models.ForeignKey('restaurante.Refeicao', on_delete=models.CASCADE)

    principal = models.TextField()
    acompanhamento = models.TextField()
    bebidas = models.TextField()

    def __str__(self):
        return self.refeicao.nome

    def clean_text(self):
        """

        This method will clean the text from the cardapio model, removing the '|' and the spaces

        :return: list of strings with the cleaned text
        """


        clean_cardapio = []

        for item in self.principal.split('|'):
            clean_cardapio.append(item.strip())

        for item in self.acompanhamento.split('|'):
            clean_cardapio.append(item.strip())

        for item in self.bebidas.split('|'):
            clean_cardapio.append(item.strip())

        print(clean_cardapio)

        return clean_cardapio