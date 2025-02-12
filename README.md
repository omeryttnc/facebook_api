to create app
https://developers.facebook.com/apps/?show_reminder=true

Graph API explorer
https://developers.facebook.com/tools/explorer/

# KURULUM

## dependency leri yuklemek icin

pip install -r requirements.txt

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
  https://github.com/omeryttnc/facebook_api

abi inceleyebilir misiniz tum yetkimiz facebook ozel sayfasinda o sayfa icerisinde

get_group_Ids -> sayfalarimizin id lerini alabiliyoruz
get_facebook_posts -> sayfamizin id sini verdigimiz sayfanin postlarini okuyabiliyoruz
comment_on_post-> sectigimiz posta yorum yapabiliyoruz
create_facebook_post-> yeni bir post olusturabiliyoruz
create_facebook_photo_post -> resimli post olusturabiliyoruz
create_facebook_video_post-> videolu post olusturabiliyoruz
delete_facebook_post-> postu silebiliyoruz
refresh_tokens -> bu islemleri yapiyorken bize iki tane token gerekli userToken ve pageToken bu ikisininde omru 2 saat normalde bunu uzun omurlu olusrutup .env dosyasina kaydediyoruz bu method cronjob olusutup icine eklemek gerekiyor yada task schedular dan da olusturulabilir hangi OS kullandigimiza bagli soyle bir sikinti var ama .env dosyasindaki degisikligi gormek icin projenin tekrar baslatilmasi lazim o yuzden bilgisayari aciliyorken en basta ilk bu code calisacak sekilde ayarlayip token lari update ederek 24 saatlik tokenlarimizi guncelleyebiliriz digger bir sorun eger token expired oldu ise expired token ile yeni token olusturamayacagimiz icin manuel olarak tekrar olsuturmamiz gerekiyor

## dikkat

- uygulamayi olusturuyorken https://developers.facebook.com/apps/?show_reminder=true
- USE CASE kisminda OTHER secip sonra BUSSINESS secmemiz gerekiyor ki istedigimiz permissionlari ekleyebilelim
- EN ONEMLISI de
  read_insights
  pages_show_list
  read_page_mailboxes
  business_management
  pages_read_engagement
  pages_read_user_content
  pages_manage_posts
  pages_manage_engagement

izinlerini ilk token olusturuyorken permission kismindan eklememiz gerekiyor

## methodlar

- get_group_Ids -> sayfalarimizin id lerini alabiliyoruz
- get_facebook_posts -> sayfamizin id sini verdigimiz sayfanin postlarini okuyabiliyoruz
- comment_on_post-> sectigimiz posta yorum yapabiliyoruz
- create_facebook_post-> yeni bir post olusturabiliyoruz
- create_facebook_photo_post -> resimli post olusturabiliyoruz
- create_facebook_video_post-> videolu post olusturabiliyoruz
- delete_facebook_post-> postu silebiliyoruz
- refresh_tokens -> bu islemleri yapiyorken bize iki tane token gerekli userToken ve pageToken bu ikisininde omru 2 saat normalde bunu uzun omurlu olusrutup .env dosyasina kaydediyoruz bu method cronjob olusutup icine eklemek gerekiyor yada task schedular dan da olusturulabilir hangi OS kullandigimiza bagli soyle bir sikinti var ama .env dosyasindaki degisikligi gormek icin projenin tekrar baslatilmasi lazim o yuzden bilgisayari aciliyorken en basta ilk bu code calisacak sekilde ayarlayip token lari update ederek 24 saatlik tokenlarimizi guncelleyebiliriz digger bir sorun eger token expired oldu ise expired token ile yeni token olusturamayacagimiz icin manuel olarak tekrar olsuturmamiz gerekiyor
- generate_ai_content -> yapay zeka kullanarak yorum olusturma
- generate_ai_image -> yapay zeka kullanarak resim olusturma

## doldurulmasi gereken .env objeleri

PAGE_ACCESS_TOKEN=**********\*\***********\*\*\***********\*\***********
USER_ACCESS_TOKEN=**********\*\***********\*\*\***********\*\***********
POST_ID=**********\*\***********\*\*\***********\*\***********
PAGE_ID=**********\*\***********\*\*\***********\*\***********
APP_ID=**********\*\***********\*\*\***********\*\***********
APP_SECRET=**********\*\***********\*\*\***********\*\***********
OPENAI_API_KEY=sk-proj---**********\*\***********\*\*\***********\*\***********
VERSION=v22.0
