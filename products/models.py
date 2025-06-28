from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from django.db import models

# Each product will have inherent values that are PIM-integrated.
# However there are values that will be specific to each
# platform and translation (e.g. description, category).
# Hence majority of Models has several different Models.

# Language + Platform


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LanguageCode(models.TextChoices):
    PL = 'pl', 'Polish'
    DE = 'de', 'German'
    HU = 'hu', 'Hungarian'
    RO = 'ro', 'Romanian'
    BG = 'bg', 'Bulgarian'
    

class Language(models.Model):
    code = models.CharField(max_length=10, choices=LanguageCode.choices, unique=True)
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Platform(TimeStampedModel):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language, related_name='platforms')
    max_product_name_length = models.PositiveIntegerField(default=255)

    def __str__(self):
        return self.name
    

# Category (per platform)


class PlatformCategory(TimeStampedModel):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255)
    external_id = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('platform', 'external_id')

    def __str__(self):
        return f'{self.platform.name} | {self.name}'
    

# Product and pim-integrated Models


class Category(TimeStampedModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Producer(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Tag(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class ProductType(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class ProductImage(TimeStampedModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    thumbnail = models.ImageField(upload_to='product_images/thumbnails/', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    alt_text = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def clean(self):
        if self.product.images.count() >= 16 and not self.pk:
            raise ValidationError(f'Maximum number of images (16) reached for product {self.product.code}.')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and not self.thumbnail:
            img = Image.open(self.image)
            img.thumbnail((300, 300))

            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG', quality=85)
            thumb_name = self.image.name.replace('product_images/', 'product_images/thumbnails/')

            self.thumbnail.save(thumb_name, ContentFile(thumb_io.getvalue()), save=False)
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.code} | Image {self.order + 1}'


class DeviceCompatibility(TimeStampedModel):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100, blank=True)
    model_codes = models.JSONField(
        help_text='List of model codes comma-separated like A2137, A2025, ...',
        null=True,
        blank=True)
    image = models.ImageField(upload_to='device_images/')
    thumbnail = models.ImageField(upload_to='device_images/thumbnails/', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Device Compatibility'
        verbose_name_plural = 'Device Compatibilities'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and not self.thumbnail:
            img = Image.open(self.image)
            img.thumbnail((100, 100))

            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG', quality=85)
            thumb_name = self.image.name.replace('device_images/', 'device_images/thumbnails/')
            self.thumbnail.save(thumb_name, ContentFile(thumb_io.getvalue()), save=False)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    code = models.CharField(max_length=50, unique=True)
    producer_code = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    related_products = models.ManyToManyField('self', blank=True, symmetrical=False)
    compatible_devices = models.ManyToManyField(DeviceCompatibility, related_name='products', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.code
    

class ProductPlatformTranslation(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='platform_translations')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def clean(self):
        max_len = self.platform.max_product_name_length
        if len(self.name) > max_len:
            raise ValidationError(
                {'name': f'Name exceeds max length of {max_len} for {self.platform.name}'}
            )

    class Meta:
        unique_together = ('product', 'platform', 'language')
        verbose_name = 'Product Platform Translation'
        verbose_name_plural = 'Product Platform Translations'

    def __str__(self):
        return self.name


# Product (per platform)


class ProductPlatformData(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='platform_data')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promo_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_promo = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    external_id = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(PlatformCategory, on_delete=models.SET_NULL, null=True, blank=True)
    
    def clean(self):
        if self.promo_price and self.promo_price >= self.price:
            raise ValidationError('Discount price must be less than regular price.')
        
    class Meta:
        unique_together = ('product', 'platform')
        verbose_name = 'Product Platform Data'

    def __str__(self):
        return f'{self.product.code} | {self.platform.name}'


# Attributes (pim-integrated and per platform)


class AttributeGroup(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Attribute(TimeStampedModel):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(AttributeGroup, on_delete=models.CASCADE, null=True, blank=True)
    is_global = models.BooleanField(default=True)
    platforms = models.ManyToManyField(Platform, blank=True)

    def __str__(self):
        return self.name
    

class AttributeTranslation(TimeStampedModel):
    name = models.CharField(max_length=255)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='translations')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('attribute', 'language')
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductAttributeValue(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attribute_values')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('product', 'attribute', 'platform')
        verbose_name = 'Product Attribute Value'
        verbose_name_plural = 'Product Attribute Values'

    def __str__(self):
        platform = self.platform.name if self.platform else 'Global'
        return f'{self.product.code} | {platform} | {self.attribute.name} = {self.value}'
