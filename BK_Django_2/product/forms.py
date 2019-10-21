from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={'required': 'Enter Product Name'},
        max_length=64, label='Product Name'
    )
    price = forms.IntegerField(
        error_messages={'required': 'Enter Product Price'},
        label='Product Price'
    )
    description = forms.CharField(
        error_messages={'required': 'Enter Product Description'},
        max_length=256, label='Product Description'
    )
    stock = forms.IntegerField(
        error_messages={'required': 'Enter Quantity of Product'},
        label='Product Quantity'
    )


    def clean(self):
        # Check password if identical
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        stock = cleaned_data.get('stock')

        if not(name and price and description and stock):
            self.add_error('name', 'Input values')
            self.add_error('price', 'Input values')
            self.add_error('description', 'Input values')
            self.add_error('stock', 'Input values')