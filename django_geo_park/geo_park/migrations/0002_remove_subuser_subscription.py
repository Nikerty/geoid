# Generated by Django 4.1.4 on 2023-03-31 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_park', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subuser',
            name='subscription',
        ),
    ]