# Generated by Django 3.2.8 on 2021-12-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0019_videoindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('date_post', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дата поста')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(default='blog/no_image.jpg', null=True, upload_to='blog/', verbose_name='Картинка')),
                ('price', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цена')),
                ('date_course', models.TextField(blank=True, null=True, verbose_name='Расписание')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(default='index_image/no_image.jpg', null=True, upload_to='index_image/', verbose_name='Верхняя картинка')),
                ('coffee_image', models.ImageField(default='index_image/no_image.jpg', null=True, upload_to='index_image/', verbose_name='Картинка кофе')),
                ('prodl_image', models.ImageField(default='index_image/no_image.jpg', null=True, upload_to='index_image/', verbose_name='Картинка продленки')),
            ],
            options={
                'verbose_name': 'Фотки на главной странице',
                'verbose_name_plural': 'Фотки на главной странице',
            },
        ),
        migrations.AlterModelOptions(
            name='videoindex',
            options={'verbose_name': 'Видео на главной странице', 'verbose_name_plural': 'Видео на главной странице'},
        ),
    ]
