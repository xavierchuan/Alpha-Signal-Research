# Alpha-Signal-Research

A lightweight research project for backtesting simple trading strategies (e.g., SMA crossover) on financial time series.

## Features
- Data loading from Yahoo Finance
- Signal generation (SMA crossover strategy)
- Backtesting with equity curve tracking
- Performance evaluation (Sharpe, Max Drawdown, Annual Return, etc.)
- Visualization of signals and equity curve
- Automatic report generation (Markdown)

## Installation
```bash
git clone https://github.com/xavierchuan/Alpha-Signal-Research.git
cd Alpha-Signal-Research
pip install -r requirements.txt
```

Usage

Run the demo backtest:
python tests/run_demo.py

Results will be saved under results/:
	•	Plots in results/plots/
	•	Reports in results/reports/
Example Results
    Trading Signals
    Equity Curve
    Backtest Report
    
    Example report is saved under:
    results/reports/backtest_report.md
