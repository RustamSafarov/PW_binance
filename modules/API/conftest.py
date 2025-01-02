<<<<<<< HEAD
import pytest
from config import Authorization, API_KEY, USERNAME, PASSWORD
from modules.API.meths import PetstoreClient

@pytest.fixture(scope="function")
def petstore_client():
    """
    Фикстура для клиента Petstore.
    """
    client = PetstoreClient(api_key=API_KEY)
    yield client
=======
import pytest
from pw_pets.config import Authorization, API_KEY, USERNAME, PASSWORD
from PW_pets.modules.API.meths import PetstoreClient

@pytest.fixture(scope="function")
def petstore_client():
    """
    Фикстура для клиента Petstore.
    """
    client = PetstoreClient(api_key=API_KEY)
    yield client
>>>>>>> 722a1c2e040ca93c033ace5debc6177c3c44ec5a
    # Здесь можно добавить teardown, если необходимо 