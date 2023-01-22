# Социальная сеть Yatube

## Описание
Yatube позволяет публиковать записи, комментировать их, а также подписываться на любимых авторов, просматривать группы

## Как запустить проект:
### Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/EvgenyMi/api_final_yatube.git
cd yatube_api
### Cоздать и активировать виртуальное окружение:

python -m venv env
source venv/Scripts/activate
### Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt
### Выполнить миграции:

python manage.py migrate
### Запустить проект:

python manage.py runserver


### Когда вы запустите проект, по адресу  http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube. В документации описано, как работает ваш API. Документация представлена в формате Redoc.