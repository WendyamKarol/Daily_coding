import yfinance as yf
import pandas as pd
import numpy as np
import datetime as dt

# === Fonction pour récupérer les données et calculer les stats ===
def get_data(stocks, start, end):
    data = yf.download(stocks, start=start, end=end)['Close']
    returns = data.pct_change().dropna()
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    return returns, mean_returns, cov_matrix

# Portfolio Performance
def portfolioPerformance(weights, mean_returns, cov_matrix, Time):
    returns = np.sum(mean_returns*weights)*Time
    std = np.sqrt( np.dot(weights.T, np.dot(cov_matrix, weights)) ) * np.sqrt(Time)
    return returns, std


stockList = ['MC', 'TTE', 'BNP', 'OR', 'AIR']
stocks = [stock+'.PA' for stock in stockList]
start_date = dt.datetime.now() - dt.timedelta(days=800)
end_date = dt.datetime.now()


returns, meanReturns, covMatrix = get_data(stocks, start=start_date, end=end_date)
returns = returns.dropna()

weights = np.random.random(len(returns.columns))
weights /= np.sum(weights)

returns['portfolio'] = returns.dot(weights)
pd.set_option('display.max_rows', None)
print(returns.tail(100))
