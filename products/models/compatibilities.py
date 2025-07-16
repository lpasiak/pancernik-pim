from django.db import models
from django.conf import settings
from PIL import Image
from urllib.parse import urljoin
import os


class Compatibility(models.Model):
    name = models.CharField(max_length=100, unique=True)

    image = models.ImageField(upload_to='compatibility_images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='compatibility_images/thumbnails/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        try:
            old = Compatibility.objects.get(pk=self.pk)
            image_changed = old.image != self.image

            if image_changed and old.image:
                old.image.delete(save=False)

            if image_changed and old.thumbnail:
                old.thumbnail.delete(save=False)

        except Compatibility.DoesNotExist:
            image_changed = True 

        super().save(*args, **kwargs)

        if self.image and (image_changed or not self.thumbnail):
            self.generate_thumbnail()
            super().save(update_fields=['thumbnail'])

    def generate_thumbnail(self):
        if not self.image:
            return
        
        from io import BytesIO
        from django.core.files.base import ContentFile

        img = Image.open(self.image)
        img = img.convert('RGB')
        img.thumbnail((150, 150))

        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG', quality=95)

        thumbnail_name = os.path.basename(self.image.name)
        self.thumbnail.save(
            f'thumbnail_{thumbnail_name}',
            ContentFile(thumb_io.getvalue()),
            save=False
        )

    @property
    def thumbnail_url(self):
        if self.thumbnail:
            return self.thumbnail.url
        return urljoin(settings.MEDIA_URL, 'compatibility_images/thumbnails/thumbnail_default_photo.jpg')

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return urljoin(settings.MEDIA_URL, 'compatibility_images/default_photo.jpg')