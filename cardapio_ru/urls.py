from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("f/", include("financeiro.urls")),
    path("r/", include("restaurante.urls")),
    path("a/", include("agendamento.urls")),
    path("c/", include("cardapio.urls")),
]
