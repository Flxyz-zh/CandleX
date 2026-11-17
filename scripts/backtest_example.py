#!/usr/bin/env python3
"""
backtest_example.py - Contoh backtesting edukatif (simulasi, BUKAN rekomendasi).

Fitur:
  * Membaca OHLC dari CSV (kolom: time,open,high,low,close[,volume]) atau membuat
    data sintetis bila --csv tidak diberikan.
  * Indikator: EMA, MACD (12,26,9), RSI (periode 14, versi rata-rata sederhana
    seperti di Nison / versi Wilder opsional), Bollinger Bands (20, 2 SD populasi).
  * Strategi contoh: EMA fast/slow crossover + filter MACD (mengikuti ide
    kombinasi EMA & MACD pada penelitian dos Santos, 2021) atau RSI+BB.
  * Eksekusi di OPEN bar berikutnya setelah sinyal (menghindari look-ahead bias).
  * Biaya: spread+slippage per transaksi dalam satuan harga.
  * Metrik: total return, win rate, profit factor, max drawdown, jumlah trade,
    rata-rata win/loss, expectancy, payoff ratio.
  * Pemisahan in-sample / out-of-sample (--oos-fraction).

Contoh:
  python backtest_example.py                       # data sintetis
  python backtest_example.py --csv data.csv --strategy ema_macd --fast 12 --slow 50
  python backtest_example.py --strategy rsi_bb --cost 0.0001

Hanya untuk edukasi dan simulasi dengan dana virtual. Hasil historis tidak
menjamin hasil di masa depan.
"""
import argparse
import math
import random
import sys

import numpy as np
import pandas as pd


# ---------------------------------------------------------------- indikator
def ema(s: pd.Series, n: int) -> pd.Series:
    """EMA dengan seed SMA n pertama dan alpha = 2/(n+1) (dos Santos, pers. 3.1-3.4)."""
    alpha = 2.0 / (n + 1)
    out = pd.Series(np.nan, index=s.index)
    if len(s) < n:
        return out
    out.iloc[n - 1] = s.iloc[:n].mean()
    for i in range(n, len(s)):
        out.iloc[i] = alpha * s.iloc[i] + (1 - alpha) * out.iloc[i - 1]
    return out


def macd(close: pd.Series, fast=12, slow=26, sig=9):
    line = ema(close, fast) - ema(close, slow)
    signal = ema(line.dropna(), sig).reindex(close.index)
    return line, signal, line - signal


def rsi(close: pd.Series, n=14, wilder=False) -> pd.Series:
    """RSI = 100 - 100/(1+RS). wilder=False: rata-rata sederhana tiap jendela
    (seperti penjelasan Nison, hlm. 226-227). wilder=True: smoothing Wilder."""
    d = close.diff()
    gain = d.clip(lower=0)
    loss = (-d).clip(lower=0)
    if wilder:
        ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
        al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    else:
        ag = gain.rolling(n).mean()
        al = loss.rolling(n).mean()
    rs = ag / al.replace(0, np.nan)
    out = 100 - 100 / (1 + rs)
    return out.where(al != 0, 100.0)


def bollinger(close: pd.Series, n=20, k=2.0):
    mid = close.rolling(n).mean()
    sd = close.rolling(n).std(ddof=0)  # SD populasi (1/N), sesuai pers. 3.15
    return mid + k * sd, mid, mid - k * sd


# ----------------------------------------------------------- data sintetis
def synthetic(n=6000, seed=7, start=1.10, vol=0.0006):
    rnd = random.Random(seed)
    price = start
    rows = []
    t = pd.Timestamp("2020-01-01")
    for _ in range(n):
        o = price
        c = o + rnd.gauss(0, vol)
        h = max(o, c) + abs(rnd.gauss(0, vol / 2))
        l = min(o, c) - abs(rnd.gauss(0, vol / 2))
        rows.append((t, o, h, l, c, rnd.randint(100, 1000)))
        price = c
        t += pd.Timedelta(minutes=30)
    return pd.DataFrame(rows, columns=["time", "open", "high", "low", "close", "volume"])


# ---------------------------------------------------------------- sinyal
def signals_ema_macd(df, fast, slow):
    c = df["close"]
    f, s = ema(c, fast), ema(c, slow)
    m, sg, _ = macd(c)
    long_ = (f > s) & (m > 0) & (sg > 0)
    short_ = (f < s) & (m < 0) & (sg < 0)
    return long_, short_


