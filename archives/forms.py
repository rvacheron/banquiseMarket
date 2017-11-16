from django import forms

class SearchForm(forms.Form):
    text = forms.CharField(label='Produit',max_length=100,required=True)