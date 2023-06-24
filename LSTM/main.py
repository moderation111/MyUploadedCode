# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import r2_score


def extract_time_data(data_in, input_ts, output_ts):
    num_step = data_in.shape[0]
    x_in = []
    y_in = []
    for i in range(0, num_step-input_ts-output_ts+1):
        x_in.append([j for j in data_in[i:i+input_ts, 0]])
        y_in.append([k for k in data_in[i+input_ts:i+input_ts+output_ts, 0]])

    x_out = np.array(x_in)
    y_out = np.array(y_in)
    return x_out, y_out
#print(tf.test.is_gpu_available())
# prepare model training data set

raw_data_file = 'train.xlsx'
dataset = pd.read_excel(raw_data_file, sheet_name='data')
data_input_range = [0, 4]
data_list = ['output']
# extract test data
test_data_file = 'test.xlsx'

train_data = np.array(dataset[data_list])
train_data = train_data.reshape(train_data.shape[0], train_data.shape[1])
input_ts = 10
output_ts = 3
x_train, y_train = extract_time_data(train_data, input_ts, output_ts)
#print(x_train.shape, y_train.shape)
#print(x_train)

#y_train = y_train.reshape([189*3,-1])
#print(y_train.shape)
#print(y_train)

#exit(3)

Dense = tf.keras.layers.Dense
LSTM = tf.keras.layers.LSTM
Dropout = tf.keras.layers.Dropout
#optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.01) #learning_rate=0.005)

model = tf.keras.models.Sequential()
model.add(LSTM(units=100, dropout=0.0, recurrent_dropout=0.0, input_shape=(input_ts, 1), return_sequences=False))
#model.add(LSTM(units=50, activation='sigmoid',return_sequences=True))
#model.add(LSTM(units=20, activation='sigmoid',return_sequences=True))
#model.add(LSTM(units=10, activation='sigmoid', return_sequences=False))

model.add(Dropout(0.1))
#model.add(Dense(units=30, activation='sigmoid'))
model.add(Dense(units=1, activation='linear'))
model.compile(optimizer='RMSprop', loss='mse', metrics='mse')
model.summary()
weight = np.ones(189)
model.fit(x_train,y_train[:,2],batch_size=50, epochs=1000, sample_weight=weight)

# extract test data
test_data_file = 'test.xlsx'
dataset = pd.read_excel(test_data_file, sheet_name='data')
test_data = np.array(dataset[data_list])
test_data = test_data.reshape(test_data.shape[0], test_data.shape[1], 1)
x_test, y_test = extract_time_data(test_data,  input_ts, output_ts)
y_test_predict = model.predict(x_test)
print(y_test.shape, y_test_predict.shape)

#y_test = y_test.reshape([-1, 1])
#y_test_predict = y_test_predict.reshape([-1, 1])
col = 2
score = r2_score(y_test[:,col], y_test_predict[:,0])
print(score)

figure1 = plt.figure()
plt.plot(y_test[:,col])
plt.plot(y_test_predict[:,0])
plt.legend(["test", "test_predict"], title='test VS predict_test')

figure2 = plt.figure()
plt.scatter(y_test_predict[:,0], y_test[:,col])
x_cal = np.linspace(0.0, 2.0, 100)
y_cal = x_cal
plt.plot(y_cal, x_cal, 'y')
plt.show()
