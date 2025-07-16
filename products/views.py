from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)

from .forms import ProductCreateForm, ProductUpdateForm
from .models import Product


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
