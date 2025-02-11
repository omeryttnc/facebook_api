import random
from dotenv import load_dotenv
import os

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

def log(message):
    """Log mesajı oluşturur"""
    log_dir = os.path.join(os.getcwd(), "logs")  # Proje dizininde 'logs' klasörü
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)  # Eğer 'logs' klasörü yoksa oluştur
    
    log_file_path = os.path.join(log_dir, "log.txt")  # Log dosyasının tam yolu

    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"\n{message}")