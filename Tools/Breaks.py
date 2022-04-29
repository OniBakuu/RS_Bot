import random
import time


class DoBreaks:
    take_break = False
    start_time = 0
    break_after = 0

    def __int__(self):
        self.break_after = random.randint(7200, 10800)
        self.start_time = time.time()

    def check_for_break(self):
        cur_elapsed = time.time() - self.start_time
        if cur_elapsed > self.break_after:
            self.take_break = True
