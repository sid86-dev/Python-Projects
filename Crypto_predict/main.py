import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.algorithms import mode
import pandas_datareader as web
import datetime as dt
import csv

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import models

from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential


def predict(crypto_currency, against_currency):
    start = dt.datetime(2019,1,1)
    end = dt.datetime.now()

    data = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', start, end)

    # print(data.head())

    scalar = MinMaxScaler(feature_range=(0,1))
    scalar_Data = scalar.fit_transform(data['Close'].values.reshape(-1,1))

    prediction_days = 10

    x_train, y_train = [], []

    for x in range(prediction_days, len(scalar_Data)):
        x_train.append(scalar_Data[x-prediction_days:x, 0])
        y_train.append(scalar_Data[x, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Create neural network

    model = Sequential()

    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    # compile model

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, epochs=25, batch_size=32)

    # Testing model

    test_start = dt.datetime(2020,1,1)
    test_end = dt.datetime.now()

    test_data = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', test_start, test_end)
    actual_price = test_data['Close'].values

    total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)

    model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values 
    model_inputs = model_inputs.reshape(-1,1)
    model_inputs = scalar.fit_transform(model_inputs)

    x_test = []

    for x in range(prediction_days, len(model_inputs)):
        x_test.append(model_inputs[x-prediction_days:x, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    prediction_prices = model.predict(x_test)
    prediction_prices = scalar.inverse_transform(prediction_prices)

    # plotting data

    plt.plot(actual_price, color='black', label='Actual Prices')
    plt.plot(prediction_prices, color='green', label='Predicted Prices')
    plt.title(f'{crypto_currency} Price Prediction')

    plt.xlabel('Time')
    plt.ylabel('Price')

    plt.legend(loc='upper left')

    # plt.show()


    # predict next day

    real_data = [model_inputs[len(model_inputs)+1 - prediction_days:len(model_inputs)+ 1, 0]]
    real_data = np.array(real_data)
    real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

    prediction = model.predict(real_data)
    prediction = scalar.inverse_transform(prediction)

    price = prediction[0][0]
    # print(math.ceil(v*100)/100)

    return price

def collect_data(times):
    
        csv_data = []
        against_currency = 'INR'
        crypto_currency = ['DNT', 'DOGE', 'ETH', 'BTC', 'REP']
        # crypto_currency = ['DNT']
        try:
            for coin in crypto_currency:
                my_dic = {}
                my_dic['Name'] = coin
                my_dic['Currency'] = against_currency
                my_dic['Date'] = dt.datetime.now()
                for i in range(1, times):
                    price = predict(crypto_currency=coin, against_currency=against_currency)

                    print(f"Tomorrow price of {coin} will be {price:.2f} {against_currency} ")
                    my_dic[f'Price{i}'] = float(f'{price:.2f}')
        except:
            return csv_data

        csv_data.append(my_dic)

        return csv_data

    # importing the csv module
def save_to_csv(csv_data, num):
    # field names
    fields = ['Name', 'Currency', 'Date'] 
    for i in range(1,num):
        fields.append(f'Price{i}')
    # name of csv file
    filename = "predicted_price.csv"
    
    # writing to csv file
    with open(filename, 'w') as csvfile:
    	# creating a csv dict writer object
    	writer = csv.DictWriter(csvfile, fieldnames = fields)
    	# writing headers (field names)
    	writer.writeheader()
    	# writing data rows
    	writer.writerows(csv_data)

def read_data(num):
    # csv file name
    filename = "predicted_price.csv"

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            prices=[]
            for i in range(1,num):
                prices.append(float(row[f"Price{i}"]))
    

            average_price = sum(prices)/(len(prices))
            print(row['Name'], average_price)

if __name__=="__main__":
    num = 6
    # csv_data = collect_data(num)
    # save_to_csv(csv_data, num)
    read_data(num)