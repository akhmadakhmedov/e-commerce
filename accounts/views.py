from django.contrib import messages, auth
from django.core.exceptions import RequestAborted
from django.db.models.query import RawQuerySet
from accounts.models import Account, forgotPassword
from django import forms
from django.forms.widgets import PasswordInput
from django.shortcuts import redirect, render
from .forms import RegistrationForm, forgotPasswordForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name            = form.cleaned_data['name']
            phone_number    = form.cleaned_data['phone_number']
            password        = form.cleaned_data['password']

            user = Account.objects.create_user(name = name, phone_number = phone_number, password = password)
            user.save()
            messages.success(request, 'Регистрация успешна')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user = auth.authenticate(phone_number=phone_number, password = password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'Успешный вход в систему')
            return redirect('home')
        else:
            messages.error(request, 'Неверные логин или пароль')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Успешный выход из системы')
    return redirect('login')

@login_required(login_url = 'login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def forgotPassword(request):
    form = forgotPasswordForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Спасибо за обращение в нашу компанию. Мы ответим Вам в ближайшее время.')
        return redirect('forgotPassword')
    context = {
        'form': form
    }
    return render(request, 'accounts/forgotPassword.html', context)

