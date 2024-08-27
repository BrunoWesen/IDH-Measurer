import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

"""
  Using Neural Network Sequencial Model to predict next values of a list using only his own data without correlation
  with other data/list
"""


def sequencial_model_predict(array: list, qtd_values: int):
    if len(array) < 2 * qtd_values:
        print("A lista deve ter pelo menos o dobro de elementos da quantidade que queira prever...")
        return array

    data = np.array(array)

    X = data[:-qtd_values]  # Previous values
    y = data[qtd_values:]  # Next corresponding values

    # Sequencial model
    model = Sequential()

    # Hidden layers
    model.add(Dense(8, input_shape=(1,), activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(8, activation='relu'))

    # Output layer
    model.add(Dense(1))

    # Compile
    model.compile(optimizer='Adam', loss='mean_squared_error')

    # Training
    model.fit(X, y, epochs=1000, verbose=0)

    # Predicting
    new_values = model.predict(data[-qtd_values:])

    data = np.append(data, list(map(int, new_values.flatten())))
    return data
