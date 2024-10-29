from django.core.management.base import BaseCommand
from django.utils import timezone
from restaurante.models import Refeicao, Restaurante, CardapioRestaurante
from agendamento.models import Agendamento
from cardapio.models import Cardapio
from usuario.models import Usuario
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Popula o banco de dados com restaurantes, cardápios, agendamentos e associações em CardapioRestaurante'

    def handle(self, *args, **options):
        cafe_da_manha, _ = Refeicao.objects.get_or_create(nome='CAFE', horario_abertura="07:00",
                                                          horario_fechamento="10:00", valor=10.00, ativo=True)
        almoco, _ = Refeicao.objects.get_or_create(nome='ALMOCO', horario_abertura="11:30", horario_fechamento="14:00",
                                                   valor=15.00, ativo=True)
        janta, _ = Refeicao.objects.get_or_create(nome='JANTA', horario_abertura="18:30", horario_fechamento="21:00",
                                                  valor=12.00, ativo=True)

        restaurante1, _ = Restaurante.objects.get_or_create(nome='RU', campus='SM', ativo=True)
        restaurante2, _ = Restaurante.objects.get_or_create(nome='RU', campus='FW', ativo=True)
        restaurante3, _ = Restaurante.objects.get_or_create(nome='RU2', campus='PA', ativo=True)
        restaurante4, _ = Restaurante.objects.get_or_create(nome='RU2', campus='SM', ativo=True)

        restaurante1.refeicoes_oferecidas.add(cafe_da_manha, almoco, janta)
        restaurante2.refeicoes_oferecidas.add(almoco, janta)
        restaurante3.refeicoes_oferecidas.add(cafe_da_manha, almoco)
        restaurante4.refeicoes_oferecidas.add(cafe_da_manha, almoco, janta)

        cardapios_data = [
            {'refeicao': cafe_da_manha, 'principal': 'Pão | Queijo', 'acompanhamento': 'Café | Leite',
             'bebidas': 'Suco de Laranja | Chá'},
            {'refeicao': almoco, 'principal': 'Arroz | Feijão | Carne', 'acompanhamento': 'Salada | Batata Frita',
             'bebidas': 'Refrigerante | Suco de Uva'},
            {'refeicao': janta, 'principal': 'Macarrão | Frango', 'acompanhamento': 'Legumes | Purê',
             'bebidas': 'Água | Suco de Maçã'},
            {'refeicao': almoco, 'principal': 'Risoto | Peixe', 'acompanhamento': 'Salada Verde | Legumes Assados',
             'bebidas': 'Suco de Manga | Água'},
            {'refeicao': cafe_da_manha, 'principal': 'Torrada | Queijo', 'acompanhamento': 'Manteiga | Geleia',
             'bebidas': 'Café | Chá'}
        ]

        cardapios = []
        for cardapio_data in cardapios_data:
            cardapio, _ = Cardapio.objects.get_or_create(**cardapio_data)
            cardapios.append(cardapio)

        today = date.today()
        cardapios_restaurantes = []
        for i, cardapio in enumerate(cardapios):
            cardapio_restaurante, _ = CardapioRestaurante.objects.get_or_create(
                data_oferecida=today + timedelta(days=i),
                cardapio=cardapio,
                restaurante=restaurante1 if i % 2 == 0 else restaurante4
            )
            cardapios_restaurantes.append(cardapio_restaurante)

        usuario1, _ = Usuario.objects.get_or_create(nome_completo="João da Silva", email="joao.silva@example.com")
        usuario2, _ = Usuario.objects.get_or_create(nome_completo="Maria Souza", email="maria.souza@example.com")
        usuario3, _ = Usuario.objects.get_or_create(nome_completo="Carlos Oliveira", email="carlos.oliveira@example.com")

        agendamentos_data = [
            {'cardapio_agendado': cardapios_restaurantes[0], 'usuario': usuario1, 'is_fila_espera': False},
            {'cardapio_agendado': cardapios_restaurantes[1], 'usuario': usuario2, 'is_fila_espera': True},
            {'cardapio_agendado': cardapios_restaurantes[2], 'usuario': usuario1, 'is_fila_espera': False},
            {'cardapio_agendado': cardapios_restaurantes[3], 'usuario': usuario3, 'is_fila_espera': False},
            {'cardapio_agendado': cardapios_restaurantes[4], 'usuario': usuario2, 'is_fila_espera': True},
        ]

        for agendamento_data in agendamentos_data:
            Agendamento.objects.get_or_create(
                cardapio_agendado=agendamento_data['cardapio_agendado'],
                usuario=agendamento_data['usuario'],
                data_agendamento=timezone.now(),
                is_fila_espera=agendamento_data['is_fila_espera']
            )

        self.stdout.write(self.style.SUCCESS('Restaurantes, cardápios, associações e agendamentos criados com sucesso!'))
