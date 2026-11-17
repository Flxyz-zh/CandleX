# Latihan Advanced (10 soal)

Angka sintetis. Rujukan: `../references/indicator-combinations.md`, `price-action-market-structure.md`, `backtesting-methodology.md`, `forex-analysis.md`, `crypto-analysis.md`, `stock-analysis.md`.
Daftar: C1-C3 (Kategori 6: Confluence Analysis), S1-S3 (Kategori 7: Market Scenario Analysis), T1-T4 (Kategori 8: Backtesting and Quantitative Evaluation).
Semua jawaban harus **tanpa perintah BUY/SELL**; gunakan level analitis dan pembatal.

---

### C1 - Hammer + RSI + volume tetapi HTF turun (Case Study) | Kategori 6 | Advanced
**Informasi (1H, instrumen sintetis):** hammer di support horizontal yang sudah teruji dua kali; RSI(14) = 28 lalu naik ke 33; volume 1,8x rata-rata 20 bar; 4H dan 1D downtrend, harga di bawah EMA 50 dan 200; belum ada candle konfirmasi.
**Pertanyaan:** Klasifikasikan confluence, uraikan bukti pendukung/lawan/konfirmasi yang kurang/pembatal.

### C2 - Evening star di resistance (Case Study) | Kategori 6 | Advanced
**Informasi:** harga di high 3 bulan sebelumnya yang pernah ditolak; evening star lengkap (candle 3 close di bawah titik tengah body 1); RSI membuat lower high saat harga higher high (bearish divergence); MACD bearish crossover di bar yang sama; volume tinggi pada candle 3; semua pola dan indikator di 1H, sedangkan 4H masih uptrend (HH-HL) tanpa tanda pembalikan.
**Pertanyaan:** Klasifikasikan confluence dan jelaskan sifat bukti (independen?), pembatal, dan batasan interpretasi.

### C3 - Sinyal bertentangan (Case Study) | Kategori 6 | Advanced
**Informasi:** bullish engulfing yang terbentuk tepat di resistance 4H; RSI = 72; MACD baru bearish crossover; EMA 12 > EMA 50 (tren naik); volume rata-rata.
**Pertanyaan:** Klasifikasikan dan jelaskan mengapa. Bagaimana skenario netral ditulis?

### S1 - Konsolidasi crypto (Case Study) | Kategori 7 | Advanced
**Informasi:** Aset X/USDT, 4H, data 40 candle terakhir: range 38.200-42.000; resistance 42.000 ditolak dua kali (high 41.950 dan 42.020 dengan close di bawah); harga sekarang 41.600; lebar Bollinger Bands terkecil dalam 60 bar; volume 35% di bawah rata-rata 20 bar; RSI(14) = 58; EMA 50 mendatar di 40.100; 1D: HH-HL sebelum range.
**Pertanyaan:** Susun Market Overview singkat, skenario bullish/bearish/neutral dengan pembatal masing-masing, dan target analitis measured move bila terjadi breakout atau breakdown. Jangan memberi instruksi transaksi.

### S2 - Gap earnings pada saham (Case Study) | Kategori 7 | Advanced
**Informasi:** Saham Y harian. Hari sebelumnya: H 1.012; L 990; C 1.000. Earnings diumumkan setelah penutupan. Hari ini: O 1.060; H 1.085; L 1.058; C 1.062; volume 3,2x rata-rata. Uptrend 8 minggu; resistance sebelumnya 1.050.
**Pertanyaan:** (a) Identifikasi window dan bentuk candle. (b) Apa makna masing-masing menurut Nison dan mana yang diutamakan? (c) Skenario berikutnya dan pembatal. (d) Peran peristiwa earnings.

### S3 - Hammer sebelum berita besar (Case Study) | Kategori 7 | Advanced
**Informasi:** EUR/USD 15M, hammer di support 1,0900; rilis berita berdampak tinggi 30 menit lagi; spread melebar dari 0,8 ke 3,5 pip; 4H downtrend, 1H sideways.
**Pertanyaan:** Bagaimana menilai situasi ini secara analitis? Hal apa yang harus disebut dan tidak boleh disebut?

### T1 - Profit factor, win rate, expectancy (Numerical Calculation) | Kategori 8 | Advanced
**Informasi:** 10 trade simulasi: menang +120, +80, +150, +60; kalah -50, -70, -40, -90, -60, -30.
**Pertanyaan:** Hitung Gross Profit, Gross Loss, Profit Factor, Win Rate, Average Win, Average Loss, payoff ratio, expectancy per trade, dan break-even win rate untuk payoff tersebut.

### T2 - Maximum drawdown (Numerical Calculation) | Kategori 8 | Advanced
**Informasi:** Equity berurutan: 10.000; 10.200; 10.100; 10.500; 9.975; 9.800; 10.300; 10.650; 10.400; 10.900.
**Pertanyaan:** Hitung maximum drawdown (nilai dan persen), total return, dan drawdown terbesar kedua.

### T3 - Membaca hasil historis dengan benar (Case Study) | Kategori 8 | Advanced
**Informasi (profit factor, EUR/USD | GBP/USD, strategi kombinasi pada data penelitian dos Santos, tabel 6.1):** 2020: 1,70 | 2,44; 2019: 0,43 | 1,15; 2018: 0,90 | 0,73; 2017: 2,63 | 2,48; 2016: 0,71 | 0,30. Jumlah trade 2020: 22 | 21.
**Pertanyaan:** (a) Hitung rata-rata sederhana dan jumlah tahun PF > 1. (b) Mengapa rata-rata PF bermasalah? (c) Apa kesimpulan yang sah dan tidak sah? (d) Sebutkan bias yang perlu dicek.

### T4 - Dampak biaya (Numerical Calculation) | Kategori 8 | Advanced
**Informasi:** 200 trade; expectancy kotor 3,0 pip per trade.
**Pertanyaan:** (a) Biaya (spread+slippage) 1,2 pip per trade: expectancy bersih dan total pip. (b) Biaya 3,5 pip? (c) Biaya impas?
