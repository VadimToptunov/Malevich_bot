from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
import random
from Malevich.tech import Tech

color_scheme = "RGB"
min = 0


class AvantGuard:
    tech = Tech()

    def random_palette(self):
        colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black",
                  "blue", "blueviolet", "brown", "chocolate", "coral", "cornflowerblue",
                  "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgrey",
                  "darkgreen",
                  "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon",
                  "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet",
                  "deeppink",
                  "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen",
                  "fuchsia",
                  "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "grey", "green", "greenyellow", "honeydew",
                  "hotpink",
                  "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon",
                  "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgreen", "lightgray",
                  "lightgrey",
                  "lightpink",
                  "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue",
                  "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue",
                  "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen",
                  "mediumturquoise",
                  "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy",
                  "oldlace",
                  "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise",
                  "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple",
                  "rebeccapurple",
                  "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell",
                  "sienna",
                  "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan",
                  "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow",
                  "yellowgreen"]

        bw = ["black", "white"]

        palette = [colors, bw]
        return random.choice(palette)

    def generate_image(self, width, height, patch: bool, lines: bool, polygon: bool, eclipse: bool, rectangle: bool):
        image = Image.new(color_scheme, (width, height), self.random_color())
        draw = ImageDraw.Draw(image)
        if patch is True:
            for i in range(self.tech.random_int(min, height)):
                image.paste((self.random_color()), (
                    self.tech.random_int(min, width), self.tech.random_int(min, height),
                    self.tech.random_int(min, width),
                    self.tech.random_int(min, height)))

        for i in range(random.randint(min, 50)):
            if lines is True:
                draw.line(self.random_parameters(height), fill=ImageColor.getrgb(self.random_color()))
            else:
                pass
            if polygon is True:
                draw.polygon(self.random_polygon(width, height), fill=self.random_color(), outline=self.random_color())
            else:
                pass

        for j in range(random.randint(min, 5)):
            if eclipse is True:
                draw.ellipse(self.random_parameters(width), fill=ImageColor.getcolor(self.random_color(), color_scheme))
            else:
                pass

        for x in range(random.randint(min, 10)):
            if rectangle is True:
                draw.rectangle(self.random_parameters(width),
                               fill=ImageColor.getcolor(self.random_color(), color_scheme))
            else:
                pass
        image_file = self.tech.create_random_filename()
        image.save(image_file)
        return image_file

    def random_parameters(self, upper_range):
        return (random.randint(min, upper_range), random.randint(min, upper_range),
                random.randint(min, upper_range), random.randint(min, upper_range))

    def random_polygon(self, x, y):
        try:
            length = random.randint(2, 500)
            polygon_x = random.sample(range(1, x), length)
            polygon_y = random.sample(range(1, y), length)
            return polygon_x + polygon_y
        except Exception as error:
            print(error)
            pass

    def random_color(self):
        return random.choice(self.random_palette())
