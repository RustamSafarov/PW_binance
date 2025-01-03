# PW_binance

Pet project для обучения автоматизированным тестам API.

## Описание проекта

**PW_binance** — это фреймворк для автоматизированного тестирования [Swagger Petstore API](https://petstore.swagger.io/). Проект использует **Pytest** для написания и выполнения тестов, а также **Allure** для генерации наглядных отчетов о результатах тестирования. Основной целью проекта является обеспечение надежности и функциональности API посредством регулярного тестирования основных и дополнительных методов.

## Быстрый старт

Следуйте приведенным ниже шагам для развертывания и запуска тестов на вашем локальном компьютере.

### 1. Клонирование репозитория

Сначала необходимо клонировать репозиторий проекта с помощью `git`:

```bash
git clone https://github.com/ваш-пользователь/pw_binance.git
cd pw_binance
```

### 2. Создание и активация виртуального окружения

Рекомендуется использовать **virtualenv** или **venv** для изоляции зависимостей проекта.

**На Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**На macOS и Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

Убедитесь, что вы находитесь в активированном виртуальном окружении, затем установите необходимые пакеты:

```bash
pip install -r pw_pets/requirements.txt
```

### 4. Настройка переменных окружения

Проект использует файл `.env` для хранения конфиденциальных данных и настроек. Создайте файл `.env` в корневой директории проекта и добавьте следующие переменные:

**Важно:** Убедитесь, что файл `.env` включен в `.gitignore`, чтобы предотвратить его случайное добавление в систему контроля версий.

### 5. Запуск тестов

Используйте **Pytest** для выполнения тестов. Для параллельного запуска тестов с использованием `pytest-xdist` выполните следующую команду:

```bash
cd pw_pets
pytest -n auto --alluredir=allure-results
```

**Пояснение:**
- `-n auto`: позволяет Pytest автоматически определить оптимальное количество параллельных процессов.
- `--alluredir=allure-results`: указывает директорию для сохранения результатов тестирования в формате Allure.

### 6. Генерация и просмотр отчета Allure

После выполнения тестов сгенерируйте и просмотрите отчет Allure с помощью следующих команд:

```bash
allure serve allure-results
```

**Пояснение:**
- Команда `allure serve` создаст отчет из результатов в директории `allure-results` и автоматически откроет его в вашем браузере.

**Альтернативный способ:**

Если вы хотите сначала сгенерировать отчет, а затем открыть его, используйте:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

### 7. Дополнительные команды

- **Запуск всех тестов без генерации отчета:**

  ```bash
  pytest -n auto
  ```

- **Запуск определённых маркеров тестов:**

  ```bash
  pytest -m smoke -n auto --alluredir=allure-results
  ```

  ```bash
  pytest -m api -n auto --alluredir=allure-results
  ```

## Структура проекта

- `pw_pets/`: основная директория проекта.
  - `modules/API/meths.py`: файл с методами для работы с API.
  - `modules/API/test_petstore.py`: файл с тестами для API.
  - `modules/API/conftest.py`: файл с фикстурами для тестов.
  - `requirements.txt`: файл с зависимостями проекта.
  - `pytest.ini`: файл с настройками для pytest.
- `.github/workflows/main.yml`: конфигурация GitHub Actions для CI/CD.

## Используемые технологии и инструменты

- **Python 3.8+**
- **Pytest:** фреймворк для написания и выполнения тестов.
- **pytest-xdist:** плагин для параллельного запуска тестов.
- **Allure:** инструмент для генерации привлекательных отчетов о тестировании.
- **Playwright:** библиотека для автоматизации браузера (используется при необходимости).
- **dotenv:** для управления переменными окружения.
- **Requests:** библиотека для выполнения HTTP-запросов.

## Контрибьюция

Приветствуется участие в проекте! Пожалуйста, создавайте **pull requests** для предложений по улучшению или исправлению ошибок.

## Лицензия

Этот проект лицензирован под лицензией MIT. См. файл [LICENSE](LICENSE) для подробностей.

## Контактная информация

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами по электронной почте [apiteam@swagger.io](mailto:apiteam@swagger.io).