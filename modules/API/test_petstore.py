from playwright.sync_api import Page
from config import Authorization, API_KEY
import pytest
from config import USERNAME, PASSWORD
from pw_pets.modules.API.meths import PetstoreClient
import uuid



@pytest.mark.smoke
@pytest.mark.api
def test_add_and_get_pet(petstore_client):
    # Генерация уникального ID
    pet_id = uuid.uuid4().int >> 96  # получение 32-битного числа
    new_pet = {
        "id": pet_id,
        "name": "SmokeTestPet",
        "status": "available"
    }
    add_response = petstore_client.add_pet(new_pet)
    assert add_response.get("id") == new_pet["id"]
    assert add_response.get("name") == new_pet["name"]
    assert add_response.get("status") == new_pet["status"]

    # Получение информации о добавленном питомце
    get_response = petstore_client.get_pet_by_id(new_pet["id"])
    assert get_response.get("id") == new_pet["id"]
    assert get_response.get("name") == new_pet["name"]
    assert get_response.get("status") == new_pet["status"]

    # Удаление питомца после теста
    delete_status = petstore_client.delete_pet(new_pet["id"])
    assert delete_status == 200 

@pytest.mark.api
def test_update_pet(petstore_client):
    # Добавление питомца для обновления
    pet = {
        "id": 123457,
        "name": "UpdateTestPet",
        "status": "pending"
    }
    petstore_client.add_pet(pet)

    # Обновление информации о питомце
    pet['name'] = "UpdatedTestPet"
    pet['status'] = "sold"
    update_response = petstore_client.update_pet(pet)
    assert update_response.get("name") == pet["name"]
    assert update_response.get("status") == pet["status"]

    # Проверка обновленной информации
    get_response = petstore_client.get_pet_by_id(pet["id"])
    assert get_response.get("name") == pet["name"]
    assert get_response.get("status") == pet["status"]

    # Удаление питомца после теста
    delete_status = petstore_client.delete_pet(pet["id"])
    assert delete_status == 200

@pytest.mark.api
def test_find_pets_by_status(petstore_client):
    # Добавление нескольких питомцев с разными статусами
    pets = [
        {"id": 123458, "name": "AvailablePet", "status": "available"},
        {"id": 123459, "name": "SoldPet", "status": "sold"}
    ]
    for pet in pets:
        petstore_client.add_pet(pet)

    # Поиск питомцев по статусу "available"
    available_pets = petstore_client.find_pets_by_status("available")
    assert any(pet["id"] == 123458 for pet in available_pets), "Питомец с ID 123458 не найден"

    # Поиск питомцев по статусу "sold"
    sold_pets = petstore_client.find_pets_by_status("sold")
    assert any(pet["id"] == 123459 for pet in sold_pets), "Питомец с ID 123459 не найден"

    # Удаление питомцев после теста
    for pet in pets:
        delete_status = petstore_client.delete_pet(pet["id"])
        assert delete_status == 200

@pytest.mark.api
def test_upload_image(petstore_client):
    pet_id = 123460
    pet = {"id": pet_id, "name": "ImageTestPet", "status": "available"}
    petstore_client.add_pet(pet)

    # Путь к файлу изображения
    file_path = "/content/pet.png"  # Замените на актуальный путь к файлу

    # Загрузка изображения
    upload_response = petstore_client.upload_image(pet_id, file_path, additional_metadata="Test Image")
    assert upload_response.get("code") == 200
    assert "message" in upload_response, "Сообщение об успешной загрузке отсутствует"

    # Удаление питомца после теста
    delete_status = petstore_client.delete_pet(pet_id)
    assert delete_status == 200

@pytest.mark.api
def test_upload_file(petstore_client):
    pet_id = 123461
    pet = {"id": pet_id, "name": "FileTestPet", "status": "available"}
    petstore_client.add_pet(pet)

    # Путь к файлу
    file_path = "content/test.txt"  # Путь к файлу относительно текущей директории

    # Загрузка файла
    upload_response = petstore_client.upload_file(pet_id, file_path, additional_metadata="Test File")
    assert upload_response.get("code") == 200
    assert "message" in upload_response, "Сообщение об успешной загрузке отсутствует"

    # Удаление питомца после теста
    delete_status = petstore_client.delete_pet(pet_id)
    assert delete_status == 200

