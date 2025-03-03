import requests
import base64
import os

# 🔑 Используем GitHub Secret для аутентификации
GITHUB_TOKEN = os.getenv("GH_TOKEN")  
GITHUB_USERNAME = "mediasevenlab"
REPO_NAME = "newrep-1"
BASE_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents"

def upload_file(filename, content, commit_message="Auto-update"):
    """Создаёт или обновляет файл в репозитории"""
    file_url = f"{BASE_URL}/{filename}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(file_url, headers=headers)
    sha = response.json().get("sha", None)

    data = {
        "message": commit_message,
        "content": base64.b64encode(content.encode()).decode(),
        "sha": sha if sha else None
    }

    response = requests.put(file_url, headers=headers, json=data)

    if response.status_code in [200, 201]:
        print(f"✅ Файл '{filename}' обновлён!")
    else:
        print(f"❌ Ошибка: {response.json()}")

# 🚀 Создаём тестовый файл
upload_file("test_file.txt", "Этот файл создан автоматически!", "Добавлен test_file.txt")
