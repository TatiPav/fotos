from django.contrib import admin

# Register your models here.
from fotonovs.models import Album, Shape, Photo, Entry

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Shape)
admin.site.register(Entry)

from fotonovs.models import Albumn, Photon

class AlbumnAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Albumn, AlbumnAdmin)

class PhotonAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Photon, PhotonAdmin)