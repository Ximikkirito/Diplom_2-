import allure


@allure.epic("Stellar Burgers API")
@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Можно залогиниться под существующим пользователем")
    def test_login_existing_user(self, api_client, registered_user):
        credentials = {
            "email": registered_user["user"]["email"],
            "password": registered_user["user"]["password"],
        }
        response = api_client.login_user(credentials)
        body = response.json()

        with allure.step("Проверить код ответа 200 и наличие токенов"):
            assert response.status_code == 200
            assert body["success"] is True
            assert "accessToken" in body
            assert "refreshToken" in body
            assert body["user"]["email"] == registered_user["user"]["email"].lower()

    @allure.title("Нельзя залогиниться с неверным логином и паролем")
    def test_login_with_wrong_credentials(self, api_client, registered_user):
        credentials = {
            "email": "not_" + registered_user["user"]["email"],
            "password": "wrong_" + registered_user["user"]["password"],
        }
        response = api_client.login_user(credentials)
        body = response.json()

        with allure.step("Проверить код ответа 401 и сообщение об ошибке"):
            assert response.status_code == 401
            assert body["success"] is False
            assert body["message"] == "email or password are incorrect"
