BASE_URL = "https://stellarburgers.education-services.ru/api"

REGISTER_URL = f"{BASE_URL}/auth/register"
LOGIN_URL = f"{BASE_URL}/auth/login"
LOGOUT_URL = f"{BASE_URL}/auth/logout"
USER_URL = f"{BASE_URL}/auth/user"
ORDERS_URL = f"{BASE_URL}/orders"
INGREDIENTS_URL = f"{BASE_URL}/ingredients"

# заведомо некорректный/несуществующий хеш ингредиента
INVALID_INGREDIENT_HASH = "111111111111111111111111"
