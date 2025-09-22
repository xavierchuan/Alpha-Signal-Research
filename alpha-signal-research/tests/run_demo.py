import os
import sys

# 保证可以找到 src 目录
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.data_loader import load_or_process_data
from src.signal_generation import generate_signals
from src.backtest import run_backtest
from src.evaluation import compute_metrics
from src.visualization import plot_equity_curve, plot_signals
from src.report_generator import save_report 

def main():
    ticker = "BTC-USD"
    start = "2020-01-01"
    end = "2020-06-01"

    print("📂 Loading data...")
    data = load_or_process_data(ticker, start, end)

    print("⚡ Generating signals...")
    signals = generate_signals(data.copy(), fast=10, slow=30)

    print("📈 Running backtest...")
    result = run_backtest(signals)

    print("📊 Evaluating performance...")
    metrics = compute_metrics(result)
    print("✅ Backtest complete. Metrics:")
    for k, v in metrics.items():
        try:
            print(f"{k}: {float(v):.4f}")
        except Exception:
            print(f"{k}: {v}")

    # 保存到 results/figures 下
    equity_path = "results/figures/equity_curve.png"
    signals_path = "results/figures/signals.png"

    print("📉 Plotting equity curve...")
    plot_equity_curve(result, f"{ticker} SMA Crossover Strategy", save_path=equity_path, show=False)

    print("📍 Plotting signals...")
    plot_signals(result, f"{ticker} SMA Crossover Signals", save_path=signals_path, show=False)

    print("🖼️ Saved plots to:")
    print(f"  - {equity_path}")
    print(f"  - {signals_path}")


def main():
    ticker = "BTC-USD"
    start, end = "2020-01-01", "2020-06-01"

    print("📂 Loading data...")
    data = load_or_process_data(ticker, start, end)

    print("⚡ Generating signals...")
    signals = generate_signals(data, fast=10, slow=30)

    print("📈 Running backtest...")
    result = run_backtest(signals)

    print("📊 Evaluating performance...")
    metrics = compute_metrics(result)

    print("✅ Backtest complete. Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    # 保存图表
    plots_dir = "results/plots"
    os.makedirs(plots_dir, exist_ok=True)
    equity_path = os.path.join(plots_dir, "equity_curve.png")
    signals_path = os.path.join(plots_dir, "signals.png")

    plot_equity_curve(result, save_path=equity_path, show=False)
    plot_signals(result, title=f"{ticker} SMA Crossover Signals", save_path=signals_path, show=False)

    # 生成报告
    save_report(
        metrics,
        plots=[equity_path, signals_path],
        params={"ticker": ticker, "start": start, "end": end, "fast": 10, "slow": 30},
        save_path="results/reports/backtest_report.md"
    )


if __name__ == "__main__":
    main()