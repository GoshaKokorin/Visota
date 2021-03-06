# Generated by Django 3.2.8 on 2021-10-30 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_alter_price_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='title')),
                ('master_class_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item', to='landing.masterclassitem')),
            ],
        ),
    ]
