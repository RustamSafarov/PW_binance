import requests
from config import API_KEY
from config import Authorization

class PetstoreClient:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self, api_key=None):
        self.api_key = api_key or API_KEY
        self.auth = Authorization()

    def _get_headers(self):
        headers = {}
        if self.api_key:
            headers['api_key'] = self.api_key
        return headers

    def add_pet(self, pet_data):
        """
        Добавляет нового питомца в магазин.

        :param pet_data: Объект питомца, который необходимо добавить в магазин
        :return: Добавленный объект питомца
        """
        url = f"{self.BASE_URL}/pet"
        response = requests.post(url, json=pet_data, headers=self._get_headers())
        return response.json()

    def update_pet(self, pet_data):
        """
        Обновляет существующего питомца.

        :param pet_data: Объект питомца, который необходимо обновить
        :return: Обновленный объект питомца
        """
        url = f"{self.BASE_URL}/pet"
        response = requests.put(url, json=pet_data, headers=self._get_headers())
        return response.json()

    def find_pets_by_status(self, status):
        """
        Находит питомцев по статусу.

        :param status: Статус питомца для фильтрации (доступны: available, pending, sold)
        :return: Список питомцев
        """
        url = f"{self.BASE_URL}/pet/findByStatus?status={status}"
        response = requests.get(url, headers=self._get_headers())
        return response.json()

    def get_pet_by_id(self, pet_id):
        """
        Получает питомца по ID.

        :param pet_id: ID питомца для получения
        :return: Объект питомца
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.get(url, headers=self._get_headers())
        return response.json()

    def delete_pet(self, pet_id):
        """
        Удаляет питомца по ID.

        :param pet_id: ID питомца для удаления
        :return: Ответ API
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.delete(url, headers=self._get_headers())
        return response.status_code

    def upload_image(self, pet_id, file_path, additional_metadata=None):
        """
        Загружает изображение питомца.

        :param pet_id: ID питомца для обновления
        :param file_path: Путь к файлу изображения
        :param additional_metadata: Дополнительные данные для передачи на сервер
        :return: Ответ API
        """
        url = f"{self.BASE_URL}/pet/{pet_id}/uploadImage"
        files = {'file': open(file_path, 'rb')}
        data = {'additionalMetadata': additional_metadata} if additional_metadata else {}
        response = requests.post(url, files=files, data=data, headers=self._get_headers())
        return response.json()

    def upload_file(self, pet_id, file_path, additional_metadata=None):
        """
        Загружает файл для питомца.

        :param pet_id: ID питомца для обновления
        :param file_path: Путь к файлу
        :param additional_metadata: Дополнительные данные для передачи на сервер
        :return: Ответ API
        """
        url = f"{self.BASE_URL}/pet/{pet_id}/uploadImage"
        files = {'file': open(file_path, 'rb')}
        data = {'additionalMetadata': additional_metadata} if additional_metadata else {}
        response = requests.post(url, files=files, data=data, headers=self._get_headers())
        return response.json()

    def get_inventory(self):
        """
        Возвращает инвентарь питомцев по статусу.

        :return: Словарь с количеством питомцев по статусам
        """
        url = f"{self.BASE_URL}/store/inventory"
        response = requests.get(url, headers=self._get_headers())
        return response.json()

    def place_order(self, order_data):
        """
        Размещает заказ на питомца.

        :param order_data: Данные заказа для размещения
        :return: Созданный объект заказа
        """
        url = f"{self.BASE_URL}/store/order"
        response = requests.post(url, json=order_data, headers=self._get_headers())
        return response.json()

    def get_order_by_id(self, order_id):
        """
        Получает заказ по ID.

        :param order_id: ID заказа для получения
        :return: Объект заказа
        """
        url = f"{self.BASE_URL}/store/order/{order_id}"
        response = requests.get(url, headers=self._get_headers())
        return response.json()

    def delete_order(self, order_id):
        """
        Удаляет заказ по ID.

        :param order_id: ID заказа для удаления
        :return: Ответ API
        """
        url = f"{self.BASE_URL}/store/order/{order_id}"
        response = requests.delete(url, headers=self._get_headers())
        return response.status_code

    def create_user(self, user_data):
        """
        Создает нового пользователя.

        :param user_data: Данные нового пользователя
        :return: Ответ API
        """
        url = f"{self.BASE_URL}/user"
        response = requests.post(url, json=user_data, headers=self._get_headers())
        return response.json()

    def create_users_with_array_input(self, users):
        """
        Создает список пользователей по заданному массиву данных.

        :param users: Массив объектов пользователей
        :return: Ответ API
        """
        url = f"{self.BASE_URL}/user/createWithArray"
        response = requests.post(url, json=users, headers=self._get_headers())
        return response.json()

    def create_users_with_list_input(self, users):
        """
        Создает список пользователей по заданному списку данных.

        :param users: Список объектов пользователей
        :return: Ответ API
        """
        url = f"{self.BASE_URL}/user/createWithList"
        response = requests.post(url, json=users, headers=self._get_headers())
        return response.json()

    def get_user_by_name(self, username):
        """
        Получает пользователя по имени.

        :param username: Имя пользователя для получения
        :return: Объект пользователя
        """
        url = f"{self.BASE_URL}/user/{username}"
        response = requests.get(url, headers=self._get_headers())
        return response.json()

    def update_user(self, username, user_data):
        """
        Обновляет данные пользователя.

        :param username: Имя пользователя для обновления
        :param user_data: Обновленные данные пользователя
        :return: Ответ API
        """
        url = f"{self.BASE_URL}/user/{username}"
        response = requests.put(url, json=user_data, headers=self._get_headers())
        return response.json()

    def delete_user(self, username):
        """
        Удаляет пользователя.

        :param username: Имя пользователя для удаления
        :return: Ответ API
        """
        url = f"{self.BASE_URL}/user/{username}"
        response = requests.delete(url, headers=self._get_headers())
        return response.status_code

    def login_user(self, username, password):
        """
        Авторизует пользователя в системе.

        :param username: Имя пользователя для входа
        :param password: Пароль пользователя
        :return: Токен авторизации или сообщение об ошибке
        """
        return self.auth.login_user(username, password)

    def logout_user(self):
        """
        Выход текущего авторизованного пользователя из системы.

        :return: Ответ API
        """
        return self.auth.logout_user()