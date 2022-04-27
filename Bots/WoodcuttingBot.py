import random
import time
from Tools import ImageDetection as id


def cut_wood():
    while True:
        x, y = id.get_closet_marked_object()
        id.click_at_coord(x, y)
        time.sleep(random.randint(10-17))


cut_wood()
