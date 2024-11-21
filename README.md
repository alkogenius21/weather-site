
# Сайт-приложение для получения погоды по городам

Проект - тестовое задние

## Основной стек

1) Python 3.13
2) Django
3) Django Rest Framework
4) Postgresql
5) Redis

## Инструкция по запуску
1) Склонируйте репозиторий на вашу машину ```git clone https://github.com/alkogenius21/weather-site.git```
2) Через Docker compose
- Требования:
    1) Docker >= 21
- Пошаговый запуск:
    1) Создайте файл ```.env``` в корне проекта и на основе шаблона заполните чувствительные данные для базы данных
    2) Прейдите в папку ```weather_site``` и создайте файл ```.env``` и на основе шаблона заполните чувствительные данные для самого приложения
    3) Запустите сборку из под корневой папки проекта командой ```sudo docker compose up -d --build```
    4) Сайт будет доступен по адресу машины или по адресу ```localhost``` из под самой машины
    5) После поднятия всех контейнеров, через менеджер баз данных(например Dbeaver) сделайте restore базы данных из дампа. Дамп лежит в папке ```db_initial```
3) Развернуть локально(dev-server)
- Требования:
    1) Python >= 3.12.0
    2) Poetry >= 1.8.0 (Необязательно)
- Пошаговый запуск:
    1) Из корня проекта перейдите в папку ```weather_site``` и создайте файл ```.env``` и на основе шаблона заполните чувствительные данные для самого приложения

    2) Убедитесь что внешний сервисы (postgres и redis) доступны на вашей машине

    3) Создайте папку ```log``` внутри проекта

    4) Создайте виртуальную среду выполнения python и активируйте её
    - Через Poetry:
        ```poetry shell```
    - Через Python:
        ```python -m venv venv``` ->
        ```source /venv/bin/activate```(Linux) или ```venv\Scripts\activate.bat```(Windows)

    5) Устновите зависимости проекта
    - Через pip:
    ``` pip install -r requirements.txt```
    - через Poetry:
    ```poetry install```

    6) Примените миграции к БД
    ```python manage.py migrate```

    7) Запустите само приложение
    ```python manage.py runserver```
    
## Эндпоинты
1) SSR приложение на django шаблонах
- При переходе на адрес приложения по умолчанию откроется версия на шаблонах. 
- Один запрос реализован исключительно на передаче контекста в шаблона
- Второй запрос сделан на базе JavaScript
2) Api приложение с использованием django rest Framework
- Api принимает запрос по пути ```/api/v1/some_path/```
- У Api приложения есть схема и удобная визуальная оболочка
    - схема доступна по адресу ```/api/v1/schema/```
    - ui доступен по адресу ```/api/v1/swagger/```
- Согласно ТЗ реализован всего один эндпоинт

## Кратко про архитектуру проекта
Для реализации я использовал отдельное django-приложение в котором описана основная логика получения координат города и погоды по этим координатам. Приложение называется ```core```, на основе его модулей я описал представления для шаблонного приложения и для api приложения.

## Использованные инструменты
Для форматирования и проверки кода на соотвествие Style Guide(Pep 8) я использовал линтер [Ruff](https://docs.astral.sh/ruff/). Настройки вы можете посмотреть в файле ```pyproject.toml```

## Авторы
Разработчик приложения - [Обухов Николай Романович](https://t.me/a1kogenius)