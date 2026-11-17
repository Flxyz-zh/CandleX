# Indikator Teknikal: Rumus, Cara Baca, Keterbatasan

Daftar isi: 0 Klasifikasi dan parameter - 1 Moving Average (SMA, WMA, EMA) - 2 MACD - 3 RSI - 4 Bollinger Bands -
5 Stochastic - 6 Volume - 7 Aturan sinyal yang diuji dos Santos - 8 Catatan konsistensi rumus - 9 Kesalahan umum

Label: **[dos Santos]** (tesis 2021, halaman cetak), **[Nison]** (halaman cetak), **[Tambahan]** (di luar buku), **[Skill]**.
Semua contoh angka adalah **sintetis** dan sudah dihitung ulang.

## 0. Klasifikasi dan parameter

[dos Santos hlm. 17, 21]: indikator adalah alat matematis atas deret harga untuk menghasilkan deret baru. Tiga kelompok:

| Kelompok | Fungsi | Contoh | Sifat |
|---|---|---|---|
| Trend | Arah tren | SMA, EMA, ADX, MACD (juga trend/momentum) | Cenderung *lagging* |
| Momentum | Kekuatan/kecepatan perubahan harga | RSI, Stochastic | Sering disebut *leading*; berosilasi |
| Volatility | Besaran fluktuasi | Bollinger Bands, ATR | Menunjukkan ekspansi/kontraksi |

**Parameter referensi** yang diuji dos Santos (hlm. 23-30): EMA 12, 26, 50, 200 (crossover 12-26, 12-50, 50-200); MACD 12-26-9; RSI periode 14,
level 30/70 dan 20/80; Bollinger Bands periode 20, deviasi standar 2. Data penelitian: EUR/USD dan GBP/USD, candle 30 menit, harga Close.

Prinsip penggunaan: indikator **bukan strategi** [dos Santos hlm. 42]; indikator tidak tahu posisi atau struktur harga. Gunakan bersama price
action; Nison menyebut osilator sebagai "awan hujan": peringatan, dengan konfirmasi akhir dari pola candlestick (hlm. 225-226).

## 1. Moving Average

### 1.1 SMA (Simple Moving Average)
- **Rumus:** SMA_n(m) = (P_{n-m+1} + ... + P_n) / m, P = harga (biasanya Close) [dos Santos pers. 3.1; Nison hlm. 217].
- **Contoh Nison-style (sintetis):** close 38, 41, 36, 41, 38 -> SMA-5 = 194/5 = 38,80.
- **Sifat:** bobot sama untuk semua harga; makin panjang periode, makin halus dan makin lambat; periode pendek mengikuti harga erat tetapi lebih
  banyak whipsaw [Nison hlm. 217-218]. Periode populer: 5, 9, 30, 50, 200 (200 paling banyak diawasi).

### 1.2 WMA (Weighted Moving Average)
- Bobot berbeda tiap harga; umumnya **front-loaded**: harga terbaru berbobot lebih besar [Nison hlm. 219].
- **Rumus umum [Tambahan]:** WMA_m = sum(w_i x P_i) / sum(w_i), dengan w_i = m untuk harga terbaru, m-1, ..., 1.

### 1.3 EMA (Exponential Moving Average)
- **Rumus [dos Santos pers. 3.2-3.4, hlm. 23]:**
  `alpha = 2 / (n + 1)`;  `EMA_t = alpha x P_t + (1 - alpha) x EMA_{t-1}` = `(P_t - EMA_{t-1}) x alpha + EMA_{t-1}`.
  Langkah: (1) hitung SMA n pertama sebagai seed; (2) hitung alpha; (3) iterasi.
- **Tabel alpha (dos Santos tabel 3.1):** n=10: 0,18182; n=20: 0,09524 (buku mencatat 0,09624 untuk n=20, lihat catatan konsistensi 8.4); n=50: 0,03922.
  Dihitung ulang: n=12: 0,1538; n=26: 0,0741; n=50: 0,03922; n=200: 0,00995.
- **Contoh hitung (sintetis, EMA-3):** close 20, 22, 21, 23, 25. Seed = SMA(20,22,21) = 21,0; alpha = 0,5.
  EMA_4 = 0,5x23 + 0,5x21 = 22,0; EMA_5 = 0,5x25 + 0,5x22 = 23,5.
- **Sifat [dos Santos hlm. 22-23; Nison hlm. 219]:** bobot lebih besar pada data terkini, semua data lama tetap ikut dengan bobot menurun eksponensial;
  lebih responsif daripada SMA; MA cepat bagus saat tren berbalik, MA lambat bagus saat tren berlanjut.

