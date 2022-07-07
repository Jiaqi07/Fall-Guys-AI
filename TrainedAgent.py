import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
import ctypes
import time
import cv2
from utils.grabscreen import grab_screen
# from utils.directkeys import PressKey, ReleaseKey, W, D, A
from fastai.vision.all import *


def label_func(x): return x.parent.name


learn_inf = load_learner("C:/trainData/export.pkl")
print("loaded learner")

# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

# Hold down W no matter what!
keyboard.press('w')

# Randomly pick action then sleep.
# 0 do nothing release everything ( except W )
# 1 hold left
# 2 hold right
# 3 Press Jump

while True:

    image = grab_screen(region=(50, 100, 799, 449))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image, (224, 224))
    # cv2.imshow("Fall", image)
    # cv2.waitKey(1)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]
    # print(result[2][0].item(), result[2][1].item(), result[2][2].item(), result[2][3].item())

    # action = random.randint(0,3)

    if action == "Jump" or result[2][0] > .1:
        print(f"JUMP! - {result[1]}")
        keyboard.press("space")
        keyboard.release("a")
        keyboard.release("d")
        time.sleep(sleepy)

    if action == "Nothing":
        # print("Doing nothing....")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == "Left":
        print(f"LEFT! - {result[1]}")
        keyboard.press("a")
        keyboard.release("d")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == "Right":
        print(f"Right! - {result[1]}")
        keyboard.press("d")
        keyboard.release("a")
        keyboard.release("space")
        time.sleep(sleepy)

    elif action == "LeftClick":
        print(f"Attack! - {result[1]}")
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        keyboard.release("space")
        keyboard.release("a")
        keyboard.release("d")
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
        time.sleep(sleepy)

    # elif action == "MoveCursor":
    #     print(f"JUMP! - {result[1]}")
    #     ctypes.windll.user32.SetCursorPos(x, y)  # FIGURE OUT HOW TO STORE VALUES FOR A CURSAOR MOVEMENT
    #     keyboard.release("space")
    #     keyboard.release("a")
    #     keyboard.release("d")
    #     time.sleep(sleepy)

    # End simulation by hitting h
    keys = key_check()
    if keys == "H":
        break

keyboard.release('W')
