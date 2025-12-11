import random

from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

from Malevich.utils.tech import Tech

color_scheme = "RGB"
MIN_VALUE = 0  # Fixed: avoid shadowing built-in min()


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
            # Fixed: create proper image for paste operation
            for i in range(self.tech.random_int(MIN_VALUE, height)):
                color = ImageColor.getrgb(self.random_color())
                # Fixed: clamp patch_size to fit within image dimensions
                max_patch_size = min(100, width, height)
                min_patch_size = min(10, max_patch_size)
                patch_size = random.randint(min_patch_size, max_patch_size)
                patch_img = Image.new(color_scheme, (patch_size, patch_size), color)
                x = self.tech.random_int(MIN_VALUE, max(MIN_VALUE, width - patch_size))
                y = self.tech.random_int(MIN_VALUE, max(MIN_VALUE, height - patch_size))
                image.paste(patch_img, (x, y))

        for i in range(random.randint(MIN_VALUE, 50)):
            if lines is True:
                draw.line(self.random_parameters(width, height), fill=ImageColor.getrgb(self.random_color()))
            else:
                pass
            if polygon is True:
                draw.polygon(self.random_polygon(width, height), fill=self.random_color(), outline=self.random_color())
            else:
                pass

        for j in range(random.randint(MIN_VALUE, 5)):
            if eclipse is True:  # Note: parameter name is 'eclipse' but should be 'ellipse'
                draw.ellipse(self.random_parameters(width, height), fill=ImageColor.getcolor(self.random_color(), color_scheme))
            else:
                pass

        for x in range(random.randint(MIN_VALUE, 10)):
            if rectangle is True:
                draw.rectangle(self.random_parameters(width, height),
                               fill=ImageColor.getcolor(self.random_color(), color_scheme))
            else:
                pass
        image_file = self.tech.create_random_filename()
        image.save(image_file)
        return image_file

    def random_parameters(self, width, height):
        """
        Generate random coordinates for drawing operations.
        Ensures coordinates are within image bounds and properly ordered.
        
        Args:
            width: Maximum x-coordinate (image width)
            height: Maximum y-coordinate (image height)
            
        Returns:
            Tuple of (x1, y1, x2, y2) coordinates within image bounds
            For rectangles and ellipses: x1 <= x2 and y1 <= y2
        """
        # Ensure valid ranges: pixel coordinates are [0, width-1] and [0, height-1]
        max_x = max(MIN_VALUE, width - 1)
        max_y = max(MIN_VALUE, height - 1)
        
        # Generate two x-coordinates and ensure x1 <= x2
        x1 = random.randint(MIN_VALUE, max_x)
        x2 = random.randint(MIN_VALUE, max_x)
        if x1 > x2:
            x1, x2 = x2, x1
        
        # Generate two y-coordinates and ensure y1 <= y2
        y1 = random.randint(MIN_VALUE, max_y)
        y2 = random.randint(MIN_VALUE, max_y)
        if y1 > y2:
            y1, y2 = y2, y1
        
        return (x1, y1, x2, y2)

    def random_polygon(self, x, y):
        try:
            # Fixed: limit length to available range, ensuring we don't sample more than available
            # Fixed: include coordinate 0 to allow polygons at image boundaries
            # Fixed: actual population size is x and y (not max(1, x)), so limit to min(x, y)
            actual_population_size = min(x, y)
            if actual_population_size < 2:
                # If not enough points available, return default polygon
                return [(x//4, y//4), (3*x//4, y//4), (3*x//4, 3*y//4), (x//4, 3*y//4)]
            max_length = min(500, actual_population_size)
            length = random.randint(2, max_length)
            # Ensure we don't try to sample more than the actual population size
            actual_length = min(length, actual_population_size)
            # Fixed: use range(0, x) instead of range(1, x) to include coordinate 0
            polygon_x = random.sample(range(0, x), actual_length)
            polygon_y = random.sample(range(0, y), actual_length)
            # Fixed: return list of coordinate tuples, not flat list
            return list(zip(polygon_x, polygon_y))
        except Exception as error:
            print(f"Error generating polygon: {error}")
            # Return default polygon if error
            return [(x//4, y//4), (3*x//4, y//4), (3*x//4, 3*y//4), (x//4, 3*y//4)]

    def random_color(self):
        return random.choice(self.random_palette())
