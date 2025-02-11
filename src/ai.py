import openai
import requests

# OpenAI API Anahtarı
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

def generate_ai_content(topic):
    """AI kullanarak belirli bir konu hakkında içerik oluşturur"""
    prompt = f"{topic} hakkında 3-4 cümlelik ilgi çekici bir sosyal medya paylaşımı yaz."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

# Kullanım:
content = generate_ai_content("Yapay zeka ve gelecek")
print(content)


# Facebook API Bilgileri
ACCESS_TOKEN = "YOUR_FACEBOOK_PAGE_ACCESS_TOKEN"
PAGE_ID = "YOUR_FACEBOOK_PAGE_ID"

def post_to_facebook(content):
    """AI tarafından üretilen içeriği Facebook'ta paylaşır"""
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
    data = {
        "message": content,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("✅ Post başarıyla paylaşıldı:", response.json())
    else:
        print("❌ Post paylaşılırken hata oluştu:", response.json())

# Kullanım:
ai_content = generate_ai_content("Yapay zeka ve sağlık sektörü")
post_to_facebook(ai_content)

def generate_ai_image(prompt):
    """AI kullanarak bir görsel üretir"""
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response["data"][0]["url"]

def post_image_to_facebook(image_url, caption):
    """AI tarafından üretilen görselle birlikte Facebook'ta post paylaşır"""
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/photos"
    data = {
        "url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post
