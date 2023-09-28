import pandas_datareader as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from scipy.stats import norm

def get_stock(ticker, startday, endday):
    # Specify the start and end dates for the data
    # Download the data using the Yahoo Finance API
    data = yf.download(ticker, start=startday, end=endday)
    # Save the data to a CSV file
    data.to_csv(f"data/{ticker}_data.csv")
    return data

# Plot the close price
def plot_close_price(df):
    plt.plot(df.Close)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Close Price Over Time')
    plt.show()

def preprocessing(df, hParams):
    data = df.Close.values

    # Split the data into training and test sets
    # Calculate the number of data points in each set
    train_size = int(len(data) * (1-hParams['test_prop']-hParams['valid_prop']))
    val_size = int(len(data) * hParams['valid_prop'])
    test_size = int(len(data)*hParams['test_prop'])

    # Split the data into training, validation, and test sets
    train_data = data[:train_size]
    val_data = data[train_size:train_size + val_size]
    test_data = data[-test_size:]

    return train_data,val_data, test_data

def calculate_mape(y_test, y_pred):
    total_error = 0
    for i in range(len(y_test)):
        total_error += abs((y_test[i] - y_pred[i]) / y_test[i])
    mape = (total_error / len(y_test)) * 100
    return mape

def BrownianModel(closing_prices):
    # Split data into train and test sets
    train_data, test_data = train_test_split(closing_prices, test_size=0.2, shuffle=False)

    # Calculate the historical log returns
    log_returns = np.diff(np.log(train_data))
    
    # Calculate the mean return and standard deviation of log returns
    mean_return = np.mean(log_returns)
    std_dev = np.std(log_returns)

    # Predict using Black-Scholes equation
    predicted_prices = [closing_prices[len(train_data)-1]]
    for i,log_return in enumerate(test_data):
        drift = mean_return - 0.5 * std_dev**2
        diffusion = std_dev * norm.ppf(np.random.rand())
        predicted_price = closing_prices[len(train_data)-3 + i] * np.exp(drift + diffusion)
        predicted_prices.append(predicted_price)
    
    return predicted_prices