from datetime import date
from datetime import datetime
import pathlib
import random
import string


min = 0
col_max = 256
name_length = 16

class Tech:

    def random_int(self, min, max):
        return random.randint(min, max)

    def random_color(self):
        return random.randint(min, col_max), random.randint(min, col_max), random.randint(min, col_max)

    def create_random_filename(self):
        directory = f"../masterpieces/{date.today()}/{datetime.now().time().hour}/"
        filename = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(name_length)) + ".jpg"
        if not pathlib.Path(directory).exists():
            pathlib.Path(directory).mkdir(parents=True)
        else:
            pass
        filepath = f"{directory}{filename}"
        text = f"File: {filepath}"
        return filepath
