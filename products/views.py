from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)

from .forms import (ProductCreateForm,
                    ProductUpdateForm,
                    ProductTypeCreateForm,
                    ProductTypeUpdateForm)

from .models import Product, ProductType, Compatibility


# Product views


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductUpdateForm
    context_object_name = 'product'
    
    def get_success_url(self):
        return reverse_lazy('product-update', kwargs={'pk': self.object.pk})


# Product Type views


class ProductTypeListView(ListView):
    model = ProductType
    template_name = 'products/product_type_list.html'
    context_object_name = 'product_types'


class ProductTypeCreateView(CreateView):
    model = ProductType
    template_name = 'products/product_type_create.html'
    form_class = ProductTypeCreateForm
    success_url = reverse_lazy('product-type-list')


class ProductTypeDeleteView(DeleteView):
    model = ProductType
    template_name = 'products/product_type_delete.html'
    context_object_name = 'product_type'
    success_url = reverse_lazy('product-type-list')


class ProductTypeUpdateView(UpdateView):
    model = ProductType
    template_name = 'products/product_type_update.html'
    form_class = ProductTypeUpdateForm
    context_object_name = 'product_type'
    
    def get_success_url(self):
        return reverse_lazy('product-type-update', kwargs={'pk': self.object.pk})


# Compatibility Views

class CompatibilityListView(ListView):
    model = Compatibility
    template_name = 'products/compatibility_list.html'
    context_object_name = 'compatibilities'
