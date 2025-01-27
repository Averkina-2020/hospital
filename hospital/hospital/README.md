# API-сервер на Django для учетных записей врачей и пациентов


## Структура репозитория
1. **tests** = `api/tests.py`
2. **code** = `myproject/`
3. **docker** = `Dockerfile`
4. **migrations** = `myproject/migrations/`
## Инструкции по локальному запуску
1. **Установите зависимости**:
    ```
    pip install -r requirements.txt
    ```
2. **Запустите миграции**:
    ```
    python manage.py migrate
    ```
3. **Запустите сервер**:
    ```
    python manage.py runserver
    ```
4. **Открытие Swagger UI**:
    После запуска сервера, откройте браузер и перейдите по следующему адресу для доступа к Swagger UI:
    http://127.0.0.1:8000/swagger/

    Или по адресу для ReDoc:
    http://127.0.0.1:8000/redoc/
5. **Отправка запросов**:
    - Для получения JWT-токена:
      ```
      POST /api/login/
      ```
    - Для получения списка пациентов:
      ```
      GET /api/patients/
      ```


## Разработка в Docker (опционально)
1. **Создайте Docker образ**:
    ```
    docker build -t mydjangoapp .
    ```
2. **Запустите контейнер**:
    ```
    docker run -p 8000:8000 mydjangoapp
    ```
3. **Открытие Swagger UI в Docker**:
    Перейдите по тому же адресу:
    http://127.0.0.1:8000/swagger/



## Тестирование
Для запуска тестов выполните команду:
```
python manage.py test api
```