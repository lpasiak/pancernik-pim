from django import forms
from .models import Product, ProductType, Compatibility, DeviceCode
from producers.models import Producer

# Product forms


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'code', 'producer_code', 'producer', 'product_type', 'compatibilities']
        

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'code', 'producer_code', 'producer', 'product_type', 'compatibilities']
        

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


class CompatibilityCreateForm(forms.ModelForm):

    class Meta:
        model = Compatibility
        fields = ['name', 'image', 'device_codes']


class CompatibilityUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Compatibility
        fields = ['name', 'image', 'device_codes']


# Device Code forms


class DeviCeCodeCreateForm(forms.ModelForm):

    class Meta:
        model = DeviceCode
        fields = ['code']
