from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
import datetime

from scraping.models import Error
from .forms import UserLoginForms, UserRegistrationForm, UserUpdateForm, ContactForm
User = get_user_model()


def login_view(request):
    """Авторизация пользователя"""
    form = UserLoginForms(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """Выход пользователя"""
    logout(request)
    return redirect('home')


def register_view(request):
    """Регистрация нового пользователя"""
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        messages.success(request, 'Пользователь зарегистрирован')
        login(request, new_user)
        return render(request, 'accounts/register_done.html', {'new_user': new_user})
    return render(request, 'accounts/register.html', {'form': form})


def update_view(request):
    """Подписка на рассылку"""
    contact_form = ContactForm()
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserUpdateForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user.city = data['city']
                user.language = data['language']
                user.send_email = data['send_email']
                user.save()
                messages.success(request, 'Настройки сохранены')
                return redirect('accounts:update')
        form = UserUpdateForm(
            initial={'city': user.city, 'language': user.language, 'send_email': user.send_email}
        )
        return render(request, 'accounts/update.html', {'form': form, 'contact_form': contact_form})
    else:
        return redirect('accounts:login')


def delete_view(request):
    """Удаление пользователя"""
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            qs = User.objects.get(pk=user.pk)
            qs.delete()
            messages.error(request, 'Ваш аккаунт был удален!')
    return redirect('home')


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            data = contact_form.cleaned_data
            city = data.get('city')
            language = data.get('language')
            email = data.get('email')
            user_data = {'city': city, 'language': language, 'email': email}
            qs = Error.objects.filter(timestamp=datetime.date.today())
            if qs.exists():
                er = qs.first()
                data = er.data.get('user_data', [])
                data.append(user_data)
                er.data['user_data'] = data
                er.save()
            else:
                data = {'user_data': [user_data]}
                Error(data=data).save()
            messages.success(request, 'Данные отправленны администраци.')
            return redirect('accounts:update')
        else:
            return redirect('accounts:update')
    else:
        return redirect('accounts:login')

