import pyautogui as pyg
import cv2 as cv


def grab_screen():
    """Screenshots Screen"""
    # This should just grab the default screen
    pyg.screenshot("Screen.png")
    img = cv.imread("Screen.png")
    return img
