import os
import cv2
from ultralytics import YOLO
import numpy as np

def run(file, model, output):
    cap = cv2.VideoCapture(file)
    model = YOLO(model)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file.")
        exit()

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can choose other codecs as well
    fps = cap.get(cv2.CAP_PROP_FPS)
    W, H = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)//2), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)//2)
    print(W, H)
    frame_size = (W, H)
    out = cv2.VideoWriter(output, fourcc, fps, frame_size)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Break the loop if no more frames are available
        if not ret:
            break

        # Display the current frame
        results = model(frame, conf=0.75)
        if len(results[0].boxes.xyxy) > 0:
            for i, _ in enumerate((results[0].boxes.cls)):
                box = results[0].boxes.xyxy[i]
                box = [int(value) for value in box.numpy()]
                x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
                cropped_image = np.array(frame)[y1:y2, x1:x2]
                reshaped_image = cv2.resize(cropped_image, (W, H))
                out.write(reshaped_image)
        
    # Release the video capture object and close the window
    cap.release()
    out.release()
    print("Cropped video saved at:", output)
    return


if __name__ == '__main__':
    run(r'.\Data\AALAJYTZ\AALAJYTZ.mp4', r'.\weights\best.pt', r'./Test_00.mp4')