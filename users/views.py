from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method != 'POST':
        # Регистрация нового пользователя
        form = UserCreationForm()
    else:
        # Обработка заполненной формы
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # После выполнения входа - переход на домашнюю страницу
            login(request, new_user)
            return redirect('fotonovs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)