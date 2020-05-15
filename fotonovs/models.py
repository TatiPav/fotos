from django.db import models
from django.contrib.auth.models import User

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
