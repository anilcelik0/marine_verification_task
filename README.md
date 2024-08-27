
## Açıklama

Bu proje Django ile yapılmıştır. İçinde bulabileceğiniz Basic özellikler şunlardır;

- Rest  Framework
- Django Signals
- Django channels  ile websocket
- Redis
- Celery
- Docker

## Bilgilendirme
-  Token doğrulaması ile kayıt için "authenticate" uygulamasına bakabilirsiniz.
Kayıt sırasında UI üzerinden bir dakika geçerli bir token ile form gönderilir.

- Otp Uygulaması için  "api" uygulamasına bakabilirsiniz.
Kullanıcı kayıt olduktan sonra signals yardımı ile bir celery task oluşur ve her dakika sonunda şifre güncellenir. Ayrıca OTP şifrelri websocket üzerinden paylaşılabilir.

###Kurlum

`$ docker-compose up -b

