import os

import requests
from dotenv import load_dotenv

load_dotenv()

USER_SESSION = os.getenv("GITHUB_SESSION")

cookies = {
    "user_session": USER_SESSION
}


url = 'https://github.com/settings/profile'


response = requests.get(url, cookies=cookies)


if response.status_code == 200:
    # Вывод данных на экран
    print("Данные с защищенной страницы:")
    print(response.text)
else:
    print("Не удалось получить доступ к защищенной странице. Код ошибки:", response.status_code)