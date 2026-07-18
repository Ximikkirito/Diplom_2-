from faker import Faker

fake = Faker()


def generate_user():
    """Генерирует данные уникального пользователя для регистрации/логина."""
    return {
        "email": f"{fake.user_name()}_{fake.random_number(digits=6)}@yandex-test.ru",
        "password": fake.password(length=10),
        "name": fake.first_name(),
    }
