from django import forms

class JobSearchForm(forms.Form):
    search_bar = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Search'
    }))