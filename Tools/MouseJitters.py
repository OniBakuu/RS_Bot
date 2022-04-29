import numpy as np
import pyautogui as pyg
import random
import mouse


def move_bezier(click_x, click_y, wiggle=True, min_duration=.01, max_duration=.045):
    """
    Moves mouse in a Bézier curve to desired point.
    Also adds some variance to curve y values to un-smooth the line
    """
    posx, posy = pyg.position()

    ran = 300
    p0, p1 = np.array([[posx, posy], [posx, posy + random.randint(-ran, ran)]])
    p2, p3 = np.array([[click_x, click_y + random.randint(-ran, ran)], [click_x, click_y]])

    bezier_curve = lambda t: (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3*(1-t) * t**2 * p2 + t**3 * p3

    points = np.array([bezier_curve(t) for t in np.linspace(0, 1, 50)])

    x, y = points[:, 0], points[:, 1]
    move_points = tuple(zip(x, y))

    duration = random.uniform(min_duration, max_duration)

    if wiggle:
        for pt in move_points:
            mouse.move(pt[0], pt[1] + random.uniform(0, 10), duration=duration)
    else:
        for pt in move_points:
            mouse.move(pt[0], pt[1], duration=duration)


def realistic_click(x, y):
    # Chances to double click or right click
    pass

