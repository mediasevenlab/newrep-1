import requests
import base64

# 🛠 Конфигурация
GITHUB_USERNAME = "your_username"
REPO_NAME = "your_repo"
GITHUB_TOKEN = "your_token_here"

BASE_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents"

def upload_file(filename, content, commit_message="Auto-update via script"):
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
        print(f"✅ Файл '{filename}' обновлён в репозитории!")
    else:
        print(f"❌ Ошибка: {response.json()}")

# 🚀 Пример вызова:
# upload_file("README.md", "# Привет, GitHub!\n\nЭто автоматическая загрузка.", "Добавлен README.md")
