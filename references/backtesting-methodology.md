# Metodologi Backtesting dan Analisis Kuantitatif

Daftar isi: 1 Definisi dan tujuan - 2 Kerangka dos Santos (Quantstrat) - 3 Alur kerja langkah demi langkah - 4 Metrik dan rumus - 5 Contoh hitung - 6 Biaya - 7 Bias dan jebakan -
8 Out-of-sample dan robustness - 9 Contoh kode Python dan R - 10 Cara melaporkan - 11 Kesalahan umum

Label: **[dos Santos]** (halaman cetak), **[Skill]**, **[Tambahan]**. Semua angka contoh sintetis dan sudah dihitung ulang.

## 1. Definisi dan tujuan

Backtesting = memasukkan data historis ke aturan strategi untuk melihat bagaimana strategi *akan* berkinerja; harapannya kinerja historis memberi gambaran kinerja masa depan [dos Santos hlm. 38].
Namun, hasil historis **bukan jaminan** masa depan; dos Santos sendiri menemukan strategi terbaik di 2020 tidak bertahan di 2016-2019 (hlm. 79-80, 87). Pisahkan selalu:
(a) **fakta historis** pada sampel tertentu, dan (b) **ekspektasi masa depan** (tidak dapat dijamin).

## 2. Kerangka dos Santos (Quantstrat, R) [hlm. 38-46]

| Tahap | Isi |
|---|---|
| Initialization | Definisikan instrumen, account, portfolio, tanggal awal (initDate harus sebelum data pertama; jika tidak, drawdown awal palsu muncul), modal awal, quantity, threshold, fee (hlm. 40-42) |
| Define strategy | **Indicators** (output matematis, tidak tahu posisi) -> **Signals** (interaksi indikator dengan data/indikator lain; tipe: sigComparison, sigCrossover, sigThreshold, sigFormula, sigPeak) -> **Rules** (aturan order: enter/exit, long/short, ordertype, orderqty, fee) (hlm. 42-45) |
| Processing | `applyStrategy()` menghasilkan transaksi; market order dieksekusi pada **candle berikutnya** setelah sinyal (hlm. 45) |
| Update | `updatePortf()`, `updateAcct()`, `updateEndEq()` menghitung P&L, equity, statistik (hlm. 46) |
| Reporting | Plot dan tabel: gross profit/loss, final capital, jumlah trade, percent profitable, profit factor, equity curve |

Indikator bukan strategi: strategi baru lengkap dengan sinyal, aturan, dan manajemen order (hlm. 42).
Gabungan sinyal memakai `sigFormula` dengan logika AND (hlm. 52-57).

## 3. Alur kerja [Skill]

1. **Hipotesis tertulis** sebelum melihat hasil (apa yang diuji dan mengapa).
2. **Data:** OHLC bersih, zona waktu konsisten, penyesuaian (saham: split/dividen), tidak ada celah/duplikat; cantumkan sumber dan rentang.
3. **Hitung indikator** hanya dengan data sampai bar t (tanpa data masa depan). Sisihkan warm-up (EMA 200 butuh >= 200 bar; hitung posisi pertama setelah itu).
4. **Hasilkan sinyal** pada penutupan bar t.
5. **Eksekusi** pada open bar t+1 (sama dengan perilaku market order Quantstrat). Terapkan spread, fee, slippage.
6. **Catat tiap trade:** waktu entry/exit, arah, harga, biaya, P&L.
7. **Bangun equity curve** (jumlah kumulatif P&L; dos Santos pers. 5.3) dan hitung metrik.
8. **Uji ulang** pada data out-of-sample / periode / instrumen berbeda; analisis sensitivitas parameter.
9. **Laporkan** dengan batasan (template `templates/backtesting-report-template.md`).

## 4. Metrik dan rumus

