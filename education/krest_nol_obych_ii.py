import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import Sequential
from keras.layers import Dense, Conv2D, Flatten
from tensorflow import keras
name_file="xo_3"
eph=1000


input = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 3, 0, 0, 2, 0, 0], [3, 2, 0, 3, 3, 2, 2, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 3, 0, 0, 0, 0], [2, 3, 2, 0, 3, 0, 0, 2, 0], [2, 3, 2, 3, 3, 2, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 2, 0], [3, 2, 3, 0, 0, 0, 0, 2, 0], [3, 2, 3, 0, 3, 0, 0, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 2, 0, 0, 0, 0], [3, 3, 2, 0, 2, 0, 0, 0, 0], [3, 3, 2, 2, 2, 0, 3, 0, 0], [3, 3, 2, 2, 2, 3, 3, 0, 2], [0, 2, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 0, 0, 0, 0, 2, 0], [3, 2, 0, 0, 3, 0, 0, 2, 2], [3, 2, 2, 0, 3, 0, 3, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 3, 0, 0, 0, 0, 2], [3, 2, 0, 3, 3, 0, 0, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 3, 2, 0, 0, 2], [0, 0, 3, 0, 3, 2, 2, 0, 2], [0, 2, 3, 0, 3, 2, 2, 3, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 2, 0, 0, 0], [3, 2, 3, 0, 0, 2, 0, 0, 0], [3, 2, 3, 2, 3, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0, 2], [3, 0, 3, 0, 0, 0, 0, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 3, 0, 0, 2, 0, 0], [3, 2, 0, 3, 3, 2, 2, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 0, 0, 0, 0, 2, 0], [3, 2, 2, 0, 3, 0, 0, 2, 0], [3, 2, 2, 3, 3, 0, 0, 2, 2], [0, 2, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 2, 0, 0, 0, 0, 0], [3, 2, 0, 2, 3, 0, 0, 0, 2], [3, 2, 3, 2, 3, 2, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 3, 0, 0, 2, 0], [2, 0, 2, 3, 3, 0, 0, 2, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 3, 0, 0, 0, 0], [2, 3, 2, 0, 3, 0, 0, 2, 0], [2, 3, 2, 3, 3, 2, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 2, 0, 0, 0, 0, 0, 0], [3, 0, 2, 3, 0, 0, 2, 0, 0], [3, 0, 2, 3, 3, 0, 2, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 2, 0, 0], [3, 3, 2, 0, 0, 0, 2, 0, 0], [3, 3, 2, 0, 3, 0, 2, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 2, 0, 0, 0], [3, 2, 3, 0, 0, 2, 0, 0, 0], [3, 2, 3, 2, 3, 2, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0], [3, 0, 2, 0, 2, 0, 0, 0, 0], [3, 0, 2, 2, 2, 0, 3, 0, 0], [3, 0, 2, 2, 2, 3, 3, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 2, 0, 0, 0, 0, 0, 0], [3, 0, 2, 3, 0, 0, 0, 0, 2], [3, 0, 2, 3, 0, 3, 2, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 3, 0, 0, 2, 0, 0], [3, 2, 0, 3, 3, 0, 2, 0, 2], [0, 0, 0, 0, 2, 0, 0, 0, 0], [3, 0, 0, 0, 2, 0, 0, 0, 2], [3, 2, 3, 0, 2, 0, 0, 0, 2], [3, 2, 3, 0, 2, 2, 0, 3, 2], [2, 0, 0, 0, 0, 0, 0, 0, 0], [2, 2, 0, 0, 3, 0, 0, 0, 0], [2, 2, 3, 0, 3, 0, 2, 0, 0], [2, 2, 3, 3, 3, 2, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 0, 0, 0, 0, 0, 0], [3, 2, 0, 3, 0, 0, 2, 0, 0], [3, 2, 0, 3, 3, 2, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 3, 0, 0, 0, 2], [2, 3, 0, 0, 3, 0, 0, 2, 2], [2, 3, 0, 2, 3, 0, 3, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 2, 0], [3, 0, 3, 0, 0, 0, 0, 2, 2], [0, 2, 0, 0, 0, 0, 0, 0, 0], [3, 2, 2, 0, 0, 0, 0, 0, 0], [3, 2, 2, 3, 0, 0, 2, 0, 0], [3, 2, 2, 3, 3, 2, 2, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 3, 0, 2, 0, 2], [0, 2, 0, 0, 3, 0, 2, 3, 2], [3, 2, 2, 0, 3, 0, 2, 3, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0, 2], [3, 2, 3, 0, 0, 0, 0, 0, 2], [3, 2, 3, 0, 2, 0, 3, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 2, 0], [3, 2, 3, 0, 0, 0, 0, 2, 0], [3, 2, 3, 2, 3, 0, 0, 2, 0], [3, 2, 3, 2, 3, 3, 0, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0, 2], [3, 2, 3, 0, 0, 0, 0, 0, 2], [3, 2, 3, 2, 0, 0, 3, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 2, 0, 0, 0, 0], [3, 3, 2, 0, 2, 0, 0, 0, 0], [3, 3, 2, 0, 2, 0, 3, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0]])

