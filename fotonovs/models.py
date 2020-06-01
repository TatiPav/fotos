from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Album(models.Model):
    title = models.CharField("Название альбома", max_length=100)
    slug = models.SlugField("Ссылка для альбома", max_length=100, unique=True)
    img = models.ImageField("Изображение альбома", upload_to='images')

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField("Название фотографии", max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    img = models.ImageField("Фото", upload_to='images')

    def __str__(self):
        return self.album

class Albumn(models.Model):
    name = models.CharField("Название альбома", max_length=200, db_index=True)
    slug = models.SlugField("Ссылка для альбома", max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'albumn'
        verbose_name_plural = 'albumns'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('fotonovs:photon_list_by_albumn',
                           args=[self.slug])


class Photon(models.Model):
    albumn = models.ForeignKey(Albumn, related_name='photos', on_delete=models.CASCADE)
    name = models.CharField("Название фото", max_length=200, db_index=True)
    slug = models.SlugField("Ссылка для фото", max_length=200, db_index=True)
    image = models.ImageField(upload_to='photonovs/%Y/%m/%d', blank=True)
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField("Доступный", default=True)
    created = models.DateTimeField("Созданный", auto_now_add=True)
    updated = models.DateTimeField("Обновлённый", auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('fotonovs:photon_detail',
                           args=[self.id, self.slug])

class Shape(models.Model):
    # Форма для предварительной записи на съемку.Формирует администратор
    text = models.CharField("Внести свободную дату с информацией", max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
    text = models.TextField("Сообщите контакты и дополнительную информацию")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # показывает частичный текст
        return f"{self.text[:50]}..."
