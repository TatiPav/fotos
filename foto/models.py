from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
import uuid

class Album(models.Model):
    title = models.CharField("Группа", max_length=70)
    description = models.TextField("Описание", max_length=800)
    thumb = ProcessedImageField( upload_to='albums', processors=[ResizeToFit(300)],
                                format='JPEG', options={'quality': 90})
    tags = models.CharField("Теги", max_length=250)
    is_visible = models.BooleanField("Доступность", default=True)
    created = models.DateTimeField("Созданный", auto_now_add=True)
    modified = models.DateTimeField("Изменённый", auto_now_add=True)
    slug = models.SlugField("Уникальное поле слага", max_length=50, db_index=True,
                            unique=True)

    def __str__(self):
        return self.title

class AlbumImage(models.Model):
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)],
                                format='JPEG',
                                options={'quality': 70})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)],
                                format='JPEG', options={'quality': 80})
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField("Созданный", auto_now_add=True)
    width = models.IntegerField("Ширина", default=0)
    height = models.IntegerField("Высота", default=0)
    slug = models.SlugField("Уникальное поле слага", max_length=70, default=uuid.uuid4,
                            editable=False)