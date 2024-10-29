from django.urls import path
from financeiro.views import ver_carteira, realizar_recarga

urlpatterns = [
    path("ver/", ver_carteira),
    path("recarga/", realizar_recarga),
]
