from carts.models import Cart, CartItem
from django.contrib import messages, auth
from django.core.exceptions import RequestAborted
from django.db.models.query import RawQuerySet
from accounts.models import Account
from django import forms
from django.forms.widgets import PasswordInput
from django.shortcuts import redirect, render
from .forms import RegistrationForm, forgotPasswordForm
from django.contrib.auth.decorators import login_required
from carts.views import _cart_id
import requests


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
            try:
                cart = Cart.objects.get(cart_id = _cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)

                    # Getting the product variations by cart id
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))

                    # Get the cart items from the user to access his product variations
                    cart_item = CartItem.objects.filter(user = user)
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)

                    
                    for pr in product_variation:
                        if pr in ex_var_list:
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CartItem.objects.get(id = item_id)
                            item.quantity += 1
                            item.user = user
                            item.save()
                        else:
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request, 'Успешный вход в систему')
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                # next=/cart/checkout
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect(dashboard)
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

