from django import forms
from .models import ProductType, Device


# Product Type forms


class ProductTypeCreateForm(forms.ModelForm):

    class Meta:
        model = ProductType
        fields = ['name']
        

class ProductTypeUpdateForm(forms.ModelForm):
    
    class Meta:
        model = ProductType
        fields = ['name']


# Device forms


class DeviceCreateForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ['name', 'image']


class DeviceUpdateForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ['name', 'image']
