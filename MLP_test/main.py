# This is a template of building up a Multilayer-Perceptron (MLP) model for data regression purpose
# In this script, the keras model & sequential methods are used.
# import key modules and libs
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


# prepare model training data set
raw_data_file = 'MLP_test.xlsx'
dataset = pd.read_excel(raw_data_file, sheet_name='raw_data')
data_input_range = [0, 4]
x_list = ['A', 'B', 'C', 'D']
x = np.array(dataset[x_list])
y_list = ['Result1', 'Result2']
y = np.array(dataset[y_list])
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=10)

model_type = 'Model' # select Model/Sequential
Dense = tf.keras.layers.Dense
# Method1: Use Model method to build model
input_layer = tf.keras.Input(shape=4,)
hidden_layer1 = Dense(units=100, activation='sigmoid',)
hidden_layer2 = Dense(units=50, activation='sigmoid',)
output_layer = Dense(units=2,)

hidden_layer1_tensor = hidden_layer1(input_layer)
hidden_layer2_tensor = hidden_layer2(hidden_layer1_tensor)
output_layer_tensor = output_layer(hidden_layer2_tensor)
model_m = tf.keras.Model(inputs=input_layer, outputs=output_layer_tensor)

# Method2: Use Sequential method to build model
model_s = tf.keras.models.Sequential()
model_s.add(Dense(units=100, input_dim=4, activation='sigmoid'))
model_s.add(Dense(units=100, activation='sigmoid'))
model_s.add(Dense(units=2))

sgd = tf.keras.optimizers.SGD(learning_rate=0.05)
if model_type == 'Model':
    model = model_m
elif model_type == 'Sequential':
    model = model_s
else:
    print('Unknown model type')
    exit(1)

model.compile(optimizer=sgd, loss='mse',metrics='mse')
model.summary()

#model training and save
model.fit(X_train, Y_train,batch_size=30, epochs=1000)
joblib.dump(model, 'Model.m')



model = joblib.load('Model.m')

#w,b = model.layers[0].get_weights()
#print(w,b)

Y_test_pred = model.predict(X_test)
print(Y_test_pred.shape)
score1 = r2_score(Y_test[:,0], Y_test_pred[:,0])
score2 = r2_score(Y_test[:,1], Y_test_pred[:,1])

print(score1, score2)

figure1 = plt.figure()
plt.scatter(Y_test_pred[:,0], Y_test[:,0])
x_cal = np.linspace(0,2,100)
y_cal = x_cal
plt.plot(y_cal, x_cal, 'y')

figure2 = plt.figure()
plt.scatter(Y_test_pred[:,1], Y_test[:,1])
x_cal = np.linspace(0,0.6,100)
y_cal = x_cal
plt.plot(y_cal, x_cal, 'y')
plt.show()
#plt.scatter(x,ypredict)
#y_test_p = model.predict([[5.1,3.5,1.4,0.2]])
#print(y_test_p)
#plt.show()