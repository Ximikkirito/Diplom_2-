import pytest

from utils.api_client import StellarBurgersClient
from utils.user_generator import generate_user


@pytest.fixture
def api_client():
    return StellarBurgersClient()


@pytest.fixture
def user_data():
    """Данные нового уникального пользователя (не регистрирует его)."""
    return generate_user()


@pytest.fixture
def registered_user(api_client):
    """
    Регистрирует нового пользователя, возвращает его данные и токены,
    после теста гарантированно удаляет пользователя (teardown).
    """
    user = generate_user()
    response = api_client.register_user(user)
    body = response.json()

    yield {
        "user": user,
        "access_token": body.get("accessToken"),
        "refresh_token": body.get("refreshToken"),
        "response": response,
    }

    access_token = body.get("accessToken")
    if access_token:
        api_client.delete_user(access_token)


@pytest.fixture
def valid_ingredient_ids(api_client):
    """Возвращает список из двух реальных id ингредиентов с сервера."""
    response = api_client.get_ingredients()
    data = response.json()["data"]
    return [data[0]["_id"], data[1]["_id"]]
