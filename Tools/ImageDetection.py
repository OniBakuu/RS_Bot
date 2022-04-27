import random

import cv2 as cv
import numpy as np
import pyautogui as pyg
import Tools.MouseJitters as mj
import time
import Tools.ScreenGrab as screengrab


def template_match():
    img_rgb = cv.imread('colorContourTest.jpg')

    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    template1 = cv.imread('levelButton.jpg', 0)

    w, h = template1.shape[::-1]

    result = cv.matchTemplate(img_gray, template1, cv.TM_CCOEFF_NORMED)

    thresh = .9

    locCoord = np.where(result >= thresh)

    for pt in zip(*locCoord[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    cv.imshow('Detected', img_rgb)
    cv.waitKey(0)


def get_object_contours():
    """Gets contours of objects on screen"""
    img_rgb = screengrab.grab_screen()
    hsv = cv.cvtColor(img_rgb, cv.COLOR_BGR2HSV)

    # blue contour
    lower_blue = np.array([120, 60, 50])
    upper_blue = np.array([130, 255, 255])

    purple = cv.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv.findContours(purple, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # cv.imshow('detection', img_rgb)
    # cv.waitKey(0)
    return contours


def test_contour_matching():
    img_rgb = screengrab.grab_screen()
    hsv = cv.cvtColor(img_rgb, cv.COLOR_BGR2HSV)

    lower_blue = np.array([120, 60, 50])
    upper_blue = np.array([130, 255, 255])

    blue = cv.inRange(hsv, lower_blue, upper_blue)
    conts, _ = cv.findContours(blue, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print(len(conts))
    for c in conts:
        cv.drawContours(img_rgb, [c], -1, (0, 255, 0), 5)

    cv.imshow('detect', img_rgb)
    cv.waitKey(0)


def get_closet_marked_object():
    screen_center_x = 2560/2
    screen_center_y = 1440/2
    contours = get_object_contours()

    distance = []

    for cont in contours:
        x, y, w, h = cv.boundingRect(cont)
        distance.append(np.sqrt((x - screen_center_x)**2 + (y - screen_center_y) ** 2))

    min_value = min(distance)
    min_index = distance.index(min_value)

    x, y, w, h = cv.boundingRect(contours[min_index])
    x_center = round(x + w / 2)
    y_center = round(y + h / 2)

    if distance[0] < 100:
        return []

    return[x_center, y_center]


def click_path():
    path = [[1321, 152], [1747, 177], [773, 631]]
    for point in path:
        print(point[0], ":", point[1])
        click_at_coord(point[0], point[1])
        time.sleep(10)


def click_at_coord(click_x, click_y, left_click=True):
    """Moves and clicks at given coord"""
    mj.move_bezier(click_x, click_y, False)

    if left_click:
        pyg.leftClick(click_x, click_y)
    else:
        pyg.rightClick(click_x, click_y)