### 1.4 Cara membaca MA
1. **Harga vs MA:** close di atas MA = bias naik, di bawah = bias turun [dos Santos hlm. 24; Nison hlm. 219-220].
2. **Crossover dua MA:** fast memotong slow dari bawah ke atas = bullish ("golden cross" dalam istilah Jepang); dari atas ke bawah = bearish ("dead cross")
   [Nison hlm. 220; dos Santos hlm. 24]. Nison: tren naik sebaiknya juga disertai kemiringan kedua MA ke atas.
3. **Dynamic support/resistance:** MA yang terbukti bekerja menjadi S/R; **jangan jadikan MA satu-satunya alasan**, tunggu sinyal candlestick (Nison hlm. 220-223).
4. **Slope:** MA mendatar atau menurun setelah kenaikan panjang = peringatan bearish [Nison hlm. 220].
5. **Envelope/band:** persentase di atas/bawah MA sebagai S/R [Nison hlm. 220].
- **Kelemahan:** lagging, whipsaw di pasar sideways, hasil bergantung periode; "MA optimum hari ini belum tentu optimum besok" [Nison hlm. 220].

### 1.5 Moving Average Oscillator [Nison hlm. 229-233]
Selisih MA pendek dan MA panjang. Nilai > 0 berarti MA pendek di atas MA panjang. Dipakai untuk divergence dan overbought/oversold (jarak terlalu jauh).
(Teks Nison menyebut pengurangan MA pendek dan panjang dengan urutan yang ambigu; skill memakai **MA pendek dikurangi MA panjang** supaya > 0 = MA pendek di atas.)

## 2. MACD (Moving Average Convergence Divergence)

- **Asal:** Gerald Appel (1970) [dos Santos hlm. 24]. Trend dan momentum dalam satu alat.
- **Rumus (konvensi 12-26-9) [Nison hlm. 237; dos Santos hlm. 24-26]:**
  `MACD line = EMA12(Close) - EMA26(Close)`
  `Signal line = EMA9(MACD line)`
  `Histogram = MACD line - Signal line`
- **Cara baca:**
  - *Crossover:* MACD memotong Signal dari bawah ke atas = bullish; dari atas ke bawah = bearish (histogram berganti tanda).
  - *Zero line:* MACD > 0 berarti EMA cepat > EMA lambat (bias naik); < 0 sebaliknya.
  - *Histogram:* tinggi/rendah menunjukkan jarak dua garis; histogram mengecil saat masih positif = momentum naik melemah.
  - *Overbought/oversold:* kurang lazim karena MACD lambat [Nison hlm. 237].
- **Contoh interpretasi (sintetis):**

| Bar | MACD | Signal | Hist |
|---|---|---|---|
| t1 | -0,0012 | -0,0007 | -0,0005 |
| t2 | -0,0006 | -0,0007 | +0,0001 |
| t3 | -0,0001 | -0,0005 | +0,0004 |
| t4 | +0,0004 | -0,0002 | +0,0006 |
| t5 | +0,0009 | +0,0002 | +0,0007 |
| t6 | +0,0012 | +0,0006 | +0,0006 |

  Bullish crossover di t2 (hist berganti positif); MACD melewati nol di t4; Signal melewati nol di t5; histogram memuncak di t5 lalu mengecil di t6
  (momentum melambat walau masih positif).
- **Kelebihan:** menggabungkan tren dan momentum; periode dapat disesuaikan gaya trading [dos Santos hlm. 25]. **Kelemahan:** lagging; crossover berulang saat sideways;
  Nison mencatat candlestick sering memberi tanda **lebih dulu** dari MACD (hlm. 237-239).
- **Aturan yang diuji dos Santos (hlm. 26):** long jika MACD dan Signal keduanya > 0; short jika keduanya < 0; tutup bila kebalikan terjadi.

## 3. RSI (Relative Strength Index)

- **Asal:** J. Welles Wilder Jr. (1978) [dos Santos hlm. 26]. Skala 0-100; memecahkan masalah momentum yang bergerigi dengan smoothing dan menyediakan rentang tetap.
- **Rumus [dos Santos pers. 3.12-3.13; Nison hlm. 226]:**
  `RS = rata-rata kenaikan / rata-rata penurunan` (periode n, biasanya 14; Nison menyebut 9 dan 14)
  `RSI = 100 - 100 / (1 + RS)`
