import os
import numpy as np
import tqdm

def Get_Dim(Data):
    X_max = 0
    Y_max = 0
    Z_max = 0
    for dir, _, files in os.walk(Data):
        for file in files:
            Temp = np.load(os.path.join(dir, file))
            X, Y, Z = Temp.shape
            print(X, Y, Z)
            X_max = max(X, X_max)
            Y_max = max(Y, Y_max)
            Z_max = max(Z, Z_max)
    return (X_max, Y_max, Z_max)

def Preprocessing(Data, Shape):
    for dir, _, files in os.walk(Data):
        for file in tqdm.tqdm(files):
            Temp = np.load(os.path.join(dir, file))
            padded_array = np.zeros(Shape)

            # Calculate the shape of the original array
            original_shape = Temp.shape

            # Calculate the ranges for copying the original data
            range_1 = min(original_shape[0], Shape[0])
            range_2 = min(original_shape[1], Shape[1])
            range_3 = min(original_shape[2], Shape[2])

            # Copy the original data into the new padded array
            padded_array[:range_1, :range_2, :range_3] = Temp[:range_1, :range_2, :range_3]

            np.save(os.path.join(dir, file), padded_array)

if __name__ == '__main__':
    Shape = Get_Dim('./Dataset/')
    Preprocessing('./Dataset/', Shape)