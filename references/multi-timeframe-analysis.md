# Analisis Multi-Timeframe (MTF)

Daftar isi: 1 Konsep - 2 Prosedur top-down - 3 Tabel konflik - 4 Contoh - 5 Batasan data - 6 Kesalahan umum

Label: **[dos Santos]** hlm. 15-17 (timeframe, tren), **[Nison]** (candle bisa dipakai di timeframe apa pun, hlm. 22), **[Skill]** (prosedur), **[Tambahan]**.

## 1. Konsep

- Timeframe menentukan berapa lama waktu dalam satu candle. Timeframe populer pada FX: 5, 15, 30 menit, 1 jam, 4 jam, 12 jam, harian, mingguan, bulanan [dos Santos hlm. 16].
- Timeframe pendek (5/15 menit) bergerak cepat dan berisik; menengah (1H/4H) lebih lambat; timeframe panjang membutuhkan modal/ketahanan lebih besar [dos Santos hlm. 16].
- Nison: candle dipakai pada mingguan (hedger), harian (swing/menengah), dan intraday (swing/day trader); alat yang sama berlaku di semua timeframe (hlm. 22).
- Tren ada pada beberapa tingkat (primer, sekunder, minor; Dow Theory, dos Santos hlm. 14). Sinyal di timeframe rendah adalah bagian dari struktur timeframe lebih tinggi.

Contoh pembagian [Skill]: **Higher TF** 1D dan 4H (tren utama, level besar); **Middle TF** 1H (struktur menengah, pullback); **Lower TF** 15M dan 5M (momentum jangka pendek, timing pola).
Rasio antar-TF umumnya 3-6x agar berbeda informasi.

## 2. Prosedur top-down [Skill]

1. **Higher TF:** tentukan tren utama (HH-HL / LH-LL / sideways), level S/R besar, posisi harga terhadap EMA 50/200 jika ada.
2. **Middle TF:** apakah harga sedang pullback, breakout, atau retest terhadap level TF atas? Cari struktur dan pola yang bermakna.
3. **Lower TF:** momentum jangka pendek (RSI/MACD), pola candle terakhir, apakah sudah close dan terkonfirmasi.
4. **Bandingkan arah:** searah (aligned), konflik (berlawanan), atau netral.
5. **Nilai pola:** apakah pola searah atau berlawanan dengan tren utama? Counter-trend = lebih rentan gagal; beri label dan batasi confluence maksimum Moderate.
6. **Tulis kesimpulan per TF**, lalu satu kalimat ringkasan keselarasan. Jika TF yang tersedia tidak cukup (mis. hanya 15M), katakan konteks TF atas tidak bisa dinilai.

## 3. Tabel konflik

| Higher TF | Middle TF | Lower TF | Pembacaan |
|---|---|---|---|
| Bullish | Bullish | Bullish | Searah. Pola bullish di TF rendah = kelanjutan; kewaspadaan: overextended di resistance TF atas |
| Bullish | Pullback bearish | Bearish | Konflik jangka pendek: koreksi dalam tren naik (umum) atau awal pembalikan (butuh bukti: patah struktur TF menengah) |
| Bullish | Sideways | Mixed | Konsolidasi; tunggu breakout/retest; pola di tepi range saja |
| Bearish | Rally bullish | Bullish | Rally counter-trend; level LH/resistance TF atas menentukan; pola bullish TF kecil dinilai lemah |
| Sideways | Trending | Trending | TF atas mengatur batas range; sinyal tengah range dikurangi bobotnya |
| Konflik di semua TF | | | Conflicting Signals; skenario netral |

## 4. Contoh (sintetis)

1D: HH-HL, harga di atas EMA 50 dan 200. 4H: harga turun ke zona support sebelumnya (HL 4H) dengan body kecil. 1H: bullish engulfing di zona itu setelah 5 candle turun.
15M: RSI keluar dari < 30, MACD histogram mulai positif. **Pembacaan:** pola bullish searah tren 1D dan terjadi di support 4H (selaras). **Pembatal analitis:** close 4H di bawah HL tersebut (struktur bullish patah).
Sebaliknya bila 1D bearish, pola yang sama adalah counter-trend: beri label Moderate maksimum.

## 5. Batasan data

- Jangan menyimpulkan tren utama dari timeframe kecil saja; tulis "tren TF atas tidak dapat dinilai".
- Pastikan zona waktu dan penutupan candle sama antar-TF (FX: batas hari bergantung broker; saham: sesi bursa; crypto: UTC).
- Candle TF atas yang belum close dapat berubah; tandai "sedang berlangsung".

## 6. Kesalahan umum

1. Mengganti timeframe sampai menemukan sinyal yang diinginkan (cherry-picking).
2. Menganggap semua TF sama penting; TF atas biasanya mendefinisikan level besar.
3. Mengabaikan konflik demi narasi tunggal.
4. Memakai parameter indikator identik di semua TF tanpa memahami konsekuensinya (EMA 200 pada 5M ≠ pada 1D).
