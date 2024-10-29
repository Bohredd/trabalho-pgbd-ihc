from django.urls import path
from cardapio.views import ver_cardapio, ver_cardapio_semana

urlpatterns = [
    path("ver/", ver_cardapio),
    path("ver/semana/", ver_cardapio_semana),
]