output = np.array([[0.0, 0.0], [0.5, 0.0], [0.5, 0.5], [1.0, 1.0], [0.5, 0.5], [0.0, 0.5], [0.5, 0.0], [1.0, 1.0], [0.0, 0.0], [0.0, 1.0], [0.5, 0.5], [1.0, 0.0], [0.0, 0.0], [0.0, 0.5], [1.0, 0.0], [0.5, 1.0], [1.0, 0.5], [0.0, 0.0], [0.5, 0.5], [1.0, 0.0], [0.5, 0.0], [0.0, 0.0], [0.5, 0.0], [0.5, 0.5], [0.5, 1.0], [0.5, 0.5], [0.0, 1.0], [1.0, 0.5], [0.0, 0.0], [0.0, 0.0], [0.0, 1.0], [0.5, 0.5], [1.0, 0.0], [0.0, 0.0], [0.0, 1.0], [0.0, 0.5], [0.0, 0.0], [0.5, 0.0], [0.5, 0.5], [1.0, 1.0], [0.0, 0.0], [0.5, 0.5], [0.5, 0.0], [0.5, 1.0], [0.0, 0.0], [0.5, 0.5], [0.0, 1.0], [1.0, 0.0], [0.5, 0.5], [0.5, 0.0], [0.5, 1.0], [0.5, 0.5], [0.0, 0.5], [0.5, 0.0], [1.0, 1.0], [0.0, 0.0], [0.5, 0.0], [0.5, 0.5], [0.5, 1.0], [0.0, 0.0], [0.0, 0.5], [0.5, 0.5], [1.0, 1.0], [0.0, 0.0], [0.0, 1.0], [0.5, 0.5], [1.0, 0.0], [0.0, 0.0], [1.0, 0.0], [0.5, 1.0], [0.0, 0.5], [0.0, 0.0], [0.5, 0.0], [0.5, 1.0], [0.5, 0.5], [0.0, 0.0], [0.5, 0.0], [0.5, 0.5], [0.5, 1.0], [0.0, 0.0], [0.0, 1.0], [1.0, 0.5], [0.5, 0.0], [0.5, 0.5], [0.0, 1.0], [0.5, 0.0], [1.0, 0.5], [0.0, 0.0], [0.5, 0.0], [0.5, 0.5], [1.0, 1.0], [0.5, 0.5], [0.0, 0.5], [1.0, 0.0], [0.0, 1.0], [0.0, 0.0], [0.0, 1.0], [0.0, 0.5], [0.0, 0.0], [0.5, 0.0], [0.5, 0.5], [1.0, 1.0], [0.5, 0.5], [1.0, 0.5], [0.0, 0.0], [0.5, 1.0], [0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.5, 0.0], [0.0, 0.0], [0.0, 1.0], [0.5, 0.5], [0.5, 1.0], [1.0, 0.0], [0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.5, 0.5], [0.0, 0.0], [0.0, 0.5], [1.0, 0.0], [0.5, 0.0], [0.0, 0.0]])

# print(input.shape)

model = keras.Sequential()
model.add(Dense(units=9, activation='relu'))
model.add(Dense(units=81, activation='relu'))
model.add(Dense(units=2, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

history = model.fit(input, output, epochs=eph, verbose=0)
print(model.summary())
plt.plot(history.history["loss"])
plt.grid(True)
plt.show()

result=model.predict([[3,2,0,3,3,2,2,0,0]])
print(result)
result=model.predict([[2,3,2,3,3,2,0,2,0]])
print([2, 2])
print(result)
model.save('education/'+name_file+'.h5', save_format='h5')