# Adaptasi untuk Forex

Daftar isi: 1 Karakter pasar - 2 Pasangan mata uang - 3 Sesi dan volatilitas - 4 Spread dan biaya - 5 Berita - 6 Dampak pada candlestick/indikator - 7 Random walk dan teknikal vs fundamental - 8 Checklist

Label: **[dos Santos]** (halaman cetak), **[Nison]**, **[Tambahan]**.

## 1. Karakter pasar
- Foreign Exchange adalah pasar terbesar dan paling likuid; rata-rata transaksi harian ±$5,3 triliun menurut laporan BIS 2016 (dikutip dos Santos hlm. 9; angka lama, cek data terbaru bila perlu).
- Tidak ada lokasi/bursa terpusat; jaringan bank (interbank) dan market maker global; buka 24 jam, 5,5 hari seminggu (hlm. 9-10).
- Sejarah ringkas: gold standard, Bretton Woods (1944), 1971 mengambang bebas, era modern sejak 1973 [dos Santos hlm. 9-10].
- Mata uang selalu berpasangan: beli base currency dan jual quote currency (atau sebaliknya). Jenis order dasar: market, stop-loss, take-profit (hlm. 11).
- Uptrend pasangan = uptrend base currency dan downtrend quote currency (hlm. 17).

## 2. Pasangan mata uang
- USD adalah mata uang paling banyak diperdagangkan (> 85% pangsa), diikuti EUR (37%), JPY (16%), GBP (15%) [dos Santos hlm. 37, mengutip BIS; pangsa dihitung dari total 200% karena dua sisi].
- **EUR/USD** pasangan paling likuid; kuotasi USD per EUR. **GBP/USD** ketiga terbesar, likuiditas lebih rendah daripada EUR/USD dan USD/JPY, cenderung bergerak tajam (hlm. 37).
- Pengelompokan **Major / Minor / Exotic** adalah [Tambahan]: Major = pasangan dengan USD dan mata uang besar; Minor (cross) = tanpa USD (mis. EUR/GBP); Exotic = satu mata uang besar dengan mata uang negara berkembang; spread dan volatilitas Exotic umumnya lebih besar.
- Karakter berbeda per pasangan (rentang harian, reaksi terhadap berita); pada data 2020 dos Santos mendapati hasil berbeda untuk EUR/USD dan GBP/USD (RSI 20/80 profit factor di atas 1 hanya untuk EUR/USD; penulis menyimpulkan parameter lebar lebih cocok EUR/USD, hlm. 68), tetapi dengan satu tahun data ini tidak membuktikan parameter terbaik. Jangan menyamakan parameter antar-pasangan; uji terpisah.

## 3. Sesi dan volatilitas [Tambahan]
Sesi Asia/Tokyo, Eropa/London, Amerika/New York; likuiditas dan volatilitas biasanya tertinggi saat sesi London dan New York overlap. Pergerakan di luar jam likuid bisa sempit/bergerigi. Sesuaikan pembacaan: pola pada sesi tipis lebih mudah palsu.

## 4. Spread dan biaya
Biaya transaksi nyata di FX adalah spread (selisih bid-ask), ditambah slippage dan swap/rollover untuk posisi menginap. Data dos Santos memakai harga ask dan biaya transaksi tetap (hlm. 36, 41). Dalam backtest, sertakan spread yang realistis, apalagi di timeframe kecil.

## 5. Berita dan analisis fundamental
Analisis fundamental menilai indikator makro (GDP, inflasi, pengangguran, neraca pembayaran, PMI) dan pasar aset/politik [dos Santos hlm. 13]. Kalender ekonomi memberi label dampak rendah/sedang/tinggi (kuning/oranye/merah). Berita dapat mengacaukan pola teknikal; dos Santos menekankan kesulitan trading berita (kecepatan, interpretasi) dan menyimpulkan perlunya menggabungkan teknikal dan fundamental (hlm. 13-14, 88). Tandai pada analisis: "ada rilis berita berdampak tinggi dalam N jam" bila diketahui.

## 6. Dampak pada candlestick dan indikator
- **Open/close tidak resmi:** Nison mencatat di pasar FX open dan close tidak resmi sehingga star lebih fleksibel dan engulfing dengan open = close sebelumnya tetap diterima (Bab 5 hlm. 62-65; Bab 14 hlm. 226-229 contoh engulfing FX). Gap (window) lebih jarang pada hari kerja; gap akhir pekan masih mungkin.
- **Volume:** umumnya tick volume broker, bukan volume pasar [Tambahan].
- **Tren:** dos Santos menemukan kinerja strategi indikator sangat terkait arah tren tahunan; evaluasi regime sebelum memercayai strategi.
- Nison menyebut EMA 9 populer di kalangan trader FX (hlm. 221-222).

## 7. Random walk vs analisis teknikal
Random Walk Theory (Bachelier; Malkiel) menyatakan harga tak terprediksi dan independen dari masa lalu; kritik analis: tidak realistis semua gerakan acak (Murphy). Dow Theory sebagai dasar teknikal modern (hlm. 11-14). Sikap skill: teknikal dipakai untuk **deskripsi struktur dan manajemen skenario**, bukan klaim prediksi pasti.

## 8. Checklist analisis FX
Instrumen dan konvensi kuotasi; timeframe; sesi; spread; berita; struktur; pola (aturan longgar open/close); indikator; MTF; skenario + pembatal.
