from django import forms


class RegisterForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        res = super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={'required': 'Enter Product Quantity'},
        label='Product Quantity'
    )
    # Order
    product = forms.IntegerField(
        error_messages={'required': 'Enter Product Name'},
        widget=forms.HiddenInput
    )


    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        # bkuser = self.request.session.get('user')

        if not(quantity and product):
            self.add_error('quantity', 'No Value')
            self.add_error('product', 'No Value')

