from django.contrib import admin
from products.models import Product, ProductType


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'product_type')
    search_fields = ('code', 'name')
    list_filter = ('product_type',)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
