from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'product_type']

        def clean_code(self):
            code = self.cleaned_data.get('code')
            if not code or len(code) < 12:
                raise forms.ValidationError("Kod musi mieć przynajmniej 12 znaków.")
            return code