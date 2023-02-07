import random
import pyautogui as pyauto

for i in range(30):
    h = random.randint(0, 1080)
    w = random.randint(0, 1920)
    pyauto.click(h, w, duration=0.3)
    pyauto.hotkey('winleft', 'm')
