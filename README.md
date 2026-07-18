# Stellar Burgers API tests

Автотесты для API сервиса [Stellar Burgers](https://stellarburgers.education-services.ru).

Документация API: https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/Api-Stellar_Burgers.pdf

## Стек

- `pytest`
- `requests`
- `allure-pytest`
- `Faker` (генерация уникальных данных пользователя)

## Что покрыто тестами

**Создание пользователя** (`tests/test_register.py`)
- создание уникального пользователя;
- создание уже зарегистрированного пользователя;
- создание пользователя без одного из обязательных полей (`email`, `password`, `name` — отдельными тестами).

**Логин пользователя** (`tests/test_login.py`)
- вход под существующим пользователем;
- вход с неверным логином и паролем.

**Создание заказа** (`tests/test_orders.py`)
- с авторизацией;
- без авторизации;
- с ингредиентами;
- без ингредиентов;
- с неверным хешем ингредиента.

Каждый тест, создающий пользователя, удаляет его после прогона (fixture `registered_user` в `conftest.py`), чтобы не засорять базу данных сервиса.

## Установка

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Для генерации Allure-отчёта дополнительно нужен установленный Allure commandline
(https://allurereport.org/docs/install/), например:

```bash
# macOS
brew install allure

# Linux (через npm)
npm install -g allure-commandline --save-dev
```

## Запуск тестов

Прогон всех тестов:

```bash
pytest
```

Прогон конкретной группы тестов:

```bash
pytest -m register
pytest -m login
pytest -m orders
```

## Формирование Allure-отчёта

1. Прогнать тесты с сохранением результатов:

```bash
pytest --alluredir=allure-results
```

2. Сгенерировать и открыть HTML-отчёт:

```bash
allure serve allure-results
```

или, чтобы собрать статический отчёт в папку `allure-report`:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Структура проекта

```
.
├── conftest.py              # общие фикстуры (клиент, тестовый пользователь, ингредиенты, teardown)
├── constants.py              # базовый URL и эндпоинты
├── pytest.ini                # маркеры и настройки pytest
├── requirements.txt
├── utils/
│   ├── api_client.py         # обёртка над requests с шагами Allure
│   └── user_generator.py     # генерация случайных данных пользователя (Faker)
└── tests/
    ├── test_register.py
    ├── test_login.py
    └── test_orders.py
```
