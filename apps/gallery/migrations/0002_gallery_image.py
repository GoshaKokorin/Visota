# Generated by Django 3.2.8 on 2021-10-25 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='gallery/no_image.jpg', null=True, upload_to='gallery/', verbose_name='image'),
        ),
    ]
