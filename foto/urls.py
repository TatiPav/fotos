from django.urls import path, include
from . import views

app_name = 'foto'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('albub_detail/', views.albub_detail, name='albub_detail'),
    path('gallery/', views.gallery, name='gallery'),
]