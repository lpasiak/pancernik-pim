from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Producer


class ProducerListView(ListView):
    model = Producer
    template_name = 'producers/producer_list.html'
    context_object_name = 'producers'


class ProducerCreateView(CreateView):
    model = Producer
    template_name = 'producers/producer_create.html'
    fields = ['name']
    success_url = reverse_lazy('producer-list')


class ProducerDeleteView(DeleteView):
    model = Producer
    template_name = 'producers/producer_delete.html'
    context_object_name = 'producer'
    success_url = reverse_lazy('producer-list')


class ProducerUpdateView(UpdateView):
    model = Producer
    template_name = 'producers/producer_update.html'
    fields = ['name']
    context_object_name = 'producer'

    def get_success_url(self):
        return reverse_lazy('producer-update', kwargs={'pk': self.object.pk})
