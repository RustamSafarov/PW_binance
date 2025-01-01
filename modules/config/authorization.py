import requests
from config import API_KEY

class Authorization:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self, api_key=None):
        self.api_key = API_KEY

    def _get_headers(self):
        headers = {}
        if self.api_key:
            headers['api_key'] = self.api_key
        return headers

    def login_user(self, username, password):
        """
        Авторизует пользователя в системе.

        :param username: Имя пользователя для входа
        :param password: Пароль пользователя
        :return: Токен авторизации или сообщение об ошибке
        """
        url = f"{self.BASE_URL}/user/login"
        params = {'username': username, 'password': password}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response.json()

    def logout_user(self):
        """
        Выход текущего авторизованного пользователя из системы.

        :return: Ответ API
        """
        url = f"{self.BASE_URL}/user/logout"
        response = requests.get(url, headers=self._get_headers())
        return response.status_code 