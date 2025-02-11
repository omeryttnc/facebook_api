import os
import openai
from dotenv import load_dotenv
load_dotenv()
from .utils import log
import time

def generate_ai_content(topic):
    api_key = os.getenv("OPENAI_API_KEY")

    openai.api_key = api_key 
    """AI kullanarak belirli bir konu hakkında içerik oluşturur"""
    prompt = f"{topic} hakkında 3-4 cümlelik ilgi çekici ingilizce bir sosyal medya paylaşımı yazabilir misin ve konuyla alakali 5 ile 10 tane hastag ekle."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Modeli seçiyoruz
            messages=[{"role": "user", "content": prompt}],  # 'messages' parametresi ile sohbet geçmişi sağlıyoruz
            max_tokens=100,  # Token sayısını sınırlıyoruz
            temperature=0.7,  # Yanıt çeşitliliği için sıcaklık parametresi
            timeout=30
        )

    except openai.OpenAIError as e:
        return f"⚠️ OpenAI API hatası: {e}"
    except Exception as e:
        return f"⚠️ Genel hata: {e}"
    return response["choices"][0]["message"]["content"]


def generate_ai_image(prompt):
    """AI kullanarak bir görsel üretir"""
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response["data"][0]["url"]


