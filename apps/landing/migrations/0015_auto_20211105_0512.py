# Generated by Django 3.2.8 on 2021-11-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0014_auto_20211101_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterclassitem',
            name='discount',
            field=models.BooleanField(default=False, verbose_name='Скидка на первое занятие'),
        ),
        migrations.AddField(
            model_name='masterclassitem',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
    ]
