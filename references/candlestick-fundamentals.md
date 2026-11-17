# Dasar Candlestick (Beginner)

Daftar isi: 1 Anatomi - 2 Rumus - 3 Klasifikasi satu candle - 4 Psikologi - 5 Doji - 6 Timeframe -
7 Contoh hitung - 8 Kesalahan umum - 9 Kelebihan dan keterbatasan

Label: **[Nison]** dari buku Nison (Bab 3, hlm. 23-29), **[dos Santos]** dari tesis (Bab 2, hlm. 15-16; Bab 3, hlm. 22),
**[Skill]** heuristik/ambang buatan skill ini, bukan aturan baku buku.

## 1. Anatomi satu candle

Setiap candle merangkum satu periode (menit, jam, hari, dst.) dengan empat harga: **Open (O), High (H),
Low (L), Close (C)**. Data yang sama dipakai bar chart Barat; candle hanya menampilkannya lebih visual.
[Nison hlm. 23-25; dos Santos hlm. 15, 22]

| Bagian | Definisi | Catatan |
|---|---|---|
| **Real body** | Rentang antara Open dan Close | Putih/hijau (kosong) bila C > O; hitam/merah (terisi) bila C < O. Nison menyebutnya "inti pergerakan harga". |
| **Upper shadow** | Garis di atas real body sampai High | Puncak shadow = High periode |
| **Lower shadow** | Garis di bawah real body sampai Low | Ujung bawah = Low periode |
| **Shaven head / shaven bottom** | Tidak ada upper / lower shadow | Close (atau Open) tepat di High / Low |
| **Range** | H - L | Ukuran total ayunan periode |

Warna real body bisa dikonfigurasi di platform; tentukan dulu arti warna di chart yang dibaca.

## 2. Rumus [Skill]

```
body          = |C - O|
upper_shadow  = H - max(O, C)
lower_shadow  = min(O, C) - L
range         = H - L
body_ratio    = body / range          (jika range = 0, candle "flat": tidak informatif)
arah          = bullish jika C > O, bearish jika C < O, netral jika C ~ O
```

Selalu hitung dulu, baru beri nama pola. Jangan mengklasifikasi hanya "dari bentuk visual" bila angka OHLC ada.

## 3. Klasifikasi satu candle [Skill: ambang heuristik]

Ambang berikut adalah titik awal praktis; sesuaikan dengan volatilitas instrumen dan timeframe. Nison menekankan
fleksibilitas definisi (Bab 1 "Some Cautions": definisi pola bisa berbeda antar sumber).

| Jenis | Ciri terukur (heuristik) | Makna menurut Nison |
|---|---|---|
| Long white / long black | body_ratio besar (>= ~0,6-0,7), shadow kecil | Satu pihak dominan: bulls (putih) atau bears (hitam) menguasai sesi |
| Spinning top | body kecil (<= ~0,25-0,3 dari range), shadow ada di dua sisi | Momentum sebelumnya melemah; warna body tidak penting |
| Doji | O ~ C (body_ratio <= ~0,05-0,1) | Ketidakpastian; sinyal reversal terutama setelah kenaikan |
| Bentuk hammer / hanging man | body kecil di ujung atas range, lower shadow >= 2x body, upper shadow tidak ada atau sangat kecil | Konteks tren menentukan nama |
| Bentuk shooting star / inverted hammer | body kecil di ujung bawah range, upper shadow panjang, lower shadow tidak ada/kecil | Konteks tren menentukan nama |
| Belt-hold | Candle panjang yang open di (hampir) low atau high sesi | Lihat patterns |
| High-wave | body kecil dengan upper dan lower shadow sama-sama panjang | Pasar bimbang; non-doji dari long-legged doji |

Kriteria "lower shadow >= 2x body" untuk hammer/hanging man berasal dari Nison (Bab 4, hlm. 34-38). Ambang lain di tabel
ini adalah [Skill].

## 4. Psikologi dan makna [Nison]

- Real body panjang = aksi satu arah; real body memendek = momentum sebelumnya mungkin melemah. Sinyal ini bisa
  muncul dalam satu sesi, lebih cepat dari bar chart (Bab 3, hlm. 26-27).
- **Open dan close** dianggap titik paling emosional hari itu. Open adalah "kemudi" sesi; close dipakai banyak
  alat Barat (MA, osilator) dan konfirmasi breakout (hlm. 28-29).
- Shadow menunjukkan penolakan harga: upper shadow panjang = bears menolak harga atas; lower shadow panjang = bulls
  menolak harga bawah (juga Bab 10, hlm. 187-192 tentang cluster shadow).
- Nama pola membawa citra emosional (evening star = bearish, morning star = bullish).

## 5. Doji ringkas

Doji = open dan close sama atau nyaris sama. Dibahas lengkap di `candlestick-patterns.md` (bagian Doji).
Kunci: doji hanya bermakna reversal bila ada tren yang bisa dibalik; di dalam range sideways ia tidak banyak berarti
[Nison Bab 8, hlm. 155-170].

## 6. Timeframe

Candle dapat dibuat pada timeframe apa pun: 1 menit sampai bulanan. Pada candle 5 menit, Open adalah harga pertama
dalam 5 menit itu dan Close harga terakhirnya. Timeframe pendek (5/15 menit) bergerak cepat dan berisik; menengah
(1H/4H) lebih lambat; panjang (harian ke atas) butuh modal/ketahanan lebih besar [dos Santos hlm. 15-16].
Pilihan timeframe mengubah makna sinyal; lihat `multi-timeframe-analysis.md`.

## 7. Contoh hitung (sintetis)

Candle EUR/USD sintetis: O = 1,1000; H = 1,1050; L = 1,0980; C = 1,1040.

```
body = 0,0040   upper_shadow = 0,0010   lower_shadow = 0,0020   range = 0,0070
body_ratio = 0,0040 / 0,0070 = 0,571   arah = bullish
```
Body sedang-besar, bulls menguasai sesi (close dekat high), ada penolakan harga bawah moderat. Bukan doji; bukan
hammer (lower shadow = 0,5x body, kurang dari 2x).

## 8. Kesalahan umum

1. Menyebut "hammer" hanya dari bentuk tanpa memeriksa tren sebelumnya (bentuk sama, nama dan makna beda).
2. Menganggap warna body menentukan sinyal pada spinning top/doji/hammer (warna tidak penting di sana).
3. Menilai candle yang belum close (bentuk berubah sampai periode selesai).
4. Mengabaikan ukuran relatif: body "besar" selalu relatif terhadap candle di sekitarnya.
5. Memakai aturan gap pada FX spot tanpa sadar bahwa open dan close tidak resmi (aturan lebih longgar).

## 9. Kelebihan dan keterbatasan

Kelebihan: lebih kaya dari line chart, sinyal visual cepat, memperlihatkan pergulatan buyer-seller
[dos Santos hlm. 15; Nison hlm. 23]. Keterbatasan: subjektif (definisi pola bervariasi), butuh candle close, tidak
memberi target harga, dan tidak menjamin arah. Paling berguna bila digabung struktur harga dan alat Barat (convergence).
