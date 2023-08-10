import os
import random as rand
import shutil
from tqdm import tqdm

def get_files_in_directory(directory):
    file_list = []
    for _, _, files in os.walk(directory):
        file_list.extend([file.split(".")[0] for file in files])
    print(len(file_list))
    return file_list

def val_test_train_split(file, train, test, val, output_folder):
    for _ in tqdm(range(val)):
        img =  file.pop(rand.randint(0, len(file)-1))
        shutil.copy2("./ALL_IMAGES/"+img+".jpg", f"{output_folder}/valid/images/")
        try:
            shutil.copy2("./ALL_LABELS/"+img+".txt", f"{output_folder}/valid/labels/")
        except:
            continue
    for _ in tqdm(range(test)):
        img =  file.pop(rand.randint(0, len(file)-1))
        shutil.copy2("./ALL_IMAGES/"+img+".jpg", f"{output_folder}/test/images/")
        try:
            shutil.copy2("./ALL_LABELS/"+img+".txt", f"{output_folder}/test/labels/")
        except:
            continue
    for index in tqdm(range(len(file))):
        shutil.copy2("./ALL_IMAGES/"+file[index]+".jpg", f"{output_folder}/train/images/")
        try:
            shutil.copy2("./ALL_LABELS/"+file[index]+".txt", f"{output_folder}/train/labels/")
        except:
            continue
    print("All done...")

# Set the random seed using the current time
rand.seed(int.from_bytes(os.urandom(4), byteorder='big'))

file = get_files_in_directory("./ALL_IMAGES")
val_size = int(len(file)*0.1)
test_size = int(len(file)*0.2)
train_size = len(file)-val_size-test_size
output_folder = "./DUMMY"
val_test_train_split(file, train_size, test_size, val_size, output_folder)