#!/usr/bin/python

import random
import string

import numpy as np
from PIL import Image

from Malevich.tech import Tech


class Magnet:

    def __init__(self, dX, dY):
        self.dX = dX
        self.dY = dY
        self.xArray = np.linspace(0.0, 1.0, dX).reshape((1, dX, 1))
        self.yArray = np.linspace(0.0, 1.0, dY).reshape((dY, 1, 1))
        self.tech = Tech()

    def randColor(self):
        return np.array([random.random(), random.random(), random.random()]).reshape((1, 1, 3))

    def getX(self):
        return self.xArray

    def getY(self):
        return self.yArray

    def safeDivide(self, a, b):
        return np.divide(a, np.maximum(b, 0.001))

    def buildImg(self, depth=0):
        functions = [(0, self.randColor),
                     (0, self.getX),
                     (0, self.getY),
                     (1, np.sin),
                     (1, np.cos),
                     (2, np.add),
                     (2, np.subtract),
                     (2, np.multiply),
                     (2, self.safeDivide)]
        depthMin = random.randint(2, 10)
        depthMax = random.randint(10, 30)

        funcs = [f for f in functions if
                 (f[0] > 0 and depth < depthMax) or
                 (f[0] == 0 and depth >= depthMin)]
        nArgs, func = random.choice(funcs)
        args = [self.buildImg(depth + 1) for n in range(nArgs)]
        return func(*args)

    def creaate_image(self):
        img = self.buildImg()

        # Ensure it has the right dimensions, dX by dY by 3
        img = np.tile(img, (int(self.dX / img.shape[0]), int(self.dY / img.shape[1]), int(3 / img.shape[2])))

        # Convert to 8-bit, send to PIL and save
        img8Bit = np.uint8(np.rint(img.clip(0.0, 1.0) * 255.0))
        Image.fromarray(img8Bit).save(self.tech.create_random_filename())