| Metrik | Rumus | Catatan |
|---|---|---|
| Total Return | (Equity akhir / Equity awal - 1) x 100% | Bukan ukuran risiko |
| Number of Trades | Jumlah round-trip | Sampel kecil = hasil tidak andal |
| Win Rate (Percent Profitable) | Trade menang / total trade [dos Santos pers. 5.2] | Tinggi belum tentu menguntungkan (lihat payoff) |
| Profit Factor | Gross Profit / Gross Loss [dos Santos pers. 5.1] | > 1 positif; sensitif terhadap beberapa trade besar |
| Average Win / Average Loss | Rata-rata P&L trade menang / kalah | |
| Payoff (Risk-to-Reward realisasi) | Avg Win / abs(Avg Loss) | Bandingkan dengan win rate |
| Expectancy per trade | (Total P&L) / N = WinRate x AvgWin - LossRate x AvgLoss | Harus > biaya + margin ketidakpastian |
| Equity Curve | EC(m) = sum P_trade sampai trade ke-m [dos Santos pers. 5.3] | Lihat bentuk: stabil atau bergantung beberapa lonjakan? |
| Maximum Drawdown | max over t dari (puncak_sampai_t - equity_t) / puncak_sampai_t | Ukuran risiko utama; juga catat durasi drawdown |

Break-even win rate untuk payoff b: `WR* = 1 / (1 + b)` (mis. payoff 2 -> 33,3%).

## 5. Contoh hitung (sintetis)

**Profit factor, win rate, expectancy.** 10 trade: menang +120, +80, +150, +60; kalah -50, -70, -40, -90, -60, -30.
Gross Profit = 410; Gross Loss = 340; PF = 410/340 = **1,206**; Win Rate = 4/10 = **40%**; Avg Win = 102,5; Avg Loss = 56,67; payoff = 1,809;
Expectancy = (410-340)/10 = **+7,0 per trade** (cek: 0,4x102,5 - 0,6x56,67 = 7,0). Total P&L = +70.

**Maximum drawdown.** Equity: 10.000; 10.200; 10.100; 10.500; 9.975; 9.800; 10.300; 10.650; 10.400; 10.900.
Puncak berjalan 10.500 -> palung 9.800 = drawdown 700 = 700/10.500 = **6,67%**. Drawdown kedua (10.650 -> 10.400) = 2,35%. Return total = +9,0%.

## 6. Biaya

Sertakan: **spread**, **fee/komisi**, **slippage** (selisih harga sinyal vs eksekusi), **funding/swap** bila relevan (perpetual crypto, posisi menginap FX).
Dampak: strategi dengan expectancy kotor 3,0 pip dan biaya 1,2 pip per trade -> expectancy bersih 1,8 pip; 200 trade = 360 pip bersih (bukan 600 pip). Pada biaya 3,5 pip, expectancy menjadi -0,5 pip (negatif).
Titik impas biaya = expectancy kotor. dos Santos memakai biaya tetap -$6 per transaksi (hlm. 41); strategi 600 trade (BB) menanggung biaya lebih besar daripada strategi 22 trade (EMA 12-50 & MACD).

## 7. Bias dan jebakan

| Masalah | Penjelasan | Pencegahan |
|---|---|---|
| **Look-ahead bias** | Memakai informasi yang belum tersedia saat keputusan (mis. entry di harga close bar sinyal sebelum candle selesai; indikator dihitung dengan seluruh sampel; swing high belum terkonfirmasi) | Eksekusi di open bar berikutnya; hitung indikator kausal; shift sinyal 1 bar |
| **Overfitting / data snooping** | Menyetel periode/level sampai bagus pada sampel; mencoba banyak kombinasi lalu melaporkan yang terbaik | Batasi jumlah parameter; uji OOS; catat semua variasi yang dicoba; sensitivitas |
| **Survivorship bias** | Hanya aset yang masih ada | Sertakan delisting/aset hilang |
| **Sampel kecil** | 21 trade tidak cukup untuk profit factor 2,44 | Laporkan jumlah trade dan ketidakpastian |
| **Regime dependence** | Kinerja bergantung tren naik/turun (dos Santos: 2017 dan 2020 baik, 2016/2018 buruk) | Pisahkan hasil per rezim/tahun |
| **Biaya diabaikan** | | Selalu bersih biaya |
| **Data snooping pada metrik** | Rata-rata PF antar tahun | Gabungkan gross profit/loss |
| **Eksekusi tidak realistis** | Mengisi order di harga yang tidak ada | Gunakan bid/ask, likuiditas |

