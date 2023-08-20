# Социальная сеть Yatube

### Описание
Yatube позволяет публиковать записи, комментировать их, а также подписываться на любимых авторов, просматривать группы

### Технологии:
Python, Django, DRF, JWT + djoser

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/EvgenyMi/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:
```bash
cd yatube_api
python manage.py migrate
```

Запустить проект:
```bash
python3 manage.py runserver
```


### Когда вы запустите проект, по адресу  http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube. В документации описано, как работает ваш API. Документация представлена в формате Redoc.
