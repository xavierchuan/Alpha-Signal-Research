import os
import pandas as pd
import yfinance as yf

def load_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Download raw data from Yahoo Finance"""
    print(f"📥 Downloading data for {ticker} from {start} to {end} ...")
    df = yf.download(ticker, start=start, end=end)

    # 如果是多级列（MultiIndex），需要扁平化
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0].lower() for col in df.columns]

    else:
        df.columns = [col.lower() for col in df.columns]

    # 只保留需要的列
    keep_cols = ["close", "high", "low", "open", "volume"]
    df = df[keep_cols].copy()

    # 添加 price 列（= close）
    df["price"] = df["close"]

    return df


def load_or_process_data(ticker: str, start: str, end: str, cache_dir="data/processed") -> pd.DataFrame:
    """Load processed data if exists, otherwise download and save"""
    os.makedirs(cache_dir, exist_ok=True)
    fname = f"{ticker}_{start}_{end}.csv"
    fpath = os.path.join(cache_dir, fname)

    if os.path.exists(fpath):
        print(f"📂 Loading cached data: {fpath}")
        df = pd.read_csv(fpath, parse_dates=[0], index_col=0)
    else:
        df = load_data(ticker, start, end)
        df.to_csv(fpath)
        print(f"💾 Saved processed data to {fpath}")

    # 确保数值列类型正确
    for col in ["price", "close", "high", "low", "open", "volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df