@pytest.mark.api
def test_get_inventory(petstore_client):
    # Получение инвентаря
    inventory = petstore_client.get_inventory()
    assert isinstance(inventory, dict), "Инвентарь должен быть словарем"

@pytest.mark.api
def test_place_order(petstore_client):
    order = {
        "id": 543210,
        "petId": 123462,
        "quantity": 1,
        "shipDate": "2023-10-10T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    # Добавление питомца для заказа
    pet = {"id": order["petId"], "name": "OrderTestPet", "status": "available"}
    petstore_client.add_pet(pet)

    # Размещение заказа
    order_response = petstore_client.place_order(order)
    assert order_response.get("id") == order["id"]
    assert order_response.get("petId") == order["petId"]
    assert order_response.get("status") == order["status"]

    # Удаление питомца после теста
    delete_status = petstore_client.delete_pet(order["petId"])
    assert delete_status == 200

@pytest.mark.api
def test_get_order_by_id(petstore_client):
    order_id = 543211
    order = {
        "id": order_id,
        "petId": 123463,
        "quantity": 2,
        "shipDate": "2023-10-11T10:00:00.000Z",
        "status": "approved",
        "complete": False
    }
    # Добавление питомца для заказа
    pet = {"id": order["petId"], "name": "GetOrderTestPet", "status": "available"}
    petstore_client.add_pet(pet)

    # Размещение заказа
    petstore_client.place_order(order)

    # Получение заказа по ID
    get_order = petstore_client.get_order_by_id(order_id)
    assert get_order.get("id") == order_id
    assert get_order.get("petId") == order["petId"]
    assert get_order.get("status") == order["status"]

    # Удаление питомца и заказа после теста
    delete_status = petstore_client.delete_pet(order["petId"])
    assert delete_status == 200
    delete_status_order = petstore_client.delete_order(order_id)
    assert delete_status_order == 200

@pytest.mark.api
def test_delete_order(petstore_client):
    order_id = 543212
    order = {
        "id": order_id,
        "petId": 123464,
        "quantity": 3,
        "shipDate": "2023-10-12T10:00:00.000Z",
        "status": "delivered",
        "complete": True
    }
    # Добавление питомца для заказа
    pet = {"id": order["petId"], "name": "DeleteOrderTestPet", "status": "available"}
    petstore_client.add_pet(pet)

    # Размещение заказа
    petstore_client.place_order(order)

    # Удаление заказа
    delete_status = petstore_client.delete_order(order_id)
    assert delete_status == 200

    # Проверка удаления заказа
    get_order = petstore_client.get_order_by_id(order_id)
    assert get_order.get("code") == 404, "Заказ не был удален"

    # Удаление питомца после теста
    delete_status_pet = petstore_client.delete_pet(order["petId"])
    assert delete_status_pet == 200

@pytest.mark.api
def test_create_and_get_user(petstore_client):
    user = {
        "id": 789012,
        "username": "test_user",
        "firstName": "Test",
        "lastName": "User",
        "email": "test_user@example.com",
        "password": "securepassword",
        "phone": "123-456-7890",
        "userStatus": 1
    }
    
    # Создание пользователя
    create_response = petstore_client.create_user(user)
    assert create_response.get("code") == 200, "Пользователь не был создан"
    
    # Получение информации о пользователе
    get_user = petstore_client.get_user_by_name(user["username"])
    assert get_user.get("username") == user["username"]
    assert get_user.get("email") == user["email"]
    
    # Удаление пользователя после теста
    delete_status = petstore_client.delete_user(user["username"])
    assert delete_status == 200

@pytest.mark.api
def test_update_user(petstore_client):
    username = "update_user"
    user = {
        "id": 789013,
        "username": username,
        "firstName": "Update",
        "lastName": "User",
        "email": "update_user@example.com",
        "password": "oldpassword",
        "phone": "321-654-0987",
        "userStatus": 2
    }
    
    # Создание пользователя
    petstore_client.create_user(user)
    
    # Обновление данных пользователя
    updated_user = {
        "id": user["id"],
        "username": username,
        "firstName": "Updated",
        "lastName": "User",
        "email": "updated_user@example.com",
        "password": "newpassword",
        "phone": "987-654-3210",
        "userStatus": 3
    }
    update_response = petstore_client.update_user(username, updated_user)
    assert update_response.get("code") == 200, "Пользователь не был обновлен"
    
    # Проверка обновленных данных
    get_user = petstore_client.get_user_by_name(username)
    assert get_user.get("firstName") == "Updated"
    assert get_user.get("email") == "updated_user@example.com"
    
    # Удаление пользователя после теста
    delete_status = petstore_client.delete_user(username)
    assert delete_status == 200

@pytest.mark.api
def test_create_users_with_array_input(petstore_client):
    users = [
        {
            "id": 789014,
            "username": "batch_user1",
            "firstName": "Batch1",
            "lastName": "User1",
            "email": "batch_user1@example.com",
            "password": "password1",
            "phone": "111-222-3333",
            "userStatus": 1
        },
        {
            "id": 789015,
            "username": "batch_user2",
            "firstName": "Batch2",
            "lastName": "User2",
            "email": "batch_user2@example.com",
            "password": "password2",
            "phone": "444-555-6666",
            "userStatus": 2
        }
    ]
    
    # Создание списка пользователей
    create_response = petstore_client.create_users_with_array_input(users)
    assert create_response.get("code") == 200, "Пользователи не были созданы"
    
    # Проверка созданных пользователей
    for user in users:
        get_user = petstore_client.get_user_by_name(user["username"])
        assert get_user.get("username") == user["username"]
        assert get_user.get("email") == user["email"]
    
    # Удаление пользователей после теста
    for user in users:
        delete_status = petstore_client.delete_user(user["username"])
        assert delete_status == 200

@pytest.mark.api
def test_create_users_with_list_input(petstore_client):
    users = [
        {
            "id": 789016,
            "username": "list_user1",
            "firstName": "List1",
            "lastName": "User1",
            "email": "list_user1@example.com",
            "password": "password1",
            "phone": "777-888-9999",
            "userStatus": 1
        },
        {
            "id": 789017,
            "username": "list_user2",
            "firstName": "List2",
            "lastName": "User2",
            "email": "list_user2@example.com",
            "password": "password2",
            "phone": "000-111-2222",
            "userStatus": 2
        }
    ]
    
    # Создание списка пользователей
    create_response = petstore_client.create_users_with_list_input(users)
    assert create_response.get("code") == 200, "Пользователи не были созданы"
    
    # Проверка созданных пользователей
    for user in users:
        get_user = petstore_client.get_user_by_name(user["username"])
        assert get_user.get("username") == user["username"]
        assert get_user.get("email") == user["email"]
    
    # Удаление пользователей после теста
    for user in users:
        delete_status = petstore_client.delete_user(user["username"])
        assert delete_status == 200

@pytest.mark.api
def test_create_and_delete_user(petstore_client):
    user = {
        "id": 789018,
        "username": "delete_user",
        "firstName": "Delete",
        "lastName": "User",
        "email": "delete_user@example.com",
        "password": "deletepassword",
        "phone": "333-444-5555",
        "userStatus": 1
    }
    
    # Создание пользователя
    create_response = petstore_client.create_user(user)
    assert create_response.get("code") == 200, "Пользователь не был создан"
    
    # Удаление пользователя
    delete_status = petstore_client.delete_user(user["username"])
    assert delete_status == 200
    
    # Проверка удаления пользователя
    get_user = petstore_client.get_user_by_name(user["username"])
    assert get_user.get("code") == 404, "Пользователь не был удален" 
