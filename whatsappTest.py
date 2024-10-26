from pyautogui import press,write
from random import choice
import time
time.sleep(5)
hits=["Georgia!!!!!","Miss me"]
for i in range(50):
     for j in hits:
        write(j)
        press("enter")
        time.sleep(0.5)


