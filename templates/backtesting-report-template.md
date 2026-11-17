# Template Laporan Backtesting

Referensi: `../references/backtesting-methodology.md`, `../scripts/backtest_example.py`.
Aturan: hasil historis bukan jaminan hasil masa depan; jangan melaporkan hasil kotor saja; wajib sertakan biaya, out-of-sample, dan batasan.

## 1. Tujuan dan hipotesis
(Apa yang diuji? Ditulis sebelum melihat hasil.)

## 2. Data
- Instrumen / Asset class / Timeframe:
- Rentang waktu, jumlah bar, sumber, zona waktu, penyesuaian (split/dividen):
- Pembagian: in-sample ... ; out-of-sample ... (tanggal atau persen)

## 3. Strategi (aturan eksak)
- Indikator dan parameter (mis. EMA 12/50, MACD 12-26-9, RSI 14 30/70, BB 20 SD 2; versi RSI: SMA/Wilder):
- Sinyal long / short / exit:
- Eksekusi: (open bar t+1; arah yang diizinkan; ukuran tetap)
- Jumlah variasi parameter yang dicoba (untuk menilai data snooping):

## 4. Asumsi biaya
- Spread / fee / slippage / funding atau swap:

## 5. Hasil
| Metrik | In-sample | Out-of-sample |
|---|---|---|
| Total Return | | |
| Number of Trades | | |
| Win Rate | | |
| Profit Factor | | |
| Maximum Drawdown (nilai, %, durasi) | | |
| Average Win / Average Loss | | |
| Expectancy per trade | | |
| Risk-to-Reward (payoff) | | |

Equity curve dan drawdown: (lampirkan atau jelaskan bentuknya: stabil / bergantung beberapa trade / bergantung rezim)

## 6. Analisis kehandalan
- Sensitivitas parameter:
- Konsistensi antar periode/instrumen/rezim:
- Look-ahead bias dicek? Overfitting? Survivorship?
- Ukuran sampel: (jumlah trade cukup?)

## 7. Kesimpulan terbatas
(Apa yang dapat dan tidak dapat disimpulkan. Pisahkan fakta historis dari ekspektasi masa depan.)

## 8. Keterbatasan
(Daftar eksplisit.)
