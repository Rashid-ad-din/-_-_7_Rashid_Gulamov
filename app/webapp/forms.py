from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        label='Поиск',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form mt-3',
            'style': 'max-width: 250px; margin-left: 495px;',
        })
    )
