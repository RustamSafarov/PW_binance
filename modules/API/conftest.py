import pytest
from config import Authorization, API_KEY, USERNAME, PASSWORD
from pw_pets.modules.API.meths import PetstoreClient

@pytest.fixture(scope="function")
def petstore_client():
    """
    Фикстура для клиента Petstore.
    """
    client = PetstoreClient(api_key=API_KEY)
    yield client
    # Здесь можно добавить teardown, если необходимо 