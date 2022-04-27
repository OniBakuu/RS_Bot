import random
import time
from Tools import ImageDetection as id
from PathImages import Path


def cut_wood():
    while True:
        x, y = id.get_closet_marked_object()
        id.click_at_coord(x, y)
        if id.check_inv_full():
            id.clear_game_chat()
            Path.walk_VET_VEB_path()
            id.bank_handling()
            Path.walk_VEB_VET_path()

        time.sleep(random.randint(10, 15))


cut_wood()
