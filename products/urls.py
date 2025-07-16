from django.urls import path
from .views import *

urlpatterns = [
    # Product
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    # Product Type
    path('product-types/', ProductTypeListView.as_view(), name='product-type-list'),
    path('product-types/create/', ProductTypeCreateView.as_view(), name='product-type-create'),
    path('product-types/<int:pk>/delete/', ProductTypeDeleteView.as_view(), name='product-type-delete'),
    path('product-types/<int:pk>/update/', ProductTypeUpdateView.as_view(), name='product-type-update'),
    # Compatibility
    path('compatibilities/', CompatibilityListView.as_view(), name='compatibility-list'),
    path('compatibilities/create/', CompatibilityCreateView.as_view(), name='compatibility-create'),
    path('compatibilities/<int:pk>/delete/', CompatibilityDeleteView.as_view(), name='compatibility-delete'),
    path('compatibilities/<int:pk>/update/', CompatibilityUpdateView.as_view(), name='compatibility-update'),
    path('compatibilities/device-code/create/', DeviceCodeCreateView.as_view(), name='device-code-create'), 
]
