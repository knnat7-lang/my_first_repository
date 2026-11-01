
import os
from dotenv import load_dotenv

# 1. Загружаем настройки из файла .env
load_dotenv()

# 2. Получаем обычную настройку
app_name = os.getenv("APP_NAME")

# 3. Получаем секретный ключ
api_key = os.getenv("API_KEY")

# 4. Проверяем обязательные переменные
if not app_name:
    print("Error: APP_NAME is missing!")
    exit()

if not api_key:
    print("Error: API_KEY is missing!")
    exit()

# 5. Выводим результат
print(f"Application name: {app_name}")
print(f"API_KEY loaded: {bool(api_key)}")
