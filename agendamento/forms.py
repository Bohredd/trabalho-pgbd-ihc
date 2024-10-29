# agendamento/forms.py
from django import forms
from agendamento.models import Agendamento
from restaurante.models import Restaurante, CardapioRestaurante

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cardapio_agendado']

    def __init__(self, restaurante_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if restaurante_id:
            self.fields['cardapio_agendado'].queryset = CardapioRestaurante.objects.filter(restaurante__id=restaurante_id)
        else:
            self.fields['cardapio_agendado'].queryset = CardapioRestaurante.objects.none()

class RestauranteSelectForm(forms.Form):
    restaurante = forms.ModelChoiceField(queryset=Restaurante.objects.all(), label="Selecione o Restaurante")
