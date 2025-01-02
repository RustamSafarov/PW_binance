import pytest
from config import Authorization, API_KEY, USERNAME, PASSWORD


@pytest.fixture(scope="session")
def auth_client():
    """
    Фикстура для авторизации и предоставления клиента API.
    Выполняет вход в систему перед запуском тестов и выход после завершения.
    """
    auth = Authorization(api_key=API_KEY)
    login_response = auth.login_user(USERNAME, PASSWORD)
    assert login_response.get("code") == 200, "Авторизация не удалась"
    yield auth
    logout_status = auth.logout_user()
    assert logout_status == 200, "Выход из системы не удался"

@pytest.fixture(scope="session")
def petstore_client(auth_client):
    """
    Фикстура для клиента Petstore, использующая авторизованный клиент.
    """