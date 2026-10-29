# Python Öğrenme Projelerim

Bu depo, Python öğrenirken geliştirdiğim küçük projeleri bir arada tutar. Her proje kendi klasöründe bulunur ve zamanla yenileri eklenir.

## Projeler

### BMI Hesaplayıcı — `bmi/`

Kullanıcıdan kilo (kilogram) ve boy (santimetre) alır, boyu metreye çevirir ve Vücut Kitle İndeksi'ni (VKİ / BMI) şu formülle hesaplar:

```text
BMI = kilo (kg) / boy (m)²
```

Program sonucu ekrana yazdırır ve basit bir kategori gösterir.

## Gereksinimler

- Python 3
- Ek paket gerekmez.

## Çalıştırma

Depo klasöründe terminal açıp şu komutu çalıştır:

```bash
python bmi/bmi.py
```

Windows'ta `python` komutu çalışmazsa:

```bash
py bmi/bmi.py
```

Program kilo değerini kilogram, boy değerini santimetre olarak ister. Örneğin `70` kg ve `175` cm girildiğinde BMI yaklaşık `22.86` olur.

## Klasör yapısı

```text
Python/
├── README.md
└── bmi/
    └── bmi.py
```

Bu proje Python pratiği içindir; BMI tek başına sağlık değerlendirmesi veya tanı amacıyla kullanılmaz.
