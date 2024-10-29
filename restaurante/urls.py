from django.urls import path
from restaurante.views import selecionar_restaurante

urlpatterns = [
    path("selecionar/", selecionar_restaurante),
]
