from django.core.management.base import BaseCommand
from usuario.models import Usuario
from financeiro.models import Carteira, Transacao

class Command(BaseCommand):
    help = 'Cria carteiras e transações para cada usuário, garantindo saldo positivo para o admin'

    def handle(self, *args, **options):
        usuarios = Usuario.objects.all()

        for usuario in usuarios:
            carteira, created = Carteira.objects.get_or_create(usuario=usuario)

            if usuario.is_superuser:
                transacoes_data = [
                    {"valor": 1000.00, "is_entrada": True},
                    {"valor": 500.00, "is_entrada": True},
                    {"valor": 200.00, "is_entrada": True},
                    {"valor": 150.00, "is_entrada": False}
                ]
            else:
                transacoes_data = [
                    {"valor": 200.00, "is_entrada": True},
                    {"valor": 150.00, "is_entrada": True},
                    {"valor": 100.00, "is_entrada": True},
                    {"valor": 50.00, "is_entrada": False}
                ]

            for transacao_data in transacoes_data:
                transacao = Transacao(
                    carteira=carteira,
                    valor=transacao_data["valor"],
                    is_entrada=transacao_data["is_entrada"]
                )
                transacao.save()

            self.stdout.write(self.style.SUCCESS(
                f'Carteira e transações criadas para {usuario.nome_completo} com saldo final de {carteira.saldo}'
            ))

        self.stdout.write(self.style.SUCCESS('Processo de criação de carteiras e transações concluído!'))
