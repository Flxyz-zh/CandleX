# Kombinasi Indikator, Confluence, dan Temuan dos Santos

Daftar isi: 1 Prinsip confluence - 2 Rubrik klasifikasi - 3 Kombinasi umum (pola + indikator) - 4 Bukti dari tesis dos Santos - 5 Cara membaca bukti itu dengan benar -
6 Template penilaian - 7 Kesalahan umum

Label: **[Nison]**, **[dos Santos]** (halaman cetak tesis), **[Skill]** (kerangka buatan skill), **[Tambahan]**.

## 1. Prinsip confluence

- **Convergence [Nison hlm. 186-192, 263-267]:** kumpulan sinyal teknikal yang bertemu di/dekat harga yang sama; semakin banyak sinyal independen berkumpul di area support/resistance,
  semakin besar peluang pembalikan. Nison juga: "candle methods by themselves are valuable" tetapi lebih kuat bila mengonfirmasi sinyal Barat; banyak indikator ("the more the better").
  Satu contoh Nison (Bab 17): garis resistance naik + shooting star + bearish engulfing jam-an + RSI/indikator lain di puncak yang sama; kombinasi itu **tidak memproyeksikan besar penurunan**.
- **Dos Santos [hlm. 74-75, 87-88]:** menggabungkan indikator dari kelompok yang sama atau berbeda mengubah jumlah trade drastis; di data 2020, kombinasi memberi profit factor lebih tinggi tetapi dengan jumlah trade jauh lebih sedikit, dan hasil
  tidak bertahan di tahun lain.
- **Independensi [Skill]:** dua indikator dari kelompok yang sama (EMA + MACD = sama-sama trend-following) bukan konfirmasi independen. Bukti yang lebih independen: struktur/level, pola candlestick, momentum, volatilitas, volume, timeframe lebih tinggi.

## 2. Rubrik klasifikasi [Skill]

| Label | Kriteria | Tindakan penulisan |
|---|---|---|
| **Strong Confluence** | >= 3 kategori independen searah, termasuk struktur/level; konfirmasi tersedia; tanpa bukti lawan berarti | Tuliskan semua bukti, pembatal, dan tetap beri skenario alternatif |
| **Moderate Confluence** | 2 kategori searah; atau >= 3 searah tetapi belum terkonfirmasi / ada satu bukti lawan kecil | Tulis apa yang masih kurang |
| **Weak Confluence** | 1 kategori searah, lainnya netral | Jangan menyimpulkan arah |
| **Conflicting Signals** | Bukti lawan setara bobot (mis. bullish pattern di resistance + RSI overbought + MACD bearish cross) | Jelaskan konflik; skenario netral/menunggu |

Kategori: (a) struktur/level, (b) candlestick, (c) tren/MA, (d) momentum (MACD/RSI/Stochastic), (e) volatilitas (BB), (f) volume, (g) timeframe lebih tinggi.
Aturan tambahan: sinyal yang **melawan** timeframe lebih tinggi dibatasi maksimum **Moderate**, kecuali ada bukti pembalikan di timeframe itu. Jangan mengubah label menjadi persentase.

## 3. Kombinasi umum: cara membaca

| Kombinasi | Yang memperkuat | Yang melemahkan / pembatal |
|---|---|---|
| **Bullish Engulfing + Support** | Terbentuk di akhir penurunan di zona support; body 1 kecil, body 2 besar; volume tinggi (Nison hlm. 43-45); low pola jadi support | Close di bawah low pola; support lemah/sekali tersentuh; tren TF atas turun kuat |
| **Hammer + RSI Oversold** | Hammer di dekat support; RSI < 30 lalu naik; bullish divergence; candle konfirmasi | RSI tetap < 30 di tren turun kuat; low hammer ditembus |
| **Morning Star + MACD Bullish Crossover** | Pola lengkap, crossover MACD di sekitar pola (Nison: candle sering mendahului MACD), MACD < 0 mulai naik | Crossover jauh sebelum/sesudah pola; MACD flat; pola di tengah range |
| **EMA Bullish Crossover + MACD** | Crossover EMA cepat > lambat dan MACD/Signal > 0 searah; tren TF atas naik | Keduanya trend-following (bukan independen); whipsaw di sideways; tahun/tren menurun (dos Santos) |
| **Bollinger Bands + RSI** | Close kembali masuk dari luar lower band dan RSI keluar dari < 30 (atau mirror untuk atas); dos Santos RSI+BB menghasilkan trade lebih banyak daripada kombinasi trend+momentum | Tren kuat "menempel" band; RSI bertahan ekstrem; ekspansi volatilitas melawan |
| **Bearish Engulfing + Resistance** | Terbentuk di resistance/high sebelumnya; tren naik matang; volume besar di candle 2; high pola jadi resistance | Close di atas high pola; resistance sudah ditembus dengan volume; TF atas naik kuat |
| **Shooting Star + Bearish Momentum** | Shooting star di resistance; RSI bearish divergence; MACD histogram mengecil/bearish cross | Close berikutnya di atas high shooting star; momentum masih menguat |
| **Doji + Support/Resistance Penting** | Doji setelah candle panjang searah tren, di titik S/R penting, pasar overbought/oversold; konfirmasi candle berikutnya | Doji di tengah range; banyak doji (kurang bermakna); close berikutnya menembus level |

