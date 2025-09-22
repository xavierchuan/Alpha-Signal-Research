import os
from typing import Optional
import matplotlib.pyplot as plt
import pandas as pd


def _ensure_dir_for(path: Optional[str]) -> None:
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)


def plot_equity_curve(
    df: pd.DataFrame,
    title: Optional[str] = None,
    save_path: Optional[str] = None,
    show: bool = False,
) -> None:
    """
    Draw and optionally save the equity curve. Requires 'equity' column.
    """
    if "equity" not in df.columns:
        raise KeyError("DataFrame must contain an 'equity' column to plot equity curve.")

    fig, ax = plt.subplots(figsize=(10, 5))
    df["equity"].plot(ax=ax, linewidth=1.2)
    ax.set_title(title or "Equity Curve")
    ax.set_xlabel("Date")
    ax.set_ylabel("Equity (1 = initial)")
    ax.grid(True, alpha=0.3)

    if save_path:
        _ensure_dir_for(save_path)
        fig.tight_layout()
        fig.savefig(save_path, dpi=150)

    if show:
        plt.show()
    plt.close(fig)


def plot_signals(
    df: pd.DataFrame,
    title: Optional[str] = None,
    save_path: Optional[str] = None,
    show: bool = False,
) -> None:
    """
    Plot price with SMA overlays and mark buy/sell points.
    Requires columns: 'price', 'sma_fast', 'sma_slow', 'position'.
    """
    required = {"price", "sma_fast", "sma_slow", "position"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Missing columns for signal plot: {missing}")

    fig, ax = plt.subplots(figsize=(11, 6))
    df["price"].plot(ax=ax, label="Price", linewidth=1)
    df["sma_fast"].plot(ax=ax, label="SMA Fast", linewidth=1)
    df["sma_slow"].plot(ax=ax, label="SMA Slow", linewidth=1)

    pos_change = df["position"].diff().fillna(0)
    buys = pos_change > 0
    sells = pos_change < 0

    ax.scatter(df.index[buys], df.loc[buys, "price"], marker="^", s=42, label="Buy")
    ax.scatter(df.index[sells], df.loc[sells, "price"], marker="v", s=42, label="Sell")

    ax.set_title(title or "Signals")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    ax.grid(True, alpha=0.3)

    if save_path:
        _ensure_dir_for(save_path)
        fig.tight_layout()
        fig.savefig(save_path, dpi=150)

    if show:
        plt.show()
    plt.close(fig)