from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("f/", include("financeiro.urls")),
    path("a/", include("agendamento.urls")),
    path("c/", include("cardapio.urls")),
    path("u/", include("usuario.urls")),
]