def signals_rsi_bb(df, lo=30, hi=70):
    c = df["close"]
    r = rsi(c)
    up, _, dn = bollinger(c)
    long_ = (r < lo) & (c < dn)
    short_ = (r > hi) & (c > up)
    return long_, short_


# --------------------------------------------------------------- engine
def run(df, long_sig, short_sig, cost=0.0, allow_short=True, start_equity=10_000.0, units=10_000):
    """Posisi berubah pada OPEN bar t+1 berdasarkan sinyal bar t (tanpa look-ahead).
    Sinyal 'long' membuka/menjaga long; sinyal berlawanan menutup dan (opsional) membalik.
    Setiap round-trip dikenai biaya 2 x 'cost' (masuk + keluar, satuan harga)."""
    o = df["open"].values
    pos = 0
    entry = 0.0
    trades = []
    equity = [start_equity]
    eq = start_equity
    for i in range(len(df) - 1):
        want = pos
        if long_sig.iloc[i]:
            want = 1
        elif short_sig.iloc[i]:
            want = -1 if allow_short else 0
        px = o[i + 1]
        if want != pos:
            if pos != 0:
                pnl = (px - entry) * pos * units - 2 * cost * units  # biaya masuk + keluar
                trades.append(pnl)
                eq += pnl
            if want != 0:
                entry = px
            pos = want
        mark = eq
        if pos != 0:
            mark = eq + (df["close"].iloc[i + 1] - entry) * pos * units
        equity.append(mark)
    return trades, pd.Series(equity)


def metrics(trades, equity, start_equity):
    n = len(trades)
    wins = [t for t in trades if t > 0]
    losses = [t for t in trades if t < 0]
    gp, gl = sum(wins), -sum(losses)
    peak = equity.cummax()
    dd = ((peak - equity) / peak).max()
    out = {
        "trades": n,
        "total_return_%": (equity.iloc[-1] / start_equity - 1) * 100,
        "win_rate_%": (len(wins) / n * 100) if n else float("nan"),
        "profit_factor": (gp / gl) if gl > 0 else (math.inf if gp > 0 else float("nan")),
        "max_drawdown_%": dd * 100,
        "avg_win": (gp / len(wins)) if wins else 0.0,
        "avg_loss": (-gl / len(losses)) if losses else 0.0,
        "expectancy_per_trade": (sum(trades) / n) if n else float("nan"),
    }
    out["payoff_ratio"] = (out["avg_win"] / -out["avg_loss"]) if out["avg_loss"] < 0 and out["avg_win"] else float("nan")
    return out


def report(title, m):
    print(f"\n== {title} ==")
    for k, v in m.items():
        print(f"{k:>22}: {v:,.4f}" if isinstance(v, float) else f"{k:>22}: {v}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv")
    ap.add_argument("--strategy", choices=["ema_macd", "rsi_bb"], default="ema_macd")
    ap.add_argument("--fast", type=int, default=12)
    ap.add_argument("--slow", type=int, default=50)
    ap.add_argument("--cost", type=float, default=0.0001, help="biaya per sisi (satuan harga)")
    ap.add_argument("--long-only", action="store_true")
    ap.add_argument("--oos-fraction", type=float, default=0.3, help="porsi data akhir untuk out-of-sample")
    a = ap.parse_args(argv)

    df = pd.read_csv(a.csv) if a.csv else synthetic()
    df.columns = [c.lower() for c in df.columns]
    need = {"open", "high", "low", "close"}
    if not need.issubset(df.columns):
        sys.exit(f"CSV harus memuat kolom {sorted(need)}")

    cut = int(len(df) * (1 - a.oos_fraction))
    for name, part in (("IN-SAMPLE", df.iloc[:cut].reset_index(drop=True)),
                       ("OUT-OF-SAMPLE", df.iloc[cut:].reset_index(drop=True))):
        if a.strategy == "ema_macd":
            ls, ss = signals_ema_macd(part, a.fast, a.slow)
        else:
            ls, ss = signals_rsi_bb(part)
        tr, eq = run(part, ls, ss, cost=a.cost, allow_short=not a.long_only)
        report(f"{a.strategy} - {name} ({len(part)} bar)", metrics(tr, eq, 10_000.0))
    print("\nCatatan: simulasi edukatif. Hasil historis bukan jaminan hasil masa depan. "
          "Data sintetis acak tidak memiliki edge; hasil mendekati nol/negatif setelah biaya itu wajar.")


if __name__ == "__main__":
    main()
