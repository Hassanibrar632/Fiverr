import cv2
import os
import numpy as np
from tqdm import tqdm
import shutil

def Scorebug(video_dir):
    for dirname, _, filenames in os.walk(video_dir):
        for file in tqdm(filenames):

            # Open video file
            cap = cv2.VideoCapture(f"{dirname}/{file}")
            
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            # Set timer parameters
            timer_interval = 1  # in seconds
            frame_rate = cap.get(cv2.CAP_PROP_FPS)
            frame_interval = int(frame_rate * timer_interval)

            # Set the position to the last frame
            cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)
            os.mkdir(f'{file.split(".")[0]}')
            # If video is not open then give error
            if not cap.isOpened():
                print("Error opening video file")
            else:
                # Start reading and processing the video
                index = 0
                while cap.isOpened():
                    ret, frame = cap.read()
                    if ret:
                        cv2.imwrite(f'{file.split(".")[0]}/{file.split(".")[0]}_{index}.jpg', frame)
                        index += 1
                    if total_frames <=5:
                        break
                    total_frames -= frame_interval
                    cap.set(cv2.CAP_PROP_POS_FRAMES, max(total_frames - 1, 0))
                cap.release()
            shutil.move(f"{dirname}/{file}", f'{file.split(".")[0]}/{file}')
    return

if __name__ == '__main__':
    Scorebug(video_dir='./z/')