import numpy as np
import tensorflow as tf
from keras import layers, models
import os

# Function to load npy files from a folder and return a list
def load_npy_files(folder):
    file_list = []
    # Load npy files and append to the list
    for file_name in os.listdir(folder):
        if file_name.endswith('.npy'):
            file_path = os.path.join(folder, file_name)
            data = np.load(file_path)
            file_list.append(data)
    return file_list

def build_generator(input_size):
    model = models.Sequential()
    
    return model

def build_discriminator(input_size):
    model = models.Sequential()
    
    return model


# Combine Generator and Discriminator into a GAN
def build_gan(generator, discriminator):

    return gan_model

# Main training loop
def train_gan(data_folder, num_epochs, batch_size):
    npy_list = load_npy_files(data_folder)
    data_shape = npy_list[0].shape  # Get the shape of a single data sample
        
                
# Parameters
data_folder = './Dataset'
num_epochs = 20
batch_size = 32

# Train the GAN
train_gan(data_folder, num_epochs, batch_size)