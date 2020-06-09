# fotos
реализация сайта фотостудии на Django.
Фото текущего вида основной страницы находится в приложении vid.

Приложение fotonovs - управление администратором.

Приложение users - регистрация пользователя с возможность создания интересующей его даты съёмки и отправки сообщения для фотографа.

Приложение foto загружает фотограции и  должно выводить их по темам с подробной информацией.


python -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install Django

pip install django-bootstrap4

pip install django-imagekit

python -m pip install Pillow

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
