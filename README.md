# 📱 Google Play Reviews Scraper (Shopee App)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Google Play](https://img.shields.io/badge/Source-Google%20Play-green?style=for-the-badge&logo=googleplay)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

Script Python sederhana untuk mengambil ulasan aplikasi dari Google Play Store menggunakan library `google-play-scraper`.

Contoh pada project ini mengambil ulasan aplikasi **Shopee Indonesia** (`com.shopee.id`) dan menyimpannya ke dalam file CSV.

---

## ✨ Fitur

✅ Mengambil ulasan terbaru dari Google Play  
✅ Bisa menentukan jumlah ulasan yang diambil  
✅ Bisa filter berdasarkan rating (1–5)  
✅ Data otomatis disimpan dalam format CSV  
✅ Struktur kolom sudah dirapikan  

---

## 📦 Library yang Digunakan

- `google-play-scraper`
- `pandas`

---

## 🚀 Cara Install

Install dependency terlebih dahulu:

```bash
pip install -r requirements.txt
```
---

## 🛠️ Konfigurasi Script

Bagian konfigurasi utama:

```python
app_id = 'com.shopee.id'
lang = 'id'
country = 'id'
```

### 📌 Penjelasan Parameter

| Parameter | Keterangan |
|-----------|------------|
| app_id | ID aplikasi di Google Play |
| lang | Bahasa ulasan |
| country | Negara toko Google Play |
| count | Jumlah ulasan yang ingin diambil |
| sort | Urutan ulasan (NEWEST / MOST_RELEVANT) |
| filter_score_with | Filter rating (1–5 atau None untuk semua) |

---

## 📊 Struktur Data Output

File output: `ulasan_shopee.csv`

Kolom yang disimpan:

| Nama Pengguna | Rating | Waktu | Komentar |
|---------------|--------|--------|-----------|
| user123 | 5 | 2025-02-01 | Aplikasinya sangat membantu |
| user456 | 1 | 2025-02-02 | Error terus tidak bisa login |

---

## 🔄 Cara Mengganti Aplikasi Target

Untuk mengambil ulasan aplikasi lain:

1. Buka Google Play di browser
2. Cari aplikasi yang diinginkan
3. Lihat URL

Contoh:

```
https://play.google.com/store/apps/details?id=com.shopee.id
```

Bagian setelah `id=` adalah `app_id`.

---

## ⚙️ Cara Kerja Script

1. Mengambil ulasan menggunakan fungsi `reviews()`  
2. Mengurutkan berdasarkan ulasan terbaru  
3. Menyimpan hasil ke dalam DataFrame  
4. Memilih kolom penting  
5. Mengubah nama kolom agar lebih rapi  
6. Mengekspor ke file CSV  

---

## 📌 Contoh Filter Rating

Jika hanya ingin mengambil rating buruk (bintang 1):

```python
filter_score_with=1
```

Jika ingin semua rating (1–5):

```python
filter_score_with=None
```

---

## ⚠️ Catatan

- Google Play memiliki pembatasan data tertentu.
- Tidak semua ulasan lama bisa diambil sekaligus.
- Jika ingin mengambil lebih banyak data, bisa menggunakan sistem pagination dengan `continuation_token`.

---

## 📈 Output

Setelah script dijalankan:

```bash
python main.py
```

Akan muncul pesan:

```
Berhasil mengambil 1000 ulasan dan disimpan ke 'ulasan_shopee.csv'
```

---

## 🎯 Tujuan Project

Project ini cocok untuk:

- Analisis sentimen
- Data mining
- Riset pengalaman pengguna
- Machine learning dataset
- Studi performa aplikasi

---

## ❤️ Dibuat dengan Python

<p align="center">
  Dibuat dengan ❤️ menggunakan Python
</p>
