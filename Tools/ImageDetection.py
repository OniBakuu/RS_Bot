import cv2 as cv
import numpy as np
import pyautogui
import ScreenGrab


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


def get_contours():
    """Gets contours of objects on screen"""
    img_rgb = ScreenGrab.grab_screen()

    # Purple contour
    lower_purp = np.array([130, 50, 130])
    upper_purp = np.array([190, 90, 190])

    purple = cv.inRange(img_rgb, lower_purp, upper_purp)

    contours, _ = cv.findContours(purple, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # cv.imshow('detection', img_rgb)
    # cv.waitKey(0)
    return contours


def get_closet_marked_object():
    screen_center_x = 2560/2
    screen_center_y = 1440/2
    contours = get_contours()

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


def click_at_coord(click_x, click_y, left_click=True):
    """Moves and clicks at given coord"""
    pyautogui.moveTo(click_x, click_y, 1.5)

    if left_click:
        pyautogui.leftClick(click_x, click_y)
    else:
        pyautogui.rightClick(click_x, click_y)


x, y = get_closet_marked_object()
click_at_coord(x, y)
