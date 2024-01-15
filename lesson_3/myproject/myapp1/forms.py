from django import forms
from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    product = forms.ImageField()
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'photo']

    