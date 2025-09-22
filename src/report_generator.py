import os

def save_report(metrics: dict, plots: list, params: dict, save_path="results/reports/report.md"):
    """
    生成回测报告 (Markdown 格式)

    Args:
        metrics (dict): 回测指标字典 (Total Return, Sharpe, Max Drawdown 等)
        plots (list): 图表路径列表
        params (dict): 策略参数 (ticker, start, end, fast, slow)
        save_path (str): 报告保存路径
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "w") as f:
        # 标题
        f.write(f"# Backtest Report - {params.get('ticker', 'Unknown')}\n\n")

        # 策略参数
        f.write("## Strategy Parameters\n")
        for k, v in params.items():
            f.write(f"- **{k}**: {v}\n")
        f.write("\n")

        # 回测结果
        f.write("## Performance Metrics\n")
        for k, v in metrics.items():
            f.write(f"- **{k}**: {v:.4f}\n")
        f.write("\n")

        # 图表
        f.write("## Plots\n")
        for plot in plots:
            f.write(f"![{os.path.basename(plot)}]({plot})\n\n")

    print(f"📝 Report saved to {save_path}")