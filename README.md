to create app
https://developers.facebook.com/apps/?show_reminder=true

Graph API explorer
https://developers.facebook.com/tools/explorer/

# Facebook API Kullanımı için README

## Gerekli Değişkenler ve Açıklamaları

Facebook API'yi kullanabilmek için aşağıdaki değişkenlerin doğru şekilde tanımlanması gerekmektedir:

### 1. **PAGE_ACCESS_TOKEN**

- Facebook sayfanız için oluşturduğunuz erişim token'ıdır.
- Bu token, sayfa üzerinde paylaşım yapmak, mesaj göndermek gibi işlemleri gerçekleştirmek için kullanılır.
- **Nasıl alınır?**
  1.  Facebook Developer portalına giriş yapın: [Facebook Developers](https://developers.facebook.com/)
  2.  Uygulamanızı seçin veya yeni bir uygulama oluşturun.
  3.  **Sayfalar için erişim token'ı oluşturma** adımlarını takip edin.
  4.  Gerekli izinleri vererek token'ı alın.

### 2. **USER_ACCESS_TOKEN**

- Kullanıcıya özel erişim token'ıdır.
- Genellikle kullanıcı bilgilerini almak veya belirli işlemleri gerçekleştirmek için kullanılır.
- **Nasıl alınır?**
  - Facebook Graph API Explorer'ı kullanarak veya OAuth yetkilendirmesi ile alınabilir.

### 3. **POST_ID**

- Facebook üzerinde bir gönderi (post) paylaşımı yaptıktan sonra o gönderinin benzersiz ID'sidir.
- Belirli bir paylaşımı güncellemek veya silmek için kullanılır.
- **Nasıl alınır?**
  - Graph API üzerinden `/me/feed` veya `/page_id/feed` endpoint'leri ile paylaşım yapıldığında dönen yanıt içinde bulunur.

### 4. **PAGE_ID**

- İşlem yapılacak olan Facebook sayfasının kimliğidir.
- **Nasıl alınır?**
  - Facebook Graph API Explorer'ı kullanarak `/me/accounts` isteği ile sayfa ID'si alınabilir.

### 5. **APP_ID ve APP_SECRET**

- Facebook uygulamanıza ait kimlik bilgileri.
- **Nasıl alınır?**
  1.  Facebook Developer paneline giriş yapın.
  2.  Uygulamanızı seçin veya yeni bir uygulama oluşturun.
  3.  "Ayarlar" bölümünde APP ID ve APP SECRET bilgilerine ulaşabilirsiniz.
  4.  **APP SECRET** gizli tutulmalıdır ve üçüncü kişilerle paylaşılmamalıdır.

### 6. **VERSION**

- Kullanılacak Facebook Graph API versiyonunu belirtir.
- **En güncel versiyon için:** [Facebook Graph API Versions](https://developers.facebook.com/docs/graph-api/changelog)
- Örneğin, `v22.0` şu an kullanılan versiyon olabilir.

## Örnek Kullanım

Facebook API'yi kullanarak bir paylaşım yapmak için aşağıdaki örneği kullanabilirsiniz:

```bash
curl -X POST "https://graph.facebook.com/{PAGE_ID}/feed" \
     -d "message=Merhaba, bu bir test paylaşımıdır!" \
     -d "access_token={PAGE_ACCESS_TOKEN}"
```

## Önemli Notlar

- API anahtarlarını ve token'ları kimseyle paylaşmayın.
- **APP_SECRET** bilgisini bir çevre değişkeni olarak saklayarak güvenli bir şekilde kullanın.
- Token'ların süresi dolabilir, bu yüzden belirli aralıklarla yenilenmesi gerekebilir.
- Graph API kullanımı hakkında daha fazla bilgi için [Facebook API Belgeleri](https://developers.facebook.com/docs/) adresini ziyaret edebilirsiniz.
