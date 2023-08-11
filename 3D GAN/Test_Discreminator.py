import os
import tensorflow as tf
from keras import models
from keras.layers import Dense, Conv2D, Conv3D, BatchNormalization, Flatten, Reshape
import numpy as np
import random

def Dicriminator(input_shape, output_shape):
    model = models.Sequential()
    model.add(Conv2D(128, (50,50), activation='relu'))
    model.add(Conv2D(64, (50,50), activation='relu'))
    
    model.add(Flatten())
    model.add(BatchNormalization())
    model.add(Dense(128*128, activation='relu'))
    model.add(BatchNormalization())
    model.add(Reshape((128, 128)))

    model.add(BatchNormalization())
    model.add(Conv2D(12, (9,9), activation='relu'))
    model.add(Conv2D(4, (9,9), activation='relu'))

    model.add(Flatten())
    model.add(BatchNormalization())
    model.add(Dense(128*128, activation='relu'))
    model.add(BatchNormalization())
    model.add(Reshape((128, 128)))

    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(Conv2D(10, (3, 3), activation='relu'))
    model.add(Dense(output_shape[0], activation='sigmoid'))

    model.compile(optimizer= tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5),
                  loss= 'categorical_crossentropy',
                  metrics=['mse', 'mae', 'accuracy', 'f1_score'])

    return model

def make_data(npy_files):
    X = []
    y = []
    len_temp = len(npy_files)
    for i, data in enumerate(npy_files):
        X.append(data)
        Temp = [0 for _ in range(len_temp)]
        Temp[i] = 1
        y.append(Temp)

    X = np.array(X)
    y = np.array(y)
    print(f'Train: {X.shape}  {y.shape}')
    return X, y

def get_files(folder):
    npy_files = []
    for dir, _, files in os.walk(folder):
        files = [file for file in files if 'npy' in file]
        for file in files:
            npy_files.append(np.load(os.path.join(dir, file)))
    npy_files = np.array(npy_files)
    input(f'Check the Shape of the files: {npy_files.shape}')
    return npy_files

if __name__ == '__main__':
    folder = './Dataset'
    npy_files = get_files(folder)
    X, y = make_data(npy_files)
    model = Dicriminator(X[0].shape, y[0].shape)

    model.fit(X, y)

    model.save('./Model')