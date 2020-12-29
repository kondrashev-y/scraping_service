from django import forms
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import check_password

from scraping.models import City, Language

User = get_user_model()


class UserLoginForms(forms.Form):
    """Форма авторизации пользователя"""
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя нет')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль')
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Данный акаунт отключен')
        return super(UserLoginForms, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    """Форма регистрации пользователя"""
    email = forms.CharField(label='Введите email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']


class UserUpdateForm(forms.Form):
    """Форма подписки на рассылку вакансий"""
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), to_field_name='slug', required=True,
        widget=forms.Select(attrs={'class': 'custom-select custom-select-sm mr-sm-2'}), label='Город'
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), to_field_name='slug', required=True,
        widget=forms.Select(attrs={'class': 'custom-select custom-select-sm mr-sm-2'}), label='Специальность'
    )
    send_email = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput,
        label='Подписаться на рассылку вакансий'
    )

    class Meta:
        model = User
        fields = ('city', 'language', 'send_email')




