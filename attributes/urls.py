from django.urls import path
from .views import *

urlpatterns = [
    # Product Type
    path('product-types/', ProductTypeListView.as_view(), name='product-type-list'),
    path('product-types/create/', ProductTypeCreateView.as_view(), name='product-type-create'),
    path('product-types/<int:pk>/delete/', ProductTypeDeleteView.as_view(), name='product-type-delete'),
    path('product-types/<int:pk>/update/', ProductTypeUpdateView.as_view(), name='product-type-update'),
    # Device
    path('devices/', DeviceListView.as_view(), name='device-list'),
    path('devices/create/', DeviceCreateView.as_view(), name='device-create'),
    path('devices/<int:pk>/delete/', DeviceDeleteView.as_view(), name='device-delete'),
    path('devices/<int:pk>/update/', DeviceUpdateView.as_view(), name='device-update')
]
