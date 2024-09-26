
## Требования

Для успешного запуска проекта вам понадобятся:

- [Python](https://www.python.org/downloads/) (версия 3.12 или выше)
- [Poetry](https://python-poetry.org/docs/#installation) для управления зависимостями
- [Docker](https://www.docker.com/get-started) для контейнеризации приложения

## Установка

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/tutuevm/weather_data_collector.git
    cd ваш_репозиторий
    ```

2. **Установите зависимости с помощью Poetry:**
    ```bash
    poetry install --no-root
    ```

3. **Запустите Docker для создания базы данных в отдельном терминале:**
    ```bash
    docker compose up --build
    ```

4. **Проведите миграцию базы данных с помощью Alembic:**
    ```bash
    poetry run alembic upgrade head
    ```

5. **Запустите приложение:**
    ```bash
    poetry run python -m src.main
    ```

## Использование

После запуска команды:

```bash
poetry run python -m src.main
```
запустится бесконечный цикл. При введении команды **export** в консоль, произойдет выгрузка последних 10 записей из базы данных в файл data/output.xlsx..
При необходимости изменения промежутка времени для сбора данных через API, необходимо заменить переменную **WEATHER_REQUEST_DELAY_SEC** в env файле
