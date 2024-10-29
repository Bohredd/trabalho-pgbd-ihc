from django.contrib import admin
from .models import Carteira, Transacao

admin.site.register(Carteira)
admin.site.register(Transacao)