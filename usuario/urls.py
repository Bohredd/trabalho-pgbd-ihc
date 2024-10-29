from django.urls import path
from usuario.views import logar_usuario, cadastrar, esqueci_senha

urlpatterns = [
    path("login/", logar_usuario, name='login'),
    path("cadastrar/", cadastrar, name='cadastrar'),
    path("esqueci-senha/", esqueci_senha, name='esqueci-senha'),
]
