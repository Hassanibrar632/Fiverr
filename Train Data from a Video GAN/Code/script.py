import os
import shutil
import tqdm

def split_data(folder):
    for dir, _, files in os.walk(folder):
        files = [file for file in files if 'jpg' in file]
        for file in tqdm.tqdm(files):
            shutil.move(os.path.join(dir, file), os.path.join('./Images', file))


if __name__ == '__main__':
    split_data('Data')