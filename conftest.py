import pytest
<<<<<<< HEAD
from config import Authorization, API_KEY, USERNAME, PASSWORD

=======
from pw_pets.config import Authorization, API_KEY, USERNAME, PASSWORD
>>>>>>> 6690f4a6bc6e061597592f8c1b5295ebc381a1d2

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
<<<<<<< HEAD
    """
=======
    """
    return auth_client  # В данном случае Authorization тоже выполняет роль клиента API
>>>>>>> 6690f4a6bc6e061597592f8c1b5295ebc381a1d2
