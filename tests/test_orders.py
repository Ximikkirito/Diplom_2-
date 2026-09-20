import allure

from constants import INVALID_INGREDIENT_HASH


@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Можно создать заказ с авторизацией и ингредиентами")
    def test_create_order_with_auth(self, api_client, registered_user, valid_ingredient_ids):
        response = api_client.create_order(
            ingredients=valid_ingredient_ids,
            access_token=registered_user["access_token"],
        )
        body = response.json()

        with allure.step("Проверить код ответа 200 и данные заказа"):
            assert response.status_code == 200
            assert body["success"] is True
            assert "name" in body["order"]
            assert isinstance(body["order"]["number"], int)

    @allure.title("Можно создать заказ без авторизации")
    def test_create_order_without_auth(self, api_client, valid_ingredient_ids):
        response = api_client.create_order(ingredients=valid_ingredient_ids)
        body = response.json()

        with allure.step("Проверить код ответа 200 и данные заказа"):
            assert response.status_code == 200
            assert body["success"] is True
            assert isinstance(body["order"]["number"], int)

    @allure.title("Можно создать заказ с ингредиентами")
    def test_create_order_with_ingredients(self, api_client, registered_user, valid_ingredient_ids):
        response = api_client.create_order(
            ingredients=valid_ingredient_ids,
            access_token=registered_user["access_token"],
        )
        body = response.json()

        with allure.step("Проверить, что заказ создан и содержит переданные ингредиенты"):
            assert response.status_code == 200
            assert body["success"] is True
            assert body["order"]["ingredients"]

    @allure.title("Нельзя создать заказ без ингредиентов")
    def test_create_order_without_ingredients(self, api_client, registered_user):
        response = api_client.create_order(
            ingredients=[],
            access_token=registered_user["access_token"],
        )
        body = response.json()

        with allure.step("Проверить код ответа 400 и сообщение об ошибке"):
            assert response.status_code == 400
            assert body["success"] is False
            assert body["message"] == "Ingredient ids must be provided"

    @allure.title("Нельзя создать заказ с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, api_client, registered_user):
        response = api_client.create_order(
            ingredients=[INVALID_INGREDIENT_HASH],
            access_token=registered_user["access_token"],
        )

        with allure.step("Проверить код ответа 500 (Internal Server Error)"):
            assert response.status_code == 500
