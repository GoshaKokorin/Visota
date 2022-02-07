# Generated by Django 3.2.8 on 2021-11-01 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_auto_20211101_0330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grouplessonsprice',
            old_name='master_class_item',
            new_name='group_class_item',
        ),
        migrations.AlterField(
            model_name='grouplessonsprice',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='grouplessonsprice',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
