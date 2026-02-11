from google_play_scraper import Sort, reviews
import pandas as pd

# 1. Konfigurasi Scraping
app_id = 'com.shopee.id' # ID aplikasi di Play Store
lang = 'id'              # Bahasa ulasan (Indonesia)
country = 'id'           # Lokasi toko (Indonesia)

# 2. Proses Scraping
# 'count' adalah jumlah ulasan yang ingin diambil (misal: 1000)
result, continuation_token = reviews(
    app_id,
    lang=lang,
    country=country,
    sort=Sort.NEWEST, # Urutkan berdasarkan yang paling Baru
    count=1000,              # Jumlah ulasan yang diambil
    filter_score_with=None   # Ambil semua rating (1-5). Ganti ke 1 jika hanya ingin rating buruk.
)

# 3. Simpan ke DataFrame (Tabel)
df = pd.DataFrame(result)

# 4. Pilih kolom yang penting saja
df = df[['userName', 'score', 'at', 'content']]
df.rename(columns={
    'userName': 'Nama Pengguna',
    'score': 'Rating',
    'at': 'Waktu',
    'content': 'Komentar'
}, inplace=True)

# 5. Ekspor ke file CSV
df.to_csv('ulasan_shopee.csv', index=False, encoding='utf-8')

print(f"Berhasil mengambil {len(df)} ulasan dan disimpan ke 'ulasan_shopee.csv'")