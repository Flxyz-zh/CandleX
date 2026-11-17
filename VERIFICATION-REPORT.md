# Source Mapping and Verification Report

Laporan ini menjelaskan apa yang berhasil diintegrasikan ke skill, bagaimana dicek, dan **keterbatasan** proses serta sumber.

## 1. Cakupan pembacaan sumber (jujur tentang apa yang dibaca)

| Sumber | Dibaca penuh | Dibaca sebagian/terarah | Tidak diproses mendalam |
|---|---|---|---|
| **dos Santos** (141 hlm. PDF, teks dapat diekstrak) | Bab 2-7 (konsep forex, random walk, fundamental/teknikal, indikator dan rumus, dataset, kerangka Quantstrat, semua aturan sinyal, hasil 2020, hasil 2016-2020, kesimpulan, keterbatasan); abstrak; daftar isi | Lampiran A (listing kode dan plot hanya diintip: judul/struktur), Lampiran B (judul dan baris awal tabel sinyal berlawanan) | Daftar pustaka; gambar/plot equity curve (tidak dibaca sebagai gambar) |
| **Nison** (298 hlm. PDF hasil OCR, teks dapat diekstrak) | Bab 2 (sejarah) dan Bab 3 (konstruksi); daftar isi; Bab 12-14 (retracement, moving average, osilator) dan potongan Bab 15 | Bab 4-9 (ekstraksi kriteria/definisi per pola dengan pencarian terarah dan cuplikan awal tiap halaman); Bab 10-11, 15-17 dan "Some Cautions" (cuplikan awal tiap halaman) | Pembahasan detail contoh chart per halaman; Glosarium A/B; bibliografi; indeks |

Konsekuensi: definisi dan kriteria pola utama diverifikasi terhadap teks; sebagian detail kecil pola (mis. syarat open Three Black Crows, rincian Three Mountains/Rivers, abandoned baby) ditulis dari ringkasan teks yang dibaca dan ditandai dengan bahasa hati-hati atau label **[Tambahan]**.
Pembaca yang membutuhkan presisi kutipan sebaiknya membuka halaman rujukan buku.

## 2. Kendala teknis yang memengaruhi nomor halaman
- PDF Nison kehilangan sejumlah halaman, sehingga selisih nomor halaman PDF terhadap nomor cetak berubah (dari sekitar +11 hingga 0). Skill memakai **halaman awal bagian menurut daftar isi buku** atau nomor cetak pada header. Kutipan bertanda "sekitar" bisa meleset sekitar +/- 2 halaman.
- dos Santos: halaman PDF = halaman cetak + 24 (konsisten).

## 3. Quality control (14 poin permintaan)

| # | Pemeriksaan | Status | Bukti/catatan |
|---|---|---|---|
| 1 | Seluruh kategori materi kedua buku dipetakan | Terpenuhi | `references/source-references.md` bagian 3-4 memetakan 14 kategori Nison dan 14 kategori dos Santos ke file skill |
| 2 | Tidak ada indikator utama terlewat | Terpenuhi | EMA, SMA, WMA, MACD, RSI, Bollinger, Stochastic, MA oscillator, volume: `technical-indicators.md` |
| 3 | Pola candlestick utama dijelaskan | Terpenuhi | Semua pola dalam daftar proyek ada di `candlestick-patterns.md` (hammer, hanging man, engulfing, dark-cloud, piercing, harami/harami cross, tweezers, belt-hold, three black crows, three white soldiers, counterattack, upside-gap two crows, three mountains/rivers, dumpling/frypan, tower, morning/evening star, doji stars, shooting star, inverted hammer, windows, tasuki, three methods, separating lines, gapping side-by-side white lines, semua jenis doji, tri-star) |
| 4 | Reversal vs continuation benar | Terpenuhi | Tabel klasifikasi di `candlestick-patterns.md` bagian 2; latihan R3 |
| 5 | Formula indikator konsisten | Terpenuhi dengan catatan | Hitung ulang EMA, RSI, BB, MACD, stochastic dengan Python; selisih definisi RSI/MACD di sumber dicatat (`technical-indicators.md` bagian 8) |
| 6 | Contoh hitung benar | Terpenuhi | Semua angka latihan dan contoh dihitung ulang dalam skrip verifikasi (B1, B4, P2 persentase penetrasi, I1-I4, T1-T4). `scripts/backtest_example.py` diuji: `ema()` = [nan, nan, 21,0, 22,0, 23,5]; `rsi(n=5)` = 62,5; `bollinger(n=5)` = 14,828 / 12,0 / 9,172 |
| 7 | Contoh analisis tidak bertentangan dengan definisi | Terpenuhi | Contoh pola sintetis diperiksa terhadap kriteria (engulfing, dark-cloud, morning star, rising three methods, window) |
| 8 | Latihan memiliki pembahasan | Terpenuhi | 28 soal, 28 entri di `answer-key.md` dengan jawaban, penjelasan, alasan, kesalahan umum |
| 9 | Tidak ada informasi dikarang | Terpenuhi dengan catatan | Label **[Nison]/[dos Santos]/[Skill]/[Tambahan]**; ambang numerik non-buku diberi label [Skill]; lihat bagian 4 |
| 10 | Setiap file berguna (tidak ada kosong/placeholder) | Terpenuhi | 22 file, terkecil sekitar 1,3 KB (template); pencarian "TODO/TBD/placeholder" hanya cocok palsu pada kata "metodologi" |
| 11 | Batasan penelitian dan risiko dijelaskan | Terpenuhi | `SKILL.md` bagian 0; `indicator-combinations.md` bagian 4-5; `backtesting-methodology.md` bagian 7 |
| 12 | Dapat dipakai untuk forex, crypto, saham | Terpenuhi dengan catatan | File pasar terpisah; konten crypto dan sebagian saham adalah **[Tambahan]** karena tidak ada di kedua buku |
| 13 | Skill berfungsi tanpa PDF | Terpenuhi | Tidak ada instruksi yang mengharuskan membuka PDF; semua referensi di dalam folder |
| 14 | Semua file saling terhubung | Terpenuhi | `SKILL.md` memuat peta file; pemeriksaan otomatis path rujukan: semua ada (satu rujukan ke `VERIFICATION-REPORT.md` terpenuhi dengan file ini) |

