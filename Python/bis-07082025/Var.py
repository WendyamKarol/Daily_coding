import yfinance as yf
import pandas as pd
import numpy as np
import datetime as dt

# === Paramètres ===
stockList = ['MC.PA', 'TTE.PA', 'BNP.PA', 'OR.PA', 'AIR.PA']  # LVMH, Total, BNP, L'Oréal, Airbus
startDate = dt.datetime.now() - dt.timedelta(days=800)
endDate = dt.datetime.now()

# === Télécharger les données ===
data = yf.download(stockList, start=startDate, end=endDate)['Close']
returns = data.pct_change().dropna()
mean_returns = returns.mean()
cov_matrix = returns.cov()

# === Création du portefeuille ===
weights = np.random.random(len(stockList))
weights /= np.sum(weights)

returns['Portfolio'] = returns.dot(weights)

# === Performance ===
def portfolio_performance(weights, mean_returns, cov_matrix, time_horizon=252):
    ret = np.sum(mean_returns * weights) * time_horizon
    risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(time_horizon)
    return ret, risk

def historical_var(returns, alpha=5):
    return np.percentile(returns, alpha)

expected_return, expected_risk = portfolio_performance(weights, mean_returns, cov_matrix)
var_95 = historical_var(returns['Portfolio'])

# === Résultat ===
print("\n=== Portefeuille (actions françaises) ===")
for stock, weight in zip(stockList, weights):
    print(f"{stock} : {weight:.2%}")
print(f"\nRendement annuel attendu : {expected_return:.2%}")
print(f"Risque annuel : {expected_risk:.2%}")
print(f"VaR à 5% (perte max probable sur 1 jour) : {var_95:.2%}")
