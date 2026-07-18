import allure
import requests

from constants import (
    REGISTER_URL,
    LOGIN_URL,
    USER_URL,
    ORDERS_URL,
    INGREDIENTS_URL,
)


class StellarBurgersClient:
    """Тонкая обёртка над requests для эндпоинтов Stellar Burgers API."""

    @allure.step("Создание пользователя (POST /auth/register)")
    def register_user(self, user_data: dict):
        return requests.post(REGISTER_URL, json=user_data)

    @allure.step("Логин пользователя (POST /auth/login)")
    def login_user(self, credentials: dict):
        return requests.post(LOGIN_URL, json=credentials)

    @allure.step("Удаление пользователя (DELETE /auth/user)")
    def delete_user(self, access_token: str):
        headers = {"Authorization": access_token}
        return requests.delete(USER_URL, headers=headers)

    @allure.step("Получение списка ингредиентов (GET /ingredients)")
    def get_ingredients(self):
        return requests.get(INGREDIENTS_URL)

    @allure.step("Создание заказа (POST /orders)")
    def create_order(self, ingredients: list, access_token: str = None):
        headers = {"Authorization": access_token} if access_token else {}
        body = {"ingredients": ingredients} if ingredients is not None else {}
        return requests.post(ORDERS_URL, json=body, headers=headers)
