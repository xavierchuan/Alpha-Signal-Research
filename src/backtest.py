import pandas as pd


def run_backtest(df: pd.DataFrame, initial_capital: float = 1_0000) -> pd.DataFrame:
    """
    Run backtest on signal DataFrame with 'position' column.
    Adds: 'return', 'strategy_return', 'equity'
    """
    out = df.copy()

    # 日收益率
    out["return"] = out["price"].pct_change().fillna(0)

    # 策略收益率（持仓 * 资产收益）
    out["strategy_return"] = out["position"].shift(1) * out["return"]
    out["strategy_return"].fillna(0, inplace=True)

    # 权益曲线
    out["equity"] = (1 + out["strategy_return"]).cumprod() * initial_capital

    return out