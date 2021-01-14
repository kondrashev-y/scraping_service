from django import forms

from scraping.models import City, Language, Vacancy


class FindForm(forms.Form):
    """Форма поиска вакансий по языку и городам"""
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), to_field_name='slug', required=False,
        widget=forms.Select(attrs={'class': 'custom-select custom-select-sm mr-sm-2'}), label='Город'
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), to_field_name='slug', required=False,
        widget=forms.Select(attrs={'class': 'custom-select custom-select-sm mr-sm-2'}), label='Специальность'
    )


class CreateVacancyForm(forms.ModelForm):
    """Форма добавления вакансий"""
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'custom-select custom-select mr-sm-2'}), label='Город'
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), to_field_name='slug',
        widget=forms.Select(attrs={'class': 'custom-select custom-select mr-2'}), label='Специальность'
    )
    url = forms.CharField(label='Url', widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label='Специальность', widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(label='Компания', widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary = forms.CharField(label='Зарплата', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Vacancy
        fields = '__all__'
