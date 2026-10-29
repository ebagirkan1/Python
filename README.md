# BMI Hesaplayıcı

Bu depo, Python öğrenirken geliştirdiğim küçük projeleri içerir. İlk proje olan `bmi`, kullanıcının kilosu ve boyunu alarak Vücut Kitle İndeksi'ni (VKİ / BMI) hesaplar.

## Projeler

### BMI Hesaplayıcı (`bmi/`)

- Kilo bilgisini kilogram, boy bilgisini santimetre olarak alır.
- Boyu metreye çevirip BMI değerini `kilo / boy²` formülüyle hesaplar.
- Sonucu ve basit bir kategori bilgisini ekrana yazdırır.

## Gereksinimler

- Python 3
- Ek bir paket gerekmez.

## Çalıştırma

Depo klasöründe terminal açıp şu komutu çalıştır:

```bash
python bmi/bmi.py
```

Windows'ta `python` komutu çalışmazsa şunu deneyebilirsin:

```bash
py bmi/bmi.py
```

Program kilo (kg) ve boy (cm) değerlerini sorar. Örneğin 70 kg ve 175 cm girildiğinde BMI yaklaşık `22.86` olur.

> Bu proje Python pratiği içindir. BMI tek başına sağlık değerlendirmesi veya tanı amacıyla kullanılmaz.
