# CandleX

**Skill AI portabel untuk analisis candlestick, price action, indikator teknikal, dan backtesting di pasar Forex, Crypto, dan Saham.**
Ditulis dalam Markdown murni, berbahasa Indonesia (istilah teknikal Inggris dipertahankan), dan dapat dipasang ke berbagai AI agent.

> **Disclaimer:** CandleX hanya untuk edukasi, analisis historis, dan simulasi. Bukan nasihat investasi dan bukan sinyal BUY/SELL.
> Tidak ada pola candlestick atau indikator yang menjamin arah harga. Hasil historis bukan jaminan hasil masa depan.
> Gunakan paper trading dengan dana virtual untuk belajar.

---

## Apa itu CandleX?

CandleX mengubah AI agent menjadi analis chart yang sistematis dan berbasis bukti. Skill ini menggabungkan dua sumber pengetahuan:

| Sumber | Peran dalam skill |
|---|---|
| Steve Nison, *Japanese Candlestick Charting Techniques* (2nd Ed.) | Pola candlestick, convergence Timur-Barat, support/resistance, moving average, osilator, volume, measured moves |
| Bruna dos Santos, *Technical Indicators Efficacy in Forex Markets* (2021) | Rumus EMA, MACD, RSI, Bollinger Bands, aturan sinyal, strategi tunggal dan kombinasi, metodologi backtesting, keterbatasan |

Isi skill ditulis ulang dengan kalimat sendiri (bukan salinan buku) dan memakai label sumber: `[Nison]`, `[dos Santos]`, `[Skill]` (kerangka buatan skill), `[Tambahan]` (pengetahuan di luar buku).

## Kemampuan

- **Analisis chart** dari screenshot atau data OHLC (CSV/JSON/tabel): struktur pasar, pola candlestick, indikator, confluence, skenario bullish/bearish/netral beserta pembatalnya.
- **Pengenalan pola** reversal, star, continuation, dan doji, dengan kriteria terukur, konteks tren, status konfirmasi, dan potensi false signal.
- **Indikator:** EMA/SMA/WMA, MACD, RSI (30/70 dan 20/80), Bollinger Bands, Stochastic, volume, lengkap dengan rumus dan contoh hitung.
- **Multi-timeframe:** tren utama, tren menengah, momentum jangka pendek, dan deteksi konflik antar-timeframe.
- **Adaptasi pasar:** Forex, Crypto, dan Saham (karakteristik masing-masing, tanpa menganggap satu strategi cocok untuk semua).
- **Backtesting:** alur kerja, metrik (return, win rate, profit factor, drawdown, expectancy, dll.), bias (look-ahead, overfitting), dan skrip Python contoh.
- **Mode tutor:** materi Beginner sampai Advanced, 28 latihan lengkap dengan kunci jawaban dan pembahasan.

## Aturan keselamatan bawaan

- Tidak memberi perintah BUY/SELL, rekomendasi leverage, alokasi modal, atau janji profit.
- Tidak mengarang data harga atau persentase keberhasilan tanpa pengujian.
- Selalu menyebut bukti pendukung, bukti lawan, konfirmasi yang belum ada, dan faktor pembatal.
- Menyatakan bila data tidak cukup untuk menyimpulkan.

## Struktur repositori

```
CandleX/
├── SKILL.md                  instruksi utama AI (mulai dari sini)
├── README.md
├── VERIFICATION-REPORT.md    laporan verifikasi dan keterbatasan sumber
├── references/               basis pengetahuan (pola, indikator, pasar, backtesting, sumber)
├── exercises/                beginner, intermediate, advanced, answer-key (28 soal)
├── templates/                template analisis chart, analisis pasar, laporan backtest
└── scripts/
    └── backtest_example.py   contoh backtest (Python: pandas, numpy)
```

`SKILL.md` berisi peta kapan setiap file referensi dibuka, sehingga agent hanya memuat yang relevan.

## Cara memasang CandleX ke AI agent

Intinya sama di semua agent: agent harus bisa membaca `SKILL.md` dan folder pendampingnya (`references/`, `exercises/`, `templates/`, `scripts/`).
Pastikan nama skill di `SKILL.md` adalah `candlex`.

### 1. Claude Code
Salin folder ke direktori skills:
```bash
# skill pribadi (semua proyek)
mkdir -p ~/.claude/skills && cp -r CandleX ~/.claude/skills/candlex

# atau skill per proyek
mkdir -p .claude/skills && cp -r CandleX .claude/skills/candlex
```
Mulai sesi baru. Agent akan memakai skill saat permintaan cocok dengan deskripsi di `SKILL.md`.

