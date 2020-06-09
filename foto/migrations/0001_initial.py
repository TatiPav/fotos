# Generated by Django 3.0.6 on 2020-06-01 16:01

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Группа')),
                ('description', models.TextField(max_length=800, verbose_name='Описание')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to='albums')),
                ('tags', models.CharField(max_length=250, verbose_name='Теги')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Доступность')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Созданный')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='Изменённый')),
                ('slug', models.SlugField(unique=True, verbose_name='Уникальное поле слага')),
            ],
        ),
    ]
