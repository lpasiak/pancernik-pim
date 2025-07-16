from django.contrib import admin
from .models import Producer


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )
    list_filter = ('name', )