### 2. Claude (web/desktop/mobile) dan produk Claude lain yang mendukung Skills
Kemas folder `CandleX` menjadi ZIP (folder `CandleX` di dalam ZIP, `SKILL.md` di dalamnya), lalu unggah melalui fitur **Skills** di pengaturan akun
(letak menu dapat berbeda antar versi aplikasi dan paket langganan; lihat dokumentasi Anthropic terbaru).

### 3. Agent lain (Cursor, GitHub Copilot, Gemini CLI, OpenAI Codex/ChatGPT, Windsurf, dll.)
Agent-agent ini memakai mekanisme berbeda (rules, instruksi kustom, atau konteks proyek). Pola umumnya:
1. Letakkan folder `CandleX` di dalam repositori/proyek Anda.
2. Tambahkan ke file instruksi agent (mis. file rules atau instruksi proyek milik agent tersebut) kalimat seperti:
   > "Untuk analisis candlestick, indikator teknikal, price action, atau backtesting, ikuti `CandleX/SKILL.md` dan buka file referensi yang ditunjuk di dalamnya sesuai kebutuhan."
3. Bila agent tidak bisa membaca file proyek, tempel isi `SKILL.md` ke instruksi sistem/kustom dan unggah isi `references/` sebagai knowledge.
Nama file dan lokasi instruksi berbeda per agent dan per versi; ikuti dokumentasi resmi agent yang Anda pakai.

### 4. Aplikasi buatan sendiri (API LLM)
Muat `SKILL.md` sebagai system prompt, lalu sediakan isi `references/` lewat retrieval atau alat baca file. Gunakan `scripts/backtest_example.py` hanya bila agent punya lingkungan eksekusi kode.

## Cara menggunakan

Contoh permintaan:

```text
Analisis screenshot chart EUR/USD 1H ini. (lampirkan gambar)
Ini data OHLC CSV BTC/USDT 4H. Jelaskan struktur pasar dan pola candle terakhir.
Jelaskan morning star lalu beri 3 soal latihan beserta pembahasannya.
Hitung RSI periode 5 dari close 100, 102, 101, 103, 104, 102.
Backtest EMA 12/50 + MACD pada data ini dan laporkan profit factor serta drawdown.
Apakah bullish engulfing ini searah dengan tren timeframe 4H?
```

Format hasil analisis chart:
1. Market Information, 2. Market Structure, 3. Candlestick Analysis, 4. Technical Indicators, 5. Confluence,
6. Scenario Analysis (beserta pembatal), 7. Final Technical Interpretation.

### Menjalankan skrip backtest (opsional)
```bash
pip install pandas numpy
python scripts/backtest_example.py                         # data sintetis
python scripts/backtest_example.py --csv data.csv --strategy ema_macd --fast 12 --slow 50 --cost 0.0001
python scripts/backtest_example.py --strategy rsi_bb --long-only
```
CSV minimal memuat kolom `open, high, low, close` (opsional `time, volume`). Skrip memisahkan in-sample dan out-of-sample dan mengeksekusi sinyal di open bar berikutnya.
Pada data sintetis acak, hasil mendekati nol atau negatif setelah biaya; itu wajar.

## Keterbatasan

- Hasil penelitian dos Santos hanya satu sampel (EUR/USD dan GBP/USD, 30 menit, 2016-2020) dan tidak bertahan konsisten antar tahun; jangan digeneralisasi.
- Kedua buku tidak membahas crypto; konten crypto dan sebagian saham adalah pengetahuan tambahan dan harus diuji terpisah.
- Pola candlestick bersifat subjektif dan membutuhkan konfirmasi dan konteks.
- Skrip R pada dokumentasi belum dijalankan; skrip Python hanya diuji pada data sintetis.
- Lihat `VERIFICATION-REPORT.md` untuk rincian cakupan pembacaan sumber dan catatan verifikasi.

## Catatan hak cipta

Repositori ini hanya berisi ringkasan dan penjelasan orisinal. **Jangan menyertakan file PDF kedua buku** di repositori. Nama buku dan penulis disebut hanya sebagai rujukan.
Tambahkan lisensi pilihan Anda (mis. MIT untuk kode, CC BY-NC-SA untuk materi) sebelum dipublikasikan.

## Kontribusi

Issue dan pull request dipersilakan: koreksi rumus, tambahan latihan (angka OHLC sintetis buatan sendiri), atau penyempurnaan adaptasi pasar. Jaga aturan keselamatan di atas.
