# Generated by Django 3.2.8 on 2021-11-01 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0013_auto_20211101_0521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grouplessonsitem',
            old_name='master_class',
            new_name='group_lessons_item',
        ),
        migrations.RenameField(
            model_name='grouplessonspoint',
            old_name='master_class_item',
            new_name='group_lessons_point',
        ),
        migrations.RenameField(
            model_name='grouplessonsprice',
            old_name='group_class_item',
            new_name='group_lessons_price',
        ),
    ]
