from datetime import date
from datetime import datetime
import pathlib
import random
import string

MIN_VALUE = 0  # Fixed: avoid shadowing built-in min()
COL_MAX = 256
NAME_LENGTH = 16


class Tech:

    def random_int(self, min, max):
        return random.randint(min, max)

    def random_color(self):
        return random.randint(MIN_VALUE, COL_MAX), random.randint(MIN_VALUE, COL_MAX), random.randint(MIN_VALUE, COL_MAX)

    def create_random_filename(self):
        # Fixed: use absolute path and better error handling
        base_dir = pathlib.Path(__file__).parent.parent
        directory = base_dir / "masterpieces" / str(date.today()) / str(datetime.now().time().hour)
        try:
            directory.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating directory: {e}")
            # Fallback to current directory
            directory = pathlib.Path(".")
        
        filename = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(NAME_LENGTH)) + ".jpg"
        filepath = directory / filename
        return str(filepath)
