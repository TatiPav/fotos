from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Shape, Entry
from .forms import ShapeForm, EntryForm


def index(request):
    # Домашняя страница для приложения fotonov
    return render(request, 'fotonovs/index.html')

@login_required
def shapes(request):
    # Показывает все даты для записи
    shapes = Shape.objects.filter(owner=request.user).order_by('date_added')
    context = {'shapes': shapes}
    return render(request, 'fotonovs/shapes.html', context)


@login_required
def shape(request, shape_id):
    # Выводит дату и запись к ней
    shape = Shape.objects.get(id=shape_id)
    if shape.owner != request.user:
        raise Http404

    entries = shape.entry_set.order_by('-date_added')
    context = {'shape': shape, 'entries': entries}
    return render(request, 'fotonovs/shape.html', context)
@login_required
def new_shape(request):
    if request.method != 'POST':
        # Создаётся новая пустая форма
        form = ShapeForm()
    else:
        # После отправки данных идёт обработка
        form = ShapeForm(data=request.POST)
        if form.is_valid():
            new_shape = form.save(commit=False)
            new_shape.owner = request.user
            new_shape.save()
            return redirect('fotonovs:shapes')

    context = {'form': form}
    return render(request, 'fotonovs/new_shape.html', context)

@login_required
def new_entry(request, shape_id):
    # Id для добавления записи к конкретной дате
    shape = Shape.objects.get(id=shape_id)

    if request.method != 'POST':
        # Создание пустой формы
        form = EntryForm()
    else:
        # Обработка внесённой информации
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.shape = shape
            new_entry.save()
            return redirect('fotonovs:shape', shape_id=shape_id)

    context = {'shape': shape, 'form': form}
    return render(request, 'fotonovs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    # Возможность редактирования записи
    entry = Entry.objects.get(id=entry_id)
    shape = entry.shape
    if shape.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Текущая запись
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('fotonovs:shape', shape_id=shape.id)

    context = {'entry': entry, 'shape': shape, 'form': form}
    return render(request, 'fotonovs/edit_entry.html', context)