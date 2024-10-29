# views.py
from django.shortcuts import render, redirect
from financeiro.models import Carteira, Transacao
from .forms import FormularioRecarga

def ver_carteira(request):
    carteira = Carteira.objects.filter(
        usuario=request.user
    ).first()

    return render(request, "financeiro/ver_carteira.html", {"carteira": carteira})

def realizar_recarga(request):
    if request.method == "POST":
        form = FormularioRecarga(request.POST)

        if form.is_valid():
            valor_recarga = form.cleaned_data['valor_recarga']

            carteira = Carteira.objects.filter(
                usuario=request.user,
            ).first()

            if carteira:

                Transacao.objects.create(
                    carteira=carteira,
                    valor=valor_recarga,
                    is_entrada=True,
                )
                return redirect('ver_carteira')
            else:
                form.add_error(None, "Nenhuma carteira encontrada para o usuário.")

    else:
        form = FormularioRecarga()

    return render(request, "financeiro/realizar_recarga.html", {"form": form})
