# Latihan Intermediate (11 soal)

Angka sintetis. Rujukan: `../references/candlestick-patterns.md`, `technical-indicators.md`, `multi-timeframe-analysis.md`.
Daftar: P4 (Kategori 2), R1-R3 (Kategori 3: Reversal and Continuation Analysis), I1-I4 (Kategori 4: Technical Indicator Interpretation), M1-M3 (Kategori 5: Multi-Timeframe Analysis).

---

### P4 - Satu bentuk, dua nama (Pattern Identification) | Kategori 2 | Intermediate
**Informasi:** Dua candle berbentuk sama (body kecil di ujung atas range, lower shadow panjang, upper shadow minimal).
- Kasus A: O 45,20; H 45,30; L 44,00; C 45,25. Didahului 6 close turun beruntun.
- Kasus B: O 52,20; H 52,30; L 51,00; C 52,25. Didahului 8 close naik beruntun dan harga di high tertinggi 3 bulan.
**Pertanyaan:** (a) Hitung body, lower shadow, rasio lower shadow terhadap body. (b) Beri nama pola tiap kasus. (c) Konfirmasi apa yang dibutuhkan masing-masing?

### R1 - Rising Three Methods? (Chart Interpretation) | Kategori 3 | Intermediate
**Informasi (O/H/L/C), tren naik sebelumnya:**
C1 10,00/10,90/9,95/10,80 | C2 10,60/10,70/10,35/10,40 | C3 10,45/10,50/10,25/10,30 | C4 10,35/10,40/10,20/10,25 | C5 10,30/11,20/10,28/11,10.
**Pertanyaan:** Apakah ini rising three methods? Periksa setiap kriteria, tentukan klasifikasi (reversal/continuation), level risiko analitis, dan apa yang membatalkan.

### R2 - Window atau bukan? (Chart Interpretation) | Kategori 3 | Intermediate
**Informasi:**
Bagian a: Candle A: O 20,0; H 21,0; L 19,8; C 20,9. Candle B: O 21,6; H 22,5; L 20,9; C 22,4.
Bagian b: Hari 1 high = 50,00. Hari 2 low = 50,40. Hari berikutnya (D3) close 50,12 lalu D4 close 49,90.
**Pertanyaan:** (a) Apakah A dan B membentuk rising window? (b) Pada bagian b, tentukan zona window, fungsi, dan status setelah D4.

### R3 - Reversal atau continuation? (Matching) | Kategori 3 | Intermediate
**Informasi:** Delapan pola: Harami; Tasuki (gap); Dark-Cloud Cover; Separating Lines; Rising Window; Three Black Crows; Rising Three Methods; Tweezers Top.
**Pertanyaan:** Klasifikasikan tiap pola sebagai Reversal atau Continuation, dan sebutkan prasyarat tren masing-masing secara singkat.

### I1 - Hitung EMA (Numerical Calculation) | Kategori 4 | Intermediate
**Informasi:** Close: 20, 22, 21, 23, 25. Gunakan EMA periode 3 dengan seed SMA 3 pertama.
**Pertanyaan:** (a) alpha, (b) EMA pada bar ke-4 dan ke-5, (c) alpha untuk periode 12, 26, 50, 200.

### I2 - Hitung RSI (Numerical Calculation) | Kategori 4 | Intermediate
**Informasi:** Close: 100, 102, 101, 103, 104, 102. Periode RSI = 5 (disederhanakan; rata-rata sederhana, bukan smoothing Wilder).
**Pertanyaan:** Hitung rata-rata naik, rata-rata turun, RS, RSI. Apakah overbought menurut 70/30?

### I3 - Hitung Bollinger Bands (Numerical Calculation) | Kategori 4 | Intermediate
**Informasi:** Close 5 bar: 10, 12, 11, 13, 14. Gunakan N = 5, k = 2, deviasi standar populasi.
**Pertanyaan:** Hitung Middle, sigma, Upper, Lower. Posisi close terakhir terhadap band? Aturan dos Santos apa yang akan memicu long atau short?

### I4 - Interpretasi MACD (Chart Interpretation) | Kategori 4 | Intermediate
**Informasi:**
| Bar | MACD | Signal |
|---|---|---|
| t1 | -0,0012 | -0,0007 |
| t2 | -0,0006 | -0,0007 |
| t3 | -0,0001 | -0,0005 |
| t4 | +0,0004 | -0,0002 |
| t5 | +0,0009 | +0,0002 |
| t6 | +0,0012 | +0,0006 |
**Pertanyaan:** (a) Hitung histogram. (b) Kapan terjadi bullish crossover? (c) Kapan MACD dan Signal melewati nol? (d) Kapan aturan MACD dos Santos "kedua garis > 0" terpenuhi? (e) Apa makna histogram t5 ke t6?

### M1 - Konflik antar-timeframe (Case Study) | Kategori 5 | Intermediate
**Informasi:** Instrumen sintetis X.
- 1D: HH-HL berurutan; harga di atas EMA 50 dan 200.
- 4H: harga turun ke zona support 4H sebelumnya dari swing high; body kecil.
- 1H: bearish engulfing di bawah resistance 1H, tiga candle turun.
- 15M: lower high dan lower low berurutan; MACD < 0.
**Pertanyaan:** Klasifikasikan keselarasan, jelaskan dua tafsir yang mungkin, dan sebut bukti yang membedakan keduanya.

### M2 - Benar atau Salah (True/False) | Kategori 5 | Intermediate
1. Cukup satu timeframe 5M untuk menyimpulkan tren utama.
2. Pola bullish di 15M yang berlawanan dengan downtrend 1D tergolong counter-trend dan lebih rentan gagal.
3. Candle 4H yang belum close dapat berubah bentuk.
4. Parameter EMA 200 bermakna sama pada 5M dan 1D.
5. Jika timeframe tersedia hanya satu, skill sebaiknya menyatakan konteks tren lebih besar tidak dapat dinilai.

### M3 - Pilih deskripsi terbaik (Multiple Choice) | Kategori 5 | Intermediate
**Informasi:** Di 15M terlihat bullish engulfing. 4H: harga tepat di bawah falling window sebagai resistance. 1D: downtrend (LH-LL).
**Pertanyaan:** Deskripsi terbaik?
- A. Strong Confluence bullish karena engulfing jelas.
- B. Pola counter-trend di bawah resistance TF atas; confluence maksimum Moderate bila ada pendukung lain; kemungkinan hanya rebound.
- C. Pola tidak relevan karena TF terlalu kecil.
- D. Sinyal jual karena 1D turun.
