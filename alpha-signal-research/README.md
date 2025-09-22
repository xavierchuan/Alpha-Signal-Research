# Alpha Signal Research: Moving Average Crossovers

This project analyzes the performance of SMA/EMA crossover signals under varying volatility regimes across BTC, ETH, and AAPL data.  
It evaluates **alpha decay**, **regime-dependence**, and in-sample vs out-of-sample performance.  

## Features
- Generate SMA/EMA crossover signals with configurable windows.
- Backtest trading strategies on BTC, ETH, and AAPL.
- Regime analysis (volatility clustering, performance by cycle).
- Visualization of signals, returns, and breakdowns.
- Export structured reports (Markdown + plots + metrics).

## Project Structure
- `src/`: Core implementation (signals, backtest, evaluation, visualization).
- `data/`: Raw and processed datasets.
- `notebooks/`: Research and prototyping.
- `results/`: Backtest results and diagnostic plots.

## Example Usage
```bash
python src/signal_generation.py --asset BTC --fast 10 --slow 50
python src/backtest.py --asset ETH --strategy crossover --start 2020-01-01 --end 2024-01-01

Requirements
pandas
numpy
matplotlib
TA-Lib
yfinance

👨‍💻 Author: Xiaochuan Li
📂 GitHub: xavierchuan