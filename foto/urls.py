from django.urls import path, include
from . import views

app_name = 'foto'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]