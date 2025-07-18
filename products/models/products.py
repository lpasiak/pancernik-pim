from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, unique=True)
    producer_code = models.CharField(max_length=100, null=True, blank=True)
    producer = models.ForeignKey('producers.Producer', on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.ForeignKey('attributes.ProductType', on_delete=models.SET_NULL, null=True, blank=True)
    devices = models.ManyToManyField('attributes.Device', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def clean(self):
        if len(self.code) < 12:
            raise ValidationError("Kod musi mieć przynajmniej 12 znaków.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
