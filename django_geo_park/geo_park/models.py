from django.db import models
from django.contrib.auth.models import User


class GeneralUser(models.Model):
    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телефона', max_length=11)
    is_active = models.IntegerField(verbose_name='Количество запросов', default=10)
    is_ban = models.BooleanField(verbose_name='Активный')

    def __str__(self):
        return f'{self.user.username}'


class SubUser(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    SUBSCRIPTION_FIELDS = [
        ('1', 'Начинающий тариф'),
        ('2', 'Оптимальный тариф'),
        ('3', 'Продвинутый тариф'),
    ]

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телефона', max_length=11)
    is_active = models.IntegerField(verbose_name='Количество запросов', default=10)
    is_ban = models.BooleanField(verbose_name='Активный')
    subscription = models.CharField(verbose_name='Подписка', choices=SUBSCRIPTION_FIELDS, max_length=1, default='2')
    start_time_sub = models.DateTimeField(verbose_name='Дата последнего платежа')
    end_time_sub = models.DateTimeField(verbose_name='Дата окончания подписки')
    is_sub = models.BooleanField(verbose_name='Активность подписки')

    def __str__(self):
        return f'{self.user.username}'


class EditImage(models.Model):
    class Meta:
        verbose_name = 'Обработка изображения'
        verbose_name_plural = 'Обработка изображений'

    user_general = models.ForeignKey(verbose_name='Гость', on_delete=models.CASCADE, to=GeneralUser,
                      blank=True, null=True)
    user_sub = models.ForeignKey(verbose_name='Пользователь с подпиской', on_delete=models.CASCADE, to=SubUser,
                                 blank=True, null=True)
    name_photo_user = models.CharField(verbose_name='Наименование фотографии пользователя', max_length=155)
    img_user_base64 = models.TextField(verbose_name='Base64')
    image_neural = models.ImageField(verbose_name='Обработанная фотография', upload_to='photo/image_user/%Y/%m/%d/',
                                     blank=True, null=True)
    desc = models.TextField(verbose_name='Описание к изображению', blank=True, null=True)
    is_done = models.BooleanField(verbose_name='Обработанный заказ', default=False)


class CategoriesNews(models.Model):
    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'
    name = models.CharField(verbose_name='Наименование категории', max_length=155)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/information/categories/%Y/%m/%d/')
    is_active = models.BooleanField(verbose_name='Активный', default=False)


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    categories = models.ForeignKey(to=CategoriesNews, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/information/news/%Y/%m/%d/')
    desc = models.TextField(verbose_name='Контент')
    is_active = models.BooleanField(verbose_name='Активный', default=True)


class TestModel(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=55)
    is_active = models.BooleanField(verbose_name='Активность')


class MyImageModel(models.Model):
    image = models.ImageField(upload_to='geo_entity_pic')
    data = models.CharField(max_length=500)