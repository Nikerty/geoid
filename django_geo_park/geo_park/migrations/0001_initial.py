# Generated by Django 4.1.4 on 2023-03-31 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Наименование категории')),
                ('photo', models.ImageField(upload_to='photo/information/categories/%Y/%m/%d/', verbose_name='Фотография')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный')),
            ],
        ),
        migrations.CreateModel(
            name='SubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('is_active', models.IntegerField(default=10, verbose_name='Количество запросов')),
                ('is_ban', models.BooleanField(verbose_name='Активный')),
                ('subscription', models.CharField(choices=[('1', 'Начинающий тариф'), ('2', 'Оптимальный тариф'), ('3', 'Продвинутый тариф')], default='2', max_length=1, verbose_name='Подписка')),
                ('start_time_sub', models.DateTimeField(verbose_name='Дата последнего платежа')),
                ('end_time_sub', models.DateTimeField(verbose_name='Дата окончания подписки')),
                ('is_sub', models.BooleanField(verbose_name='Активность подписки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('photo', models.ImageField(upload_to='photo/information/news/%Y/%m/%d/', verbose_name='Фотография')),
                ('desc', models.TextField(verbose_name='Контент')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_park.categoriesnews', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('is_active', models.IntegerField(default=10, verbose_name='Количество запросов')),
                ('is_ban', models.BooleanField(verbose_name='Активный')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='EditImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_user', models.ImageField(upload_to='photo/image_user/%Y/%m/%d/', verbose_name='Фотография пользователя')),
                ('image_neural', models.ImageField(blank=True, null=True, upload_to='photo/image_user/%Y/%m/%d/', verbose_name='Обработанная фотография')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание к изображению')),
                ('is_done', models.BooleanField(default=False, verbose_name='Обработанный заказ')),
                ('user_general', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo_park.generaluser', verbose_name='Гость')),
                ('user_sub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo_park.subuser', verbose_name='Пользователь с подпиской')),
            ],
        ),
    ]
