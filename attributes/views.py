from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)
from .forms import (DeviceCreateForm,
                    DeviceUpdateForm,
                    ProductTypeCreateForm,
                    ProductTypeUpdateForm)

from .models import ProductType, Device


class ProductTypeListView(ListView):
    model = ProductType
    template_name = 'attributes/product_types/product_type_list.html'
    context_object_name = 'product_types'


class ProductTypeCreateView(CreateView):
    model = ProductType
    template_name = 'attributes/product_types/product_type_create.html'
    form_class = ProductTypeCreateForm
    success_url = reverse_lazy('product-type-list')


class ProductTypeDeleteView(DeleteView):
    model = ProductType
    template_name = 'attributes/product_types/product_type_delete.html'
    context_object_name = 'product_type'
    success_url = reverse_lazy('product-type-list')


class ProductTypeUpdateView(UpdateView):
    model = ProductType
    template_name = 'attributes/product_types/product_type_update.html'
    form_class = ProductTypeUpdateForm
    context_object_name = 'product_type'
    
    def get_success_url(self):
        return reverse_lazy('product-type-update', kwargs={'pk': self.object.pk})


# Device Views


class DeviceListView(ListView):
    model = Device
    template_name = 'attributes/devices/device_list.html'
    context_object_name = 'devices'


class DeviceCreateView(CreateView):
    model = Device
    template_name = 'attributes/devices/device_create.html'
    form_class = DeviceCreateForm
    success_url = reverse_lazy('device-list')


class DeviceDeleteView(DeleteView):
    model = Device
    template_name = 'attributes/devices/device_delete.html'
    context_object_name = 'device'
    success_url = reverse_lazy('device-list')


class DeviceUpdateView(UpdateView):
    model = Device
    template_name = 'attributes/devices/device_update.html'
    form_class = DeviceUpdateForm
    context_object_name = 'device'

    def get_success_url(self):
        return reverse_lazy('device-update', kwargs={'pk': self.object.pk})
