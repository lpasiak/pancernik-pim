from django import forms
from .models import Product, ProductType

# Product forms


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['code', 'name', 'product_type']

        def clean_code(self):
            code = self.cleaned_data.get('code')
            if not code or len(code) < 12:
                raise forms.ValidationError("Kod musi mieć przynajmniej 12 znaków.")
            return code
        

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['code', 'name', 'product_type']

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
