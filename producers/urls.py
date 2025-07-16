from django.urls import path
from .views import *

urlpatterns = [
    path('', ProducerListView.as_view(), name='producer-list'),
    path('create/', ProducerCreateView.as_view(), name='producer-create'),
    path('<int:pk>/delete/', ProducerDeleteView.as_view(), name='producer-delete'),
    path('<int:pk>/update/', ProducerUpdateView.as_view(), name='producer-update')
]
