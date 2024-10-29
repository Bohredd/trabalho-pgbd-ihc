from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from .forms import UsuarioCreationForm
from .models import Usuario

def cadastrar(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('logar_usuario')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados e tente novamente.')
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuario/cadastrar.html', {'form': form})


def logar_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'E-mail ou senha incorretos. Tente novamente.')
    return render(request, 'usuario/login.html')


def esqueci_senha(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            email = password_reset_form.cleaned_data['email']
            associated_users = Usuario.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = 'Redefinição de senha solicitada'
                    email_template_name = 'password_reset_email.html'
                    # context = {
                    #     "email": user.email,
                    #     'domain': settings.DOMAIN,
                    #     'site_name': 'Seu Site',
                    #     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    #     "user": user,
                    #     'token': default_token_generator.make_token(user),
                    #     'protocol': 'http',
                    # }
                    # email_message = render_to_string(email_template_name, context)
                    # send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [user.email])
                    messages.success(request, 'Instruções de redefinição de senha enviadas para o seu e-mail.')
                    return redirect('logar_usuario')
            else:
                messages.error(request, 'Nenhum usuário associado a esse e-mail.')
    password_reset_form = PasswordResetForm()
    return render(request, 'usuario/esqueci_senha.html', {'password_reset_form': password_reset_form})
