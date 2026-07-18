import allure

from utils.user_generator import generate_user


@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
class TestRegisterUser:

    @allure.title("Можно создать уникального пользователя")
    def test_create_unique_user(self, api_client, user_data):
        response = api_client.register_user(user_data)
        body = response.json()

        with allure.step("Проверить код ответа 200 и успешную регистрацию"):
            assert response.status_code == 200
            assert body["success"] is True
            assert body["user"]["email"] == user_data["email"].lower()
            assert body["user"]["name"] == user_data["name"]
            assert "accessToken" in body
            assert "refreshToken" in body

        # teardown: удаляем созданного пользователя, чтобы не засорять базу
        api_client.delete_user(body["accessToken"])

    @allure.title("Нельзя создать пользователя, который уже зарегистрирован")
    def test_create_already_registered_user(self, api_client, registered_user):
        duplicate_response = api_client.register_user(registered_user["user"])
        body = duplicate_response.json()

        with allure.step("Проверить код ответа 403 и сообщение об ошибке"):
            assert duplicate_response.status_code == 403
            assert body["success"] is False
            assert body["message"] == "User already exists"

    @allure.title("Нельзя создать пользователя без обязательного поля email")
    def test_create_user_without_email(self, api_client, user_data):
        del user_data["email"]
        response = api_client.register_user(user_data)
        body = response.json()

        with allure.step("Проверить код ответа 403 и сообщение об ошибке"):
            assert response.status_code == 403
            assert body["success"] is False
            assert body["message"] == "Email, password and name are required fields"

    @allure.title("Нельзя создать пользователя без обязательного поля password")
    def test_create_user_without_password(self, api_client, user_data):
        del user_data["password"]
        response = api_client.register_user(user_data)
        body = response.json()

        with allure.step("Проверить код ответа 403 и сообщение об ошибке"):
            assert response.status_code == 403
            assert body["success"] is False
            assert body["message"] == "Email, password and name are required fields"

    @allure.title("Нельзя создать пользователя без обязательного поля name")
    def test_create_user_without_name(self, api_client, user_data):
        del user_data["name"]
        response = api_client.register_user(user_data)
        body = response.json()

        with allure.step("Проверить код ответа 403 и сообщение об ошибке"):
            assert response.status_code == 403
            assert body["success"] is False
            assert body["message"] == "Email, password and name are required fields"
