from django import forms
from django.forms import widgets


class NoteForm(forms.Form):
    author = forms.CharField(
        label='Автор',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form mt-3',
        })
    )
    email = forms.CharField(
        label='Почта',
        max_length=254,
        required=True,
        widget=widgets.EmailInput(attrs={
            'class': 'form mt-3',
        })
    )
    text = forms.CharField(
        label='Текст',
        max_length=2500,
        required=True,
        widget=widgets.Textarea(attrs={
            'class': 'form mt-3',
        })
    )


class SearchForm(forms.Form):
    search = forms.CharField(
        label='Поиск',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form mt-3',
            'style': 'max-width: 250px; margin-left: 495px;',
        })
    )
