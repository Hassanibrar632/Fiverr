import os
import cv2

for dirname, _, filenamess in os.walk("./IMAGES/"):
    for i in range(5, 6):
        filenames = [file.split(".")[0] for file in filenamess if f"nfl_football_{str(i)}_" in file]
        input(f"starting... {i} set")
        print(len(filenames))
        for file in filenames[:50:5]:
            img = cv2.imread(f"./IMAGES/{file}.jpg")
            with open(f"./LABELS/{file}.txt", 'r') as file:
                annotations = file.readlines()
                h, w, _ = img.shape
                for annotation in annotations:
                    values = annotation.strip().split()
                    x_center, y_center, width, height = map(float, values[1:])

                    x_min = int((x_center - width / 2) * w)
                    y_min = int((y_center - height / 2) * h)
                    x_max = int((x_center + width / 2) * w)
                    y_max = int((y_center + height / 2) * h)

                    img = cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            cv2.imshow("Image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
