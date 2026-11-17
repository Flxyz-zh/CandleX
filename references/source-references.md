# Pemetaan Sumber dan Referensi

Daftar isi: 1 Sumber - 2 Cara membaca nomor halaman - 3 Peta Buku 1 (Nison) -> file skill - 4 Peta Buku 2 (dos Santos) -> file skill - 5 Hubungan antar-buku -
6 Konsep komplementer - 7 Konsep yang tidak ada di sumber - 8 Batasan sumber

## 1. Sumber

| Kode | Rincian lengkap |
|---|---|
| **Nison** | Steve Nison, *Japanese Candlestick Charting Techniques: A Contemporary Guide to the Ancient Investment Techniques of the Far East*, 2nd Edition. New York Institute of Finance, 2001 (ISBN 0-7352-0181-1). 17 bab, 2 glosarium, bibliografi. |
| **dos Santos** | Bruna Filipa Gonçalves dos Santos, *Technical Indicators Efficacy in Forex Markets*, tesis MSc Information Systems and Computer Engineering, Instituto Superior Técnico (Universidade de Lisboa), September 2021. Pembimbing: Prof. Luís Cavique Santos. |

## 2. Cara membaca nomor halaman

- **dos Santos:** nomor halaman = nomor **cetak** pada tesis. Halaman PDF = halaman cetak + 24 (untuk bagian isi utama).
- **Nison:** nomor halaman = nomor **cetak** buku. File PDF yang dipakai saat ekstraksi memiliki halaman yang hilang, sehingga selisih halaman PDF dan cetak berubah sepanjang buku (sekitar +11 di Bab 3-4 hingga +0 di akhir).
  Kutipan halaman di skill memakai **halaman awal bagian menurut daftar isi buku** (mis. Hammer hlm. 34), atau nomor cetak yang terlihat pada header halaman. Untuk kutipan yang tertulis "sekitar hlm.", periksa sekitar +/- 2 halaman.
- Ringkasan di skill ditulis dengan kalimat sendiri; skill tidak menyalin paragraf, ilustrasi, atau latihan buku.

## 3. Peta Buku 1 (Nison)

| Bab / bagian (hlm. cetak) | Kategori yang diminta | Dicakup di |
|---|---|---|
| 1 Introduction (1-13): konteks, "Some Cautions" (8-10), pentingnya analisis teknikal (11) | Introduction; batasan | `candlestick-patterns.md` bagian 1; SKILL.md bagian 0 |
| 2 Historical Background (15-19): Osaka, Dojima Rice Exchange, rice coupons sebagai futures pertama, Munehisa Homma | Historical background | Ringkasan di bawah; `README.md` |
| 3 Constructing the Candlestick Lines (23-29): real body, shadow, spinning top, doji, open/close | Constructing | `candlestick-fundamentals.md` |
| 4 Reversal Patterns (31-59): Umbrella lines/Hammer 34, Hanging Man 38, Engulfing 42, Dark-Cloud 49, Piercing 55 | Reversal | `candlestick-patterns.md` bagian 3 |
| 5 Stars (61-79): Morning 62, Evening 66, Doji Stars 70, Shooting Star 75, Inverted Hammer 77 | Star patterns | `candlestick-patterns.md` bagian 4 |
| 6 More Reversal Patterns (81-123): Harami 82, Harami Cross 83, Tweezers 87, Belt-Hold 93, Upside-Gap Two Crows 95, Three Black Crows 97, Three White Soldiers 99, Three Mountains/Rivers 103, Counterattack 109, Dumpling/Frypan 114, Tower 119 | Reversal | `candlestick-patterns.md` bagian 3-5 |
| 7 Continuation Patterns (125-153): Windows 126, Tasuki 134, Gapping Plays 136, Gapping Side-by-Side White Lines 139, Rising/Falling Three Methods 142, Separating Lines 150 | Continuation | `candlestick-patterns.md` bagian 6 |
| 8 The Magic Doji (155-171): Northern Doji 158, Long-Legged/Gravestone/Dragonfly 161, Tri-Star 170 | Doji | `candlestick-patterns.md` bagian 7 |
| 9 Putting It All Together (173-179) | Latihan interpretasi chart | `candlestick-patterns.md` bagian 8-9 (prinsip: konteks) |
| Part 2 Convergence (181) dan 10 Cluster of Candles (187) | Convergence; clusters | `price-action-market-structure.md` bagian 9; `indicator-combinations.md` bagian 1 |
| 11 Candles with Trend Lines (193): Springs and Upthrusts 199, Change of Polarity 205 | Trendline; spring/upthrust; polarity | `price-action-market-structure.md` bagian 5-7 |
| 12 Candles with Retracement Levels (213) | Retracement | `price-action-market-structure.md` bagian 8 |
| 13 Candles with Moving Averages (217): SMA 217, WMA 219, EMA 219 | MA | `technical-indicators.md` bagian 1 |
| 14 Candles with Oscillators (225): RSI 226, MA Oscillator 229, Stochastics 233, MACD 237 | Oscillators | `technical-indicators.md` bagian 1.5, 2, 3, 5 |
| 15 Candles with Volume (241) | Volume | `technical-indicators.md` bagian 6 |
| 16 Measured Moves (249): Boxes 250, Swing Targets/Flags/Pennants 255 (+ triangle) | Measured moves | `price-action-market-structure.md` bagian 10 |
| 17 Best of East and West (263), Conclusion (267) | Konvergensi Timur-Barat | `indicator-combinations.md` bagian 1 |
| Glossary A (269), Glossary B (279) | Terminologi | Istilah dipakai di seluruh file |

