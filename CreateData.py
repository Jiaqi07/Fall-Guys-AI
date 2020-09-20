import numpy as np
import cv2
import time
import os

from utils.grabscreen import grab_screen
from utils.getkeys import key_check


file_name = "C:/Users/programmer/Desktop/FallGuys/data/training_data.npy"
file_name2 = "C:/Users/programmer/Desktop/FallGuys/data/target_data.npy"


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    print(lower)
    upper = int(min(255, (1.0 + sigma) * v))
    print(upper)
    edged = cv2.Canny(image, lower, upper)
    # return the edged image
    return edged


def get_data():

    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets


def save_data(image_data, targets):
    np.save(file_name, image_data)
    np.save(file_name2, targets)


image_data, targets = get_data()
while True:
    keys = key_check()
    print("waiting press B to start")
    if keys == "B":
        print("Starting")
        break


count = 0
while True:
    count +=1
    last_time = time.time()
    # Grab Image GrayScale
    image = grab_screen(region=(50, 100, 799, 449))
    #cv2.imwrite(f"E:/examples/Full{count}.png", image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite(f"E:/examples/gray{count}.png", image)
    
    #GRAY = image
    image = cv2.Canny(image, threshold1=119, threshold2=250)
    #cv2.imwrite(f"E:/examples/Lines{count}.png", image)
    
    # image = auto_canny(GRAY)
    # cv2.imwrite(f"E:/examples/LineAUTO{count}.png", image)

    image = cv2.resize(image, (224, 224))
    #cv2.imwrite(f"E:/examples/resize{count}.png", image)

    # Debug line to show image
    # cv2.imshow("AI Peak", image)
    # cv2.waitKey(1)

    # Convert to numpy array
    image = np.array(image)
    image_data.append(image)

    keys = key_check()
    targets.append(keys)
    if keys == "H":
        break

    print('loop took {} seconds'.format(time.time()-last_time))

save_data(image_data, targets)