import random
from dotenv import load_dotenv

load_dotenv()

ENV_FILE_PATH = ".env"

def get_random_comment():
    """Önceden belirlenmiş yorumlardan rastgele birini seçer"""
    comments = [
        "Harika bir paylaşım! 😊",
        "Bu konuda daha fazla bilgi almak isterim!",
        "Çok güzel bir yazı olmuş, teşekkürler!",
        "Katılıyorum! 👏",
        "Bunu paylaşmak harika bir fikir!"
    ]
    return random.choice(comments)

def filter_posts(posts, keyword):
    """Belirtilen kelimeyi içeren postları filtreler"""
    return [post for post in posts if keyword.lower() in post.get("message", "").lower()]

def update_env_file(key, value):
    """
    .env dosyasındaki belirli bir anahtarı günceller.
    """
    with open(ENV_FILE_PATH, "r") as file:
        lines = file.readlines()

    with open(ENV_FILE_PATH, "w") as file:
        for line in lines:
            if line.startswith(f"{key}="):
                file.write(f"{key}={value}\n")
            else:
                file.write(line)