## 4. Bukti dari tesis dos Santos

Rancangan [Bab 4, hlm. 35-57]: data Oanda, EUR/USD dan GBP/USD, 30 menit, harga Close (ask), 2020 untuk analisis rinci lalu 2016-2020; posisi long dan short; tanpa leverage;
modal awal $10.000 dan $100.000 (order quantity = modal awal; biaya transaksi tetap -$6 per transaksi dalam kode, hlm. 41); eksekusi market order di candle berikutnya setelah sinyal; Quantstrat (R).

### 4.1 Profit factor 2020 (tabel 5.12, hlm. 73)

| Strategi | EUR/USD $10k | GBP/USD $10k | EUR/USD $100k | GBP/USD $100k |
|---|---|---|---|---|
| EMA 12-26 | 0,67 | 0,87 | 0,94 | 1,08 |
| EMA 12-50 | 0,87 | 1,10 | 1,15 | 1,34 |
| EMA 50-200 | 1,41 | 0,90 | 1,71 | 1,00 |
| MACD | 0,80 | 0,88 | 1,06 | 1,06 |
| RSI 70-30 | 0,80 | 0,85 | 1,06 | 1,04 |
| RSI 80-20 | 1,28 | 0,84 | 1,47 | 0,94 |
| BB | 0,62 | 0,83 | 1,00 | 1,11 |
| EMA 12-26 & MACD | - | 0,99 | - | 1,01 |
| EMA 12-50 & MACD | 1,70 | 2,44 | 1,78 | 2,56 |
| RSI 70-30 & BB | 1,39 | 1,17 | 1,53 | 1,27 |
| RSI 80-20 & BB | 1,63 | 1,22 | 1,74 | 1,29 |

Jumlah trade 2020 (hlm. 63-72): EMA 12-26 = 343 (EUR) / 337 (GBP); EMA 12-50 = 231 / 234; EMA 50-200 = 64 / 71; MACD = 240 / 246; RSI 30-70 = 436 / 464; RSI 20-80 = 153 / 169;
BB = 609 / 611; EMA 12-26 & MACD = 0 / 13; EMA 12-50 & MACD = 22 / 21; RSI 30-70 & BB = 92 / 102; RSI 20-80 & BB = 28 / 29. Persentase menang: strategi mean-reversion (RSI, BB) 65-74%
tetapi profit factor tipis; strategi trend-following (EMA, MACD) menang 28-38% tetapi payoff ratio lebih besar.

### 4.2 Hasil 2016-2020 (tabel 6.1-6.3, hlm. 79-84)

- Kombinasi EMA 12-50 & MACD (terbaik di 2020), profit factor per tahun, EUR/USD | GBP/USD: 2020: 1,70 | 2,44; 2019: 0,43 | 1,15; 2018: 0,90 | 0,73; 2017: 2,63 | 2,48; 2016: 0,71 | 0,30.
- Tidak bertahan: strategi yang bagus di 2020 buruk di tahun lain; granularitas 15 menit tidak mengubah kesimpulan (hlm. 79).
- Tahun baik (2017, 2020) = pasar cenderung **uptrend**; tahun buruk (2016, 2018, juga 2019 dalam kesimpulan) = **downtrend**; penulis menghubungkan kinerja dengan arah tren pasar (hlm. 82-84, 88).
- Kombinasi yang tidak pernah menghasilkan trade selama 5 tahun: EMA (semua parameter) + RSI, EMA + BB, MACD + RSI, MACD + BB (hlm. 80). Hanya EMA+MACD dan RSI+BB yang memicu trade.
- Variasi sinyal berlawanan (satu indikator beli, satu jual) menghasilkan trade pada semua kombinasi, tetapi hasilnya tetap tidak konsisten antar tahun (hlm. 82, 87).

