import random

from Malevich.magnet_image_generator import Magnet
from Malevich import avantguard

width = 1200
height = 1200
ag = avantguard.AvantGuard()
magnet = Magnet(width, height)


def generate_image():
    boolean = [True, False]
    return ag.generate_image(width, height, random.choice(boolean), random.choice(boolean),
                             random.choice(boolean),
                             random.choice(boolean), random.choice(boolean))


if __name__ == "__main__":
    for i in range(10):
        # Fix: choose function, not result
        random.choice([generate_image, magnet.create_image])()
