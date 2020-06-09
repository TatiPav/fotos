# Generated by Django 3.0.6 on 2020-05-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotonovs', '0007_auto_20200529_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photon',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступный'),
        ),
        migrations.AlterField(
            model_name='photon',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Созданный'),
        ),
        migrations.AlterField(
            model_name='photon',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='photon',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Название фото'),
        ),
        migrations.AlterField(
            model_name='photon',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='Ссылка для фото'),
        ),
        migrations.AlterField(
            model_name='photon',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлённый'),
        ),
    ]
