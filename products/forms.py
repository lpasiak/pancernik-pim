from django import forms
from .models import Product, ProductType, Compatibility, DeviceCode
from django_select2.forms import ModelSelect2TagWidget, Select2TagWidget

# Widgets


class CompatibilityWidget(Select2TagWidget):
    model = Compatibility
    search_fields = ['name__icontains']

    def get_queryset(self):
        return Compatibility.objects.all()


# Product forms


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['code', 'name', 'product_type', 'compatibilities']
        widgets = {
            'compatibilities': CompatibilityWidget
        }

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not code or len(code) < 12:
            raise forms.ValidationError("Kod musi mieć przynajmniej 12 znaków.")
        return code
        

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['code', 'name', 'product_type', 'compatibilities']
        widgets = {
            'compatibilities': CompatibilityWidget
        }


    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not code or len(code) < 12:
            raise forms.ValidationError("Kod musi mieć przynajmniej 12 znaków.")
        return code
        

# Product Type forms


class ProductTypeCreateForm(forms.ModelForm):

    class Meta:
        model = ProductType
        fields = ['name']
        

class ProductTypeUpdateForm(forms.ModelForm):
    
    class Meta:
        model = ProductType
        fields = ['name']


# Compatibility forms


class CompatibilityForm(forms.ModelForm):

    class Meta:
        model = Compatibility
        fields = ['name']
