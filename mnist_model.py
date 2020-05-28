from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
from keras.optimizers import RMSprop
from sklearn.metrics import accuracy_score

(X_train, y_train) , (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(-1, 784)
X_test = X_test.reshape(-1, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()

model.add(Dense(units=512, input_shape=(784,), activation='relu'))
model.add(Dense(units=10, activation='softmax'))

model.summary()

model.compile(optimizer=RMSprop(), loss='categorical_crossentropy', metrics=['accuracy'])

epoch = model.fit(X_train, y_train, epochs=1, validation_data=(X_test , y_test))

model.save('mnist_model_trained.h5')

accuracy = model.history.history.get('accuracy')
accuracy=accuracy[-1]*100

print(accuracy)





