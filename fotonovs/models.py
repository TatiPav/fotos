from django.db import models
from django.contrib.auth.models import User

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
