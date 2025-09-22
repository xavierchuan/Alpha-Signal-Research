import numpy as np
import pandas as pd


def compute_metrics(strategy: pd.DataFrame, freq: int = 252) -> dict:
    """
    Compute performance metrics from strategy DataFrame.
    """
    returns = strategy["strategy_return"].dropna()

    total_return = (1 + returns).prod() - 1
    annual_return = (1 + total_return) ** (freq / len(returns)) - 1
    sharpe = np.sqrt(freq) * returns.mean() / returns.std() if returns.std() != 0 else 0
    cummax = (1 + returns).cumprod().cummax()
    drawdown = (1 + returns).cumprod() / cummax - 1
    max_drawdown = drawdown.min()

    return {
        "Total Return": round(total_return, 4),
        "Annual Return": round(annual_return, 4),
        "Sharpe": round(sharpe, 4),
        "Max Drawdown": round(abs(max_drawdown), 4),
    }