- **Contoh hitung (sintetis, n=5):** close 100, 102, 101, 103, 104, 102 -> perubahan +2, -1, +2, +1, -2. Rata-rata naik = 5/5 = 1,0; rata-rata turun = 3/5 = 0,6;
  RS = 1,6667; RSI = 100 - 100/2,6667 = **62,5**.
- **Level:** overbought > 70, oversold < 30 (Wilder); dos Santos juga menguji **20/80** (lebih ekstrem, sinyal lebih jarang) [hlm. 27-29, 66-69].
- **Cara baca [Nison hlm. 226-229; dos Santos hlm. 28-29]:**
  1. *Overbought/oversold:* hanya peringatan; pada tren kuat RSI bisa bertahan di zona ekstrem lama (Murphy via dos Santos: perhatikan "gerak kedua" indikator).
  2. *Divergence:* harga membuat high baru tetapi RSI tidak = negative/bearish divergence; harga low baru tetapi RSI tidak = positive/bullish divergence. Lebih bermakna di zona overbought/oversold.
  3. *Trendline pada RSI* dapat dipakai.
- **Aturan yang diuji dos Santos (hlm. 29):** long jika RSI_{t-1} < 30 dan RSI_t > 30; short jika RSI_{t-1} < 70 dan RSI_t > 70 (sebagaimana tercetak; lihat 8.2). Tutup bila kebalikan.
- **Kelemahan:** menyesatkan saat gerak kuat (maksimum 100), mengabaikan struktur harga, parameter sensitif (periode pendek = lebih sensitif).

## 4. Bollinger Bands

- **Asal:** John Bollinger, 1980-an [dos Santos hlm. 29]. Pengukur volatilitas dan posisi harga relatif terhadap rata-rata.
- **Rumus (periode N = 20, k = 2) [dos Santos pers. 3.14-3.17]:**
  `Middle = SMA_N(Close)`
  `sigma = akar( (1/N) x sum((Close_i - Middle)^2) )`  (deviasi standar **populasi**)
  `Upper = Middle + 2 sigma`;  `Lower = Middle - 2 sigma`
- **Contoh hitung (sintetis, N=5):** close 10, 12, 11, 13, 14. Middle = 12,0; deviasi = -2, 0, -1, 1, 2; kuadrat = 4, 0, 1, 1, 4 = 10; sigma = akar(10/5) = 1,4142.
  Upper = 12 + 2,8284 = 14,8284; Lower = 12 - 2,8284 = 9,1716. Close 14 masih di bawah Upper.
- **Cara baca:** *Squeeze* (bands menyempit) = volatilitas rendah, sering diikuti ekspansi (arah belum diketahui). *Expansion* = volatilitas naik. Harga menyentuh upper band =
  relatif tinggi, lower band = relatif rendah; **walk the band** pada tren kuat berarti menyentuh band bukan otomatis reversal [Tambahan].
  Buku: ~95,4% harga berada dalam band (asumsi distribusi normal; harga nyata tidak normal, jadi anggap perkiraan) [dos Santos hlm. 29].
- **Aturan yang diuji dos Santos (hlm. 30-31):** long jika Close_{t-1} < Lower_{t-1} dan Close_t > Lower_t (kembali ke dalam band dari bawah);
  short jika Close_{t-1} > Upper_{t-1} dan Close_t < Upper_t; tutup ketika Close memotong band berlawanan. Rasionalnya: lebih baik masuk saat harga **keluar dari zona ekstrem** daripada saat menyentuhnya.
- **Kelemahan:** sulit memprediksi berapa lama harga bertahan di luar band; hasil BB tunggal pada data 2020 termasuk yang terburuk (profit factor 0,62-1,11; hlm. 69, 73).

## 5. Stochastic Oscillator [Nison hlm. 233-237]

- **Rumus:** `fast %K = 100 x (Close - Lowest Low_N) / (Highest High_N - Lowest Low_N)`; `slow %K = SMA_3(fast %K)`; `%D = SMA_3(slow %K)`. Periode umum 14, 19, 21.
- **Contoh (sintetis):** HH_N = 50, LL_N = 40, Close = 47 -> %K = 100 x (47-40)/(50-40) = **70**.
- **Baca:** > 80 overbought, < 20 oversold; crossover %K-%D; divergence. Sinyal beli lebih kuat bila %D <= 20, ada positive divergence, dan %K memotong %D ke atas.
- **Kelemahan:** berisik pada tren kuat; wajib bersama candlestick/struktur.

## 6. Volume [Nison Bab 15, hlm. 241-248]

