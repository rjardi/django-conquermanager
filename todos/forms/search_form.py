from django import forms

class SearchForm(forms.Form):
    search_string=forms.CharField(label="Introduce una cadena de texto:", max_length=100)
    