**Sejarah (Bab 2) ringkas:** Jepang abad 16-18 bersatu di bawah Tokugawa; perdagangan nasional berkembang; Osaka menjadi pusat; Dojima Rice Exchange (akhir 1600-an) memperdagangkan rice coupon sebagai kontrak berjangka pertama di dunia; Munehisa Homma (1724-1803)
diyakini mengembangkan prinsip yang menjadi metodologi candlestick; istilah "Sakata's Rules". Nison memperkenalkan candlestick ke Barat pada 1989/1991 (hlm. 15-19, Preface).

## 4. Peta Buku 2 (dos Santos)

| Bab (hlm. cetak) | Kategori yang diminta | Dicakup di |
|---|---|---|
| 1 Introduction (1-5): tujuan, kontribusi, organisasi | Konteks | `forex-analysis.md`; `source-references.md` |
| 2.1 Forex: sejarah dan konsep (9-11) | Forex Market Concepts | `forex-analysis.md` bagian 1-2 |
| 2.2.1 Random Walk (11-13); 2.2.2 Fundamental (13-14) | Random Walk; Fundamental vs Technical | `forex-analysis.md` bagian 5 dan 7 |
| 2.3 Technical Analysis (14-17): Dow Theory, chart analysis, timeframe, tren, kelompok indikator | Chart, timeframe, tren | `price-action-market-structure.md` bagian 1; `multi-timeframe-analysis.md`; `candlestick-fundamentals.md` |
| 3 Technical Indicators (21-31): EMA, MACD, RSI, Bollinger Bands + rumus + aturan | Indikator; perhitungan matematis | `technical-indicators.md` |
| 4 Indicators, Signals, Rules, Strategies, Implementation in R (35-57) | Sinyal, aturan, strategi tunggal dan kombinasi; metodologi backtest | `backtesting-methodology.md`; `indicator-combinations.md` |
| 5 Results 2020 (61-75); 6 Results 2016-2020 (79-84) | Historical performance; strategy evaluation | `indicator-combinations.md` bagian 4 |
| 7 Conclusion (87-88), 7.1 Limitations (88) | Keterbatasan dan kesimpulan | `indicator-combinations.md` bagian 4.3 dan 5 |
| Appendix A (93-111): plot, kode R, equity curve; Appendix B (113-115): tabel hasil sinyal berlawanan | Lampiran | `indicator-combinations.md` bagian 4.2; `backtesting-methodology.md` bagian 9 (kerangka) |

Parameter referensi yang dicakup: EMA 12, 26, 50, 200 (crossover 12-26, 12-50, 50-200); MACD 12-26-9; RSI 14 (30/70 dan 20/80); BB 20 periode, 2 SD.

## 5. Hubungan antara kedua buku

| Topik | Nison | dos Santos | Catatan skill |
|---|---|---|---|
| Candle (OHLC) | Bab 3: konstruksi, makna | hlm. 15-16, 22 | Konsisten; skill mengutamakan hitung angka dulu |
| MA/EMA | Bab 13 (SMA/WMA/EMA, golden/dead cross) | 3.1: rumus EMA, crossover 12-26, 12-50, 50-200 | Nison konseptual; dos Santos rumus dan uji |
| MACD | Bab 14: 12/26/9 | 3.2: rumus dan aturan MACD, signal > 0 | Nison: candle sering mendahului MACD |
| RSI | Bab 14: formula, 70/30, divergence | 3.3: formula, 30/70 dan 20/80 | Perbedaan formula dicatat di `technical-indicators.md` bagian 8 |
| Bollinger Bands | (tidak dibahas sebagai topik; Nison menyinggung moving average band) | 3.4 | Dari dos Santos saja |
| Tren, S/R | Bab 11 (garis tren, polarity) | 2.3.3 (tren) | Saling melengkapi |
| Volume | Bab 15 | disebut di Dow Theory | |
| Kombinasi sinyal | Bab 10 dan 17 (convergence) | Bab 4-6 (kombinasi AND) | Nison: kualitatif; dos Santos: kuantitatif dan menunjukkan hasil tidak stabil |
| Backtesting | (tidak ada; tekanan pada manajemen risiko, stop, target) | Bab 4-6 | Dari dos Santos |

## 6. Konsep yang saling melengkapi
1. Candlestick (Nison) sebagai sinyal timing dan level + indikator (dos Santos) sebagai ukuran tren/momentum/volatilitas.
2. Konsep convergence Nison dapat diuji secara kuantitatif memakai kerangka backtest dos Santos (dengan batasan sampel).
3. Peringatan Nison "all clouds do not rain" (osilator = awan) selaras dengan temuan dos Santos bahwa indikator saja tidak andal.
4. Konsep tren Nison/Dow (tren sebagai konteks pola) selaras dengan temuan dos Santos bahwa efektivitas bergantung arah tren pasar.

## 7. Konsep yang tidak ada di sumber (diberi label [Tambahan] di file lain)
Supply/Demand zone, sesi forex detail, klasifikasi Major/Minor/Exotic, karakter crypto, corporate action saham, Wilder smoothing, walk-forward/Monte Carlo, ATR, definisi eksak ambang body/shadow (selain 2x untuk hammer), rubrik confluence.

## 8. Batasan sumber
Lihat `VERIFICATION-REPORT.md` bagian "Keterbatasan". Ringkas: hasil dos Santos satu sampel (EUR/USD, GBP/USD, 30 menit, 2016-2020, tanpa leverage, modal tetap); Nison berfokus pasar AS dan tidak menyediakan statistik keberhasilan pola;
tidak ada bukti dari kedua buku untuk crypto; pola candlestick bersifat subjektif dan membutuhkan konfirmasi.
