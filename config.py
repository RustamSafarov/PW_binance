<<<<<<< HEAD
import os
from dotenv import load_dotenv
import requests

# Загружаем переменные окружения из файла .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
USERNAME = os.getenv("AUTH_USERNAME")
PASSWORD = os.getenv("AUTH_PASSWORD")
ROLE = os.getenv("ROLE")

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
=======
import os
from dotenv import load_dotenv
import requests

# Загружаем переменные окружения из файла .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
USERNAME = os.getenv("AUTH_USERNAME")
PASSWORD = os.getenv("AUTH_PASSWORD")
ROLE = os.getenv("ROLE")

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
>>>>>>> 722a1c2e040ca93c033ace5debc6177c3c44ec5a
        return response.status_code