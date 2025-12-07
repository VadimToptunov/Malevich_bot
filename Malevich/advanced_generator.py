"""
Advanced generator for avant-garde art styles: cubism, expressionism, surrealism,
and styles inspired by psychiatric conditions (within Instagram guidelines).
All documentation and comments in English.
"""
import random
import math
from typing import Tuple, List, Optional, Dict
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops
from colorsys import hsv_to_rgb, rgb_to_hsv


class AdvancedGenerator:
    """
    Advanced generator for various avant-garde art styles.
    Supports: cubism, expressionism, surrealism, and psychiatric-inspired styles.
    """
    
    # Color palettes for different art movements
    ART_PALETTES: Dict[str, List[Tuple[int, int, int]]] = {
        # Suprematism (Malevich)
        'suprematist': [
            (0, 0, 0), (255, 255, 255), (255, 0, 0),
            (0, 0, 255), (255, 255, 0)
        ],
        # Cubism (Picasso, Braque) - earth tones, muted colors
        'cubist': [
            (139, 90, 43), (101, 67, 33), (160, 82, 45),
            (205, 133, 63), (139, 69, 19), (85, 107, 47),
            (72, 61, 139), (105, 105, 105)
        ],
        # Expressionism (Van Gogh, Munch) - bold, emotional colors
        'expressionist': [
            (255, 69, 0), (255, 140, 0), (255, 215, 0),
            (50, 205, 50), (0, 191, 255), (138, 43, 226),
            (220, 20, 60), (255, 20, 147)
        ],
        # Surrealism (Dali) - dreamlike, vibrant
        'surrealist': [
            (255, 255, 0), (255, 165, 0), (255, 20, 147),
            (0, 191, 255), (138, 43, 226), (255, 0, 127),
            (0, 255, 127), (255, 192, 203)
        ],
        # Fragmented perception (inspired by certain conditions)
        'fragmented': [
            (255, 255, 255), (0, 0, 0), (128, 128, 128),
            (255, 0, 0), (0, 0, 255), (255, 255, 0),
            (0, 255, 0), (255, 0, 255)
        ],
        # Intense mood swings (high contrast, emotional)
        'intense': [
            (255, 0, 0), (0, 0, 0), (255, 255, 255),
            (255, 255, 0), (0, 0, 255), (255, 0, 255),
            (0, 255, 255), (128, 0, 128)
        ],
        # Monochrome with accents
        'monochrome': [
            (20, 20, 20), (60, 60, 60), (120, 120, 120),
            (180, 180, 180), (240, 240, 240), (255, 255, 255)
        ]
    }
    
    def __init__(self, width: int = 1080, height: int = 1080):
        """
        Initialize the generator.
        
        Args:
            width: Image width (default 1080 for Instagram)
            height: Image height (default 1080 for Instagram)
        """
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
    
    def generate(self, style: str = 'auto', palette_name: Optional[str] = None) -> Image.Image:
        """
        Generate an avant-garde image in the specified style.
        
        Args:
            style: Art style ('cubism', 'expressionism', 'surrealism', 
                   'fragmented', 'intense', 'hybrid', 'auto')
            palette_name: Palette name from ART_PALETTES
            
        Returns:
            PIL Image object
        """
        if style == 'auto':
            style = random.choice(['cubism', 'expressionism', 'surrealism', 
                                  'fragmented', 'intense', 'hybrid'])
        
        palette = self._get_palette(palette_name, style)
        image = Image.new('RGB', (self.width, self.height), 
                         self._get_background_color(palette))
        
        if style == 'cubism':
            image = self._create_cubist_composition(image, palette)
        elif style == 'expressionism':
            image = self._create_expressionist_composition(image, palette)
        elif style == 'surrealism':
            image = self._create_surrealist_composition(image, palette)
        elif style == 'fragmented':
            image = self._create_fragmented_composition(image, palette)
        elif style == 'intense':
            image = self._create_intense_composition(image, palette)
        else:  # hybrid
            image = self._create_hybrid_composition(image, palette)
        
        # Final processing
        image = self._apply_final_touches(image, style)
        return image
    
    def _get_palette(self, palette_name: Optional[str], style: str) -> List[Tuple[int, int, int]]:
        """Get color palette based on style or name."""
        if palette_name and palette_name in self.ART_PALETTES:
            return self.ART_PALETTES[palette_name]
        
        # Auto-select palette based on style
        style_palette_map = {
            'cubism': 'cubist',
            'expressionism': 'expressionist',
            'surrealism': 'surrealist',
            'fragmented': 'fragmented',
            'intense': 'intense'
        }
        
        palette_key = style_palette_map.get(style, 'surrealist')
        return self.ART_PALETTES.get(palette_key, self.ART_PALETTES['surrealist'])
    
    def _get_background_color(self, palette: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
        """Select background color from palette (prefer light or dark)."""
        weights = []
        for color in palette:
            brightness = sum(color) / 3
            if brightness < 50 or brightness > 200:
                weights.append(3)
            else:
                weights.append(1)
        return random.choices(palette, weights=weights)[0]
    
    def _create_cubist_composition(self, image: Image.Image, 
                                   palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Create cubist composition with geometric fragmentation and multiple perspectives.
        Inspired by Picasso and Braque.
        """
        draw = ImageDraw.Draw(image)
        
        # Cubism: fragmented forms, multiple viewpoints, geometric shapes
        num_fragments = random.randint(8, 20)
        
        for _ in range(num_fragments):
            color = random.choice(palette)
            
            # Create fragmented geometric shapes
            fragment_type = random.choice(['polygon', 'rectangle', 'triangle'])
            
            # Multiple perspective points
            if random.random() < 0.6:
                # Use rule of thirds for key fragments
                third_w = self.width // 3
                third_h = self.height // 3
                x = random.choice([third_w, third_w * 2, self.center_x])
                y = random.choice([third_h, third_h * 2, self.center_y])
            else:
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
            
            size = random.randint(self.width // 15, self.width // 4)
            
            if fragment_type == 'polygon':
                # Irregular polygons for fragmentation effect
                sides = random.randint(3, 8)
                points = []
                for i in range(sides):
                    angle = 2 * math.pi * i / sides + random.uniform(-0.5, 0.5)
                    offset = random.uniform(0.7, 1.3) * size
                    px = x + offset * math.cos(angle)
                    py = y + offset * math.sin(angle)
                    points.append((int(px), int(py)))
                draw.polygon(points, fill=color, outline=color, width=2)
            
            elif fragment_type == 'rectangle':
                # Angled rectangles
                angle = random.uniform(0, 45)
                w = size * random.uniform(0.5, 1.5)
                h = size * random.uniform(0.5, 1.5)
                x1 = x - w // 2
                y1 = y - h // 2
                x2 = x + w // 2
                y2 = y + h // 2
                draw.rectangle([x1, y1, x2, y2], fill=color, outline=color, width=2)
            
            else:  # triangle
                points = [
                    (x, y - size),
                    (x - size, y + size),
                    (x + size, y + size)
                ]
                # Slight rotation
                rotated_points = []
                for px, py in points:
                    angle = random.uniform(-15, 15) * math.pi / 180
                    rx = x + (px - x) * math.cos(angle) - (py - y) * math.sin(angle)
                    ry = y + (px - x) * math.sin(angle) + (py - y) * math.cos(angle)
                    rotated_points.append((int(rx), int(ry)))
                draw.polygon(rotated_points, fill=color, outline=color, width=2)
        
        # Add overlapping lines for depth
        for _ in range(random.randint(5, 15)):
            color = random.choice(palette)
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=random.randint(1, 4))
        
        return image
    
    def _create_expressionist_composition(self, image: Image.Image,
                                         palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Create expressionist composition with bold colors, emotional intensity,
        and distorted forms. Inspired by Van Gogh and Munch.
        """
        draw = ImageDraw.Draw(image)
        
        # Expressionism: bold colors, emotional brushstrokes, distorted reality
        num_elements = random.randint(5, 12)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            
            # Create bold, expressive shapes
            element_type = random.choice(['swirl', 'wave', 'burst', 'line'])
            
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 10, self.width // 3)
            
            if element_type == 'swirl':
                # Swirling patterns
                points = []
                for t in np.linspace(0, 4 * math.pi, 50):
                    radius = size * (1 - t / (4 * math.pi))
                    px = x + radius * math.cos(t)
                    py = y + radius * math.sin(t)
                    points.append((int(px), int(py)))
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i+1]], fill=color, width=random.randint(3, 8))
            
            elif element_type == 'wave':
                # Wavy, emotional lines
                points = []
                for i in range(20):
                    px = x + (i * size // 10)
                    py = y + size * math.sin(i * 0.5) * random.uniform(0.5, 1.5)
                    points.append((int(px), int(py)))
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i+1]], fill=color, width=random.randint(4, 10))
            
            elif element_type == 'burst':
                # Radial burst pattern
                num_rays = random.randint(8, 16)
                for i in range(num_rays):
                    angle = 2 * math.pi * i / num_rays
                    x2 = x + size * math.cos(angle)
                    y2 = y + size * math.sin(angle)
                    draw.line([(x, y), (int(x2), int(y2))], fill=color, width=random.randint(3, 7))
            
            else:  # line
                # Bold, expressive lines
                x2 = x + random.randint(-self.width//2, self.width//2)
                y2 = y + random.randint(-self.height//2, self.height//2)
                draw.line([(x, y), (x2, y2)], fill=color, width=random.randint(5, 15))
        
        return image
    
    def _create_surrealist_composition(self, image: Image.Image,
                                      palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Create surrealist composition with dreamlike elements, melting forms,
        and impossible geometries. Inspired by Dali.
        """
        draw = ImageDraw.Draw(image)
        
        # Surrealism: dreamlike, melting, impossible perspectives
        num_elements = random.randint(4, 10)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            
            element_type = random.choice(['melt', 'impossible_shape', 'floating', 'distorted'])
            
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 12, self.width // 4)
            
            if element_type == 'melt':
                # Melting/dripping effect
                base_y = y
                points = []
                for i in range(15):
                    px = x + (i - 7) * size // 7
                    # Melting curve
                    melt_factor = math.exp(-((i - 7) ** 2) / 10)
                    py = base_y + size * melt_factor * random.uniform(0.8, 1.2)
                    points.append((int(px), int(py)))
                draw.polygon(points + [(x, base_y)], fill=color, outline=color)
            
            elif element_type == 'impossible_shape':
                # Impossible geometry (like Escher)
                sides = random.randint(4, 6)
                points = []
                for i in range(sides):
                    angle = 2 * math.pi * i / sides
                    # Add perspective distortion
                    perspective = 1 + 0.3 * math.sin(angle * 2)
                    px = x + size * perspective * math.cos(angle)
                    py = y + size * perspective * math.sin(angle)
                    points.append((int(px), int(py)))
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
                    distortion = 1 + 0.4 * math.sin(angle * 3)
                    px = x + size * distortion * math.cos(angle)
                    py = y + size * distortion * math.sin(angle)
                    points.append((int(px), int(py)))
                draw.polygon(points, fill=color, outline=color)
        
        # Add dreamlike gradients
        if random.random() < 0.5:
            base_color = random.choice(palette)
            target_color = random.choice([c for c in palette if c != base_color])
            image = self._create_radial_gradient(image, base_color, target_color,
                                                center_x=random.randint(0, self.width),
                                                center_y=random.randint(0, self.height))
        
        return image
    
    def _create_fragmented_composition(self, image: Image.Image,
                                       palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Create fragmented composition inspired by fragmented perception.
        Uses sharp breaks, overlapping layers, and disjointed elements.
        """
        draw = ImageDraw.Draw(image)
        
        # Fragmented: sharp breaks, overlapping, disjointed
        num_fragments = random.randint(10, 25)
        
        # Create base layer with fragments
        fragments = []
        for _ in range(num_fragments):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 20, self.width // 6)
            
            # Sharp, angular fragments
            sides = random.randint(3, 6)
            points = []
            for i in range(sides):
                angle = 2 * math.pi * i / sides + random.uniform(-0.3, 0.3)
                offset = size * random.uniform(0.8, 1.2)
                px = x + offset * math.cos(angle)
                py = y + offset * math.sin(angle)
                points.append((int(px), int(py)))
            
            fragments.append((points, color))
        
        # Draw fragments with varying opacity effect (simulated)
        for points, color in fragments:
            draw.polygon(points, fill=color, outline=color, width=1)
        
        # Add sharp dividing lines
        for _ in range(random.randint(5, 12)):
            color = random.choice(palette)
            if random.random() < 0.5:
                # Vertical break
                x = random.randint(0, self.width)
                draw.line([(x, 0), (x, self.height)], fill=color, width=random.randint(2, 5))
            else:
                # Horizontal break
                y = random.randint(0, self.height)
                draw.line([(0, y), (self.width, y)], fill=color, width=random.randint(2, 5))
        
        return image
    
    def _create_intense_composition(self, image: Image.Image,
                                    palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Create intense composition with high contrast, emotional extremes,
        and dramatic color shifts.
        """
        draw = ImageDraw.Draw(image)
        
        # Intense: high contrast, emotional extremes, dramatic shifts
        num_elements = random.randint(6, 15)
        
        # Create high-contrast elements
        for _ in range(num_elements):
            # Choose from extreme ends of palette
            if random.random() < 0.5:
                # Very dark or very light
                bright_colors = [c for c in palette if sum(c) / 3 > 200 or sum(c) / 3 < 50]
                color = random.choice(bright_colors if bright_colors else palette)
            else:
                color = random.choice(palette)
            
            element_type = random.choice(['circle', 'rectangle', 'line', 'burst'])
            
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 15, self.width // 4)
            
            if element_type == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=color, width=random.randint(2, 6))
            
            elif element_type == 'rectangle':
                w = size * random.uniform(0.5, 2)
                h = size * random.uniform(0.5, 2)
                draw.rectangle([x - w//2, y - h//2, x + w//2, y + h//2],
                             fill=color, outline=color, width=random.randint(2, 6))
            
            elif element_type == 'line':
                x2 = x + random.randint(-self.width//2, self.width//2)
                y2 = y + random.randint(-self.height//2, self.height//2)
                draw.line([(x, y), (x2, y2)], fill=color, width=random.randint(4, 12))
            
            else:  # burst
                num_rays = random.randint(6, 12)
                for i in range(num_rays):
                    angle = 2 * math.pi * i / num_rays
                    x2 = x + size * math.cos(angle)
                    y2 = y + size * math.sin(angle)
                    draw.line([(x, y), (int(x2), int(y2))], fill=color, width=random.randint(3, 8))
        
        # Add dramatic color zones
        if random.random() < 0.6:
            zone_color = random.choice(palette)
            zone_x = random.randint(0, self.width)
            zone_y = random.randint(0, self.height)
            zone_size = random.randint(self.width // 4, self.width // 2)
            draw.ellipse([zone_x - zone_size, zone_y - zone_size,
                         zone_x + zone_size, zone_y + zone_size],
                        fill=None, outline=zone_color, width=random.randint(3, 8))
        
        return image
    
    def _create_hybrid_composition(self, image: Image.Image,
                                   palette: List[Tuple[int, int, int]]) -> Image.Image:
        """Create hybrid composition mixing different styles."""
        # Start with gradient background
        base_color = random.choice(palette)
        target_color = random.choice([c for c in palette if c != base_color])
        image = self._create_radial_gradient(image, base_color, target_color)
        
        # Add elements from different styles
        draw = ImageDraw.Draw(image)
        
        # Cubist fragments
        for _ in range(random.randint(2, 5)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 20, self.width // 8)
            sides = random.randint(3, 6)
            points = []
            for i in range(sides):
                angle = 2 * math.pi * i / sides
                px = x + size * math.cos(angle)
                py = y + size * math.sin(angle)
                points.append((int(px), int(py)))
            draw.polygon(points, fill=color, outline=color)
        
        # Expressionist lines
        for _ in range(random.randint(3, 7)):
            color = random.choice(palette)
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=random.randint(3, 10))
        
        # Surrealist elements
        for _ in range(random.randint(1, 3)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 15, self.width // 6)
            draw.ellipse([x - size, y - size, x + size, y + size],
                        fill=color, outline=color)
        
        return image
    
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
                dist = dist ** 0.7  # Smoother transition
                r = int(color1[0] * (1 - dist) + color2[0] * dist)
                g = int(color1[1] * (1 - dist) + color2[1] * dist)
                b = int(color1[2] * (1 - dist) + color2[2] * dist)
                gradient.putpixel((x, y), (r, g, b))
        
        return Image.blend(image, gradient, alpha=0.6)
    
    def _apply_final_touches(self, image: Image.Image, style: str) -> Image.Image:
        """Apply final effects based on style."""
        # Contrast enhancement
        enhancer = ImageEnhance.Contrast(image)
        contrast_factor = 1.15 if style in ['expressionism', 'intense'] else 1.1
        image = enhancer.enhance(contrast_factor)
        
        # Color saturation
        enhancer = ImageEnhance.Color(image)
        saturation_factor = 1.1 if style in ['surrealism', 'expressionist'] else 1.05
        image = enhancer.enhance(saturation_factor)
        
        # Optional blur for certain styles
        if style == 'surrealism' and random.random() < 0.3:
            image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
        
        # Optional sharpening for cubism
        if style == 'cubism' and random.random() < 0.4:
            image = image.filter(ImageFilter.SHARPEN)
        
        return image

