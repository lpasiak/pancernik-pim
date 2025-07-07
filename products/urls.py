from django.urls import path
from .views import (ProductListView,
                    ProductDetailView,
                    ProductCreateView,
                    ProductDeleteView,
                    ProductUpdateView)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
]
