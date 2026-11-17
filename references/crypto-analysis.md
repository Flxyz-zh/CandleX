# Adaptasi untuk Cryptocurrency

Daftar isi: 1 Karakter - 2 Volume dan likuiditas - 3 Struktur dan candle - 4 Indikator - 5 Risiko spesifik - 6 Backtesting - 7 Checklist

> **Catatan sumber:** kedua buku tidak membahas crypto (Nison terbit 2001, dos Santos 2021 fokus FX). Seluruh isi file ini adalah **[Tambahan]** kecuali bila ditandai Nison/dos Santos untuk konsep umum.
> Prinsip candle Nison berlaku "di semua pasar dan timeframe" (Nison hlm. 22), tetapi **adaptasi harus diuji terpisah per aset**.

## 1. Karakter [Tambahan]
- Perdagangan **24/7** tanpa penutupan sesi; "close harian" bergantung zona waktu bursa (umumnya UTC). Tidak ada gap sesi seperti saham; gap sering muncul hanya di futures atau antar-venue.
- Volatilitas umumnya tinggi dan berubah cepat; pergerakan ekstrem dapat dipicu berita, likuidasi posisi, atau perubahan sentimen.
- Karakter berbeda drastis antar aset (kapitalisasi besar vs altcoin kecil); perilaku satu aset tidak boleh digeneralisasi.

## 2. Volume dan likuiditas
- Volume terfragmentasi antar bursa; volume dari satu bursa tidak mewakili pasar. Volume palsu/wash trading mungkin terjadi pada venue kecil. Gunakan volume sebagai pendukung, bukan penentu [Nison Bab 15 untuk prinsip volume umum].
- Likuiditas tipis (order book) menyebabkan slippage dan sumbu panjang; shadow panjang pada aset ilikuid kurang informatif dibanding aset likuid.

## 3. Struktur dan candle
- Karena tidak ada sesi open/close resmi, aturan fleksibel seperti pada FX (Nison hlm. 62-65) relevan untuk star dan engulfing.
- Window/gap Nison hampir tidak terjadi di spot; jangan menyebut "gap" tanpa data futures/penutupan yang jelas.
- Shadow panjang (wicks) umum saat likuidasi; periksa apakah ditutup (close) kembali di dalam level (konsep spring/upthrust, Nison hlm. 199-205).
- Tren sering bergerak impulsif; breakout palsu sering terjadi; tunggu close dan retest [Skill].

## 4. Indikator
- Parameter populer (EMA 12/26/50/200, RSI 14, MACD 12-26-9, BB 20/2) umum tersedia, tetapi **tidak ada bukti dari kedua buku** bahwa parameter tersebut optimal untuk crypto.
- Volatilitas tinggi membuat RSI bertahan lama di zona ekstrem dan BB sering menempel band; baca divergence dan struktur, bukan level mentah.
- Skala volatilitas berubah antar rezim; gunakan ATR/BB width untuk menormalkan.

## 5. Risiko spesifik [Tambahan]
Risiko bursa/kustodi, regulasi, likuidasi berantai, funding rate untuk perpetual futures, spread dan fee berbeda antar venue. Skill tidak menyarankan leverage atau trading dana nyata; gunakan data historis dan paper trading.

## 6. Backtesting
Sertakan fee taker/maker, slippage, funding cost (untuk perpetual), dan survivorship bias (aset yang hilang dari daftar). Uji per aset dan per rezim volatilitas; hasil Bitcoin tidak berlaku untuk altcoin.

## 7. Checklist
Aset dan bursa sumber data; zona waktu candle; volume reliabel?; struktur; apakah wick ditutup kembali; volatilitas (BB width); berita/event; skenario + pembatal; jangan generalisasi antar aset.
