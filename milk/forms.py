from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['date', 'customer', 'litres_sold', 'price_per_litre', 'paid', 'payment_type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
