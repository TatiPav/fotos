from django.contrib import admin

# Register your models here.
from fotonovs.models import Album, Shape, Photo, Entry

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Shape)
admin.site.register(Entry)
