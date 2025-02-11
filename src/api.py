import requests
from src.config import  PAGE_ACCESS_TOKEN, USER_ACCESS_TOKEN, POST_ID, PAGE_ID, VERSION, APP_ID, APP_SECRET
from src.utils import update_env_file


def get_group_Ids():
    """Facebook sayfasındaki group id'leri çeker"""
    url = f"https://graph.facebook.com/{VERSION}/me/accounts?access_token={USER_ACCESS_TOKEN}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Postları çekerken hata oluştu:", response.json())
        return response.json().get("data", [])
    else:
        print("Postları çekerken hata oluştu:", response.json())
        return []
    
def get_facebook_posts():
    """Facebook sayfasındaki postları çeker"""
    url = f"https://graph.facebook.com/{VERSION}/{PAGE_ID}/posts?access_token={PAGE_ACCESS_TOKEN}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Postları çekerken hata oluştu:", response.json())
        return response.json().get("data", [])
    else:
        print("Postları çekerken hata oluştu:", response.json())
        return []

def comment_on_post(post_id, message):
    """Belirtilen post'a otomatik yorum yapar"""
    url = f"https://graph.facebook.com/{VERSION}/{post_id}/comments?message={message}&access_token={PAGE_ACCESS_TOKEN}"
    # data = {
    #     "message": message,
    #     "access_token": ACCESS_TOKEN
    # }
    response = requests.post(url)
    # response = requests.post(url, data=data)

    if response.status_code == 200:
        print(f"Başarıyla yorum yapıldı: {message}")
    else:
        print("Yorum yaparken hata oluştu:", response.json())

def create_facebook_post(message):
    """Facebook sayfasına yeni bir post atar"""
    url = f"https://graph.facebook.com/{VERSION}/{PAGE_ID}/feed"
    data = {
        "message": message,
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("✅ Post başarıyla paylaşıldı:", response.json())
    else:
        print("❌ Post paylaşılırken hata oluştu:", response.json())

def create_facebook_photo_post(image_url, message):
    """Facebook sayfasına fotoğraflı bir post atar"""
    url = f"https://graph.facebook.com/{VERSION}/{PAGE_ID}/photos"
    data = {
        "url": image_url,  # Fotoğrafın internet üzerindeki URL’si
        "caption": message,
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("✅ Fotoğraflı post başarıyla paylaşıldı:", response.json())
    else:
        print("❌ Fotoğraflı post paylaşılırken hata oluştu:", response.json())

def create_facebook_video_post(video_url, description):
    """Facebook sayfasına video post atar"""
    url = f"https://graph.facebook.com/{VERSION}/{PAGE_ID}/videos"
    data = {
        "file_url": video_url,  # Videonun URL'si
        "description": description,
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("✅ Video başarıyla yüklendi:", response.json())
    else:
        print("❌ Video yüklenirken hata oluştu:", response.json())

def delete_facebook_post(post_id):
    """Facebook sayfasındaki bir postu siler"""
    url = f"https://graph.facebook.com/{VERSION}/{post_id}"
    data = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.delete(url, data=data)

    if response.status_code == 200:
        print("✅ Post başarıyla silindi!")
    else:
        print("❌ Post silinirken hata oluştu:", response.json())
    
def get_long_lived_user_token(user_access_token):
    """
    Kullanıcı token'ını uzun ömürlü token ile değiştirir.
    """
    url = f"https://graph.facebook.com/{VERSION}/oauth/access_token"
    params = {
        "grant_type": "fb_exchange_token",
        "client_id": APP_ID,
        "client_secret": APP_SECRET,
        "fb_exchange_token": user_access_token
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "access_token" in data:
        print("Yeni uzun ömürlü USER_ACCESS_TOKEN alındı!")
        new_token = data["access_token"]
        update_env_file("USER_ACCESS_TOKEN", new_token)  # .env dosyasına yaz
        return new_token
    else:
        print("USER_ACCESS_TOKEN yenileme başarısız:", data)
        return None

def get_page_access_token(page_id, long_lived_user_token):
    """
    Kullanıcı token'ı ile sayfa token'ını yeniler.
    """
    url = f"https://graph.facebook.com/{VERSION}/{page_id}"
    params = {
        "fields": "access_token",
        "access_token": long_lived_user_token
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "access_token" in data:
        print("Yeni PAGE_ACCESS_TOKEN alındı!")
        new_token = data["access_token"]
        update_env_file("PAGE_ACCESS_TOKEN", new_token)  # .env dosyasına yaz
        return new_token
    else:
        print("PAGE_ACCESS_TOKEN yenileme başarısız:", data)
        return None

def refresh_tokens():
    """
    Kullanıcı token'ını ve ardından sayfa token'ını yeniler.
    """
    global USER_ACCESS_TOKEN  # Yeni token'ı saklayalım
    global PAGE_ACCESS_TOKEN

    new_user_token = get_long_lived_user_token(USER_ACCESS_TOKEN)
    if new_user_token:
        USER_ACCESS_TOKEN = new_user_token  # Güncelle
        new_page_token = get_page_access_token(PAGE_ID, new_user_token)
        if new_page_token:
            PAGE_ACCESS_TOKEN = new_page_token  # Güncelle
            print("Tüm tokenlar başarıyla yenilendi!")
        else:
            print("PAGE_ACCESS_TOKEN yenileme başarısız.")
    else:
        print("USER_ACCESS_TOKEN yenileme başarısız.")