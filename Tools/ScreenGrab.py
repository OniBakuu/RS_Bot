import pyautogui as pyg
import cv2 as cv


def grab_screen():
    """Screenshots Screen"""
    # This should just grab the default screen
    pyg.screenshot("Screen.png", (0, 0, 2525, 1400))
    img = cv.imread("Screen.png")
    return img


def grab_minimap():
    pyg.screenshot("minimap.png", (2200, 23, 320, 285))
    img = cv.imread("minimap.png")
    return img


def grab_chat():
    pyg.screenshot("chatbox.png", (0, 1150, 776, 210))
    img = cv.imread("chatbox.png")
    return img


def get_mouse_coords():
    print(pyg.position())


get_mouse_coords()