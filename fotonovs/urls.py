"""Определяет шаблоны URL-адресов для fotonovs."""
from django.urls import path

from . import views

app_name = 'fotonovs'
urlpatterns = [
    # Домашняя страница с выводом всех тем для фото
    path('', views.index, name='index'),

    path('albumn/', views.photon_list, name='list'),

    path('<slug:albumn_slug>/', views.photon_list, name='photon_list_by_albumn'),

    path('<int:id>/<slug:slug>/', views.photon_detail,
         name='photon_detail'),
    # с выводом всех дат
    path('shapes/', views.shapes, name='shapes'),
    # информация о записи
    path('shapes/<int:shape_id>/', views.shape, name='shape'),
    # создание новой страницы с датой
    path('new_shape/', views.new_shape, name='new_shape'),
    path('new_entry/<int:shape_id>/', views.new_entry, name='new_entry'),
    # Для редактирования информации
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]