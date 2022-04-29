import random

import cv2 as cv
import numpy as np
import pyautogui as pyg
import Tools.MouseJitters as mj
import time
import Tools.ScreenGrab as screengrab


def template_match_test():
    img_rgb = screengrab.grab_chat()

    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    #template1 = cv.imread('A:/Jaeger/UnityProjects/RS_Bot/PathImages/VarrockEastBank_VarrockEastTrees/landmark_0.png', 0)
    template1 = cv.imread('A:/Jaeger/UnityProjects/RS_Bot/Tools/invFull.png', 0)
    w, h = template1.shape[::-1]

    result = cv.matchTemplate(img_gray, template1, cv.TM_CCOEFF_NORMED)

    thresh = .8

    locCoord = np.where(result >= thresh)

    for pt in zip(*locCoord[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    cv.imshow('Detected', img_rgb)
    cv.waitKey(0)


def get_map_coord(file):
    """Gets the coord of matched point on minimap"""
    print(file)
    mini_map = screengrab.grab_minimap()
    map_gray = cv.cvtColor(mini_map, cv.COLOR_BGR2GRAY)
    img = cv.imread(file, 0)

    w, h = img.shape[::-1]
    result = cv.matchTemplate(map_gray, img, cv.TM_CCOEFF_NORMED)
    thresh = .7
    coord = np.where(result >= thresh)

    for pt in zip(*coord[::-1]):
        cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        point = [(pt[0] + w/2), (pt[1] + h/2)]
        print(point)
        return point


def get_template_coord(img_path, chat=False):
    screen = screengrab.grab_screen()
    if chat:
        screen = screengrab.grab_chat()
    screen = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
    img = cv.imread(img_path, 0)

    w, h = img.shape[::-1]
    result = cv.matchTemplate(screen, img, cv.TM_CCOEFF_NORMED)
    thresh = .8
    coord = np.where(result >= thresh)
    if chat:
        if np.amax(result) >= thresh:
            return True

    for pt in zip(*coord[::-1]):
        cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        point = [(pt[0] + w / 2), (pt[1] + h / 2)]
        print(point)
        return point


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
    """Gets coord of the closest object marked in Runelite"""
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


def click_at_coord(click_x, click_y, left_click=True, min_duration=.01, max_duration=.045):
    """Moves and clicks at given coord"""
    mj.move_bezier(click_x, click_y, min_duration=min_duration, max_duration=max_duration)

    if left_click:
        pyg.leftClick(click_x, click_y)
    else:
        pyg.rightClick(click_x, click_y)


def clear_game_chat():
    click_at_coord(139, 1381, False)
    pyg.leftClick(134, 1335, duration=.5)


def check_inv_full():
    path = 'A:/Jaeger/UnityProjects/RS_Bot/Tools/invFull.png'
    try:
        if get_template_coord(path, True):
            return True
    except TypeError:
        return False
    except AttributeError:
        return False


def bank_handling():
    """Deposits everything in inventory"""
    x, y = get_closet_marked_object()
    click_at_coord(x, y)
    click_at_coord(1342, 1110)
    time.sleep(random.uniform(1, 1.5))
    click_at_coord(1414, 48)
    time.sleep(random.uniform(1, 1.5))

# template_match_test()