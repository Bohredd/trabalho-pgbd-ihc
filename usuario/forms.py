# forms.py
from django import forms
from .models import Usuario


class UsuarioCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    class Meta:
        model = Usuario
        fields = ['nome_completo', 'email', 'cpf', 'telefone', 'data_nascimento', 'imagem']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('As senhas não coincidem.')

        return password_confirm


    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user