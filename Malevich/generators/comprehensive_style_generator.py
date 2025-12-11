"""
Comprehensive art style generator with extensive range of artistic styles and techniques.
Includes: hyperrealism, photorealism, minimalism, pop art, op art, fauvism, futurism,
dadaism, constructivism, de stijl, art deco, art nouveau, neoclassicism, romanticism,
realism, naturalism, mannerism, rococo, classicism, symbolism, precisionism, and more.
All documentation in English.
"""
import random
import math
from typing import Tuple, List, Optional, Dict
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops
from colorsys import hsv_to_rgb, rgb_to_hsv

# Import advanced color system
from Malevich.utils.color_systems import AdvancedColorSystem


class ComprehensiveStyleGenerator:
    """
    Comprehensive generator supporting 30+ art styles and techniques.
    From classical to contemporary, including hyperrealism.
    """
    
    # Extended color palettes for various art movements
    STYLE_PALETTES: Dict[str, List[Tuple[int, int, int]]] = {
        # Hyperrealism: natural, realistic colors with subtle variations
        'hyperrealism': [
            (240, 235, 230), (220, 210, 200), (200, 190, 180),
            (180, 170, 160), (160, 150, 140), (140, 130, 120),
            (120, 110, 100), (100, 90, 80), (80, 70, 60)
        ],
        # Photorealism: similar to hyperrealism
        'photorealism': [
            (250, 245, 240), (230, 225, 220), (210, 205, 200),
            (190, 185, 180), (170, 165, 160), (150, 145, 140)
        ],
        # Minimalism: limited, muted palette
        'minimalism': [
            (255, 255, 255), (240, 240, 240), (220, 220, 220),
            (200, 200, 200), (180, 180, 180), (0, 0, 0),
            (50, 50, 50), (100, 100, 100)
        ],
        # Pop Art: bright, saturated colors
        'pop_art': [
            (255, 0, 0), (0, 255, 0), (0, 0, 255),
            (255, 255, 0), (255, 0, 255), (0, 255, 255),
            (255, 128, 0), (128, 0, 255), (255, 192, 203)
        ],
        # Op Art: high contrast black and white with some color
        'op_art': [
            (0, 0, 0), (255, 255, 255), (128, 128, 128),
            (200, 200, 200), (50, 50, 50), (255, 0, 0),
            (0, 0, 255), (255, 255, 0)
        ],
        # Fauvism: wild, unnatural colors
        'fauvism': [
            (255, 50, 50), (50, 255, 50), (50, 50, 255),
            (255, 200, 50), (200, 50, 255), (50, 255, 200),
            (255, 100, 100), (100, 255, 100), (100, 100, 255)
        ],
        # Futurism: dynamic, vibrant colors
        'futurism': [
            (255, 100, 0), (0, 200, 255), (255, 200, 0),
            (200, 0, 255), (0, 255, 150), (255, 0, 150),
            (150, 0, 255), (255, 150, 0)
        ],
        # Dadaism: random, unexpected colors
        'dadaism': [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(12)
        ],
        # Constructivism: red, black, white, geometric
        'constructivism': [
            (220, 20, 60), (0, 0, 0), (255, 255, 255),
            (128, 128, 128), (192, 192, 192), (255, 0, 0),
            (0, 0, 0), (255, 255, 255)
        ],
        # De Stijl: primary colors + black/white
        'de_stijl': [
            (255, 0, 0), (0, 0, 255), (255, 255, 0),
            (0, 0, 0), (255, 255, 255), (128, 128, 128)
        ],
        # Art Deco: metallic, luxurious colors
        'art_deco': [
            (220, 200, 150), (180, 160, 140), (200, 180, 160),
            (240, 220, 200), (160, 140, 120), (255, 215, 0),
            (192, 192, 192), (139, 69, 19)
        ],
        # Art Nouveau: natural, organic colors
        'art_nouveau': [
            (200, 220, 200), (220, 200, 180), (180, 200, 220),
            (200, 180, 200), (220, 220, 180), (180, 220, 220),
            (200, 200, 160), (160, 200, 200)
        ],
        # Neoclassicism: restrained, classical colors
        'neoclassicism': [
            (200, 190, 180), (180, 170, 160), (160, 150, 140),
            (220, 210, 200), (140, 130, 120), (240, 230, 220),
            (120, 110, 100), (100, 90, 80)
        ],
        # Romanticism: dramatic, emotional colors
        'romanticism': [
            (180, 100, 80), (100, 80, 120), (120, 100, 140),
            (140, 120, 100), (160, 140, 120), (100, 120, 140),
            (120, 140, 160), (80, 100, 120)
        ],
        # Realism: natural, true-to-life colors
        'realism': [
            (200, 180, 160), (180, 160, 140), (160, 140, 120),
            (140, 120, 100), (220, 200, 180), (200, 190, 170),
            (180, 170, 150), (160, 150, 130)
        ],
        # Naturalism: nature-based colors
        'naturalism': [
            (100, 130, 80), (120, 150, 100), (140, 170, 120),
            (80, 100, 60), (160, 140, 100), (180, 160, 120),
            (200, 180, 140), (120, 100, 80)
        ],
        # Mannerism: sophisticated, complex colors
        'mannerism': [
            (180, 160, 200), (200, 180, 160), (160, 200, 180),
            (220, 200, 180), (180, 200, 220), (200, 220, 180),
            (160, 180, 200), (200, 160, 180)
        ],
        # Rococo: light, decorative colors
        'rococo': [
            (255, 250, 240), (255, 240, 230), (240, 255, 250),
            (250, 240, 255), (240, 250, 255), (255, 245, 240),
            (245, 255, 240), (240, 245, 255)
        ],
        # Classicism: balanced, harmonious colors
        'classicism': [
            (200, 190, 180), (190, 180, 170), (180, 170, 160),
            (210, 200, 190), (170, 160, 150), (220, 210, 200),
            (160, 150, 140), (150, 140, 130)
        ],
        # Symbolism: symbolic, meaningful colors
        'symbolism': [
            (120, 100, 140), (140, 120, 100), (100, 140, 120),
            (160, 140, 160), (140, 160, 140), (160, 160, 140),
            (140, 140, 160), (120, 120, 140)
        ],
        # Precisionism: precise, industrial colors
        'precisionism': [
            (200, 200, 200), (180, 180, 180), (160, 160, 160),
            (140, 140, 140), (120, 120, 120), (100, 100, 100),
            (220, 220, 220), (80, 80, 80)
        ],
    }
    
    def __init__(self, width: int = 1080, height: int = 1080):
        """Initialize comprehensive style generator."""
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.golden_ratio = 1.618033988749895
    
    def generate(self, style: str = 'auto', palette_name: Optional[str] = None) -> Image.Image:
        """
        Generate image in specified artistic style.
        
        Args:
            style: Art style (see available styles below)
            palette_name: Specific palette name
            
        Returns:
            PIL Image object
        """
        if style == 'auto':
            style = random.choice(list(self.STYLE_PALETTES.keys()))
        
        palette = self._get_palette(palette_name, style)
        image = Image.new('RGB', (self.width, self.height), self._get_background_color(palette))
        
        # Route to style-specific generation
        style_methods = {
            'hyperrealism': self._create_hyperrealism,
            'photorealism': self._create_photorealism,
            'minimalism': self._create_minimalism,
            'pop_art': self._create_pop_art,
            'op_art': self._create_op_art,
            'fauvism': self._create_fauvism,
            'futurism': self._create_futurism,
            'dadaism': self._create_dadaism,
            'constructivism': self._create_constructivism,
            'de_stijl': self._create_de_stijl,
            'art_deco': self._create_art_deco,
            'art_nouveau': self._create_art_nouveau,
            'neoclassicism': self._create_neoclassicism,
            'romanticism': self._create_romanticism,
            'realism': self._create_realism,
            'naturalism': self._create_naturalism,
            'mannerism': self._create_mannerism,
            'rococo': self._create_rococo,
            'classicism': self._create_classicism,
            'symbolism': self._create_symbolism,
            'precisionism': self._create_precisionism,
        }
        
        if style in style_methods:
            image = style_methods[style](image, palette)
        else:
            # Fallback to abstract
            image = self._create_abstract(image, palette)
        
        # Apply final style-specific touches
        image = self._apply_style_finish(image, style)
        return image
    
    def _get_palette(self, palette_name: Optional[str], style: str) -> List[Tuple[int, int, int]]:
        """Get color palette based on style."""
        if palette_name and palette_name in self.STYLE_PALETTES:
            return self.STYLE_PALETTES[palette_name]
        
        return self.STYLE_PALETTES.get(style, self.STYLE_PALETTES['realism'])
    
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
    
    def _create_hyperrealism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Hyperrealism: Photographic precision, extreme detail, subtle variations.
        Techniques: fine brushwork, subtle color transitions, texture detail.
        """
        draw = ImageDraw.Draw(image)
        
        # Create hyperrealistic texture with fine details
        # Use sophisticated color variations
        base_color = random.choice(palette)
        complex_palette = AdvancedColorSystem.generate_complex_harmony(
            base_color, 'analogous_extended', variations=20
        )
        
        # Create subtle texture overlay
        texture_overlay = Image.new('RGB', (self.width, self.height))
        texture_pixels = texture_overlay.load()
        
        for y in range(self.height):
            for x in range(self.width):
                # Subtle color variation for texture
                base_idx = (x + y) % len(complex_palette)
                color = complex_palette[base_idx]
                
                # Add micro-variations (simulating fine brushwork)
                variation = random.randint(-3, 3)
                r = max(0, min(255, color[0] + variation))
                g = max(0, min(255, color[1] + variation))
                b = max(0, min(255, color[2] + variation))
                texture_pixels[x, y] = (r, g, b)
        
        image = Image.blend(image, texture_overlay, alpha=0.7)
        
        # Add fine details (simulating hyperrealistic elements)
        num_details = random.randint(50, 100)
        for _ in range(num_details):
            detail_color = random.choice(complex_palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1, 3)
            
            # Very fine detail points
            for i in range(size):
                for j in range(size):
                    px = x + i
                    py = y + j
                    if 0 <= px < self.width and 0 <= py < self.height:
                        # Blend with existing pixel
                        existing = image.getpixel((px, py))
                        blended = (
                            (existing[0] + detail_color[0]) // 2,
                            (existing[1] + detail_color[1]) // 2,
                            (existing[2] + detail_color[2]) // 2
                        )
                        image.putpixel((px, py), blended)
        
        # Apply sharpening for detail
        image = image.filter(ImageFilter.SHARPEN)
        
        return image
    
    def _create_photorealism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Photorealism: Photo-like quality, high detail, realistic rendering.
        Similar to hyperrealism but with photographic composition.
        """
        # Similar to hyperrealism but with more photographic composition
        image = self._create_hyperrealism(image, palette)
        
        # Add photographic effects
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.1)
        
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(1.05)
        
        return image
    
    def _create_minimalism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Minimalism: Simplicity, limited elements, clean composition.
        Focus on essential forms and negative space.
        """
        draw = ImageDraw.Draw(image)
        
        # Minimal elements
        num_elements = random.randint(1, 4)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            
            # Use golden ratio for placement
            golden_x = int(self.width / self.golden_ratio)
            golden_y = int(self.height / self.golden_ratio)
            
            x = random.choice([golden_x, self.width - golden_x, self.center_x])
            y = random.choice([golden_y, self.height - golden_y, self.center_y])
            
            size = random.randint(self.width // 8, self.width // 4)
            
            shape = random.choice(['rectangle', 'circle', 'line'])
            
            if shape == 'rectangle':
                w = size
                h = size // random.choice([2, 3, 4])
                draw.rectangle([x - w//2, y - h//2, x + w//2, y + h//2],
                             fill=color, outline=None)
            elif shape == 'circle':
                draw.ellipse([x - size//2, y - size//2, x + size//2, y + size//2],
                           fill=color, outline=None)
            else:  # line
                thickness = random.randint(2, 5)
                x2 = x + random.randint(-self.width//4, self.width//4)
                y2 = y + random.randint(-self.height//4, self.height//4)
                draw.line([(x, y), (x2, y2)], fill=color, width=thickness)
        
        return image
    
    def _create_pop_art(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Pop Art: Bright colors, bold forms, mass culture imagery.
        Techniques: Ben-Day dots, bold outlines, high contrast.
        """
        draw = ImageDraw.Draw(image)
        
        # Bold, high-contrast elements
        num_elements = random.randint(5, 12)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            # High saturation
            r, g, b = [c / 255.0 for c in color]
            h, s, v = rgb_to_hsv(r, g, b)
            s = min(1.0, s * 1.5)
            r, g, b = hsv_to_rgb(h, s, v)
            color = (int(r * 255), int(g * 255), int(b * 255))
            
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 10, self.width // 4)
            
            # Bold shapes
            shape = random.choice(['circle', 'rectangle', 'star'])
            
            if shape == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=(0, 0, 0), width=4)
            elif shape == 'rectangle':
                draw.rectangle([x - size, y - size, x + size, y + size],
                             fill=color, outline=(0, 0, 0), width=4)
            else:  # star
                points = []
                for i in range(10):
                    angle = math.pi * i / 5
                    r = size if i % 2 == 0 else size // 2
                    px = int(x + r * math.cos(angle))
                    py = int(y + r * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=(0, 0, 0), width=4)
        
        # Add Ben-Day dot pattern (simplified)
        if random.random() < 0.5:
            dot_size = 3
            spacing = 8
            for y in range(0, self.height, spacing):
                for x in range(0, self.width, spacing):
                    if random.random() < 0.3:
                        dot_color = random.choice(palette)
                        draw.ellipse([x - dot_size, y - dot_size, x + dot_size, y + dot_size],
                                   fill=dot_color)
        
        return image
    
    def _create_op_art(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Op Art: Optical illusions, geometric patterns, visual effects.
        Techniques: moiré patterns, vibrating colors, geometric precision.
        """
        draw = ImageDraw.Draw(image)
        
        # Create optical illusion patterns
        pattern_type = random.choice(['spiral', 'grid', 'concentric', 'moire'])
        
        if pattern_type == 'spiral':
            # Spiral pattern
            center_x, center_y = self.center_x, self.center_y
            for i in range(100):
                angle = i * 0.2
                radius = i * 2
                x = int(center_x + radius * math.cos(angle))
                y = int(center_y + radius * math.sin(angle))
                color = palette[i % len(palette)]
                draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=color)
        
        elif pattern_type == 'grid':
            # Grid with optical illusion
            spacing = 20
            for x in range(0, self.width, spacing):
                for y in range(0, self.height, spacing):
                    # Alternating colors for illusion
                    color = palette[(x // spacing + y // spacing) % len(palette)]
                    draw.rectangle([x, y, x + spacing, y + spacing],
                                 fill=color, outline=None)
        
        elif pattern_type == 'concentric':
            # Concentric circles
            center_x, center_y = self.center_x, self.center_y
            for i in range(20):
                radius = i * 30
                color = palette[i % len(palette)]
                draw.ellipse([center_x - radius, center_y - radius,
                            center_x + radius, center_y + radius],
                           fill=None, outline=color, width=3)
        
        else:  # moire
            # Moiré pattern
            for i in range(30):
                y = i * (self.height // 30)
                thickness = 2 + (i % 3)
                color = palette[i % len(palette)]
                draw.line([(0, y), (self.width, y)], fill=color, width=thickness)
        
        return image
    
    def _create_fauvism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Fauvism: Wild, unnatural colors, bold brushstrokes, emotional expression.
        Techniques: pure color, visible brushstrokes, non-naturalistic colors.
        """
        draw = ImageDraw.Draw(image)
        
        # Wild, expressive brushstrokes
        num_strokes = random.randint(100, 200)
        
        for _ in range(num_strokes):
            color = random.choice(palette)
            # Intensify colors
            r, g, b = color
            r = min(255, int(r * 1.3))
            g = min(255, int(g * 1.3))
            b = min(255, int(b * 1.3))
            color = (r, g, b)
            
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            
            # Bold, visible brushstrokes
            angle = random.uniform(0, 2 * math.pi)
            length = random.randint(20, 60)
            x2 = int(x + length * math.cos(angle))
            y2 = int(y + length * math.sin(angle))
            
            thickness = random.randint(5, 15)
            draw.line([(x, y), (x2, y2)], fill=color, width=thickness)
        
        # Add bold color blocks
        for _ in range(random.randint(3, 8)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 8, self.width // 4)
            draw.ellipse([x - size, y - size, x + size, y + size],
                       fill=color, outline=None)
        
        return image
    
    def _create_futurism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Futurism: Movement, speed, dynamism, technology.
        Techniques: motion lines, dynamic composition, fragmented forms.
        """
        draw = ImageDraw.Draw(image)
        
        # Dynamic, movement-oriented elements
        num_elements = random.randint(8, 15)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            
            # Motion lines
            for i in range(random.randint(3, 8)):
                angle = random.uniform(0, 2 * math.pi)
                length = random.randint(30, 100)
                x2 = int(x + length * math.cos(angle))
                y2 = int(y + length * math.sin(angle))
                thickness = random.randint(2, 6)
                draw.line([(x, y), (x2, y2)], fill=color, width=thickness)
                x, y = x2, y2
        
        # Fragmented geometric forms (speed lines)
        for _ in range(random.randint(5, 10)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(20, 60)
            
            # Fragmented shape
            points = []
            for i in range(6):
                angle = 2 * math.pi * i / 6
                offset = size * random.uniform(0.7, 1.3)
                px = int(x + offset * math.cos(angle))
                py = int(y + offset * math.sin(angle))
                points.append((px, py))
            draw.polygon(points, fill=color, outline=None)
        
        return image
    
    def _create_dadaism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Dadaism: Randomness, chance, anti-art, absurdity.
        Techniques: collage elements, random placement, unexpected combinations.
        """
        draw = ImageDraw.Draw(image)
        
        # Random, chaotic elements
        num_elements = random.randint(10, 25)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(10, 80)
            
            # Random shapes and placements
            element_type = random.choice(['circle', 'rectangle', 'line', 'polygon', 'texture'])
            
            if element_type == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=None)
            elif element_type == 'rectangle':
                w = random.randint(size // 2, size * 2)
                h = random.randint(size // 2, size * 2)
                draw.rectangle([x - w//2, y - h//2, x + w//2, y + h//2],
                             fill=color, outline=None)
            elif element_type == 'line':
                x2 = random.randint(0, self.width)
                y2 = random.randint(0, self.height)
                draw.line([(x, y), (x2, y2)], fill=color, width=random.randint(1, 8))
            elif element_type == 'polygon':
                sides = random.randint(3, 8)
                points = []
                for i in range(sides):
                    angle = 2 * math.pi * i / sides
                    r = size * random.uniform(0.5, 1.5)
                    px = int(x + r * math.cos(angle))
                    py = int(y + r * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=None)
            else:  # texture
                # Random texture patches
                for _ in range(random.randint(5, 15)):
                    tx = x + random.randint(-size, size)
                    ty = y + random.randint(-size, size)
                    if 0 <= tx < self.width and 0 <= ty < self.height:
                        draw.ellipse([tx - 2, ty - 2, tx + 2, ty + 2], fill=color)
        
        return image
    
    def _create_constructivism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Constructivism: Geometric forms, industrial aesthetic, red/black/white.
        Techniques: precise geometry, bold lines, dynamic composition.
        """
        draw = ImageDraw.Draw(image)
        
        # Geometric, industrial forms
        num_elements = random.randint(6, 12)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 12, self.width // 5)
            
            # Geometric shapes
            shape = random.choice(['rectangle', 'triangle', 'circle', 'line'])
            
            if shape == 'rectangle':
                w = size
                h = size * random.uniform(0.5, 2.0)
                draw.rectangle([x - w//2, y - h//2, x + w//2, y + h//2],
                             fill=color, outline=(0, 0, 0), width=2)
            elif shape == 'triangle':
                points = [
                    (x, y - size),
                    (x - size, y + size),
                    (x + size, y + size)
                ]
                draw.polygon(points, fill=color, outline=(0, 0, 0), width=2)
            elif shape == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=(0, 0, 0), width=2)
            else:  # line
                angle = random.uniform(0, 2 * math.pi)
                x2 = int(x + size * 2 * math.cos(angle))
                y2 = int(y + size * 2 * math.sin(angle))
                draw.line([(x, y), (x2, y2)], fill=color, width=4)
        
        return image
    
    def _create_de_stijl(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        De Stijl: Primary colors, black/white, geometric grid.
        Techniques: horizontal/vertical lines, rectangles, primary colors only.
        """
        draw = ImageDraw.Draw(image)
        
        # Grid-based composition with primary colors
        grid_size = self.width // 8
        
        for x in range(0, self.width, grid_size):
            for y in range(0, self.height, grid_size):
                if random.random() < 0.3:
                    color = random.choice(palette)
                    draw.rectangle([x, y, x + grid_size, y + grid_size],
                                 fill=color, outline=(0, 0, 0), width=2)
        
        # Add bold horizontal/vertical lines
        for _ in range(random.randint(3, 6)):
            color = random.choice(palette)
            if random.random() < 0.5:
                # Horizontal line
                y = random.randint(0, self.height)
                draw.line([(0, y), (self.width, y)], fill=color, width=4)
            else:
                # Vertical line
                x = random.randint(0, self.width)
                draw.line([(x, 0), (x, self.height)], fill=color, width=4)
        
        return image
    
    def _create_art_deco(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Art Deco: Decorative, geometric, luxurious, streamlined.
        Techniques: geometric patterns, metallic colors, symmetry.
        """
        draw = ImageDraw.Draw(image)
        
        # Decorative geometric patterns
        num_patterns = random.randint(4, 8)
        
        for _ in range(num_patterns):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 10, self.width // 5)
            
            # Art Deco patterns (sunburst, chevrons, etc.)
            pattern_type = random.choice(['sunburst', 'chevron', 'zigzag', 'fan'])
            
            if pattern_type == 'sunburst':
                # Sunburst pattern
                for i in range(16):
                    angle = 2 * math.pi * i / 16
                    x2 = int(x + size * math.cos(angle))
                    y2 = int(y + size * math.sin(angle))
                    draw.line([(x, y), (x2, y2)], fill=color, width=3)
            
            elif pattern_type == 'chevron':
                # Chevron pattern
                for i in range(5):
                    offset = i * size // 5
                    points = [
                        (x - size + offset, y),
                        (x - size//2 + offset, y - size//2),
                        (x + offset, y),
                        (x - size//2 + offset, y + size//2)
                    ]
                    draw.polygon(points, fill=color, outline=None)
            
            elif pattern_type == 'zigzag':
                # Zigzag pattern
                points = []
                for i in range(8):
                    px = x + (i - 4) * size // 4
                    py = y + (size // 2 if i % 2 == 0 else -size // 2)
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=None)
            
            else:  # fan
                # Fan pattern
                for i in range(12):
                    angle = -math.pi / 2 + (math.pi / 12) * i
                    x2 = int(x + size * math.cos(angle))
                    y2 = int(y + size * math.sin(angle))
                    draw.line([(x, y), (x2, y2)], fill=color, width=2)
        
        return image
    
    def _create_art_nouveau(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Art Nouveau: Flowing lines, organic forms, nature motifs.
        Techniques: curved lines, floral patterns, organic shapes.
        """
        draw = ImageDraw.Draw(image)
        
        # Flowing, organic lines
        num_curves = random.randint(8, 15)
        
        for _ in range(num_curves):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            
            # Curved, flowing lines
            points = []
            for i in range(20):
                t = i / 20
                angle = 2 * math.pi * t * random.uniform(1, 3)
                radius = random.randint(30, 80) * (1 - t * 0.5)
                px = int(x + radius * math.cos(angle))
                py = int(y + radius * math.sin(angle))
                points.append((px, py))
            
            # Draw smooth curve
            for i in range(len(points) - 1):
                draw.line([points[i], points[i+1]], fill=color, width=random.randint(2, 5))
        
        # Floral/organic patterns
        for _ in range(random.randint(3, 6)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(30, 60)
            
            # Organic shape (flower-like)
            points = []
            for i in range(12):
                angle = 2 * math.pi * i / 12
                r = size * (1 + 0.3 * math.sin(angle * 3))
                px = int(x + r * math.cos(angle))
                py = int(y + r * math.sin(angle))
                points.append((px, py))
            draw.polygon(points, fill=color, outline=None)
        
        return image
    
    def _create_neoclassicism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Neoclassicism: Classical forms, restrained colors, balanced composition.
        Techniques: classical proportions, clear forms, balanced composition.
        """
        draw = ImageDraw.Draw(image)
        
        # Classical, balanced forms
        num_elements = random.randint(4, 8)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            
            # Use classical proportions
            x = random.choice([
                int(self.width / 3), int(self.width * 2 / 3),
                self.center_x, int(self.width / self.golden_ratio),
                int(self.width - self.width / self.golden_ratio)
            ])
            y = random.choice([
                int(self.height / 3), int(self.height * 2 / 3),
                self.center_y, int(self.height / self.golden_ratio),
                int(self.height - self.height / self.golden_ratio)
            ])
            
            size = random.randint(self.width // 12, self.width // 6)
            
            # Classical shapes
            shape = random.choice(['circle', 'rectangle', 'triangle'])
            
            if shape == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=None)
            elif shape == 'rectangle':
                w = size
                h = size * self.golden_ratio  # Golden ratio
                draw.rectangle([x - w//2, y - h//2, x + w//2, y + h//2],
                             fill=color, outline=None)
            else:  # triangle
                points = [
                    (x, y - size),
                    (x - size, y + size),
                    (x + size, y + size)
                ]
                draw.polygon(points, fill=color, outline=None)
        
        return image
    
    def _create_romanticism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Romanticism: Emotion, drama, nature, individual expression.
        Techniques: dramatic lighting, emotional colors, dynamic composition.
        """
        draw = ImageDraw.Draw(image)
        
        # Dramatic, emotional composition
        # Create dramatic lighting effect
        light_x = random.randint(0, self.width)
        light_y = random.randint(0, self.height // 2)
        
        # Radial gradient for dramatic lighting
        for y in range(self.height):
            for x in range(self.width):
                dist = math.sqrt((x - light_x)**2 + (y - light_y)**2)
                max_dist = math.sqrt(self.width**2 + self.height**2)
                factor = 1.0 - min(1.0, (dist / max_dist) * 1.5)
                
                base_color = random.choice(palette)
                r = int(base_color[0] * (0.3 + factor * 0.7))
                g = int(base_color[1] * (0.3 + factor * 0.7))
                b = int(base_color[2] * (0.3 + factor * 0.7))
                image.putpixel((x, y), (r, g, b))
        
        # Add dramatic elements
        num_elements = random.randint(5, 10)
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(30, 100)
            
            # Dramatic forms
            draw.ellipse([x - size, y - size, x + size, y + size],
                       fill=color, outline=None)
        
        return image
    
    def _create_realism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Realism: Objective representation, true-to-life colors, natural forms.
        Techniques: accurate proportions, natural colors, realistic rendering.
        """
        draw = ImageDraw.Draw(image)
        
        # Realistic, natural forms
        num_elements = random.randint(6, 12)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(20, 80)
            
            # Natural, realistic shapes
            shape = random.choice(['circle', 'ellipse', 'organic'])
            
            if shape == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=None)
            elif shape == 'ellipse':
                w = size
                h = int(size * random.uniform(0.6, 1.4))
                draw.ellipse([x - w, y - h, x + w, y + h],
                           fill=color, outline=None)
            else:  # organic
                # Organic, natural shape
                points = []
                for i in range(12):
                    angle = 2 * math.pi * i / 12
                    r = size * random.uniform(0.8, 1.2)
                    px = int(x + r * math.cos(angle))
                    py = int(y + r * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=None)
        
        # Apply subtle texture for realism
        image = image.filter(ImageFilter.GaussianBlur(radius=0.3))
        
        return image
    
    def _create_naturalism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Naturalism: Detailed nature representation, scientific accuracy.
        Techniques: fine detail, natural colors, accurate representation.
        """
        # Similar to realism but with nature focus
        image = self._create_realism(image, palette)
        
        # Add nature-inspired details
        draw = ImageDraw.Draw(image)
        
        # Add texture details (simulating natural textures)
        for _ in range(random.randint(30, 60)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1, 3)
            draw.ellipse([x - size, y - size, x + size, y + size], fill=color)
        
        return image
    
    def _create_mannerism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Mannerism: Elongated forms, complex composition, sophisticated elegance.
        Techniques: elongated proportions, complex poses, sophisticated colors.
        """
        draw = ImageDraw.Draw(image)
        
        # Elongated, sophisticated forms
        num_elements = random.randint(5, 10)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            
            # Elongated forms
            w = random.randint(20, 60)
            h = int(w * random.uniform(1.5, 3.0))  # Elongated
            
            # Elongated ellipse
            draw.ellipse([x - w, y - h, x + w, y + h],
                       fill=color, outline=None)
        
        # Complex, sophisticated patterns
        for _ in range(random.randint(3, 6)):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(30, 80)
            
            # Complex polygon
            sides = random.randint(6, 10)
            points = []
            for i in range(sides):
                angle = 2 * math.pi * i / sides
                r = size * random.uniform(0.7, 1.3)
                px = int(x + r * math.cos(angle))
                py = int(y + r * math.sin(angle))
                points.append((px, py))
            draw.polygon(points, fill=color, outline=None)
        
        return image
    
    def _create_rococo(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Rococo: Light, decorative, playful, ornate.
        Techniques: delicate forms, pastel colors, decorative patterns.
        """
        draw = ImageDraw.Draw(image)
        
        # Light, decorative elements
        num_elements = random.randint(8, 15)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            # Lighten colors (pastel effect)
            r, g, b = color
            r = min(255, int(r + (255 - r) * 0.4))
            g = min(255, int(g + (255 - g) * 0.4))
            b = min(255, int(b + (255 - b) * 0.4))
            color = (r, g, b)
            
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(15, 40)
            
            # Decorative, delicate forms
            shape = random.choice(['circle', 'flower', 'scroll'])
            
            if shape == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=None)
            elif shape == 'flower':
                # Flower-like pattern
                for i in range(8):
                    angle = 2 * math.pi * i / 8
                    px = int(x + size * math.cos(angle))
                    py = int(y + size * math.sin(angle))
                    draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=color)
            else:  # scroll
                # Scroll-like curve
                points = []
                for i in range(15):
                    t = i / 15
                    px = int(x + size * 2 * t)
                    py = int(y + size * math.sin(t * math.pi * 2))
                    points.append((px, py))
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i+1]], fill=color, width=2)
        
        return image
    
    def _create_classicism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Classicism: Balance, harmony, clarity, order.
        Techniques: balanced composition, clear forms, harmonious colors.
        """
        draw = ImageDraw.Draw(image)
        
        # Balanced, harmonious composition
        num_elements = random.randint(4, 8)
        
        # Use symmetrical placement
        positions = [
            (self.width // 4, self.height // 4),
            (3 * self.width // 4, self.height // 4),
            (self.width // 4, 3 * self.height // 4),
            (3 * self.width // 4, 3 * self.height // 4),
            (self.center_x, self.center_y),
        ]
        
        for i, (x, y) in enumerate(positions[:num_elements]):
            color = random.choice(palette)
            size = random.randint(self.width // 15, self.width // 8)
            
            # Balanced, clear forms
            shape = random.choice(['circle', 'square'])
            
            if shape == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=None)
            else:  # square
                draw.rectangle([x - size, y - size, x + size, y + size],
                             fill=color, outline=None)
        
        return image
    
    def _create_symbolism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Symbolism: Symbolic meaning, metaphors, dreamlike quality.
        Techniques: symbolic forms, meaningful colors, suggestive imagery.
        """
        draw = ImageDraw.Draw(image)
        
        # Symbolic, meaningful elements
        num_elements = random.randint(6, 12)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(30, 80)
            
            # Symbolic forms (abstract, suggestive)
            element_type = random.choice(['spiral', 'mandala', 'abstract'])
            
            if element_type == 'spiral':
                # Spiral (symbol of growth, transformation)
                points = []
                for i in range(50):
                    t = i / 50
                    angle = 4 * math.pi * t
                    radius = size * t
                    px = int(x + radius * math.cos(angle))
                    py = int(y + radius * math.sin(angle))
                    points.append((px, py))
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i+1]], fill=color, width=2)
            
            elif element_type == 'mandala':
                # Mandala pattern (symbolic circle)
                for i in range(8):
                    angle = 2 * math.pi * i / 8
                    x2 = int(x + size * math.cos(angle))
                    y2 = int(y + size * math.sin(angle))
                    draw.line([(x, y), (x2, y2)], fill=color, width=2)
                draw.ellipse([x - size//2, y - size//2, x + size//2, y + size//2],
                           fill=None, outline=color, width=2)
            
            else:  # abstract
                # Abstract symbolic form
                points = []
                for i in range(10):
                    angle = 2 * math.pi * i / 10
                    r = size * random.uniform(0.5, 1.5)
                    px = int(x + r * math.cos(angle))
                    py = int(y + r * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=None)
        
        return image
    
    def _create_precisionism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Precisionism: Precise, clean lines, industrial forms, geometric precision.
        Techniques: sharp edges, clean forms, industrial aesthetic.
        """
        draw = ImageDraw.Draw(image)
        
        # Precise, industrial forms
        num_elements = random.randint(6, 12)
        
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(self.width // 15, self.width // 6)
            
            # Precise geometric forms
            shape = random.choice(['rectangle', 'triangle', 'precise_circle'])
            
            if shape == 'rectangle':
                w = size
                h = size * random.uniform(0.5, 2.0)
                draw.rectangle([x - w//2, y - h//2, x + w//2, y + h//2],
                             fill=color, outline=(0, 0, 0), width=1)
            elif shape == 'triangle':
                points = [
                    (x, y - size),
                    (x - size, y + size),
                    (x + size, y + size)
                ]
                draw.polygon(points, fill=color, outline=(0, 0, 0), width=1)
            else:  # precise_circle
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=(0, 0, 0), width=1)
        
        # Add precise lines (industrial)
        for _ in range(random.randint(5, 10)):
            color = random.choice(palette)
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=2)
        
        return image
    
    def _create_abstract(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """Abstract: Non-representational, form and color focused."""
        draw = ImageDraw.Draw(image)
        
        num_elements = random.randint(8, 15)
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(20, 100)
            
            shape = random.choice(['circle', 'rectangle', 'polygon'])
            if shape == 'circle':
                draw.ellipse([x - size, y - size, x + size, y + size], fill=color)
            elif shape == 'rectangle':
                draw.rectangle([x - size, y - size, x + size, y + size], fill=color)
            else:
                sides = random.randint(3, 8)
                points = []
                for i in range(sides):
                    angle = 2 * math.pi * i / sides
                    px = int(x + size * math.cos(angle))
                    py = int(y + size * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color)
        
        return image
    
    def _apply_style_finish(self, image: Image.Image, style: str) -> Image.Image:
        """Apply final style-specific effects."""
        # Contrast adjustments
        enhancer = ImageEnhance.Contrast(image)
        contrast_factors = {
            'hyperrealism': 1.15,
            'photorealism': 1.12,
            'pop_art': 1.3,
            'op_art': 1.4,
            'fauvism': 1.2,
            'futurism': 1.15,
            'constructivism': 1.2,
            'precisionism': 1.1,
            'minimalism': 1.05,
        }
        factor = contrast_factors.get(style, 1.1)
        image = enhancer.enhance(factor)
        
        # Saturation adjustments
        enhancer = ImageEnhance.Color(image)
        saturation_factors = {
            'pop_art': 1.4,
            'fauvism': 1.5,
            'futurism': 1.3,
            'hyperrealism': 0.95,  # More natural
            'photorealism': 0.95,
            'realism': 0.9,
            'naturalism': 0.9,
            'minimalism': 0.8,
        }
        factor = saturation_factors.get(style, 1.05)
        image = enhancer.enhance(factor)
        
        # Blur for certain styles
        if style in ['hyperrealism', 'photorealism', 'realism', 'naturalism']:
            # Very slight blur for texture
            image = image.filter(ImageFilter.GaussianBlur(radius=0.2))
        elif style == 'rococo':
            # Soft blur for delicate effect
            image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
        
        # Sharpening for precision
        if style in ['precisionism', 'op_art', 'constructivism', 'de_stijl']:
            image = image.filter(ImageFilter.SHARPEN)
        
        return image

