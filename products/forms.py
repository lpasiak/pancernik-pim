from django import forms
from .models import Product
from django_select2.forms import Select2Widget


# Product forms


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'producer': Select2Widget,
            'product_type': Select2Widget
        }
        

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'code', 'producer_code', 'producer', 'product_type', 'devices']
