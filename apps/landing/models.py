from django.db import models
from django.urls import reverse_lazy


class Contact(models.Model):
    name = models.CharField('name', max_length=255, null=True, blank=True)
    connection = models.CharField('connection', max_length=255, null=True, blank=True)
    text = models.TextField('text', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class MainPage(models.Model):
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    image = models.ImageField('Верхняя картинка', upload_to='index_image/', default='index_image/no_image.jpg',
                              null=True)
    coffee_image = models.ImageField('Картинка кофе', upload_to='index_image/', default='index_image/no_image.jpg',
                                     null=True)
    prodl_image = models.ImageField('Картинка продленки', upload_to='index_image/', default='index_image/no_image.jpg',
                                    null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотки на главной странице'
        verbose_name_plural = 'Фотки на главной странице'


class MasterClass(models.Model):
    title = models.CharField('title', max_length=255, null=True, blank=True)
    slug = models.SlugField('slug', max_length=255, blank=True, unique=True)
    image = models.ImageField('image', upload_to='master_class/', default='master_class/no_image.jpg', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мастер классы'
        verbose_name_plural = 'Мастер классы'

    def get_absolute_url(self):
        return '/master-classes/%s/' % self.slug


class MasterClassItem(models.Model):
    master_class = models.ForeignKey(MasterClass, related_name='master_class_item', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255, null=True, blank=True)
    slug = models.SlugField('slug', max_length=255, blank=True, unique=True)
    text = models.TextField('text', null=True, blank=True)
    teacher = models.CharField('teacher', max_length=255, null=True, blank=True)
    profession = models.CharField('profession', max_length=255, null=True, blank=True)
    photo = models.ImageField('photo', upload_to='photo_teacher/', default='photo_teacher/no_image.jpg',
                              null=True)
    image = models.ImageField('image', upload_to='master_class_item/', default='master_class_item/no_image.jpg',
                              null=True)
    discount = models.BooleanField('Скидка на первое занятие', default=False)
    publish = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мастер класс'
        verbose_name_plural = 'Мастер класс'

    def get_absolute_url(self):
        return '/master-class/%s/' % self.slug


class MasterClassPoint(models.Model):
    master_class_item = models.ForeignKey(MasterClassItem, related_name='master_class_point', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class MasterClassPrice(models.Model):
    master_class_item = models.ForeignKey(MasterClassItem, related_name='master_class_price', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255, null=True, blank=True)
    text = models.CharField('text', max_length=255, null=True, blank=True)
    units = models.CharField('Единица', max_length=255, null=True, blank=True)
    sale = models.BooleanField('Скидка', default=False)
    price_sale = models.CharField('Цена по скидке', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    # ----------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------


class GroupLessons(models.Model):
    title = models.CharField('title', max_length=255, null=True, blank=True)
    slug = models.SlugField('slug', max_length=255, blank=True, unique=True)
    image = models.ImageField('image', upload_to='group_lessons/', default='group_lessons/no_image.jpg', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Групповые занятия'
        verbose_name_plural = 'Групповые занятия'

    def get_absolute_url(self):
        return '/group-lessons/%s/' % self.slug


class GroupLessonsItem(models.Model):
    group_lessons_item = models.ForeignKey(GroupLessons, related_name='group_lessons_item', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255, null=True, blank=True)
    slug = models.SlugField('slug', max_length=255, blank=True, unique=True)
    text = models.TextField('text', null=True, blank=True)
    teacher = models.CharField('teacher', max_length=255, null=True, blank=True)
    profession = models.CharField('profession', max_length=255, null=True, blank=True)
    photo = models.ImageField('photo', upload_to='photo_teacher/', default='photo_teacher/no_image.jpg',
                              null=True, )
    image = models.ImageField('image', upload_to='group_lessons_item/', default='group_lessons_item/no_image.jpg',
                              null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Групповое занятие'
        verbose_name_plural = 'Групповое занятие'

    def get_absolute_url(self):
        return '/group-lesson/%s/' % self.slug


class GroupLessonsPoint(models.Model):
    group_lessons_point = models.ForeignKey(GroupLessonsItem, related_name='group_lessons_point',
                                            on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class GroupLessonsPrice(models.Model):
    group_lessons_price = models.ForeignKey(GroupLessonsItem, related_name='group_lessons_price',
                                            on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    text = models.CharField('Цена', max_length=255, null=True, blank=True)
    units = models.CharField('Единица', max_length=255, null=True, blank=True)
    sale = models.BooleanField('Скидка', default=False)
    price_sale = models.CharField('Цена по скидке', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class VideoIndex(models.Model):
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    video = models.FileField('Видео', upload_to='video/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео на главной странице'
        verbose_name_plural = 'Видео на главной странице'


class BlogDetails(models.Model):
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    slug = models.SlugField('slug', max_length=255, blank=True, unique=True)
    date_post = models.CharField('Дата поста', max_length=255, null=True, blank=True)
    text_mini = models.TextField('Текст в посте', null=True, blank=True)
    text = models.TextField('Текст', null=True, blank=True)
    image = models.ImageField('Картинка', upload_to='blog/', default='blog/no_image.jpg',
                              null=True)
    price = models.CharField('Цена', max_length=255, null=True, blank=True)
    date_course = models.TextField('Расписание', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/blog-list/%s/' % self.slug

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
