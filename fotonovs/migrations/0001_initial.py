# Generated by Django 3.0.6 on 2020-05-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название альбома')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Ссылка для альбома')),
                ('img', models.ImageField(upload_to='images', verbose_name='Изображение альбома')),
            ],
        ),
    ]
