import os
import shutil
import tqdm

def Create(folder, lable, D_I, D_L, cond):
    for dir, _, files in os.walk(folder):
        files = [file.split('.')[0] for file in files if file.startswith(cond)]
        for file in tqdm.tqdm(files):
            shutil.move(os.path.join(dir, f'{file}.jpg'), os.path.join(D_I, f'{file}.jpg'))
            try:
                shutil.move(os.path.join(lable, f'{file}.txt'), os.path.join(D_L, f'{file}.txt'))
            except:
                continue


if __name__ == '__main__':
    Create('Images/', 'Lables', 'ALL_IMAGES', 'ALL_LABLES', 'AS')