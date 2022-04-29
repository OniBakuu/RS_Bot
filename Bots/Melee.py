import random
import time
from Tools import ImageDetection as id
from PathImages import Path


def attack():
    while True:
        x, y = id.get_closet_marked_object()
        id.click_at_coord(x, y, min_duration=.0015, max_duration=.0055)
        time.sleep(random.randint(15, 20))


attack()
