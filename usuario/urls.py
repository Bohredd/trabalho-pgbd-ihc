from django.urls import path
from usuario.views import logar_usuario, cadastrar, esqueci_senha

urlpatterns = [
    path("login/", logar_usuario),
    path("cadastrar/", cadastrar),
    path("esqueci-senha/", esqueci_senha),
]
