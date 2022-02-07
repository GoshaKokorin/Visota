from django.db import models


class Gallery(models.Model):
    image = models.ImageField('image', upload_to='gallery/', default='gallery/no_image.jpg', null=True)

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'