import pyautogui
import time

def press_left_key():
    
    pyautogui.keyDown('left')
    time.sleep(0.5)
    pyautogui.keyUp('left')

def press_right_key():

    pyautogui.keyDown('right')
    time.sleep(0.5)
    pyautogui.keyUp('right')

def press_space_key():

    pyautogui.keyDown('space')
    time.sleep(0.5)
    pyautogui.keyUp('space')