## 8. Out-of-sample dan robustness [Tambahan/Skill]

- **Pisah data:** in-sample (mengembangkan) vs out-of-sample (hanya satu kali uji akhir). Skrip contoh memakai `--oos-fraction`.
- **Walk-forward:** parameter dioptimasi pada jendela awal, diuji pada jendela berikutnya, lalu digeser maju.
- **Sensitivitas parameter:** hasil harus relatif stabil di sekitar parameter terpilih (mis. EMA 10-14, bukan hanya tepat 12).
- **Multi-instrumen dan multi-periode:** konsisten antar pasangan/tahun (dos Santos: tidak konsisten).
- **Monte Carlo/bootstrapping trade** untuk gambaran distribusi drawdown (opsional, [Tambahan]).

## 9. Contoh kode

### Python (teruji; lihat `scripts/backtest_example.py`)
```bash
python scripts/backtest_example.py                       # data sintetis, EMA 12/50 + MACD
python scripts/backtest_example.py --csv data.csv --strategy rsi_bb --cost 0.0001
```
Inti logika (versi ringkas):
```python
# sinyal pada bar t, eksekusi pada open bar t+1
f, s = ema(close, 12), ema(close, 50)
macd_line, signal, hist = macd(close)
long_ = (f > s) & (macd_line > 0) & (signal > 0)
short_ = (f < s) & (macd_line < 0) & (signal < 0)
trades, equity = run(df, long_, short_, cost=0.0001)
print(metrics(trades, equity, 10_000))
```
Pada data sintetis acak, hasil mendekati nol atau negatif setelah biaya; itu wajar dan menegaskan perlunya uji pada data nyata dan OOS.

### R (kerangka mengikuti pendekatan tesis; **belum dijalankan di lingkungan pembuatan skill ini**)
```r
library(quantstrat)  # quantstrat, blotter, FinancialInstrument, TTR
initDate <- "2019-12-31"
strategy("ema_macd", store = TRUE)
add.indicator("ema_macd", name = "EMA", arguments = list(x = quote(Cl(mktdata)), n = 12), label = "ema12")
add.indicator("ema_macd", name = "EMA", arguments = list(x = quote(Cl(mktdata)), n = 50), label = "ema50")
add.signal("ema_macd", name = "sigCrossover",
           arguments = list(columns = c("ema12", "ema50"), relationship = "gt"), label = "ema12.gt.ema50")
add.rule("ema_macd", name = "ruleSignal",
         arguments = list(sigcol = "ema12.gt.ema50", sigval = TRUE, orderqty = 10000,
                          ordertype = "market", orderside = "long", TxnFees = -6),
         type = "enter")
# ... tambahkan rule exit, initPortf/initAcct/initOrders, applyStrategy(), updatePortf() dst. (lihat tesis hlm. 40-46)
```

## 10. Cara melaporkan

Gunakan `templates/backtesting-report-template.md`. Wajib ada: data dan rentang, aturan eksak, biaya, metrik lengkap, equity curve/drawdown, hasil OOS, keterbatasan, dan pernyataan
bahwa hasil historis bukan jaminan. Jangan menambahkan klaim "strategi ini menguntungkan" tanpa konteks.

## 11. Kesalahan umum

1. Melaporkan hanya total return tanpa drawdown dan jumlah trade.
2. Memilih periode awal/akhir yang menguntungkan.
3. Memakai close bar yang sama untuk sinyal dan eksekusi.
4. Mengoptimalkan parameter pada seluruh data lalu menyebutnya "teruji".
5. Membandingkan strategi dengan jumlah trade sangat berbeda tanpa memperhitungkan ketidakpastian.
6. Mengabaikan perbedaan versi indikator (RSI SMA vs Wilder).