- Volume seperti tekanan air pada selang; **volume sebaiknya meningkat searah tren**; volume yang menurun saat tren berlanjut mengurangi keyakinan.
- Nison tidak membahas OBV/open interest di bab ini (menyebut tidak dibahas). Gunakan **volume relatif** (dibanding rata-rata) bukan angka mutlak.
- **Dengan candlestick:** doji atau spinning top bervolume sangat tinggi setelah kenaikan panjang menunjukkan suplai besar menahan rally; di akhir penurunan
  menunjukkan demand agresif menyerap suplai; pola reversal (engulfing, dll.) lebih meyakinkan bila volumenya mendukung; candle putih panjang breakout dengan volume ringan
  adalah catatan negatif. Rising window bervolume tinggi menjadi support lebih kokoh.
- **Catatan FX:** spot FX tidak punya volume terpusat; "volume" di chart biasanya tick volume broker [Tambahan].

## 7. Ringkasan aturan sinyal dos Santos (sebagaimana diuji, bukan rekomendasi)

| Indikator | Long | Short | Exit |
|---|---|---|---|
| EMA crossover (12-26, 12-50, 50-200) | EMA cepat memotong EMA lambat ke atas | Memotong ke bawah | Saat kebalikan terjadi |
| MACD (12-26-9) | MACD dan Signal > 0 | MACD dan Signal < 0 | Kebalikan |
| RSI (30/70 atau 20/80), n=14 | RSI_{t-1} < 30 dan RSI_t > 30 | RSI_{t-1} < 70 dan RSI_t > 70 (sebagaimana tercetak) | Kebalikan |
| Bollinger (20, 2) | Close memotong Lower dari bawah ke atas | Close memotong Upper dari atas ke bawah | Close memotong band berlawanan |

Kombinasi menggunakan logika **AND** (kedua sinyal bersamaan): EMA+MACD, EMA+RSI, EMA+BB, MACD+RSI, MACD+BB, RSI+BB (hlm. 52-57). Hasilnya dibahas di `indicator-combinations.md`.
Penelitian tidak memakai leverage, memakai harga Close, dan eksekusi market order di candle berikutnya setelah sinyal (hlm. 38, 45).

## 8. Catatan konsistensi rumus (QC)

1. **RSI:** dos Santos pers. 3.8-3.11 mendefinisikan U_t dan D_t sebagai indikator biner (1/0) sehingga RS tampak sebagai rasio *jumlah hari naik/turun*. Versi baku Wilder dan penjelasan
   Nison memakai **besaran** kenaikan/penurunan (rata-rata gain / rata-rata loss, pada Wilder dengan smoothing). Skill memakai versi besaran (`scripts/backtest_example.py` mendukung sederhana dan Wilder). [Tambahan untuk Wilder smoothing]
2. **RSI short rule** yang tercetak (RSI_{t-1} < 70 dan RSI_t > 70) tampak sebagai *persilangan ke atas 70*; konvensi mean-reversion umum adalah persilangan ke bawah dari >70. Skill melaporkan aturan sebagaimana
   tercetak, tetapi kode contoh dapat disesuaikan; periksa implementasi sebelum membandingkan hasil.
3. **MACD:** pers. 3.5 dos Santos ditulis dengan penjumlahan EMA; praktiknya adalah selisih EMA12 dan EMA26 (konvensi Nison/Appel). Skill memakai selisih.
4. **Tabel alpha:** nilai alpha n=20 pada tabel 3.1 tercetak 0,09624, sedangkan 2/21 = 0,09524. Gunakan 2/(n+1).
5. **Persentase band:** 2 deviasi standar mencakup 95,45% pada distribusi normal (buku: 95,4%); asumsi normal tidak berlaku ketat pada harga.
6. **Kolom "hari":** buku menyebut parameter dalam "hari" padahal data 30 menit; maksudnya jumlah periode/candle.

## 9. Kesalahan umum

1. Memakai indikator tanpa melihat struktur harga atau tren timeframe lebih tinggi.
2. Menganggap RSI > 70 = "jual" atau RSI < 30 = "beli" (di tren kuat bisa bertahan lama).
3. Menghitung EMA/MACD tanpa data pemanasan (warm-up) yang cukup (EMA 200 butuh >= 200 candle plus margin).
4. Mengubah periode demi mencocokkan data masa lalu (overfitting).
5. Mencampur indikator yang sama jenisnya (EMA + MACD keduanya trend) lalu menyebutnya "konfirmasi independen".
6. Membandingkan RSI dari platform berbeda tanpa mengecek versi (SMA vs Wilder).
