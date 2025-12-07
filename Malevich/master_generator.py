"""
Master generator based on techniques of famous artists from the last 800 years.
Applies real artistic methods: composition, color theory, brushstroke techniques.
All documentation in English.
"""
import random
import math
from typing import Tuple, List, Optional, Dict
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops


class MasterGenerator:
    """
    Advanced generator applying techniques from famous artists:
    - Renaissance: perspective, golden ratio, chiaroscuro
    - Baroque: dynamic composition, dramatic lighting
    - Impressionism: short brushstrokes, light capture
    - Post-Impressionism: expressive brushstrokes, vibrant colors
    - Cubism: geometric fragmentation, multiple perspectives
    - Surrealism: dreamlike elements, impossible geometry
    - Suprematism: pure geometric forms
    - Abstract Expressionism: action painting, color fields
    """
    
    # Color palettes based on historical art movements
    ART_PALETTES: Dict[str, List[Tuple[int, int, int]]] = {
        # Renaissance: earthy tones, natural colors
        'renaissance': [
            (139, 90, 43), (101, 67, 33), (160, 82, 45),
            (205, 133, 63), (139, 69, 19), (85, 107, 47),
            (72, 61, 139), (105, 105, 105), (176, 196, 222)
        ],
        # Baroque: rich, dramatic colors with high contrast
        'baroque': [
            (139, 0, 0), (0, 0, 139), (139, 69, 19),
            (25, 25, 112), (184, 134, 11), (139, 0, 139),
            (0, 0, 0), (255, 255, 255), (128, 128, 128)
        ],
        # Impressionism: light, bright colors, pastels
        'impressionist': [
            (255, 250, 240), (255, 228, 196), (255, 218, 185),
            (176, 224, 230), (255, 182, 193), (221, 160, 221),
            (255, 239, 213), (240, 248, 255), (255, 228, 225)
        ],
        # Post-Impressionism (Van Gogh): vibrant, intense colors
        'post_impressionist': [
            (255, 215, 0), (255, 140, 0), (255, 69, 0),
            (50, 205, 50), (0, 191, 255), (138, 43, 226),
            (220, 20, 60), (255, 20, 147), (255, 255, 0)
        ],
        # Cubism (Picasso): muted earth tones, grays
        'cubist': [
            (139, 90, 43), (101, 67, 33), (160, 82, 45),
            (205, 133, 63), (139, 69, 19), (85, 107, 47),
            (72, 61, 139), (105, 105, 105), (128, 128, 128)
        ],
        # Surrealism (Dali): dreamlike, vibrant, unexpected
        'surrealist': [
            (255, 255, 0), (255, 165, 0), (255, 20, 147),
            (0, 191, 255), (138, 43, 226), (255, 0, 127),
            (0, 255, 127), (255, 192, 203), (255, 218, 185)
        ],
        # Suprematism (Malevich): pure, bold colors
        'suprematist': [
            (0, 0, 0), (255, 255, 255), (255, 0, 0),
            (0, 0, 255), (255, 255, 0), (0, 255, 0)
        ],
        # Abstract Expressionism (Pollock, Rothko): bold, emotional
        'abstract_expressionist': [
            (255, 0, 0), (0, 0, 0), (255, 255, 255),
            (255, 255, 0), (0, 0, 255), (255, 0, 255),
            (0, 255, 255), (128, 0, 128), (139, 69, 19)
        ],
        # Expressionism (Munch): emotional, intense
        'expressionist': [
            (255, 69, 0), (255, 140, 0), (255, 215, 0),
            (50, 205, 50), (0, 191, 255), (138, 43, 226),
            (220, 20, 60), (255, 20, 147), (139, 0, 0)
        ]
    }
    
    def __init__(self, width: int = 1080, height: int = 1080):
        """
        Initialize generator.
        
        Args:
            width: Image width
            height: Image height
        """
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        # Golden ratio for composition
        self.golden_ratio = 1.618
    
    def generate(self, style: str = 'auto', palette_name: Optional[str] = None) -> Image.Image:
        """
        Generate image in specified artistic style.
        
        Args:
            style: Art style ('renaissance', 'baroque', 'impressionist', 
                   'post_impressionist', 'cubist', 'surrealist', 
                   'suprematist', 'abstract_expressionist', 'expressionist', 'auto')
            palette_name: Palette name from ART_PALETTES
            
        Returns:
            PIL Image object
        """
        if style == 'auto':
            style = random.choice(list(self.ART_PALETTES.keys()))
        
        palette = self._get_palette(palette_name, style)
        image = Image.new('RGB', (self.width, self.height), self._get_background_color(palette))
        
        # Apply style-specific generation
        if style == 'renaissance':
            image = self._create_renaissance_composition(image, palette)
        elif style == 'baroque':
            image = self._create_baroque_composition(image, palette)
        elif style == 'impressionist':
            image = self._create_impressionist_composition(image, palette)
        elif style == 'post_impressionist':
            image = self._create_post_impressionist_composition(image, palette)
        elif style == 'cubist':
            image = self._create_cubist_composition(image, palette)
        elif style == 'surrealist':
            image = self._create_surrealist_composition(image, palette)
        elif style == 'suprematist':
            image = self._create_suprematist_composition(image, palette)
        elif style == 'abstract_expressionist':
            image = self._create_abstract_expressionist_composition(image, palette)
        elif style == 'expressionist':
            image = self._create_expressionist_composition(image, palette)
        
        # Apply final touches based on style
        image = self._apply_style_finish(image, style)
        return image
    
    def _get_palette(self, palette_name: Optional[str], style: str) -> List[Tuple[int, int, int]]:
        """Get color palette based on style."""
        if palette_name and palette_name in self.ART_PALETTES:
            return self.ART_PALETTES[palette_name]
        
        style_palette_map = {
            'renaissance': 'renaissance',
            'baroque': 'baroque',
            'impressionist': 'impressionist',
            'post_impressionist': 'post_impressionist',
            'cubist': 'cubist',
            'surrealist': 'surrealist',
            'suprematist': 'suprematist',
            'abstract_expressionist': 'abstract_expressionist',
            'expressionist': 'expressionist'
        }
        
        palette_key = style_palette_map.get(style, 'surrealist')
        return self.ART_PALETTES.get(palette_key, self.ART_PALETTES['surrealist'])
    
    def _get_background_color(self, palette: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
        """Select background color from palette."""
        weights = []
        for color in palette:
            brightness = sum(color) / 3
            if brightness < 50 or brightness > 200:
                weights.append(3)
            else:
                weights.append(1)
        return random.choices(palette, weights=weights)[0]
    
    def _create_renaissance_composition(self, image: Image.Image,
                                       palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Renaissance style: perspective, golden ratio, chiaroscuro (light/shadow).
        Inspired by Leonardo da Vinci, Michelangelo.
        """
        draw = ImageDraw.Draw(image)
        
        # Use golden ratio for composition
        golden_x = int(self.width / self.golden_ratio)
        golden_y = int(self.height / self.golden_ratio)
        
        # Create geometric forms with perspective
        num_elements = random.randint(3, 6)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            
            # Place elements using golden ratio
            if random.random() < 0.7:
                x = random.choice([golden_x, self.width - golden_x, self.center_x])
                y = random.choice([golden_y, self.height - golden_y, self.center_y])
            else:
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
            
            # Create perspective effect (forms get smaller with distance)
            size = random.randint(self.width // 15, self.width // 6)
            perspective_factor = 1.0 - (y / self.height) * 0.5
            size = int(size * perspective_factor)
            
            # Draw geometric forms (circles, rectangles, triangles)
            shape = random.choice(['circle', 'rectangle', 'triangle'])
            
            if shape == 'circle':
                # Add chiaroscuro effect (light/shadow)
                self._draw_with_chiaroscuro(draw, x, y, size, color, 'circle')
            elif shape == 'rectangle':
                self._draw_with_chiaroscuro(draw, x, y, size, color, 'rectangle')
            else:  # triangle
                points = [
                    (x, y - size),
                    (x - size, y + size),
                    (x + size, y + size)
                ]
                draw.polygon(points, fill=color, outline=color)
        
        # Add perspective lines
        for _ in range(random.randint(2, 4)):
            color = random.choice(palette)
            # Vanishing point perspective
            vp_x = self.center_x + random.randint(-self.width//4, self.width//4)
            vp_y = self.height + random.randint(0, self.height//4)
            
            for i in range(3):
                start_x = random.randint(0, self.width)
                start_y = random.randint(0, self.height//2)
                draw.line([(start_x, start_y), (vp_x, vp_y)], fill=color, width=2)
        
        return image
    
    def _create_baroque_composition(self, image: Image.Image,
                                   palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Baroque style: dynamic composition, dramatic chiaroscuro, emotional intensity.
        Inspired by Caravaggio, Rembrandt.
        """
        draw = ImageDraw.Draw(image)
        
        # Create dramatic lighting (strong light/dark contrast)
        # Add light source effect
        light_x = random.randint(0, self.width)
        light_y = random.randint(0, self.height)
        
        # Create radial gradient for light source
        light_color = (255, 255, 200)
        dark_color = (20, 20, 20)
        image = self._create_radial_gradient(image, light_color, dark_color,
                                            center_x=light_x, center_y=light_y)
        
        # Add dynamic, diagonal elements
        num_elements = random.randint(4, 8)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            
            # Diagonal, dynamic placement
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = x1 + random.randint(-self.width//2, self.width//2)
            y2 = y1 + random.randint(-self.height//2, self.height//2)
            
            # Thick, expressive lines
            thickness = random.randint(3, 12)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=thickness)
            
            # Add dramatic forms
            if random.random() < 0.5:
                size = random.randint(self.width // 20, self.width // 8)
                draw.ellipse([x1 - size, y1 - size, x1 + size, y1 + size],
                           fill=color, outline=color, width=2)
        
        return image
    
    def _create_impressionist_composition(self, image: Image.Image,
                                         palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Impressionism: short brushstrokes, light capture, broken color.
        Inspired by Monet, Renoir.
        """
        draw = ImageDraw.Draw(image)
        
        # Create impressionist brushstrokes (short, visible strokes)
        num_strokes = random.randint(200, 400)
        
        for _ in range(num_strokes):
            color = random.choice(palette)
            
            # Short brushstrokes
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            
            # Vary stroke direction and length
            angle = random.uniform(0, 2 * math.pi)
            length = random.randint(5, 25)
            x2 = int(x + length * math.cos(angle))
            y2 = int(y + length * math.sin(angle))
            
            # Vary thickness
            thickness = random.randint(1, 4)
            draw.line([(x, y), (x2, y2)], fill=color, width=thickness)
        
        # Add light, airy forms
        for _ in range(random.randint(3, 6)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 20, self.width // 10)
            
            # Soft, blurred circles
            draw.ellipse([x - size, y - size, x + size, y + size],
                        fill=color, outline=color)
        
        # Apply soft blur to simulate impressionist technique
        image = image.filter(ImageFilter.GaussianBlur(radius=1.0))
        
        return image
    
    def _create_post_impressionist_composition(self, image: Image.Image,
                                              palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Post-Impressionism: expressive brushstrokes, vibrant colors, emotional intensity.
        Inspired by Van Gogh.
        """
        draw = ImageDraw.Draw(image)
        
        # Create expressive, swirling brushstrokes
        num_strokes = random.randint(150, 300)
        
        for _ in range(num_strokes):
            color = random.choice(palette)
            
            # Swirling, curved strokes
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            
            # Create curved stroke
            points = []
            for t in np.linspace(0, 1, 10):
                angle = 2 * math.pi * t * random.uniform(1, 3)
                radius = random.randint(10, 40) * t
                px = int(x + radius * math.cos(angle))
                py = int(y + radius * math.sin(angle))
                points.append((px, py))
            
            # Draw connected strokes
            for i in range(len(points) - 1):
                thickness = random.randint(2, 6)
                draw.line([points[i], points[i+1]], fill=color, width=thickness)
        
        # Add bold, vibrant forms
        for _ in range(random.randint(3, 7)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 15, self.width // 6)
            
            # Bold circles or stars
            if random.random() < 0.7:
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=color, width=3)
            else:
                # Star-like form
                num_points = random.randint(5, 8)
                points = []
                for i in range(num_points * 2):
                    angle = math.pi * i / num_points
                    r = size if i % 2 == 0 else size // 2
                    px = int(x + r * math.cos(angle))
                    py = int(y + r * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=color)
        
        return image
    
    def _create_cubist_composition(self, image: Image.Image,
                                  palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Cubism: geometric fragmentation, multiple perspectives, angular forms.
        Inspired by Picasso, Braque.
        """
        draw = ImageDraw.Draw(image)
        
        # Create fragmented geometric forms
        num_fragments = random.randint(12, 25)
        
        for _ in range(num_fragments):
            color = random.choice(palette)
            
            # Multiple perspective points
            if random.random() < 0.6:
                third_w = self.width // 3
                third_h = self.height // 3
                x = random.choice([third_w, third_w * 2, self.center_x])
                y = random.choice([third_h, third_h * 2, self.center_y])
            else:
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
            
            size = random.randint(self.width // 20, self.width // 5)
            
            # Angular, fragmented polygons
            sides = random.randint(3, 7)
            points = []
            for i in range(sides):
                angle = 2 * math.pi * i / sides + random.uniform(-0.3, 0.3)
                offset = size * random.uniform(0.7, 1.3)
                px = int(x + offset * math.cos(angle))
                py = int(y + offset * math.sin(angle))
                points.append((px, py))
            
            draw.polygon(points, fill=color, outline=color, width=2)
        
        # Add overlapping lines for depth
        for _ in range(random.randint(8, 18)):
            color = random.choice(palette)
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=random.randint(1, 3))
        
        return image
    
    def _create_surrealist_composition(self, image: Image.Image,
                                      palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Surrealism: dreamlike elements, melting forms, impossible geometry.
        Inspired by Dali, Magritte.
        """
        draw = ImageDraw.Draw(image)
        
        # Create dreamlike, impossible forms
        num_elements = random.randint(4, 10)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            
            element_type = random.choice(['melt', 'impossible', 'floating', 'distorted'])
            
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 15, self.width // 4)
            
            if element_type == 'melt':
                # Melting/dripping effect (Dali's clocks)
                base_y = y
                points = []
                for i in range(20):
                    px = x + (i - 10) * size // 10
                    melt_factor = math.exp(-((i - 10) ** 2) / 15)
                    py = base_y + size * melt_factor * random.uniform(0.8, 1.3)
                    points.append((int(px), int(py)))
                draw.polygon(points + [(x, base_y)], fill=color, outline=color)
            
            elif element_type == 'impossible':
                # Impossible geometry (Escher-like)
                sides = random.randint(4, 6)
                points = []
                for i in range(sides):
                    angle = 2 * math.pi * i / sides
                    perspective = 1 + 0.4 * math.sin(angle * 2)
                    px = int(x + size * perspective * math.cos(angle))
                    py = int(y + size * perspective * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=color, width=2)
            
            elif element_type == 'floating':
                # Floating, disconnected elements
                for _ in range(random.randint(2, 4)):
                    offset_x = random.randint(-size, size)
                    offset_y = random.randint(-size, size)
                    draw.ellipse([x + offset_x - size//3, y + offset_y - size//3,
                                 x + offset_x + size//3, y + offset_y + size//3],
                                fill=color, outline=color)
            
            else:  # distorted
                # Distorted, warped shapes
                points = []
                for i in range(8):
                    angle = 2 * math.pi * i / 8
                    distortion = 1 + 0.5 * math.sin(angle * 3)
                    px = int(x + size * distortion * math.cos(angle))
                    py = int(y + size * distortion * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=color)
        
        # Add dreamlike gradients
        if random.random() < 0.6:
            base_color = random.choice(palette)
            # Fixed: handle case where all colors are identical
            different_colors = [c for c in palette if c != base_color]
            if different_colors:
                target_color = random.choice(different_colors)
            else:
                # If all colors are the same, create a slightly modified version
                target_color = tuple(min(255, max(0, c + random.randint(-30, 30))) for c in base_color)
            image = self._create_radial_gradient(image, base_color, target_color,
                                                center_x=random.randint(0, self.width),
                                                center_y=random.randint(0, self.height))
        
        return image
    
    def _create_suprematist_composition(self, image: Image.Image,
                                       palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Suprematism: pure geometric forms, minimalism, bold colors.
        Inspired by Malevich.
        """
        draw = ImageDraw.Draw(image)
        
        # Minimal geometric forms
        num_elements = random.randint(3, 8)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            
            # Use golden ratio for placement
            golden_x = int(self.width / self.golden_ratio)
            golden_y = int(self.height / self.golden_ratio)
            
            if random.random() < 0.7:
                x = random.choice([golden_x, self.width - golden_x, self.center_x])
                y = random.choice([golden_y, self.height - golden_y, self.center_y])
            else:
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
            
            size = random.randint(self.width // 12, self.width // 4)
            
            shape = random.choice(['square', 'circle', 'rectangle', 'triangle', 'cross'])
            
            if shape == 'square':
                draw.rectangle([x - size//2, y - size//2, x + size//2, y + size//2],
                             fill=color, outline=color, width=3)
            elif shape == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=color, width=3)
            elif shape == 'rectangle':
                w = size * random.uniform(1.5, 2.5)
                h = size * random.uniform(0.5, 1.0)
                draw.rectangle([x - w//2, y - h//2, x + w//2, y + h//2],
                             fill=color, outline=color, width=3)
            elif shape == 'triangle':
                points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
                draw.polygon(points, fill=color, outline=color, width=3)
            else:  # cross
                # Draw cross
                thickness = size // 3
                draw.rectangle([x - size, y - thickness//2, x + size, y + thickness//2],
                             fill=color, outline=color)
                draw.rectangle([x - thickness//2, y - size, x + thickness//2, y + size],
                             fill=color, outline=color)
        
        return image
    
    def _create_abstract_expressionist_composition(self, image: Image.Image,
                                                  palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Abstract Expressionism: action painting, color fields, spontaneous marks.
        Inspired by Pollock, Rothko.
        """
        draw = ImageDraw.Draw(image)
        
        # Pollock-style drips and splatters
        if random.random() < 0.6:
            num_drips = random.randint(50, 150)
            for _ in range(num_drips):
                color = random.choice(palette)
                
                # Drip paths
                start_x = random.randint(0, self.width)
                start_y = random.randint(0, self.height // 2)
                
                # Curved drip path
                points = []
                for i in range(20):
                    x = start_x + random.randint(-5, 5)
                    y = start_y + i * random.randint(3, 8)
                    if y > self.height:
                        break
                    points.append((x, y))
                
                # Draw drip
                for i in range(len(points) - 1):
                    thickness = random.randint(1, 4)
                    draw.line([points[i], points[i+1]], fill=color, width=thickness)
        
        # Rothko-style color fields
        num_fields = random.randint(2, 4)
        field_height = self.height // num_fields
        
        for i in range(num_fields):
            color = random.choice(palette)
            y_start = i * field_height
            y_end = (i + 1) * field_height
            
            # Create gradient-like color field
            for y in range(y_start, y_end):
                # Slight color variation
                variation = random.randint(-10, 10)
                r = max(0, min(255, color[0] + variation))
                g = max(0, min(255, color[1] + variation))
                b = max(0, min(255, color[2] + variation))
                draw.line([(0, y), (self.width, y)], fill=(r, g, b), width=1)
        
        # Add spontaneous marks
        for _ in range(random.randint(20, 50)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(2, 15)
            draw.ellipse([x - size, y - size, x + size, y + size], fill=color)
        
        return image
    
    def _create_expressionist_composition(self, image: Image.Image,
                                        palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Expressionism: emotional intensity, distorted forms, bold colors.
        Inspired by Munch, Kirchner.
        """
        draw = ImageDraw.Draw(image)
        
        # Bold, emotional forms
        num_elements = random.randint(6, 15)
        
        for _ in range(num_elements):
            # Choose from extreme colors
            if random.random() < 0.5:
                bright_colors = [c for c in palette if sum(c) / 3 > 200 or sum(c) / 3 < 50]
                color = random.choice(bright_colors if bright_colors else palette)
            else:
                color = random.choice(palette)
            
            element_type = random.choice(['swirl', 'wave', 'burst', 'line', 'form'])
            
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 20, self.width // 5)
            
            if element_type == 'swirl':
                # Swirling, emotional patterns
                points = []
                for t in np.linspace(0, 3 * math.pi, 50):
                    radius = size * (1 - t / (3 * math.pi))
                    px = int(x + radius * math.cos(t))
                    py = int(y + radius * math.sin(t))
                    points.append((px, py))
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i+1]], fill=color, width=random.randint(3, 8))
            
            elif element_type == 'wave':
                # Wavy, emotional lines
                points = []
                for i in range(30):
                    px = x + (i * size // 15)
                    py = y + size * math.sin(i * 0.5) * random.uniform(0.8, 1.5)
                    points.append((int(px), int(py)))
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i+1]], fill=color, width=random.randint(4, 10))
            
            elif element_type == 'burst':
                # Radial burst
                num_rays = random.randint(8, 16)
                for i in range(num_rays):
                    angle = 2 * math.pi * i / num_rays
                    x2 = int(x + size * math.cos(angle))
                    y2 = int(y + size * math.sin(angle))
                    draw.line([(x, y), (x2, y2)], fill=color, width=random.randint(3, 7))
            
            elif element_type == 'line':
                # Bold, expressive lines
                x2 = x + random.randint(-self.width//2, self.width//2)
                y2 = y + random.randint(-self.height//2, self.height//2)
                draw.line([(x, y), (x2, y2)], fill=color, width=random.randint(5, 15))
            
            else:  # form
                # Distorted forms
                sides = random.randint(3, 8)
                points = []
                for i in range(sides):
                    angle = 2 * math.pi * i / sides
                    distortion = 1 + 0.4 * math.sin(angle * 2)
                    px = int(x + size * distortion * math.cos(angle))
                    py = int(y + size * distortion * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=color, width=2)
        
        return image
    
    def _draw_with_chiaroscuro(self, draw: ImageDraw.Draw, x: int, y: int,
                               size: int, color: Tuple[int, int, int], shape: str):
        """Draw shape with chiaroscuro (light/shadow) effect."""
        # Create lighter and darker versions
        light_color = tuple(min(255, c + 40) for c in color)
        dark_color = tuple(max(0, c - 40) for c in color)
        
        if shape == 'circle':
            # Draw with gradient effect (simplified)
            draw.ellipse([x - size, y - size, x + size, y + size],
                        fill=color, outline=dark_color, width=2)
            # Add highlight
            draw.ellipse([x - size//2, y - size//2, x, y],
                        fill=light_color, outline=None)
        
        elif shape == 'rectangle':
            w = size
            h = size * random.uniform(0.7, 1.3)
            draw.rectangle([x - w//2, y - h//2, x + w//2, y + h//2],
                         fill=color, outline=dark_color, width=2)
            # Add highlight
            draw.rectangle([x - w//4, y - h//4, x, y],
                         fill=light_color, outline=None)
    
    def _create_radial_gradient(self, image: Image.Image, color1: Tuple[int, int, int],
                               color2: Tuple[int, int, int],
                               center_x: Optional[int] = None,
                               center_y: Optional[int] = None) -> Image.Image:
        """Create radial gradient overlay."""
        if center_x is None:
            center_x = self.center_x
        if center_y is None:
            center_y = self.center_y
        
        width, height = image.size
        gradient = Image.new('RGB', (width, height))
        max_dist = math.sqrt(center_x**2 + center_y**2)
        
        for x in range(width):
            for y in range(height):
                dist = math.sqrt((x - center_x)**2 + (y - center_y)**2) / max_dist
                dist = min(dist, 1.0)
                dist = dist ** 0.7
                r = int(color1[0] * (1 - dist) + color2[0] * dist)
                g = int(color1[1] * (1 - dist) + color2[1] * dist)
                b = int(color1[2] * (1 - dist) + color2[2] * dist)
                gradient.putpixel((x, y), (r, g, b))
        
        return Image.blend(image, gradient, alpha=0.6)
    
    def _apply_style_finish(self, image: Image.Image, style: str) -> Image.Image:
        """Apply final effects based on artistic style."""
        # Contrast enhancement
        enhancer = ImageEnhance.Contrast(image)
        contrast_factors = {
            'baroque': 1.2,
            'post_impressionist': 1.15,
            'expressionist': 1.2,
            'abstract_expressionist': 1.1,
            'renaissance': 1.1,
            'cubist': 1.15
        }
        factor = contrast_factors.get(style, 1.1)
        image = enhancer.enhance(factor)
        
        # Color saturation
        enhancer = ImageEnhance.Color(image)
        saturation_factors = {
            'post_impressionist': 1.15,
            'surrealist': 1.1,
            'expressionist': 1.12,
            'impressionist': 1.05
        }
        factor = saturation_factors.get(style, 1.05)
        image = enhancer.enhance(factor)
        
        # Optional blur for impressionism
        if style == 'impressionist' and random.random() < 0.5:
            image = image.filter(ImageFilter.GaussianBlur(radius=0.8))
        
        # Sharpening for cubism
        if style == 'cubist' and random.random() < 0.4:
            image = image.filter(ImageFilter.SHARPEN)
        
        return image

