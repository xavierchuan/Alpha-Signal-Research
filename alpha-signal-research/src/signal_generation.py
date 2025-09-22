import pandas as pd


def generate_signals(df: pd.DataFrame, fast: int = 10, slow: int = 30) -> pd.DataFrame:
    """
    Generate SMA crossover trading signals.
    Adds: 'sma_fast', 'sma_slow', 'position'
    """
    out = df.copy()

    # 移动平均线
    out["sma_fast"] = out["price"].rolling(window=fast, min_periods=1).mean()
    out["sma_slow"] = out["price"].rolling(window=slow, min_periods=1).mean()

    # 生成信号: 快均线 > 慢均线 -> 做多，否则做空
    out["position"] = 0
    out.loc[out["sma_fast"] > out["sma_slow"], "position"] = 1
    out.loc[out["sma_fast"] < out["sma_slow"], "position"] = -1

    return out