## 4. Hal yang perlu diwaspadai (catatan verifikasi)

1. **Ambang numerik pada klasifikasi candle** (doji <= ~0,05-0,1; spinning top <= ~0,25-0,3; marubozu-like >= ~0,6-0,7) adalah heuristik skill, bukan aturan buku. Hanya "lower shadow >= 2x body" untuk hammer/hanging man yang eksplisit dari Nison.
2. **Rubrik confluence** (kategori independen, batas Moderate untuk sinyal melawan timeframe atas) adalah kerangka skill yang terinspirasi prinsip convergence Nison; bukan klasifikasi dari buku.
3. **Rumus RSI dalam tesis** tercetak berbasis hitungan hari naik/turun (biner); skill memakai versi besaran (Nison/Wilder) dan menunjukkan selisih angkanya pada latihan I2 (62,5 vs 60,0).
4. **Aturan short RSI dos Santos** (RSI_{t-1} < 70 dan RSI_t > 70) dilaporkan apa adanya dan ditandai tampak tidak lazim.
5. **Ketidakselarasan internal tesis** dicatat (27 vs 12 kombinasi; PF 0,99 dengan total gain positif; nilai alpha EMA-20 0,09624 vs 2/21 = 0,09524; selisih kecil gross vs total).
6. **Penjelasan MA oscillator Nison** ambigu urutan pengurangan; skill memakai MA pendek dikurangi MA panjang.
7. **Skrip backtest** hanya diuji pada data sintetis acak (hasil mendekati nol/negatif setelah biaya, sesuai harapan). Tidak divalidasi terhadap data pasar nyata atau terhadap Quantstrat. **Contoh R tidak dijalankan** (R tidak diuji di lingkungan ini).
8. **Data pasar:** angka pasar forex 2016 ($5,3 triliun/hari) berasal dari tesis (BIS 2016) dan sudah usang; jangan dipakai sebagai angka terkini.

## 5. Keterbatasan sumber
- **dos Santos:** dua pasangan mata uang, satu timeframe (30 menit), 2016-2020, tanpa leverage, ukuran order tetap, biaya tetap, hanya empat indikator, tanpa uji out-of-sample formal atau uji signifikansi; jumlah trade kombinasi sangat kecil (13-29 trade untuk beberapa strategi); hasil 2020 tidak bertahan di tahun lain. Penulis sendiri menyatakan sampel kecil dan perlunya data lebih panjang dan faktor fundamental.
- **Nison:** orientasi pasar AS; tidak ada statistik keberhasilan pola; definisi pola bervariasi antar sumber dan subjektif; terbit 2001 (tidak mencakup crypto dan perdagangan algoritmik modern).
- **Kedua buku:** tidak membahas crypto; tidak membuktikan bahwa strategi yang sama akan berhasil di instrumen/periode lain.

## 6. Batasan skill
Hanya edukasi dan analisis historis. Tidak ada rekomendasi transaksi, alokasi modal, atau leverage. Skill tidak menggantikan nasihat profesional berlisensi.
