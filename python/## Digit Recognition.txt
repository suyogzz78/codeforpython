## Digit Recognition

import keras
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras import backend as K
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.layers import Dense, Dropout, Flatten
import matplotlib.pyplot as plt
%matplotlib inline

fig = plt.figure
n_classes = 10
input_shape = (28, 28, 1)
batch_size = 128
num_classes = 10
epochs = 10

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
print("Training data shape {} , test data shape {}".format(X_train.shape, Y_train.shape))

img = X_train[1]

plt.imshow(img, cmap='gray')
plt.show()

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

Y_train = to_categorical(Y_train, n_classes)
Y_test = to_categorical(Y_test, n_classes)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
print('x_train shape:', X_train.shape)
print('train samples ',X_train.shape[0],)
print('test samples',X_test.shape[0])

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

history = model.fit(X_train, Y_train,batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(X_test, Y_test))

output_score = model.evaluate(X_test, Y_test, verbose=0)
print('Testing loss:', output_score[0])
print('Testing accuracy:', output_score[1])