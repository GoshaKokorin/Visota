# Generated by Django 3.2.8 on 2021-12-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0020_auto_20211214_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetails',
            name='text_mini',
            field=models.TextField(blank=True, null=True, verbose_name='Текст в посте'),
        ),
    ]