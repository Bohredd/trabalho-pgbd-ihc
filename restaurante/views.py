from django.shortcuts import render
from .models import Restaurante


def selecionar_restaurante(request):

    restaurantes = Restaurante.objects.all()

    return render("restaurante/selecionar_restaurante.html", {"restaurantes": restaurantes})