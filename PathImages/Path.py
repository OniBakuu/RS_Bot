import os
import random
import time

import cv2 as cv
import pyautogui

import Tools.ImageDetection as id


def walk_VET_VEB_path():
    directory = 'A:/Jaeger/UnityProjects/RS_Bot/PathImages/VarrockEastTrees_VarrockEastBank/'
    for file in os.listdir(directory):
        print(file)
        file_path = directory + file
        x, y = id.get_map_coord(file_path)
        x_offset = random.uniform(1, 3)
        y_offset = random.uniform(1, 3)
        id.click_at_coord(x + 2200 + x_offset, y + 23 + y_offset)  # Offset since the screenshot is only the corner
        pyautogui.moveRel(0, 100, duration=.75)  # point can block the map and cause missed template match
        time.sleep(12)


def walk_VEB_VET_path():
    directory = 'A:/Jaeger/UnityProjects/RS_Bot/PathImages/VarrockEastBank_VarrockEastTrees/'
    for file in os.listdir(directory):
        print(file)
        file_path = directory + file
        x, y = id.get_map_coord(file_path)
        id.click_at_coord(x + 2200, y + 23)  # Offset since the screenshot is only the corner
        pyautogui.moveRel(0, 100, duration=.75)  # point can block the map and cause missed template match
        time.sleep(12)