### 4.3 Kesimpulan penulis (hlm. 87-88)

1. Mengombinasikan indikator lebih menguntungkan daripada indikator tunggal **pada data yang diuji**, dengan trade jauh lebih sedikit.
2. Efektivitas terkait tren pasar tahunan; pasar turun menurunkan efisiensi.
3. Modal awal lebih besar memberi hasil lebih baik (penulis menduga karena drawdown besar dapat dipulihkan).
4. Penulis menyimpulkan bahwa mengandalkan analisis teknikal/indikator saja tidak andal; faktor ekonomi dan berita perlu dipertimbangkan.
5. **Keterbatasan (hlm. 88):** hanya 4 indikator; sampel kecil; disarankan data 20 tahun, timeframe berbeda, dan gabungan dengan indikator fundamental.

## 5. Cara membaca bukti itu dengan benar [Skill]

1. **Satu sampel, dua pasangan mata uang, satu timeframe.** Jangan generalisasi ke instrumen/pasar/periode lain.
2. **Jumlah trade kecil.** EMA 12-50 & MACD hanya 21-22 trade pada 2020; profit factor 2,44 dari 21 trade tidak signifikan secara statistik tanpa interval kepercayaan. Nilai berbintang di tabel 6.2 (EMA 12-26 & MACD 2017: 5,42 dan 13,08 dari 4 trade) diabaikan oleh penulis sendiri.
3. **Tidak ada uji out-of-sample formal** selain pengulangan per tahun; hasil per tahun berubah drastis (tanda ketidakstabilan atau ketergantungan rezim).
4. **Rata-rata profit factor antar tahun tidak sahih secara statistik** (rasio). Contoh sintetis dari tabel 6.1: rata-rata sederhana EUR/USD = 1,27; GBP/USD = 1,42; hanya 2 dan 3 dari 5 tahun yang di atas 1. Hitung ulang dengan menjumlahkan gross profit dan gross loss seluruh tahun.
5. **Biaya:** kode memakai biaya tetap per transaksi (-$6) tanpa spread/slippage terpisah yang jelas; strategi dengan ratusan trade lebih terdampak biaya. Penjelasan "modal besar lebih baik" mungkin juga dipengaruhi biaya tetap yang relatif lebih kecil [Skill: hipotesis, tidak diverifikasi di buku].
6. **Tidak ada klaim kausal.** Hubungan hasil-tren pasar adalah observasi deskriptif.
7. **Ketidakselarasan internal yang dicatat:** teks menyebut "27 strategi kombinasi" yang dijalankan dengan hanya empat memicu trade (hlm. 70) tetapi kesimpulan menyebut "12 kombinasi" (hlm. 87);
   tabel 5.8 EMA 12-26 & MACD GBP/USD $10k menunjukkan profit factor 0,99 dengan total gain positif ($851,70). Selisih kecil gross profit/loss vs total gain mungkin karena posisi terbuka/biaya. Perlakukan angka sebagai ilustrasi, bukan bukti presisi.

## 6. Template penilaian confluence

```
Bukti pendukung: [kategori] - [bukti terukur dengan angka] ...
Bukti lawan: [kategori] - [bukti] ...
Konfirmasi yang belum ada: ...
Faktor pembatal: (level/kejadian spesifik)
Label: Strong / Moderate / Weak / Conflicting  (alasan 1-2 kalimat)
Keterbatasan data: ...
```

## 7. Kesalahan umum

1. Menumpuk indikator sejenis lalu menyebut "banyak konfirmasi".
2. Mengabaikan bukti lawan karena sudah punya bias.
3. Menyebut "Strong" saat konfirmasi (close candle berikutnya) belum ada.
4. Menggunakan hasil backtest 2020 sebagai bukti strategi umum (dos Santos sendiri menunjukkan hasil tidak bertahan).
5. Mengubah label confluence menjadi angka peluang.
