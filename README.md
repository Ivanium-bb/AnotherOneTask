## Задача:

#### Реализовать приложение с возможностью регистрации, авторизации, выхода из аккаунат. Пользвоатели могут создавать записи. Доступны для простомтра, изменения и удаления только записи, созданные определённым пользователем. Покрыть весь функционал тестами.
## Запуск и проверка:

#### Иницализация БД:

``` $ docker-compose up ```

#### Применение миграций:

``` $ python manage.py migrate ```

#### Запуск тестов:

``` $ python manage.py test ```

#### Запуск приложения:

``` $ python manage.py runserver ```
## Регистрация:

###    

    curl --location --request POST 'http://127.0.0.1:8000/api/v1/register/' \ 
    --form 'email="ivan10@gmail.com"' \
    --form 'name="ivan10"' \
    --form 'password="Skzw11235"'   

## Получение всех записей залогиненного пользователя:

###  

    curl --location --request GET 'http://127.0.0.1:8000/api/v1/note/' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4Mzc5NDg3LCJpYXQiOjE2NzgzNTc4ODcsImp0aSI6IjUyZTU5ZjgwZDEzMTQ3ZTY4MDY3YTgzMWVlMmFjNTU1IiwidXNlcl9pZCI6NH0.tS3CmgreZZr4NP3pQKcQ9h_7suL0RTm1sXYXMvaUhWo' \

## Создание записи:

###  

    curl --location --request POST 'http://127.0.0.1:8000/api/v1/note/' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4MzcxMzMwLCJpYXQiOjE2NzgzNDk3MzAsImp0aSI6ImJiYTY4MDUxOTA4NzQ2MmFiMTcxZTAzMGVkN2QxYmIzIiwidXNlcl9pZCI6MTR9.Z6A7I829EXHwOz25itRr_bKXaZvKi3MuCaqvC4H-X3U' \
    --form 'title="title10"' \
    --form 'description="description10"'


## Примечание:

### Для обеспечения должного уровня безопасности, оптимальным вариантом будет использование secure cookie в Front-End приложении. Сейчас же реализованна возможность добавлять Refresh token в BlackList.