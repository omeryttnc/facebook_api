import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()

PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
USER_ACCESS_TOKEN = os.getenv("USER_ACCESS_TOKEN")
POST_ID = os.getenv("POST_ID")
PAGE_ID = os.getenv("PAGE_ID")
VERSION= os.getenv("VERSION")
APP_ID= os.getenv("APP_ID")
APP_SECRET= os.getenv("APP_SECRET")

if not PAGE_ACCESS_TOKEN or not USER_ACCESS_TOKEN:
    raise ValueError("Lütfen .env dosyasına ACCESS_TOKEN ve PAGE_ID ekleyin!")
