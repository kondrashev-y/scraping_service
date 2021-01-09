from django import forms

from scraping.models import City, Language


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
