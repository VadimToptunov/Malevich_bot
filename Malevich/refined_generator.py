"""
Improved generator for avant-garde images with more refined techniques.
Uses gradients, advanced color palettes, and compositional rules.
All documentation in English.
"""
import random
import math
from typing import Tuple, List, Optional
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from colorsys import hsv_to_rgb, rgb_to_hsv


class RefinedGenerator:
    """Generator for refined avant-garde images."""
    
    # Color palettes in avant-garde style
    AVANTGARDE_PALETTES = {
        'suprematist': [
            # Black, white, red, blue, yellow - suprematism classics
            (0, 0, 0), (255, 255, 255), (255, 0, 0), 
            (0, 0, 255), (255, 255, 0)
        ],
        'constructivist': [
            # Red, black, white, gray
            (220, 20, 60), (0, 0, 0), (255, 255, 255),
            (128, 128, 128), (192, 192, 192)
        ],
        'modern_abstract': [
            # Modern abstraction with muted tones
            (139, 69, 19), (70, 130, 180), (255, 140, 0),
            (75, 0, 130), (255, 20, 147)
        ],
        'monochrome': [
            # Monochrome with accents
            (20, 20, 20), (60, 60, 60), (120, 120, 120),
            (180, 180, 180), (240, 240, 240)
        ],
        'vibrant': [
            # Bright contrasting colors
            (255, 0, 127), (0, 255, 127), (127, 0, 255),
            (255, 127, 0), (0, 127, 255)
        ]
    }
    
    def __init__(self, width: int = 1080, height: int = 1080):
        """
        Initialize generator.
        
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
        Generate refined avant-garde image.
        
        Args:
            style: Generation style ('geometric', 'organic', 'gradient', 'hybrid', 'auto')
            palette_name: Palette name from AVANTGARDE_PALETTES
            
        Returns:
            PIL Image object
        """
        if style == 'auto':
            style = random.choice(['geometric', 'organic', 'gradient', 'hybrid'])
        
        palette = self._get_palette(palette_name)
        image = Image.new('RGB', (self.width, self.height), self._get_background_color(palette))
        
        if style == 'geometric':
            image = self._add_geometric_composition(image, palette)
        elif style == 'organic':
            image = self._add_organic_shapes(image, palette)
        elif style == 'gradient':
            image = self._add_gradient_composition(image, palette)
        else:  # hybrid
            image = self._add_hybrid_composition(image, palette)
        
        # Final processing
        image = self._apply_final_touches(image)
        return image
    
    def _get_palette(self, palette_name: Optional[str] = None) -> List[Tuple[int, int, int]]:
        """Get color palette."""
        if palette_name and palette_name in self.AVANTGARDE_PALETTES:
            return self.AVANTGARDE_PALETTES[palette_name]
        return random.choice(list(self.AVANTGARDE_PALETTES.values()))
    
    def _get_background_color(self, palette: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
        """Select background color from palette (usually light or dark)."""
        # Prefer light or dark colors for background
        weights = []
        for color in palette:
            brightness = sum(color) / 3
            # Prefer very light or very dark
            if brightness < 50 or brightness > 200:
                weights.append(3)
            else:
                weights.append(1)
        return random.choices(palette, weights=weights)[0]
    
    def _add_geometric_composition(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """Add geometric composition with rule of thirds."""
        draw = ImageDraw.Draw(image)
        
        # Use rule of thirds for element placement
        third_w = self.width // 3
        third_h = self.height // 3
        
        num_elements = random.randint(3, 8)
        
        for _ in range(num_elements):
            shape_type = random.choice(['rectangle', 'ellipse', 'polygon', 'line'])
            color = random.choice(palette)
            alpha = random.randint(200, 255)
            
            # Place elements at key points (rule of thirds)
            if random.random() < 0.7:  # 70% of elements at key points
                x = random.choice([third_w, third_w * 2, self.center_x])
                y = random.choice([third_h, third_h * 2, self.center_y])
            else:
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
            
            size = random.randint(self.width // 10, self.width // 3)
            
            if shape_type == 'rectangle':
                # Rectangles with possible rotation
                angle = random.uniform(0, 45) if random.random() < 0.3 else 0
                self._draw_rotated_rectangle(draw, x, y, size, size * random.uniform(0.5, 1.5), 
                                            color, angle)
            elif shape_type == 'ellipse':
                draw.ellipse([x - size//2, y - size//2, x + size//2, y + size//2], 
                           fill=color, outline=color, width=random.randint(1, 5))
            elif shape_type == 'polygon':
                points = self._generate_polygon_points(x, y, size, random.randint(3, 8))
                draw.polygon(points, fill=color, outline=color)
            else:  # line
                # Thick lines for drama
                thickness = random.randint(2, 15)
                x2 = x + random.randint(-self.width//2, self.width//2)
                y2 = y + random.randint(-self.height//2, self.height//2)
                draw.line([x, y, x2, y2], fill=color, width=thickness)
        
        return image
    
    def _add_organic_shapes(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """Add organic shapes with smooth transitions."""
        draw = ImageDraw.Draw(image)
        
        # Create smooth Bezier curves
        num_shapes = random.randint(2, 5)
        
        for _ in range(num_shapes):
            color = random.choice(palette)
            
            # Generate Bezier curve
            start_x = random.randint(0, self.width)
            start_y = random.randint(0, self.height)
            
            control1_x = random.randint(0, self.width)
            control1_y = random.randint(0, self.height)
            control2_x = random.randint(0, self.width)
            control2_y = random.randint(0, self.height)
            
            end_x = random.randint(0, self.width)
            end_y = random.randint(0, self.height)
            
            # Draw curve with points for smoothness
            points = []
            for t in np.linspace(0, 1, 100):
                x = (1-t)**3 * start_x + 3*(1-t)**2*t * control1_x + 3*(1-t)*t**2 * control2_x + t**3 * end_x
                y = (1-t)**3 * start_y + 3*(1-t)**2*t * control1_y + 3*(1-t)*t**2 * control2_y + t**3 * end_y
                points.append((int(x), int(y)))
            
            # Create fill around curve
            thickness = random.randint(10, 50)
            for i, (px, py) in enumerate(points):
                if i < len(points) - 1:
                    draw.line([(px, py), points[i+1]], fill=color, width=thickness)
        
        return image
    
    def _add_gradient_composition(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """Create composition based on gradients."""
        # Create gradient background
        base_color = random.choice(palette)
        target_color = random.choice([c for c in palette if c != base_color])
        
        # Gradient direction
        direction = random.choice(['horizontal', 'vertical', 'diagonal', 'radial'])
        
        if direction == 'radial':
            image = self._create_radial_gradient(image, base_color, target_color)
        else:
            image = self._create_linear_gradient(image, base_color, target_color, direction)
        
        # Add geometric elements on top
        draw = ImageDraw.Draw(image)
        num_elements = random.randint(2, 5)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 15, self.width // 5)
            
            shape = random.choice(['circle', 'square', 'triangle'])
            if shape == 'circle':
                draw.ellipse([x-size, y-size, x+size, y+size], 
                           fill=color, outline=color)
            elif shape == 'square':
                angle = random.uniform(0, 45)
                self._draw_rotated_rectangle(draw, x, y, size, size, color, angle)
            else:  # triangle
                points = [(x, y-size), (x-size, y+size), (x+size, y+size)]
                draw.polygon(points, fill=color, outline=color)
        
        return image
    
    def _add_hybrid_composition(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """Hybrid composition with elements from different styles."""
        # Start with gradient
        base_color = random.choice(palette)
        target_color = random.choice([c for c in palette if c != base_color])
        image = self._create_radial_gradient(image, base_color, target_color, 
                                           center_x=random.randint(0, self.width),
                                           center_y=random.randint(0, self.height))
        
        draw = ImageDraw.Draw(image)
        
        # Add geometric elements
        for _ in range(random.randint(2, 4)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 20, self.width // 6)
            
            if random.random() < 0.5:
                draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
            else:
                points = self._generate_polygon_points(x, y, size, random.randint(3, 6))
                draw.polygon(points, fill=color)
        
        # Add organic lines
        for _ in range(random.randint(1, 3)):
            color = random.choice(palette)
            thickness = random.randint(3, 20)
            start_x = random.randint(0, self.width)
            start_y = random.randint(0, self.height)
            end_x = random.randint(0, self.width)
            end_y = random.randint(0, self.height)
            draw.line([(start_x, start_y), (end_x, end_y)], fill=color, width=thickness)
        
        return image
    
    def _create_linear_gradient(self, image: Image.Image, color1: Tuple[int, int, int], 
                               color2: Tuple[int, int, int], direction: str) -> Image.Image:
        """Create linear gradient."""
        width, height = image.size
        gradient = Image.new('RGB', (width, height))
        
        if direction == 'horizontal':
            for x in range(width):
                ratio = x / width
                r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                for y in range(height):
                    gradient.putpixel((x, y), (r, g, b))
        elif direction == 'vertical':
            for y in range(height):
                ratio = y / height
                r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                for x in range(width):
                    gradient.putpixel((x, y), (r, g, b))
        else:  # diagonal
            max_dist = math.sqrt(width**2 + height**2)
            for x in range(width):
                for y in range(height):
                    dist = math.sqrt(x**2 + y**2) / max_dist
                    r = int(color1[0] * (1 - dist) + color2[0] * dist)
                    g = int(color1[1] * (1 - dist) + color2[1] * dist)
                    b = int(color1[2] * (1 - dist) + color2[2] * dist)
                    gradient.putpixel((x, y), (r, g, b))
        
        # Overlay gradient on original image
        return Image.blend(image, gradient, alpha=0.7)
    
    def _create_radial_gradient(self, image: Image.Image, color1: Tuple[int, int, int],
                               color2: Tuple[int, int, int], 
                               center_x: Optional[int] = None,
                               center_y: Optional[int] = None) -> Image.Image:
        """Create radial gradient."""
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
                # Use quadratic function for smoother transition
                dist = dist ** 0.7
                r = int(color1[0] * (1 - dist) + color2[0] * dist)
                g = int(color1[1] * (1 - dist) + color2[1] * dist)
                b = int(color1[2] * (1 - dist) + color2[2] * dist)
                gradient.putpixel((x, y), (r, g, b))
        
        return Image.blend(image, gradient, alpha=0.8)
    
    def _generate_polygon_points(self, center_x: int, center_y: int, 
                                radius: int, sides: int) -> List[Tuple[int, int]]:
        """Generate points for regular polygon."""
        points = []
        for i in range(sides):
            angle = 2 * math.pi * i / sides
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.append((int(x), int(y)))
        return points
    
    def _draw_rotated_rectangle(self, draw: ImageDraw.Draw, center_x: int, center_y: int,
                               width: int, height: int, color: Tuple[int, int, int], 
                               angle: float) -> None:
        """Draw rotated rectangle."""
        # Simplified version - draw regular rectangle
        # For true rotation, more complex logic is needed
        x1 = center_x - width // 2
        y1 = center_y - height // 2
        x2 = center_x + width // 2
        y2 = center_y + height // 2
        draw.rectangle([x1, y1, x2, y2], fill=color, outline=color)
    
    def _apply_final_touches(self, image: Image.Image) -> Image.Image:
        """Apply final effects to improve quality."""
        # Slight contrast increase
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.1)
        
        # Slight saturation increase
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(1.05)
        
        # Optional: slight blur for softening
        if random.random() < 0.3:
            image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
        
        return image
