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
import numpy as np

# Advanced image processing libraries (optional)
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False
    cv2 = None

try:
    from scipy import ndimage, interpolate
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    ndimage = None
    interpolate = None

try:
    from skimage import filters, morphology, restoration
    SKIMAGE_AVAILABLE = True
except ImportError:
    SKIMAGE_AVAILABLE = False
    filters = None
    morphology = None
    restoration = None

# Import advanced color system
from Malevich.utils.color_systems import AdvancedColorSystem


class ComprehensiveStyleGenerator:
    """
    Comprehensive generator supporting 30+ art styles and techniques.
    From classical to contemporary, including hyperrealism.
    """
    
    # Extended color palettes for various art movements
    STYLE_PALETTES: Dict[str, List[Tuple[int, int, int]]] = {
        # Hyperrealism: vibrant natural colors with rich depth and detail
        'hyperrealism': [
            (180, 140, 100), (200, 160, 120), (160, 120, 80),  # Earth tones
            (140, 180, 220), (120, 160, 200), (100, 140, 180),  # Sky blues
            (220, 180, 140), (200, 160, 120), (180, 140, 100),  # Warm beiges
            (100, 140, 100), (120, 160, 120), (80, 120, 80),   # Natural greens
            (220, 200, 180), (200, 180, 160), (180, 160, 140),  # Light tones
            (60, 40, 30), (80, 60, 50), (100, 80, 70)          # Dark accents
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
        # Dadaism: random, unexpected colors (generated at runtime, not at import time)
        # Note: This list is a placeholder. Actual colors are generated in _get_palette()
        'dadaism': None,  # Special marker: generate random colors at runtime
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
        # Realism: natural, true-to-life colors with rich variety
        'realism': [
            (150, 120, 90), (170, 140, 110), (130, 100, 70),   # Earth browns
            (100, 150, 200), (80, 130, 180), (120, 170, 220),  # Sky blues
            (180, 150, 120), (200, 170, 140), (160, 130, 100), # Sand tones
            (80, 120, 80), (100, 140, 100), (60, 100, 60),     # Forest greens
            (220, 200, 180), (200, 180, 160), (240, 220, 200), # Light creams
            (40, 30, 20), (60, 50, 40), (80, 70, 60)           # Deep shadows
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
        # Classicism: balanced, harmonious colors with classical elegance
        'classicism': [
            (240, 230, 220), (220, 210, 200), (200, 190, 180),  # Marble whites
            (180, 160, 140), (160, 140, 120), (140, 120, 100),  # Stone grays
            (200, 180, 160), (220, 200, 180), (180, 160, 140),  # Warm stones
            (100, 120, 140), (120, 140, 160), (80, 100, 120),   # Cool grays
            (220, 200, 180), (200, 180, 160), (180, 160, 140),  # Beige tones
            (60, 50, 40), (80, 70, 60), (100, 90, 80)           # Dark accents
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
        # Impressionism: soft, light colors, visible brushstrokes
        'impressionism': [
            (240, 230, 220), (220, 210, 200), (200, 220, 240),  # Soft whites and sky blues
            (180, 200, 220), (220, 200, 180), (200, 180, 160), # Light pastels
            (240, 220, 200), (200, 240, 220), (220, 200, 240), # Soft pinks and greens
            (180, 220, 200), (220, 180, 200), (200, 200, 220), # Lavender and mint
            (160, 180, 200), (200, 160, 180), (180, 200, 160)  # Gentle tones
        ],
    }
    
    def __init__(self, width: int = 1080, height: int = 1080):
        """Initialize comprehensive style generator."""
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.golden_ratio = 1.618033988749895
    
    def generate(self, style: str = 'auto', palette_name: Optional[str] = None, 
                 creative_mode: bool = True, subject: Optional[str] = None) -> Image.Image:
        """
        Generate image in specified artistic style with creative enhancements.
        
        Args:
            style: Art style (see available styles below)
            palette_name: Specific palette name
            creative_mode: Enable creative enhancements (mixing, effects, surprises)
            subject: Subject type ('landscape', 'portrait', 'animal', 'interior', None for abstract)
            
        Returns:
            PIL Image object
        """
        if style == 'auto':
            style = random.choice(list(self.STYLE_PALETTES.keys()))
        
        palette = self._get_palette(palette_name, style)
        image = Image.new('RGB', (self.width, self.height), self._get_background_color(palette))
        
        # Generate subject first if specified
        if subject:
            subject_methods = {
                'landscape': self._create_landscape,
                'portrait': self._create_portrait,
                'animal': self._create_animal,
                'interior': self._create_interior,
            }
            if subject in subject_methods:
                image = subject_methods[subject](image, palette)
            else:
                # Fallback to abstract if unknown subject
                subject = None
        
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
            'impressionism': self._create_impressionism,
        }
        
        if style in style_methods:
            # If subject was created, blend style with it; otherwise create style from scratch
            if subject:
                style_image = Image.new('RGB', (self.width, self.height), self._get_background_color(palette))
                style_image = style_methods[style](style_image, palette)
                # Blend subject with style
                image = Image.blend(image, style_image, alpha=0.6)
            else:
                image = style_methods[style](image, palette)
        else:
            # Warn about unsupported style
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"Unsupported style '{style}'. Using fallback.")
            # Fallback to abstract
            if not subject:
                image = self._create_abstract(image, palette)
            # If subject exists but style is unsupported, keep subject without style blending
        
        # Apply creative enhancements
        if creative_mode:
            image = self._apply_creative_enhancements(image, style, palette)
        
        # Apply final style-specific touches
        image = self._apply_style_finish(image, style)
        return image
    
    def _get_palette(self, palette_name: Optional[str], style: str) -> List[Tuple[int, int, int]]:
        """Get color palette based on style."""
        if palette_name and palette_name in self.STYLE_PALETTES:
            palette = self.STYLE_PALETTES[palette_name]
            # Fixed: Generate random colors for dadaism at runtime, not at import time
            if palette is None and palette_name == 'dadaism':
                return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        for _ in range(12)]
            return palette
        
        palette = self.STYLE_PALETTES.get(style, self.STYLE_PALETTES['realism'])
        # Fixed: Generate random colors for dadaism at runtime, not at import time
        if palette is None and style == 'dadaism':
            return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    for _ in range(12)]
        return palette
    
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
        Hyperrealism: Photographic precision, extreme detail, rich colors.
        Techniques: fine brushwork, subtle color transitions, texture detail, realistic forms,
        photographic lighting, extreme depth, micro-details.
        """
        draw = ImageDraw.Draw(image)
        
        # Create rich, vibrant base with complex color harmony
        base_color = random.choice(palette)
        complex_palette = AdvancedColorSystem.generate_complex_harmony(
            base_color, 'analogous_extended', variations=40
        )
        
        # Create sophisticated gradient background with rich colors and depth
        gradient_overlay = Image.new('RGB', (self.width, self.height))
        gradient_pixels = gradient_overlay.load()
        
        # Multiple gradient sources for depth
        grad_centers = [
            (random.randint(0, self.width - 1), random.randint(0, self.height - 1)),
            (random.randint(0, self.width - 1), random.randint(0, self.height - 1)),
            (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        ]
        
        for y in range(self.height):
            for x in range(self.width):
                # Combine multiple gradients
                total_influence = 0
                r_sum, g_sum, b_sum = 0, 0, 0
                
                for center_x, center_y in grad_centers:
                    dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                    max_dist = math.sqrt(self.width**2 + self.height**2)
                    influence = max(0, 1.0 - (dist / max_dist) * 1.5)
                    
                    if influence > 0:
                        color_idx = int((dist / max_dist) * (len(complex_palette) - 1))
                        color = complex_palette[min(color_idx, len(complex_palette) - 1)]
                        r_sum += color[0] * influence
                        g_sum += color[1] * influence
                        b_sum += color[2] * influence
                        total_influence += influence
                
                if total_influence > 0:
                    r = int(r_sum / total_influence)
                    g = int(g_sum / total_influence)
                    b = int(b_sum / total_influence)
                else:
                    r, g, b = complex_palette[0]
                
                # Add fine texture variation (micro-details)
                variation = random.randint(-3, 3)
                r = max(0, min(255, r + variation))
                g = max(0, min(255, g + variation))
                b = max(0, min(255, b + variation))
                gradient_pixels[x, y] = (r, g, b)
        
        image = Image.blend(image, gradient_overlay, alpha=0.85)
        
        # Photographic lighting setup
        main_light_x = random.randint(self.width // 4, 3 * self.width // 4)
        main_light_y = random.randint(0, self.height // 3)
        fill_light_x = self.width - main_light_x
        fill_light_y = self.height - main_light_y
        
        # Add realistic forms and structures with extreme detail
        num_forms = random.randint(10, 18)
        for _ in range(num_forms):
            form_color = random.choice(complex_palette)
            x = random.randint(self.width // 5, 4 * self.width // 5)
            y = random.randint(self.height // 5, 4 * self.height // 5)
            size = random.randint(40, 150)
            
            # Create hyperrealistic form with photographic lighting
            form_overlay = Image.new('RGB', (self.width, self.height), (0, 0, 0))
            form_pixels = form_overlay.load()
            
            for sy in range(max(0, y - size), min(self.height, y + size)):
                for sx in range(max(0, x - size), min(self.width, x + size)):
                    dx = (sx - x) / size
                    dy = (sy - y) / size
                    dist = math.sqrt(dx*dx + dy*dy)
                    
                    if dist < 1.0:
                        # Calculate 3D surface normal (for realistic lighting)
                        if dist > 0:
                            nx = dx / dist
                            ny = dy / dist
                            nz = math.sqrt(1.0 - min(1.0, dist*dist))
                        else:
                            nx, ny, nz = 0, 0, 1
                        
                        # Main light (key light)
                        light_dir_x = (sx - main_light_x) / size
                        light_dir_y = (sy - main_light_y) / size
                        light_dir_len = math.sqrt(light_dir_x*light_dir_x + light_dir_y*light_dir_y)
                        if light_dir_len > 0:
                            light_dir_x /= light_dir_len
                            light_dir_y /= light_dir_len
                        
                        # Calculate lighting (dot product of normal and light direction)
                        light_dot = max(0, nz * 0.7 + (nx * light_dir_x + ny * light_dir_y) * 0.3)
                        
                        # Fill light (softer, from opposite side)
                        fill_light_dir_x = (sx - fill_light_x) / size
                        fill_light_dir_y = (sy - fill_light_y) / size
                        fill_light_dir_len = math.sqrt(fill_light_dir_x*fill_light_dir_x + fill_light_dir_y*fill_light_dir_y)
                        if fill_light_dir_len > 0:
                            fill_light_dir_x /= fill_light_dir_len
                            fill_light_dir_y /= fill_light_dir_len
                        
                        fill_light_dot = max(0, nz * 0.5 + (nx * fill_light_dir_x + ny * fill_light_dir_y) * 0.2)
                        
                        # Combine lights
                        total_light = min(1.0, light_dot * 0.7 + fill_light_dot * 0.3)
                        # Add ambient light
                        total_light = max(0.15, total_light + 0.1)
                        
                        # Apply lighting to color
                        r, g, b = form_color
                        r = int(r * total_light)
                        g = int(g * total_light)
                        b = int(b * total_light)
                        
                        # Add specular highlight (photographic shine)
                        if light_dot > 0.8:
                            highlight = (light_dot - 0.8) * 5
                            r = min(255, int(r + highlight * 50))
                            g = min(255, int(g + highlight * 50))
                            b = min(255, int(b + highlight * 50))
                        
                        # Add micro-texture (fine detail)
                        texture = random.randint(-4, 4)
                        r = max(0, min(255, r + texture))
                        g = max(0, min(255, g + texture))
                        b = max(0, min(255, b + texture))
                        
                        form_pixels[sx, sy] = (r, g, b)
            
            image = Image.blend(image, form_overlay, alpha=0.75)
            draw = ImageDraw.Draw(image)
        
        # Add extreme fine details (hyperrealistic texture)
        num_fine_details = random.randint(200, 400)
        detail_overlay = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        detail_pixels = detail_overlay.load()
        
        for _ in range(num_fine_details):
            detail_x = random.randint(0, self.width - 1)
            detail_y = random.randint(0, self.height - 1)
            detail_color = random.choice(complex_palette)
            
            # Very small detail (1-2 pixels)
            detail_size = random.randint(1, 2)
            for dy in range(-detail_size, detail_size + 1):
                for dx in range(-detail_size, detail_size + 1):
                    px = detail_x + dx
                    py = detail_y + dy
                    if 0 <= px < self.width and 0 <= py < self.height:
                        existing = image.getpixel((px, py))
                        # Subtle blend for fine detail
                        blend_factor = 0.3
                        blended = (
                            int(existing[0] * (1 - blend_factor) + detail_color[0] * blend_factor),
                            int(existing[1] * (1 - blend_factor) + detail_color[1] * blend_factor),
                            int(existing[2] * (1 - blend_factor) + detail_color[2] * blend_factor)
                        )
                        detail_pixels[px, py] = blended
        
        image = Image.blend(image, detail_overlay, alpha=0.4)
        
        # Add photographic texture (film grain effect)
        grain_overlay = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        grain_pixels = grain_overlay.load()
        
        for y in range(self.height):
            for x in range(self.width):
                existing = image.getpixel((x, y))
                # Fine grain
                grain = random.randint(-2, 2)
                r = max(0, min(255, existing[0] + grain))
                g = max(0, min(255, existing[1] + grain))
                b = max(0, min(255, existing[2] + grain))
                grain_pixels[x, y] = (r, g, b)
        
        image = Image.blend(image, grain_overlay, alpha=0.15)
        
        # Enhance photographic quality
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.25)  # Strong contrast for photographic look
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(1.3)  # Sharp for hyperrealistic detail
        
        # Use OpenCV for advanced sharpening if available
        if CV2_AVAILABLE:
            # Unsharp masking for professional sharpening
            image = self._enhance_with_opencv(image, enhancement_type='detail')
        else:
            # Very subtle sharpen filter
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
            
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
            
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
                x2 = random.randint(0, self.width - 1)
                y2 = random.randint(0, self.height - 1)
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
                y = random.randint(0, self.height - 1)
                draw.line([(0, y), (self.width, y)], fill=color, width=4)
            else:
                # Vertical line
                x = random.randint(0, self.width - 1)
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
        light_x = random.randint(0, self.width - 1)
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            size = random.randint(30, 100)
            
            # Dramatic forms
            draw.ellipse([x - size, y - size, x + size, y + size],
                       fill=color, outline=None)
        
        return image
    
    def _create_realism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Realism: Objective representation, true-to-life colors, natural forms.
        Techniques: accurate proportions, natural colors, realistic rendering, clear composition,
        chiaroscuro lighting, natural textures, depth and volume.
        """
        draw = ImageDraw.Draw(image)
        
        # Create rich, natural color palette
        natural_palette = []
        for color in palette:
            # Ensure colors are natural and not too saturated
            r, g, b = color
            # Convert to HSV to reduce saturation
            h, s, v = rgb_to_hsv(r/255.0, g/255.0, b/255.0)
            s = min(0.7, s * 0.8)  # Reduce saturation for natural look
            r, g, b = hsv_to_rgb(h, s, v)
            natural_palette.append((int(r*255), int(g*255), int(b*255)))
        
        # Create natural composition with clear forms and depth
        num_elements = random.randint(6, 12)
        
        # Use rule of thirds for composition
        thirds_x = [self.width // 3, 2 * self.width // 3]
        thirds_y = [self.height // 3, 2 * self.height // 3]
        
        # Light source for realistic lighting
        light_x = random.randint(self.width // 4, 3 * self.width // 4)
        light_y = random.randint(0, self.height // 3)
        
        for i in range(num_elements):
            color = random.choice(natural_palette)
            
            # Place elements using rule of thirds
            if i < len(thirds_x) * len(thirds_y):
                x = thirds_x[i % len(thirds_x)]
                y = thirds_y[i // len(thirds_x)]
            else:
                x = random.randint(self.width // 4, 3 * self.width // 4)
                y = random.randint(self.height // 4, 3 * self.height // 4)
            
            size = random.randint(50, 120)
            
            # Natural, realistic shapes with depth and lighting
            shape = random.choice(['sphere', 'organic', 'landscape', 'natural_form'])
            
            if shape == 'sphere':
                # Realistic sphere with lighting (3D effect)
                sphere_overlay = Image.new('RGB', (self.width, self.height), (0, 0, 0))
                sphere_pixels = sphere_overlay.load()
                
                for sy in range(max(0, y - size), min(self.height, y + size)):
                    for sx in range(max(0, x - size), min(self.width, x + size)):
                        dx = sx - x
                        dy = sy - y
                        dist = math.sqrt(dx*dx + dy*dy)
                        
                        if dist < size:
                            # Calculate 3D sphere lighting
                            # Normalize to sphere surface
                            z = math.sqrt(size*size - dist*dist)
                            # Calculate light direction
                            light_dx = sx - light_x
                            light_dy = sy - light_y
                            light_dist = math.sqrt(light_dx*light_dx + light_dy*light_dy)
                            
                            # Simple lighting model
                            light_factor = max(0.4, min(1.0, 1.0 - (dist / size) * 0.3))
                            # Add highlight from light source
                            if light_dist < size * 1.5:
                                highlight = max(0, 1.0 - light_dist / (size * 1.5))
                                light_factor = min(1.0, light_factor + highlight * 0.3)
                            
                            # Apply lighting to color
                            r, g, b = color
                            r = int(r * light_factor)
                            g = int(g * light_factor)
                            b = int(b * light_factor)
                            
                            # Add subtle texture
                            texture = random.randint(-5, 5)
                            r = max(0, min(255, r + texture))
                            g = max(0, min(255, g + texture))
                            b = max(0, min(255, b + texture))
                            
                            sphere_pixels[sx, sy] = (r, g, b)
                
                image = Image.blend(image, sphere_overlay, alpha=0.8)
                draw = ImageDraw.Draw(image)
                
            elif shape == 'organic':
                # Organic, natural shape with depth
                points = []
                num_points = random.randint(8, 12)
                for j in range(num_points):
                    angle = 2 * math.pi * j / num_points
                    r = size * random.uniform(0.75, 1.15)
                    px = int(x + r * math.cos(angle))
                    py = int(y + r * math.sin(angle))
                    points.append((px, py))
                
                # Create gradient fill for depth
                if len(points) > 2:
                    # Base shape
                    draw.polygon(points, fill=color, outline=None)
                    
                    # Add highlight from light source
                    highlight_x = x + (light_x - x) * 0.3
                    highlight_y = y + (light_y - y) * 0.3
                    highlight_size = size // 3
                    highlight_color = (
                        min(255, int(color[0] * 1.3)),
                        min(255, int(color[1] * 1.3)),
                        min(255, int(color[2] * 1.3))
                    )
                    draw.ellipse([highlight_x - highlight_size, highlight_y - highlight_size,
                                highlight_x + highlight_size, highlight_y + highlight_size],
                               fill=highlight_color, outline=None)
                    
                    # Add shadow on opposite side
                    shadow_x = x - (light_x - x) * 0.3
                    shadow_y = y - (light_y - y) * 0.3
                    shadow_size = size // 4
                    shadow_color = (
                        max(0, int(color[0] * 0.6)),
                        max(0, int(color[1] * 0.6)),
                        max(0, int(color[2] * 0.6))
                    )
                    draw.ellipse([shadow_x - shadow_size, shadow_y - shadow_size,
                                shadow_x + shadow_size, shadow_y + shadow_size],
                               fill=shadow_color, outline=None)
                
            elif shape == 'landscape':
                # Create realistic landscape elements with depth
                horizon_y = y
                sky_color = random.choice(natural_palette)
                # Lighten for sky
                r, g, b = sky_color
                r = min(255, int(r + (255 - r) * 0.3))
                g = min(255, int(g + (255 - g) * 0.3))
                b = min(255, int(b + (255 - b) * 0.3))
                sky_color = (r, g, b)
                
                # Sky gradient
                for sy in range(max(0, horizon_y - size*2), horizon_y):
                    gradient_t = (sy - (horizon_y - size*2)) / (size*2) if size*2 > 0 else 0
                    gradient_t = max(0, min(1, gradient_t))
                    grad_r = int(sky_color[0] * (1 - gradient_t * 0.2))
                    grad_g = int(sky_color[1] * (1 - gradient_t * 0.2))
                    grad_b = int(sky_color[2] * (1 - gradient_t * 0.2))
                    draw.rectangle([x - size*2, sy, x + size*2, sy + 1],
                                  fill=(grad_r, grad_g, grad_b), outline=None)
                
                # Ground with texture
                ground_color = random.choice(natural_palette)
                # Darken for ground
                r, g, b = ground_color
                r = max(0, int(r * 0.7))
                g = max(0, int(g * 0.7))
                b = max(0, int(b * 0.7))
                ground_color = (r, g, b)
                
                for sy in range(horizon_y, min(self.height, horizon_y + size)):
                    # Add texture variation
                    texture = random.randint(-10, 10)
                    tex_r = max(0, min(255, ground_color[0] + texture))
                    tex_g = max(0, min(255, ground_color[1] + texture))
                    tex_b = max(0, min(255, ground_color[2] + texture))
                    draw.rectangle([x - size*2, sy, x + size*2, sy + 1],
                                  fill=(tex_r, tex_g, tex_b), outline=None)
                
            else:  # natural_form
                # Natural form with realistic volume
                form_overlay = Image.new('RGB', (self.width, self.height), (0, 0, 0))
                form_pixels = form_overlay.load()
                
                for sy in range(max(0, y - size), min(self.height, y + size)):
                    for sx in range(max(0, x - size), min(self.width, x + size)):
                        dx = (sx - x) / size
                        dy = (sy - y) / size
                        dist = math.sqrt(dx*dx + dy*dy)
                        
                        if dist < 1.0:
                            # Calculate lighting
                            light_dx = sx - light_x
                            light_dy = sy - light_y
                            light_dist = math.sqrt(light_dx*light_dx + light_dy*light_dy)
                            light_factor = max(0.5, 1.0 - (dist * 0.4))
                            
                            if light_dist < size * 2:
                                highlight = max(0, 1.0 - light_dist / (size * 2))
                                light_factor = min(1.0, light_factor + highlight * 0.2)
                            
                            r, g, b = color
                            r = int(r * light_factor)
                            g = int(g * light_factor)
                            b = int(b * light_factor)
                            
                            form_pixels[sx, sy] = (r, g, b)
                
                image = Image.blend(image, form_overlay, alpha=0.75)
                draw = ImageDraw.Draw(image)
        
        # Add natural texture overlay
        texture_overlay = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        texture_pixels = texture_overlay.load()
        
        for y in range(self.height):
            for x in range(self.width):
                existing = image.getpixel((x, y))
                # Add subtle texture noise
                noise = random.randint(-3, 3)
                r = max(0, min(255, existing[0] + noise))
                g = max(0, min(255, existing[1] + noise))
                b = max(0, min(255, existing[2] + noise))
                texture_pixels[x, y] = (r, g, b)
        
        image = Image.blend(image, texture_overlay, alpha=0.3)
        
        # Enhance natural appearance
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.15)
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(0.95)  # Slightly desaturate for natural look
        
        # Use OpenCV for better texture if available
        if CV2_AVAILABLE:
            # Bilateral filter for natural texture (smooth but preserves edges)
            image = self._enhance_with_opencv(image, enhancement_type='smooth')
        else:
            # Very subtle blur for natural texture
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            
            # Elongated forms
            w = random.randint(20, 60)
            h = int(w * random.uniform(1.5, 3.0))  # Elongated
            
            # Elongated ellipse
            draw.ellipse([x - w, y - h, x + w, y + h],
                       fill=color, outline=None)
        
        # Complex, sophisticated patterns
        for _ in range(random.randint(3, 6)):
            color = random.choice(palette)
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
            
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
        Classicism: Balance, harmony, clarity, order, classical elegance.
        Techniques: balanced composition, clear forms, harmonious colors, symmetry.
        """
        draw = ImageDraw.Draw(image)
        
        # Create classical composition with symmetry and order
        num_elements = random.randint(6, 12)
        
        # Use golden ratio and symmetrical placement
        golden_x = int(self.width / self.golden_ratio)
        golden_y = int(self.height / self.golden_ratio)
        
        # Symmetrical positions
        positions = [
            (golden_x, golden_y),
            (self.width - golden_x, golden_y),
            (golden_x, self.height - golden_y),
            (self.width - golden_x, self.height - golden_y),
            (self.center_x, self.center_y),
            (self.width // 2, golden_y),
            (self.width // 2, self.height - golden_y),
            (golden_x, self.height // 2),
            (self.width - golden_x, self.height // 2),
        ]
        
        for i, (x, y) in enumerate(positions[:num_elements]):
            color = random.choice(palette)
            size = random.randint(self.width // 12, self.width // 6)
            
            # Classical, balanced forms with depth
            shape = random.choice(['circle', 'square', 'column', 'arch'])
            
            if shape == 'circle':
                # Perfect circle with subtle outline
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=color, outline=(int(color[0]*0.7), int(color[1]*0.7), int(color[2]*0.7)), width=2)
            elif shape == 'square':
                # Perfect square
                draw.rectangle([x - size, y - size, x + size, y + size],
                             fill=color, outline=(int(color[0]*0.7), int(color[1]*0.7), int(color[2]*0.7)), width=2)
            elif shape == 'column':
                # Classical column shape
                column_width = size // 3
                draw.rectangle([x - column_width, y - size*2, x + column_width, y + size*2],
                             fill=color, outline=None)
                # Capital
                draw.ellipse([x - size//2, y - size*2, x + size//2, y - size*2 + size//2],
                           fill=color, outline=None)
            else:  # arch
                # Classical arch
                draw.arc([x - size, y - size, x + size, y + size],
                        start=0, end=180, fill=color, width=size//4)
                draw.rectangle([x - size, y, x + size, y + size],
                             fill=color, outline=None)
        
        # Add classical texture and finish
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(1.05)
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.1)
        
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
            x1 = random.randint(0, self.width - 1)
            y1 = random.randint(0, self.height - 1)
            x2 = random.randint(0, self.width - 1)
            y2 = random.randint(0, self.height - 1)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=2)
        
        return image
    
    def _create_impressionism(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Impressionism: Visible brushstrokes, emphasis on light, ordinary subjects.
        Techniques: broken color, visible brushstrokes, soft edges, light effects.
        """
        draw = ImageDraw.Draw(image)
        
        # Create soft, light-filled base
        base_color = random.choice(palette)
        # Lighten colors for impressionist effect
        r, g, b = base_color
        r = min(255, int(r + (255 - r) * 0.3))
        g = min(255, int(g + (255 - g) * 0.3))
        b = min(255, int(b + (255 - b) * 0.3))
        base_color = (r, g, b)
        
        # Create gradient background with soft colors
        for y in range(self.height):
            for x in range(self.width):
                # Soft gradient variation
                t = (x + y) / (self.width + self.height)
                color_idx = int(t * (len(palette) - 1))
                color = palette[min(color_idx, len(palette) - 1)]
                
                # Lighten for impressionist effect
                r, g, b = color
                r = min(255, int(r + (255 - r) * 0.2))
                g = min(255, int(g + (255 - g) * 0.2))
                b = min(255, int(b + (255 - b) * 0.2))
                color = (r, g, b)
                
                # Add soft variation
                variation = random.randint(-10, 10)
                r = max(0, min(255, color[0] + variation))
                g = max(0, min(255, color[1] + variation))
                b = max(0, min(255, color[2] + variation))
                image.putpixel((x, y), (r, g, b))
        
        # Add visible brushstrokes (broken color technique)
        num_strokes = random.randint(150, 300)
        for _ in range(num_strokes):
            color = random.choice(palette)
            # Slightly vary color for broken color effect
            r, g, b = color
            r = max(0, min(255, r + random.randint(-20, 20)))
            g = max(0, min(255, g + random.randint(-20, 20)))
            b = max(0, min(255, b + random.randint(-20, 20)))
            color = (r, g, b)
            
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            
            # Visible brushstroke (short, directional)
            angle = random.uniform(0, 2 * math.pi)
            length = random.randint(20, 60)
            x2 = int(x + length * math.cos(angle))
            y2 = int(y + length * math.sin(angle))
            thickness = random.randint(3, 8)
            draw.line([(x, y), (x2, y2)], fill=color, width=thickness)
        
        # Add light effects (emphasis on changing light)
        if random.random() < 0.7:
            light_x = random.randint(0, self.width - 1)
            light_y = random.randint(0, self.height // 2)  # Light from above
            light_color = random.choice(palette)
            # Make light color very light
            r, g, b = light_color
            r = min(255, int(r + (255 - r) * 0.5))
            g = min(255, int(g + (255 - g) * 0.5))
            b = min(255, int(b + (255 - b) * 0.5))
            light_color = (r, g, b)
            
            for y in range(self.height):
                for x in range(self.width):
                    dist = math.sqrt((x - light_x)**2 + (y - light_y)**2)
                    max_dist = math.sqrt(self.width**2 + self.height**2)
                    intensity = max(0, 1.0 - (dist / max_dist) * 1.2)
                    
                    if intensity > 0:
                        existing = image.getpixel((x, y))
                        lit = (
                            int(existing[0] + (light_color[0] - existing[0]) * intensity * 0.3),
                            int(existing[1] + (light_color[1] - existing[1]) * intensity * 0.3),
                            int(existing[2] + (light_color[2] - existing[2]) * intensity * 0.3)
                        )
                        image.putpixel((x, y), lit)
        
        # Add soft, organic forms (ordinary subjects)
        num_forms = random.randint(5, 12)
        for _ in range(num_forms):
            color = random.choice(palette)
            # Soften color
            r, g, b = color
            r = min(255, int(r + (255 - r) * 0.2))
            g = min(255, int(g + (255 - g) * 0.2))
            b = min(255, int(b + (255 - b) * 0.2))
            color = (r, g, b)
            
            x = random.randint(self.width // 4, 3 * self.width // 4)
            y = random.randint(self.height // 4, 3 * self.height // 4)
            size = random.randint(30, 100)
            
            # Soft, organic shapes with visible brushstrokes
            shape = random.choice(['circle', 'ellipse', 'organic'])
            if shape == 'circle':
                # Soft circle with visible strokes
                for r in range(size, 0, -3):
                    alpha = r / size
                    stroke_color = (
                        int(color[0] * alpha),
                        int(color[1] * alpha),
                        int(color[2] * alpha)
                    )
                    draw.ellipse([x - r, y - r, x + r, y + r],
                               fill=None, outline=stroke_color, width=2)
            elif shape == 'ellipse':
                w = size
                h = int(size * random.uniform(0.7, 1.3))
                draw.ellipse([x - w, y - h, x + w, y + h],
                           fill=color, outline=None)
            else:  # organic
                # Organic, soft form
                points = []
                for i in range(12):
                    angle = 2 * math.pi * i / 12
                    r = size * random.uniform(0.8, 1.2)
                    px = int(x + r * math.cos(angle))
                    py = int(y + r * math.sin(angle))
                    points.append((px, py))
                draw.polygon(points, fill=color, outline=None)
        
        # Apply soft blur for impressionist effect (soft edges)
        image = image.filter(ImageFilter.GaussianBlur(radius=0.8))
        
        # Enhance brightness slightly (emphasis on light)
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(1.1)
        
        return image
    
    def _create_abstract(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """Abstract: Non-representational, form and color focused."""
        draw = ImageDraw.Draw(image)
        
        num_elements = random.randint(8, 15)
        for _ in range(num_elements):
            color = random.choice(palette)
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
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
    
    def _apply_creative_enhancements(self, image: Image.Image, style: str, 
                                     palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Apply style-specific creative enhancements that enhance each style's uniqueness.
        Each style gets enhancements that match its character.
        """
        draw = ImageDraw.Draw(image)
        
        # Style-specific creative enhancements
        style_enhancements = {
            'hyperrealism': self._enhance_hyperrealism,
            'photorealism': self._enhance_photorealism,
            'realism': self._enhance_realism,
            'classicism': self._enhance_classicism,
            'pop_art': self._enhance_pop_art,
            'op_art': self._enhance_op_art,
            'fauvism': self._enhance_fauvism,
            'futurism': self._enhance_futurism,
            'minimalism': self._enhance_minimalism,
            'dadaism': self._enhance_dadaism,
            'constructivism': self._enhance_constructivism,
            'de_stijl': self._enhance_de_stijl,
            'art_deco': self._enhance_art_deco,
            'art_nouveau': self._enhance_art_nouveau,
            'romanticism': self._enhance_romanticism,
            'neoclassicism': self._enhance_neoclassicism,
            'naturalism': self._enhance_naturalism,
            'mannerism': self._enhance_mannerism,
            'rococo': self._enhance_rococo,
            'symbolism': self._enhance_symbolism,
            'precisionism': self._enhance_precisionism,
            'impressionism': self._enhance_impressionism,
        }
        
        # Apply style-specific enhancement
        if style in style_enhancements:
            image = style_enhancements[style](image, palette, draw)
        else:
            # Generic creative enhancement for unknown styles
            image = self._enhance_generic(image, palette, draw)
        
        return image
    
    def _enhance_hyperrealism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                              draw: ImageDraw.Draw) -> Image.Image:
        """Hyperrealism: Add photographic details, depth, realistic lighting."""
        # Add realistic depth with subtle shadows
        if random.random() < 0.4:
            num_shadows = random.randint(3, 6)
            for _ in range(num_shadows):
                shadow_x = random.randint(0, self.width - 1)
                shadow_y = random.randint(0, self.height - 1)
                shadow_size = random.randint(50, 150)
                
                for y in range(self.height):
                    for x in range(self.width):
                        dist = math.sqrt((x - shadow_x)**2 + (y - shadow_y)**2)
                        if dist < shadow_size:
                            intensity = 1.0 - (dist / shadow_size) * 0.3
                            existing = image.getpixel((x, y))
                            shadowed = (
                                int(existing[0] * (1 - intensity * 0.2)),
                                int(existing[1] * (1 - intensity * 0.2)),
                                int(existing[2] * (1 - intensity * 0.2))
                            )
                            image.putpixel((x, y), shadowed)
        
        # Add fine texture details
        if random.random() < 0.5:
            num_texture_points = random.randint(200, 400)
            for _ in range(num_texture_points):
                detail_color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                existing = image.getpixel((x, y))
                blended = (
                    (existing[0] + detail_color[0]) // 2,
                    (existing[1] + detail_color[1]) // 2,
                    (existing[2] + detail_color[2]) // 2
                )
                image.putpixel((x, y), blended)
        
        return image
    
    def _enhance_photorealism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                              draw: ImageDraw.Draw) -> Image.Image:
        """Photorealism: Photographic effects, depth of field, realistic lighting."""
        # Similar to hyperrealism but with more photographic effects
        image = self._enhance_hyperrealism(image, palette, draw)
        
        # Add depth of field effect (slight blur on edges)
        if random.random() < 0.3:
            # Create edge blur mask
            blur_mask = Image.new('L', (self.width, self.height), 255)
            blur_draw = ImageDraw.Draw(blur_mask)
            center_x, center_y = self.center_x, self.center_y
            max_dist = math.sqrt(self.width**2 + self.height**2)
            
            for y in range(self.height):
                for x in range(self.width):
                    dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                    blur_intensity = min(255, int(255 * (dist / max_dist) * 0.5))
                    blur_mask.putpixel((x, y), blur_intensity)
            
            blurred = image.filter(ImageFilter.GaussianBlur(radius=1.0))
            image = Image.composite(image, blurred, blur_mask)
        
        return image
    
    def _enhance_realism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                        draw: ImageDraw.Draw) -> Image.Image:
        """Realism: Natural composition, realistic forms, subtle variations."""
        # Add natural variations and organic textures
        if random.random() < 0.4:
            num_variations = random.randint(50, 100)
            for _ in range(num_variations):
                var_color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                size = random.randint(2, 5)
                
                for i in range(size):
                    for j in range(size):
                        px = x + i - size//2
                        py = y + j - size//2
                        if 0 <= px < self.width and 0 <= py < self.height:
                            existing = image.getpixel((px, py))
                            blended = (
                                (existing[0] + var_color[0]) // 2,
                                (existing[1] + var_color[1]) // 2,
                                (existing[2] + var_color[2]) // 2
                            )
                            image.putpixel((px, py), blended)
        
        return image
    
    def _enhance_classicism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                           draw: ImageDraw.Draw) -> Image.Image:
        """Classicism: Balanced composition, elegant details, harmonious additions."""
        # Add elegant decorative elements
        if random.random() < 0.5:
            num_decorations = random.randint(2, 5)
            for _ in range(num_decorations):
                decor_color = random.choice(palette)
                x = random.randint(self.width // 4, 3 * self.width // 4)
                y = random.randint(self.height // 4, 3 * self.height // 4)
                size = random.randint(10, 25)
                
                # Elegant decorative pattern
                decor_type = random.choice(['circle', 'square', 'ornament'])
                if decor_type == 'circle':
                    draw.ellipse([x-size, y-size, x+size, y+size],
                               fill=None, outline=decor_color, width=2)
                elif decor_type == 'square':
                    draw.rectangle([x-size, y-size, x+size, y+size],
                                 fill=None, outline=decor_color, width=2)
                else:  # ornament
                    # Simple ornamental pattern
                    for i in range(4):
                        angle = i * math.pi / 2
                        x2 = int(x + size * math.cos(angle))
                        y2 = int(y + size * math.sin(angle))
                        draw.line([(x, y), (x2, y2)], fill=decor_color, width=1)
        
        return image
    
    def _enhance_pop_art(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                        draw: ImageDraw.Draw) -> Image.Image:
        """Pop Art: Bold colors, Ben-Day dots, high contrast effects."""
        # Add more Ben-Day dots
        if random.random() < 0.6:
            dot_size = 2
            spacing = 6
            for y in range(0, self.height, spacing):
                for x in range(0, self.width, spacing):
                    if random.random() < 0.4:
                        dot_color = random.choice(palette)
                        draw.ellipse([x-dot_size, y-dot_size, x+dot_size, y+dot_size],
                                   fill=dot_color)
        
        # Add bold outlines to existing elements
        if random.random() < 0.4:
            num_outlines = random.randint(3, 8)
            for _ in range(num_outlines):
                outline_color = (0, 0, 0) if random.random() < 0.5 else (255, 255, 255)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                size = random.randint(30, 80)
                draw.ellipse([x-size, y-size, x+size, y+size],
                           fill=None, outline=outline_color, width=5)
        
        return image
    
    def _enhance_op_art(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                       draw: ImageDraw.Draw) -> Image.Image:
        """Op Art: More optical illusions, vibrating patterns."""
        # Add additional optical illusion layers
        if random.random() < 0.5:
            # Create vibrating grid
            spacing = 15
            for x in range(0, self.width, spacing):
                for y in range(0, self.height, spacing):
                    if (x // spacing + y // spacing) % 2 == 0:
                        color = palette[0] if len(palette) > 0 else (255, 255, 255)
                    else:
                        color = palette[-1] if len(palette) > 0 else (0, 0, 0)
                    draw.rectangle([x, y, x + spacing, y + spacing], fill=color)
        
        return image
    
    def _enhance_fauvism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                         draw: ImageDraw.Draw) -> Image.Image:
        """Fauvism: More wild brushstrokes, intense colors."""
        # Add more expressive brushstrokes
        if random.random() < 0.6:
            num_strokes = random.randint(50, 100)
            for _ in range(num_strokes):
                color = random.choice(palette)
                # Make colors even more intense
                r, g, b = color
                r = min(255, int(r * 1.4))
                g = min(255, int(g * 1.4))
                b = min(255, int(b * 1.4))
                color = (r, g, b)
                
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                angle = random.uniform(0, 2 * math.pi)
                length = random.randint(30, 80)
                x2 = int(x + length * math.cos(angle))
                y2 = int(y + length * math.sin(angle))
                thickness = random.randint(8, 20)
                draw.line([(x, y), (x2, y2)], fill=color, width=thickness)
        
        return image
    
    def _enhance_futurism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                         draw: ImageDraw.Draw) -> Image.Image:
        """Futurism: More motion, speed lines, dynamic effects."""
        # Add more motion lines
        if random.random() < 0.6:
            num_motion_lines = random.randint(10, 20)
            for _ in range(num_motion_lines):
                color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                
                # Create motion trail
                for i in range(random.randint(5, 12)):
                    angle = random.uniform(0, 2 * math.pi)
                    length = random.randint(20, 60)
                    x2 = int(x + length * math.cos(angle))
                    y2 = int(y + length * math.sin(angle))
                    thickness = max(1, 6 - i)
                    draw.line([(x, y), (x2, y2)], fill=color, width=thickness)
                    x, y = x2, y2
        
        return image
    
    def _enhance_minimalism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                           draw: ImageDraw.Draw) -> Image.Image:
        """Minimalism: Keep it minimal, subtle variations only."""
        # Very subtle enhancements - maintain minimalism
        if random.random() < 0.3:
            # Add one subtle element
            color = random.choice(palette)
            x = random.randint(self.width // 3, 2 * self.width // 3)
            y = random.randint(self.height // 3, 2 * self.height // 3)
            size = random.randint(5, 15)
            draw.ellipse([x-size, y-size, x+size, y+size],
                       fill=color, outline=None)
        
        return image
    
    def _enhance_dadaism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                        draw: ImageDraw.Draw) -> Image.Image:
        """Dadaism: More randomness, unexpected combinations."""
        # Add completely random unexpected elements
        if random.random() < 0.7:
            num_random = random.randint(5, 15)
            for _ in range(num_random):
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                size = random.randint(5, 40)
                
                element = random.choice(['circle', 'square', 'line', 'dot'])
                if element == 'circle':
                    draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
                elif element == 'square':
                    draw.rectangle([x-size, y-size, x+size, y+size], fill=color)
                elif element == 'line':
                    x2 = random.randint(0, self.width - 1)
                    y2 = random.randint(0, self.height - 1)
                    draw.line([(x, y), (x2, y2)], fill=color, width=random.randint(1, 5))
                else:
                    draw.ellipse([x-2, y-2, x+2, y+2], fill=color)
        
        return image
    
    def _enhance_constructivism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                               draw: ImageDraw.Draw) -> Image.Image:
        """Constructivism: More geometric precision, bold lines."""
        # Add more geometric elements
        if random.random() < 0.5:
            num_geometric = random.randint(3, 8)
            for _ in range(num_geometric):
                color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                size = random.randint(20, 60)
                
                shape = random.choice(['rectangle', 'triangle', 'line'])
                if shape == 'rectangle':
                    w = size
                    h = size * random.uniform(0.5, 2.0)
                    draw.rectangle([x-w//2, y-h//2, x+w//2, y+h//2],
                                 fill=color, outline=(0, 0, 0), width=3)
                elif shape == 'triangle':
                    points = [(x, y-size), (x-size, y+size), (x+size, y+size)]
                    draw.polygon(points, fill=color, outline=(0, 0, 0), width=3)
                else:
                    angle = random.uniform(0, 2 * math.pi)
                    x2 = int(x + size * 2 * math.cos(angle))
                    y2 = int(y + size * 2 * math.sin(angle))
                    draw.line([(x, y), (x2, y2)], fill=color, width=5)
        
        return image
    
    def _enhance_de_stijl(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                         draw: ImageDraw.Draw) -> Image.Image:
        """De Stijl: More grid-based elements, primary color blocks."""
        # Add more grid elements
        if random.random() < 0.5:
            grid_size = self.width // 10
            for x in range(0, self.width, grid_size):
                for y in range(0, self.height, grid_size):
                    if random.random() < 0.2:
                        color = random.choice(palette)
                        draw.rectangle([x, y, x + grid_size, y + grid_size],
                                     fill=color, outline=(0, 0, 0), width=2)
        
        return image
    
    def _enhance_art_deco(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                          draw: ImageDraw.Draw) -> Image.Image:
        """Art Deco: More decorative patterns, luxurious details."""
        # Add more decorative elements
        if random.random() < 0.5:
            num_decorative = random.randint(3, 6)
            for _ in range(num_decorative):
                color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                size = random.randint(30, 80)
                
                # Art Deco decorative pattern
                pattern = random.choice(['sunburst', 'fan', 'chevron'])
                if pattern == 'sunburst':
                    for i in range(12):
                        angle = 2 * math.pi * i / 12
                        x2 = int(x + size * math.cos(angle))
                        y2 = int(y + size * math.sin(angle))
                        draw.line([(x, y), (x2, y2)], fill=color, width=2)
                elif pattern == 'fan':
                    for i in range(8):
                        angle = -math.pi / 2 + (math.pi / 8) * i
                        x2 = int(x + size * math.cos(angle))
                        y2 = int(y + size * math.sin(angle))
                        draw.line([(x, y), (x2, y2)], fill=color, width=2)
                else:  # chevron
                    for i in range(3):
                        offset = i * size // 3
                        points = [
                            (x - size + offset, y),
                            (x - size//2 + offset, y - size//2),
                            (x + offset, y)
                        ]
                        draw.polygon(points, fill=color, outline=None)
        
        return image
    
    def _enhance_art_nouveau(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                            draw: ImageDraw.Draw) -> Image.Image:
        """Art Nouveau: More flowing lines, organic forms."""
        # Add more flowing organic lines
        if random.random() < 0.6:
            num_curves = random.randint(5, 12)
            for _ in range(num_curves):
                color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                
                # Flowing curve
                points = []
                for i in range(20):
                    t = i / 20
                    px = int(x + 100 * t * math.cos(t * math.pi * 2))
                    py = int(y + 50 * math.sin(t * math.pi * 4))
                    points.append((px, py))
                
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i+1]], fill=color, width=3)
        
        return image
    
    def _enhance_romanticism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                            draw: ImageDraw.Draw) -> Image.Image:
        """Romanticism: Dramatic lighting, emotional depth."""
        # Add dramatic lighting
        if random.random() < 0.5:
            light_x = random.randint(0, self.width - 1)
            light_y = random.randint(0, self.height - 1)
            light_color = random.choice(palette)
            
            for y in range(self.height):
                for x in range(self.width):
                    dist = math.sqrt((x - light_x)**2 + (y - light_y)**2)
                    max_dist = math.sqrt(self.width**2 + self.height**2)
                    intensity = max(0, 1.0 - (dist / max_dist) * 1.5)
                    
                    if intensity > 0:
                        existing = image.getpixel((x, y))
                        lit = (
                            int(existing[0] + (light_color[0] - existing[0]) * intensity * 0.4),
                            int(existing[1] + (light_color[1] - existing[1]) * intensity * 0.4),
                            int(existing[2] + (light_color[2] - existing[2]) * intensity * 0.4)
                        )
                        image.putpixel((x, y), lit)
        
        return image
    
    def _enhance_neoclassicism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                              draw: ImageDraw.Draw) -> Image.Image:
        """Neoclassicism: Classical elements, restrained elegance."""
        # Add classical architectural elements
        if random.random() < 0.4:
            num_elements = random.randint(2, 4)
            for _ in range(num_elements):
                color = random.choice(palette)
                x = random.randint(self.width // 4, 3 * self.width // 4)
                y = random.randint(self.height // 4, 3 * self.height // 4)
                size = random.randint(20, 40)
                
                # Classical column or arch
                element = random.choice(['column', 'arch'])
                if element == 'column':
                    draw.rectangle([x-size//4, y-size*2, x+size//4, y+size*2],
                                 fill=color, outline=None)
                    draw.ellipse([x-size//2, y-size*2, x+size//2, y-size*2+size//2],
                               fill=color, outline=None)
                else:  # arch
                    draw.arc([x-size, y-size, x+size, y+size],
                           start=0, end=180, fill=color, width=size//3)
        
        return image
    
    def _enhance_naturalism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                           draw: ImageDraw.Draw) -> Image.Image:
        """Naturalism: Nature details, organic textures."""
        # Add natural texture details
        if random.random() < 0.5:
            num_textures = random.randint(30, 60)
            for _ in range(num_textures):
                texture_color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                size = random.randint(1, 3)
                draw.ellipse([x-size, y-size, x+size, y+size], fill=texture_color)
        
        return image
    
    def _enhance_mannerism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                          draw: ImageDraw.Draw) -> Image.Image:
        """Mannerism: Elongated forms, sophisticated complexity."""
        # Add more elongated sophisticated forms
        if random.random() < 0.5:
            num_elongated = random.randint(3, 6)
            for _ in range(num_elongated):
                color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                w = random.randint(15, 40)
                h = int(w * random.uniform(2.0, 4.0))  # Elongated
                draw.ellipse([x-w, y-h, x+w, y+h], fill=color, outline=None)
        
        return image
    
    def _enhance_rococo(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                       draw: ImageDraw.Draw) -> Image.Image:
        """Rococo: More decorative, delicate, ornate details."""
        # Add more delicate decorative elements
        if random.random() < 0.6:
            num_delicate = random.randint(8, 15)
            for _ in range(num_delicate):
                color = random.choice(palette)
                # Lighten for pastel effect
                r, g, b = color
                r = min(255, int(r + (255 - r) * 0.5))
                g = min(255, int(g + (255 - g) * 0.5))
                b = min(255, int(b + (255 - b) * 0.5))
                color = (r, g, b)
                
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                size = random.randint(8, 20)
                
                # Delicate flower-like pattern
                for i in range(6):
                    angle = 2 * math.pi * i / 6
                    px = int(x + size * math.cos(angle))
                    py = int(y + size * math.sin(angle))
                    draw.ellipse([px-2, py-2, px+2, py+2], fill=color)
        
        return image
    
    def _enhance_symbolism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                          draw: ImageDraw.Draw) -> Image.Image:
        """Symbolism: More symbolic forms, meaningful patterns."""
        # Add symbolic patterns
        if random.random() < 0.5:
            num_symbols = random.randint(3, 6)
            for _ in range(num_symbols):
                color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                size = random.randint(30, 60)
                
                # Symbolic spiral or mandala
                symbol = random.choice(['spiral', 'mandala'])
                if symbol == 'spiral':
                    points = []
                    for i in range(40):
                        t = i / 40
                        angle = 4 * math.pi * t
                        radius = size * t
                        px = int(x + radius * math.cos(angle))
                        py = int(y + radius * math.sin(angle))
                        points.append((px, py))
                    for i in range(len(points) - 1):
                        draw.line([points[i], points[i+1]], fill=color, width=2)
                else:  # mandala
                    for i in range(8):
                        angle = 2 * math.pi * i / 8
                        x2 = int(x + size * math.cos(angle))
                        y2 = int(y + size * math.sin(angle))
                        draw.line([(x, y), (x2, y2)], fill=color, width=2)
                    draw.ellipse([x-size//2, y-size//2, x+size//2, y+size//2],
                               fill=None, outline=color, width=2)
        
        return image
    
    def _enhance_precisionism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                             draw: ImageDraw.Draw) -> Image.Image:
        """Precisionism: More precise lines, industrial precision."""
        # Add more precise geometric lines
        if random.random() < 0.5:
            num_lines = random.randint(5, 10)
            for _ in range(num_lines):
                color = random.choice(palette)
                x1 = random.randint(0, self.width - 1)
                y1 = random.randint(0, self.height - 1)
                x2 = random.randint(0, self.width - 1)
                y2 = random.randint(0, self.height - 1)
                draw.line([(x1, y1), (x2, y2)], fill=color, width=2)
        
        return image
    
    def _enhance_impressionism(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                              draw: ImageDraw.Draw) -> Image.Image:
        """Impressionism: More visible brushstrokes, light effects, broken color."""
        # Add more visible brushstrokes
        if random.random() < 0.7:
            num_strokes = random.randint(100, 200)
            for _ in range(num_strokes):
                color = random.choice(palette)
                # Broken color effect - vary slightly
                r, g, b = color
                r = max(0, min(255, r + random.randint(-15, 15)))
                g = max(0, min(255, g + random.randint(-15, 15)))
                b = max(0, min(255, b + random.randint(-15, 15)))
                color = (r, g, b)
                
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                angle = random.uniform(0, 2 * math.pi)
                length = random.randint(25, 70)
                x2 = int(x + length * math.cos(angle))
                y2 = int(y + length * math.sin(angle))
                thickness = random.randint(4, 10)
                draw.line([(x, y), (x2, y2)], fill=color, width=thickness)
        
        # Add more light effects
        if random.random() < 0.5:
            light_x = random.randint(0, self.width - 1)
            light_y = random.randint(0, self.height // 3)
            light_color = random.choice(palette)
            # Very light color
            r, g, b = light_color
            r = min(255, int(r + (255 - r) * 0.6))
            g = min(255, int(g + (255 - g) * 0.6))
            b = min(255, int(b + (255 - b) * 0.6))
            light_color = (r, g, b)
            
            for y in range(self.height):
                for x in range(self.width):
                    dist = math.sqrt((x - light_x)**2 + (y - light_y)**2)
                    max_dist = math.sqrt(self.width**2 + self.height**2)
                    intensity = max(0, 1.0 - (dist / max_dist) * 1.0)
                    
                    if intensity > 0:
                        existing = image.getpixel((x, y))
                        lit = (
                            int(existing[0] + (light_color[0] - existing[0]) * intensity * 0.4),
                            int(existing[1] + (light_color[1] - existing[1]) * intensity * 0.4),
                            int(existing[2] + (light_color[2] - existing[2]) * intensity * 0.4)
                        )
                        image.putpixel((x, y), lit)
        
        return image
    
    def _enhance_generic(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                        draw: ImageDraw.Draw) -> Image.Image:
        """Generic creative enhancement for unknown styles."""
        # Minimal generic enhancement
        if random.random() < 0.3:
            num_elements = random.randint(2, 5)
            for _ in range(num_elements):
                color = random.choice(palette)
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                size = random.randint(10, 30)
                draw.ellipse([x-size, y-size, x+size, y+size], fill=color, outline=None)
        
        return image
    
    def _create_landscape(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Create landscape: sky, horizon, terrain, natural elements.
        """
        draw = ImageDraw.Draw(image)
        
        # Sky gradient (top portion)
        sky_height = int(self.height * random.uniform(0.4, 0.6))
        sky_colors = [c for c in palette if sum(c) / 3 > 100]  # Lighter colors for sky
        if not sky_colors:
            sky_colors = palette
        
        for y in range(sky_height):
            t = y / sky_height
            color_idx = int(t * (len(sky_colors) - 1))
            sky_color = sky_colors[min(color_idx, len(sky_colors) - 1)]
            
            # Add variation
            variation = random.randint(-10, 10)
            r = max(0, min(255, sky_color[0] + variation))
            g = max(0, min(255, sky_color[1] + variation))
            b = max(0, min(255, sky_color[2] + variation))
            
            draw.line([(0, y), (self.width, y)], fill=(r, g, b), width=1)
        
        # Horizon line
        horizon_y = sky_height
        horizon_color = random.choice(palette)
        draw.line([(0, horizon_y), (self.width, horizon_y)], fill=horizon_color, width=3)
        
        # Terrain/ground (bottom portion)
        ground_colors = [c for c in palette if sum(c) / 3 < 150]  # Darker colors for ground
        if not ground_colors:
            ground_colors = palette
        
        for y in range(horizon_y, self.height):
            t = (y - horizon_y) / (self.height - horizon_y)
            color_idx = int(t * (len(ground_colors) - 1))
            ground_color = ground_colors[min(color_idx, len(ground_colors) - 1)]
            
            # Add terrain variation
            variation = random.randint(-15, 15)
            r = max(0, min(255, ground_color[0] + variation))
            g = max(0, min(255, ground_color[1] + variation))
            b = max(0, min(255, ground_color[2] + variation))
            
            draw.line([(0, y), (self.width, y)], fill=(r, g, b), width=1)
        
        # Add landscape elements
        # Mountains/hills
        if random.random() < 0.7:
            num_mountains = random.randint(2, 5)
            for _ in range(num_mountains):
                mountain_color = random.choice(ground_colors)
                base_x = random.randint(0, self.width - 1)
                base_y = horizon_y + random.randint(0, self.height // 4)
                peak_x = base_x + random.randint(-self.width // 8, self.width // 8)
                peak_y = base_y - random.randint(self.height // 8, self.height // 4)
                
                # Mountain triangle
                points = [
                    (base_x - self.width // 10, base_y),
                    (peak_x, peak_y),
                    (base_x + self.width // 10, base_y)
                ]
                draw.polygon(points, fill=mountain_color, outline=None)
        
        # Trees/vegetation
        if random.random() < 0.6:
            num_trees = random.randint(3, 8)
            for _ in range(num_trees):
                tree_color = random.choice(ground_colors)
                tree_x = random.randint(0, self.width - 1)
                tree_base_y = horizon_y + random.randint(0, self.height // 3)
                tree_height = random.randint(30, 80)
                
                # Tree trunk
                trunk_width = random.randint(5, 15)
                draw.rectangle([tree_x - trunk_width//2, tree_base_y, 
                               tree_x + trunk_width//2, tree_base_y + tree_height],
                              fill=tree_color, outline=None)
                
                # Tree foliage
                foliage_size = random.randint(20, 50)
                draw.ellipse([tree_x - foliage_size, tree_base_y - foliage_size,
                            tree_x + foliage_size, tree_base_y],
                           fill=tree_color, outline=None)
        
        # Sun/moon
        if random.random() < 0.5:
            celestial_color = random.choice(sky_colors)
            celestial_x = random.randint(self.width // 4, 3 * self.width // 4)
            celestial_y = random.randint(self.height // 8, sky_height // 2)
            celestial_size = random.randint(30, 60)
            draw.ellipse([celestial_x - celestial_size, celestial_y - celestial_size,
                        celestial_x + celestial_size, celestial_y + celestial_size],
                       fill=celestial_color, outline=None)
        
        # Clouds
        if random.random() < 0.6:
            num_clouds = random.randint(2, 5)
            for _ in range(num_clouds):
                cloud_color = random.choice(sky_colors)
                cloud_x = random.randint(0, self.width - 1)
                cloud_y = random.randint(0, sky_height // 2)
                cloud_size = random.randint(40, 80)
                
                # Cloud (multiple overlapping circles)
                for i in range(3):
                    offset_x = cloud_x + random.randint(-cloud_size//2, cloud_size//2)
                    offset_y = cloud_y + random.randint(-cloud_size//4, cloud_size//4)
                    draw.ellipse([offset_x - cloud_size//2, offset_y - cloud_size//3,
                                offset_x + cloud_size//2, offset_y + cloud_size//3],
                               fill=cloud_color, outline=None)
        
        return image
    
    def _apply_advanced_texture(self, image: Image.Image, intensity: float = 0.3) -> Image.Image:
        """
        Apply advanced texture using OpenCV and scikit-image for realistic skin/texture.
        """
        if not CV2_AVAILABLE or not SKIMAGE_AVAILABLE:
            return image
        
        # Convert PIL to numpy array
        img_array = np.array(image)
        
        # Apply bilateral filter for skin smoothing (preserves edges)
        if random.random() < 0.7:
            img_array = cv2.bilateralFilter(img_array, 5, 50, 50)
        
        # Add subtle noise for texture
        if random.random() < 0.5:
            noise = np.random.normal(0, intensity * 10, img_array.shape).astype(np.uint8)
            img_array = np.clip(img_array.astype(np.int16) + noise, 0, 255).astype(np.uint8)
        
        # Convert back to PIL
        return Image.fromarray(img_array)
    
    def _apply_smooth_gradient(self, image: Image.Image, start_color: Tuple[int, int, int],
                              end_color: Tuple[int, int, int], direction: str = 'vertical') -> Image.Image:
        """
        Apply smooth gradient using scipy interpolation for realistic color transitions.
        """
        if not SCIPY_AVAILABLE:
            # Fallback to simple gradient
            draw = ImageDraw.Draw(image)
            if direction == 'vertical':
                for y in range(self.height):
                    t = y / self.height
                    r = int(start_color[0] * (1 - t) + end_color[0] * t)
                    g = int(start_color[1] * (1 - t) + end_color[1] * t)
                    b = int(start_color[2] * (1 - t) + end_color[2] * t)
                    draw.line([(0, y), (self.width, y)], fill=(r, g, b), width=1)
            return image
        
        # Use scipy for smoother interpolation
        img_array = np.array(image)
        
        if direction == 'vertical':
            y_coords = np.linspace(0, 1, self.height)
            for c in range(3):  # RGB channels
                values = np.linspace(start_color[c], end_color[c], self.height)
                # Interpolate for smooth transition
                interp_func = interpolate.interp1d(y_coords, values, kind='cubic', 
                                                   fill_value='extrapolate')
                for y in range(self.height):
                    img_array[y, :, c] = np.clip(interp_func(y / self.height), 0, 255)
        
        return Image.fromarray(img_array.astype(np.uint8))
    
    def _enhance_with_opencv(self, image: Image.Image, enhancement_type: str = 'detail') -> Image.Image:
        """
        Enhance image using OpenCV filters for better realism.
        """
        if not CV2_AVAILABLE:
            return image
        
        img_array = np.array(image)
        
        if enhancement_type == 'detail':
            # Unsharp masking for detail enhancement
            gaussian = cv2.GaussianBlur(img_array, (0, 0), 2.0)
            img_array = cv2.addWeighted(img_array, 1.5, gaussian, -0.5, 0)
        elif enhancement_type == 'smooth':
            # Bilateral filter for smooth but detailed texture
            img_array = cv2.bilateralFilter(img_array, 9, 75, 75)
        elif enhancement_type == 'sharpen':
            # Sharpening kernel
            kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])
            img_array = cv2.filter2D(img_array, -1, kernel)
        
        return Image.fromarray(np.clip(img_array, 0, 255).astype(np.uint8))
    
    def _create_portrait(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Create realistic portrait: face, head, shoulders, features with depth and lighting.
        Uses chiaroscuro, realistic proportions, skin textures, and natural colors.
        """
        draw = ImageDraw.Draw(image)
        
        # Portrait centered
        face_center_x = self.center_x
        face_center_y = self.center_y - self.height // 8  # Slightly above center
        face_size = min(self.width, self.height) // 2.5  # Larger face for more detail
        
        # Realistic skin tones (warm, natural colors)
        skin_base = random.choice([
            (240, 200, 180), (220, 180, 160), (200, 160, 140),  # Light skin
            (180, 140, 120), (160, 120, 100), (140, 100, 80),   # Medium skin
            (120, 80, 60), (100, 70, 50), (80, 60, 40)         # Dark skin
        ])
        
        face_width = face_size
        face_height = int(face_size * 1.15)  # Slightly elongated oval
        
        # Create face with gradient for volume (3D effect)
        face_overlay = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        face_pixels = face_overlay.load()
        
        # Light source (from top-left)
        light_x = face_center_x - face_width * 0.3
        light_y = face_center_y - face_height * 0.3
        
        for y in range(self.height):
            for x in range(self.width):
                # Check if pixel is within face oval
                dx = (x - face_center_x) / face_width
                dy = (y - face_center_y) / face_height
                dist = math.sqrt(dx*dx + dy*dy)
                
                if dist < 1.0:
                    # Calculate distance from light source
                    light_dist = math.sqrt((x - light_x)**2 + (y - light_y)**2)
                    max_light_dist = math.sqrt(face_width**2 + face_height**2)
                    light_intensity = max(0.3, 1.0 - (light_dist / max_light_dist) * 0.5)
                    
                    # Add subtle shadow on right side
                    shadow_factor = 1.0 - (dx * 0.2) if dx > 0 else 1.0
                    light_intensity *= shadow_factor
                    
                    # Create skin color with lighting
                    r, g, b = skin_base
                    r = int(r * light_intensity)
                    g = int(g * light_intensity)
                    b = int(b * light_intensity)
                    
                    # Add subtle texture variation
                    texture = random.randint(-8, 8)
                    r = max(0, min(255, r + texture))
                    g = max(0, min(255, g + texture))
                    b = max(0, min(255, b + texture))
                    
                    face_pixels[x, y] = (r, g, b)
        
        image = Image.blend(image, face_overlay, alpha=0.9)
        draw = ImageDraw.Draw(image)
        
        # Eyes - more realistic with iris, pupil, highlights
        eye_y = face_center_y - face_height // 3
        eye_size = face_size // 6
        eye_spacing = face_width // 2.2
        
        # Left eye
        left_eye_x = face_center_x - eye_spacing
        # Eye socket shadow
        draw.ellipse([left_eye_x - eye_size*1.3, eye_y - eye_size*1.1,
                    left_eye_x + eye_size*1.3, eye_y + eye_size*1.1],
                   fill=(int(skin_base[0]*0.7), int(skin_base[1]*0.7), int(skin_base[2]*0.7)), outline=None)
        
        # Eye white
        draw.ellipse([left_eye_x - eye_size*0.9, eye_y - eye_size*0.7,
                    left_eye_x + eye_size*0.9, eye_y + eye_size*0.7],
                   fill=(250, 240, 230), outline=None)
        
        # Iris (colored part)
        iris_color = random.choice([
            (100, 150, 200), (150, 100, 50), (50, 100, 50),  # Blue, brown, green
            (120, 80, 60), (80, 120, 80), (100, 80, 120)     # Brown, green, hazel
        ])
        iris_size = eye_size // 2
        draw.ellipse([left_eye_x - iris_size, eye_y - iris_size,
                    left_eye_x + iris_size, eye_y + iris_size],
                   fill=iris_color, outline=None)
        
        # Pupil
        pupil_size = iris_size // 2
        draw.ellipse([left_eye_x - pupil_size, eye_y - pupil_size,
                    left_eye_x + pupil_size, eye_y + pupil_size],
                   fill=(20, 20, 30), outline=None)
        
        # Eye highlight
        highlight_size = pupil_size // 2
        draw.ellipse([left_eye_x - highlight_size//2, eye_y - highlight_size//2,
                    left_eye_x + highlight_size//2, eye_y + highlight_size//2],
                   fill=(255, 255, 255), outline=None)
        
        # Right eye (same process)
        right_eye_x = face_center_x + eye_spacing
        draw.ellipse([right_eye_x - eye_size*1.3, eye_y - eye_size*1.1,
                    right_eye_x + eye_size*1.3, eye_y + eye_size*1.1],
                   fill=(int(skin_base[0]*0.7), int(skin_base[1]*0.7), int(skin_base[2]*0.7)), outline=None)
        draw.ellipse([right_eye_x - eye_size*0.9, eye_y - eye_size*0.7,
                    right_eye_x + eye_size*0.9, eye_y + eye_size*0.7],
                   fill=(250, 240, 230), outline=None)
        draw.ellipse([right_eye_x - iris_size, eye_y - iris_size,
                    right_eye_x + iris_size, eye_y + iris_size],
                   fill=iris_color, outline=None)
        draw.ellipse([right_eye_x - pupil_size, eye_y - pupil_size,
                    right_eye_x + pupil_size, eye_y + pupil_size],
                   fill=(20, 20, 30), outline=None)
        draw.ellipse([right_eye_x - highlight_size//2, eye_y - highlight_size//2,
                    right_eye_x + highlight_size//2, eye_y + highlight_size//2],
                   fill=(255, 255, 255), outline=None)
        
        # Eyebrows
        eyebrow_y = eye_y - eye_size * 1.2
        eyebrow_width = eye_size * 1.5
        eyebrow_color = (int(skin_base[0]*0.4), int(skin_base[1]*0.3), int(skin_base[2]*0.2))
        # Left eyebrow
        for i in range(5):
            offset = (i - 2) * eyebrow_width // 5
            draw.ellipse([left_eye_x + offset - 3, eyebrow_y - 2,
                        left_eye_x + offset + 3, eyebrow_y + 2],
                       fill=eyebrow_color, outline=None)
        # Right eyebrow
        for i in range(5):
            offset = (i - 2) * eyebrow_width // 5
            draw.ellipse([right_eye_x + offset - 3, eyebrow_y - 2,
                        right_eye_x + offset + 3, eyebrow_y + 2],
                       fill=eyebrow_color, outline=None)
        
        # Nose - more realistic with shading
        nose_y = face_center_y
        nose_width = face_size // 8
        # Nose bridge shadow
        draw.ellipse([face_center_x - nose_width*0.3, nose_y - face_size//4,
                    face_center_x + nose_width*0.3, nose_y + face_size//3],
                   fill=(int(skin_base[0]*0.85), int(skin_base[1]*0.85), int(skin_base[2]*0.85)), outline=None)
        # Nose tip highlight
        # Fixed: clamp color values to valid RGB range [0, 255]
        nose_highlight = (
            min(255, int(skin_base[0]*1.1)),
            min(255, int(skin_base[1]*1.1)),
            min(255, int(skin_base[2]*1.1))
        )
        draw.ellipse([face_center_x - nose_width*0.5, nose_y + face_size//6,
                    face_center_x + nose_width*0.5, nose_y + face_size//4],
                   fill=nose_highlight, outline=None)
        # Nostrils
        nostril_size = nose_width // 3
        draw.ellipse([face_center_x - nose_width*0.7, nose_y + face_size//5,
                    face_center_x - nose_width*0.3, nose_y + face_size//4],
                   fill=(int(skin_base[0]*0.6), int(skin_base[1]*0.6), int(skin_base[2]*0.6)), outline=None)
        draw.ellipse([face_center_x + nose_width*0.3, nose_y + face_size//5,
                    face_center_x + nose_width*0.7, nose_y + face_size//4],
                   fill=(int(skin_base[0]*0.6), int(skin_base[1]*0.6), int(skin_base[2]*0.6)), outline=None)
        
        # Mouth - more realistic with lips
        mouth_y = face_center_y + face_height // 2.5
        mouth_width = face_size // 3
        # Upper lip
        lip_color = (min(255, int(skin_base[0]*1.3)), max(0, int(skin_base[1]*0.7)), max(0, int(skin_base[2]*0.7)))
        upper_lip_points = []
        for i in range(15):
            t = i / 14
            x = face_center_x - mouth_width + (mouth_width * 2 * t)
            y = mouth_y - int(8 * math.sin(t * math.pi))
            upper_lip_points.append((int(x), int(y)))
        if len(upper_lip_points) > 2:
            draw.polygon(upper_lip_points, fill=lip_color, outline=None)
        
        # Lower lip (fuller)
        lower_lip_points = []
        for i in range(15):
            t = i / 14
            x = face_center_x - mouth_width + (mouth_width * 2 * t)
            y = mouth_y + int(12 * math.sin(t * math.pi))
            lower_lip_points.append((int(x), int(y)))
        if len(lower_lip_points) > 2:
            draw.polygon(lower_lip_points, fill=lip_color, outline=None)
        
        # Lip highlight
        highlight_y = mouth_y + 3
        draw.ellipse([face_center_x - mouth_width*0.3, highlight_y - 2,
                    face_center_x + mouth_width*0.3, highlight_y + 2],
                   fill=(min(255, int(lip_color[0]*1.2)), lip_color[1], lip_color[2]), outline=None)
        
        # Cheekbones - subtle shading
        cheek_color = (int(skin_base[0]*0.9), int(skin_base[1]*0.9), int(skin_base[2]*0.9))
        # Left cheek
        draw.ellipse([face_center_x - face_width*0.7, face_center_y - face_height//6,
                    face_center_x - face_width*0.3, face_center_y + face_height//6],
                   fill=cheek_color, outline=None)
        # Right cheek
        draw.ellipse([face_center_x + face_width*0.3, face_center_y - face_height//6,
                    face_center_x + face_width*0.7, face_center_y + face_height//6],
                   fill=cheek_color, outline=None)
        
        # Hair - more realistic with texture
        if random.random() < 0.9:
            hair_color = random.choice([
                (30, 20, 15), (50, 30, 20), (80, 60, 40),  # Dark brown, brown
                (120, 80, 50), (150, 100, 70), (180, 140, 100),  # Light brown, blonde
                (200, 180, 160), (220, 200, 180)  # Very light blonde
            ])
            hair_y_start = face_center_y - face_height
            hair_height = int(face_size / 2.5)
            
            # Hair base
            hair_points = []
            for i in range(30):
                t = i / 29
                x = face_center_x - face_width*1.1 + (face_width * 2.2 * t)
                y = hair_y_start - int(hair_height * 0.6 * math.sin(t * math.pi))
                hair_points.append((int(x), int(y)))
            hair_points.append((face_center_x + face_width*1.1, hair_y_start))
            hair_points.append((face_center_x - face_width*1.1, hair_y_start))
            
            if len(hair_points) > 2:
                draw.polygon(hair_points, fill=hair_color, outline=None)
            
            # Hair texture (individual strands)
            for _ in range(random.randint(50, 100)):
                strand_x = face_center_x + random.randint(-int(face_width*1.1), int(face_width*1.1))
                strand_y = hair_y_start + random.randint(-hair_height, 0)
                strand_length = random.randint(10, 30)
                angle = random.uniform(-math.pi/3, -2*math.pi/3)
                strand_x2 = int(strand_x + strand_length * math.cos(angle))
                strand_y2 = int(strand_y + strand_length * math.sin(angle))
                # Vary hair color slightly
                r, g, b = hair_color
                strand_color = (
                    max(0, min(255, r + random.randint(-15, 15))),
                    max(0, min(255, g + random.randint(-15, 15))),
                    max(0, min(255, b + random.randint(-15, 15)))
                )
                draw.line([(strand_x, strand_y), (strand_x2, strand_y2)], fill=strand_color, width=1)
        
        # Neck with shading
        neck_width = face_width // 1.8
        neck_height = face_size // 3
        neck_y = face_center_y + face_height
        
        # Neck shadow
        neck_shadow = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        neck_draw = ImageDraw.Draw(neck_shadow)
        neck_draw.ellipse([face_center_x - neck_width, neck_y,
                          face_center_x + neck_width, neck_y + neck_height],
                         fill=(int(skin_base[0]*0.85), int(skin_base[1]*0.85), int(skin_base[2]*0.85)), outline=None)
        image = Image.blend(image, neck_shadow, alpha=0.7)
        draw = ImageDraw.Draw(image)
        
        # Shoulders - more realistic
        shoulder_width = face_width * 2.2
        shoulder_y = neck_y + neck_height
        
        # Left shoulder with shading
        shoulder_shadow = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        shoulder_draw = ImageDraw.Draw(shoulder_shadow)
        shoulder_draw.ellipse([face_center_x - shoulder_width, shoulder_y - shoulder_width//3,
                              face_center_x, shoulder_y + shoulder_width//3],
                             fill=(int(skin_base[0]*0.9), int(skin_base[1]*0.9), int(skin_base[2]*0.9)), outline=None)
        image = Image.blend(image, shoulder_shadow, alpha=0.6)
        draw = ImageDraw.Draw(image)
        
        # Right shoulder
        shoulder_shadow2 = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        shoulder_draw2 = ImageDraw.Draw(shoulder_shadow2)
        shoulder_draw2.ellipse([face_center_x, shoulder_y - shoulder_width//3,
                               face_center_x + shoulder_width, shoulder_y + shoulder_width//3],
                              fill=(int(skin_base[0]*0.9), int(skin_base[1]*0.9), int(skin_base[2]*0.9)), outline=None)
        image = Image.blend(image, shoulder_shadow2, alpha=0.6)
        
        # Apply advanced texture for realistic skin
        if CV2_AVAILABLE or SKIMAGE_AVAILABLE:
            # Create mask for face area
            face_mask = Image.new('L', (self.width, self.height), 0)
            face_draw = ImageDraw.Draw(face_mask)
            face_draw.ellipse([face_center_x - face_width, face_center_y - face_height,
                              face_center_x + face_width, face_center_y + face_height],
                             fill=255, outline=None)
            
            # Apply texture only to face area
            textured_face = self._apply_advanced_texture(image, intensity=0.2)
            image = Image.composite(textured_face, image, face_mask)
            
            # Enhance details with OpenCV
            if random.random() < 0.6:
                image = self._enhance_with_opencv(image, enhancement_type='detail')
        
        return image
    
    def _create_animal(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Create animal: body, head, features, natural pose.
        """
        draw = ImageDraw.Draw(image)
        
        # Animal type - expanded variety
        animal_type = random.choice([
            'cat', 'dog', 'bird', 'deer', 'horse', 'rabbit', 'fox', 'wolf',
            'bear', 'elephant', 'lion', 'tiger', 'abstract'
        ])
        
        animal_center_x = self.center_x
        animal_center_y = self.center_y
        animal_size = min(self.width, self.height) // 3
        
        animal_color = random.choice(palette)
        
        if animal_type == 'cat' or animal_type == 'dog':
            # Body (oval)
            body_width = animal_size
            body_height = int(animal_size * 1.5)
            body_y = animal_center_y + animal_size // 4
            
            draw.ellipse([animal_center_x - body_width, body_y - body_height,
                        animal_center_x + body_width, body_y + body_height],
                       fill=animal_color, outline=None)
            
            # Head (circle, above body)
            head_size = animal_size // 2
            head_y = body_y - body_height - head_size // 2
            
            draw.ellipse([animal_center_x - head_size, head_y - head_size,
                        animal_center_x + head_size, head_y + head_size],
                       fill=animal_color, outline=None)
            
            # Ears
            ear_size = head_size // 3
            # Left ear
            left_ear_x = animal_center_x - head_size // 2
            left_ear_y = head_y - head_size // 2
            ear_points = [
                (left_ear_x, left_ear_y),
                (left_ear_x - ear_size, left_ear_y - ear_size),
                (left_ear_x + ear_size, left_ear_y - ear_size)
            ]
            draw.polygon(ear_points, fill=animal_color, outline=None)
            
            # Right ear
            right_ear_x = animal_center_x + head_size // 2
            right_ear_y = head_y - head_size // 2
            ear_points = [
                (right_ear_x, right_ear_y),
                (right_ear_x - ear_size, right_ear_y - ear_size),
                (right_ear_x + ear_size, right_ear_y - ear_size)
            ]
            draw.polygon(ear_points, fill=animal_color, outline=None)
            
            # Eyes
            eye_size = head_size // 6
            eye_color = (0, 0, 0)  # Black eyes
            eye_y = head_y
            
            # Left eye
            draw.ellipse([animal_center_x - head_size//3 - eye_size, eye_y - eye_size,
                        animal_center_x - head_size//3 + eye_size, eye_y + eye_size],
                       fill=eye_color, outline=None)
            
            # Right eye
            draw.ellipse([animal_center_x + head_size//3 - eye_size, eye_y - eye_size,
                        animal_center_x + head_size//3 + eye_size, eye_y + eye_size],
                       fill=eye_color, outline=None)
            
            # Nose
            nose_size = head_size // 8
            nose_y = head_y + head_size // 4
            nose_color = random.choice(palette)
            draw.ellipse([animal_center_x - nose_size, nose_y - nose_size,
                        animal_center_x + nose_size, nose_y + nose_size],
                       fill=nose_color, outline=None)
            
            # Tail
            if random.random() < 0.7:
                tail_start_x = animal_center_x + body_width
                tail_start_y = body_y
                tail_length = animal_size
                tail_angle = random.uniform(-math.pi/4, math.pi/4)
                tail_end_x = int(tail_start_x + tail_length * math.cos(tail_angle))
                tail_end_y = int(tail_start_y + tail_length * math.sin(tail_angle))
                
                tail_width = animal_size // 8
                # Fixed: ensure coordinates are ordered correctly (x1 <= x2, y1 <= y2)
                tail_x1 = min(tail_start_x - tail_width, tail_end_x - tail_width)
                tail_x2 = max(tail_start_x + tail_width, tail_end_x + tail_width)
                tail_y1 = min(tail_start_y - tail_width, tail_end_y - tail_width)
                tail_y2 = max(tail_start_y + tail_width, tail_end_y + tail_width)
                # Clamp to image bounds
                tail_x1 = max(0, min(tail_x1, self.width - 1))
                tail_x2 = max(0, min(tail_x2, self.width - 1))
                tail_y1 = max(0, min(tail_y1, self.height - 1))
                tail_y2 = max(0, min(tail_y2, self.height - 1))
                draw.ellipse([tail_x1, tail_y1, tail_x2, tail_y2],
                           fill=animal_color, outline=None)
            
            # Legs
            leg_width = animal_size // 6
            leg_height = animal_size // 2
            leg_y = body_y + body_height
            
            # Front legs
            front_leg_x = animal_center_x - body_width // 2
            draw.rectangle([front_leg_x - leg_width//2, leg_y,
                          front_leg_x + leg_width//2, leg_y + leg_height],
                         fill=animal_color, outline=None)
            
            front_leg_x2 = animal_center_x + body_width // 2
            draw.rectangle([front_leg_x2 - leg_width//2, leg_y,
                          front_leg_x2 + leg_width//2, leg_y + leg_height],
                         fill=animal_color, outline=None)
        
        elif animal_type == 'bird':
            # Bird body (oval, horizontal)
            body_width = animal_size * 1.5
            body_height = animal_size // 2
            
            draw.ellipse([animal_center_x - body_width, animal_center_y - body_height,
                        animal_center_x + body_width, animal_center_y + body_height],
                       fill=animal_color, outline=None)
            
            # Head (smaller circle)
            head_size = animal_size // 3
            head_x = animal_center_x - body_width + head_size
            head_y = animal_center_y - head_size // 2
            
            draw.ellipse([head_x - head_size, head_y - head_size,
                        head_x + head_size, head_y + head_size],
                       fill=animal_color, outline=None)
            
            # Beak
            beak_size = head_size // 3
            beak_x = head_x - head_size
            beak_y = head_y
            beak_points = [
                (beak_x, beak_y),
                (beak_x - beak_size, beak_y - beak_size//2),
                (beak_x - beak_size, beak_y + beak_size//2)
            ]
            beak_color = random.choice(palette)
            draw.polygon(beak_points, fill=beak_color, outline=None)
            
            # Wings
            wing_size = animal_size
            # Left wing
            wing_x = animal_center_x - body_width // 2
            wing_y = animal_center_y
            draw.ellipse([wing_x - wing_size, wing_y - wing_size//2,
                        wing_x, wing_y + wing_size//2],
                       fill=animal_color, outline=None)
            
            # Right wing
            wing_x = animal_center_x + body_width // 2
            draw.ellipse([wing_x, wing_y - wing_size//2,
                        wing_x + wing_size, wing_y + wing_size//2],
                       fill=animal_color, outline=None)
            
            # Eye
            eye_size = head_size // 6
            eye_x = head_x - head_size // 3
            eye_y = head_y - head_size // 4
            draw.ellipse([eye_x - eye_size, eye_y - eye_size,
                        eye_x + eye_size, eye_y + eye_size],
                       fill=(0, 0, 0), outline=None)
        
        elif animal_type == 'deer' or animal_type == 'horse':
            # Body (elongated oval)
            body_width = animal_size * 1.2
            body_height = animal_size
            body_y = animal_center_y + animal_size // 4
            
            draw.ellipse([animal_center_x - body_width, body_y - body_height,
                        animal_center_x + body_width, body_y + body_height],
                       fill=animal_color, outline=None)
            
            # Head (smaller, above body)
            head_size = animal_size // 2
            head_y = body_y - body_height - head_size // 2
            
            draw.ellipse([animal_center_x - head_size, head_y - head_size,
                        animal_center_x + head_size, head_y + head_size],
                       fill=animal_color, outline=None)
            
            # Antlers/horns (for deer) or ears (for horse)
            if animal_type == 'deer':
                # Antlers
                antler_size = head_size
                antler_y = head_y - head_size
                # Left antler
                antler_points = [
                    (animal_center_x - head_size//3, antler_y),
                    (animal_center_x - head_size//2, antler_y - antler_size),
                    (animal_center_x - head_size//4, antler_y - antler_size//2)
                ]
                draw.polygon(antler_points, fill=animal_color, outline=None)
                # Right antler
                antler_points = [
                    (animal_center_x + head_size//3, antler_y),
                    (animal_center_x + head_size//2, antler_y - antler_size),
                    (animal_center_x + head_size//4, antler_y - antler_size//2)
                ]
                draw.polygon(antler_points, fill=animal_color, outline=None)
            else:
                # Ears
                ear_size = head_size // 4
                # Left ear
                draw.ellipse([animal_center_x - head_size//2, head_y - head_size,
                            animal_center_x - head_size//2 + ear_size, head_y - head_size + ear_size],
                           fill=animal_color, outline=None)
                # Right ear
                draw.ellipse([animal_center_x + head_size//2 - ear_size, head_y - head_size,
                            animal_center_x + head_size//2, head_y - head_size + ear_size],
                           fill=animal_color, outline=None)
            
            # Legs (4 legs)
            leg_width = animal_size // 8
            leg_height = animal_size
            leg_y = body_y + body_height
            
            leg_positions = [
                animal_center_x - body_width * 0.6,
                animal_center_x - body_width * 0.2,
                animal_center_x + body_width * 0.2,
                animal_center_x + body_width * 0.6
            ]
            
            for leg_x in leg_positions:
                draw.rectangle([leg_x - leg_width//2, leg_y,
                              leg_x + leg_width//2, leg_y + leg_height],
                             fill=animal_color, outline=None)
            
            # Tail
            if random.random() < 0.7:
                tail_x = animal_center_x + body_width
                tail_y = body_y
                tail_length = animal_size // 2
                # Fixed: compute coordinate ranges first, then clamp separately (correct pattern)
                tail_x1 = tail_x - tail_length // 2
                tail_x2 = tail_x + tail_length
                tail_y1 = tail_y - tail_length // 2
                tail_y2 = tail_y + tail_length // 2
                # Ensure coordinates are ordered correctly
                if tail_x1 > tail_x2:
                    tail_x1, tail_x2 = tail_x2, tail_x1
                if tail_y1 > tail_y2:
                    tail_y1, tail_y2 = tail_y2, tail_y1
                # Clamp to image bounds (separate step, like lines 2995-2998)
                tail_x1 = max(0, min(tail_x1, self.width - 1))
                tail_x2 = max(0, min(tail_x2, self.width - 1))
                tail_y1 = max(0, min(tail_y1, self.height - 1))
                tail_y2 = max(0, min(tail_y2, self.height - 1))
                draw.ellipse([tail_x1, tail_y1, tail_x2, tail_y2],
                           fill=animal_color, outline=None)
        
        elif animal_type in ['rabbit', 'fox', 'wolf']:
            # Small to medium mammals with similar structure
            body_width = animal_size * 0.9
            body_height = animal_size * 1.2
            body_y = animal_center_y + animal_size // 4
            
            draw.ellipse([animal_center_x - body_width, body_y - body_height,
                        animal_center_x + body_width, body_y + body_height],
                       fill=animal_color, outline=None)
            
            # Head
            head_size = animal_size // 2
            head_y = body_y - body_height - head_size // 2
            
            draw.ellipse([animal_center_x - head_size, head_y - head_size,
                        animal_center_x + head_size, head_y + head_size],
                       fill=animal_color, outline=None)
            
            # Long ears (rabbit) or pointed ears (fox/wolf)
            ear_size = int(head_size // 2) if animal_type == 'rabbit' else int(head_size // 3)
            # Left ear
            ear_x1 = int(animal_center_x - head_size // 2)
            ear_y1 = int(head_y - head_size)
            ear_x2 = int(ear_x1 - ear_size // 2) if animal_type == 'rabbit' else int(ear_x1)
            ear_y2 = int(ear_y1 - ear_size * (2 if animal_type == 'rabbit' else 1))
            draw.polygon([(ear_x1, ear_y1), (ear_x2, ear_y2), (int(ear_x1 + ear_size), ear_y1)],
                        fill=animal_color, outline=None)
            # Right ear
            ear_x1 = int(animal_center_x + head_size // 2)
            ear_x2 = int(ear_x1 + ear_size // 2) if animal_type == 'rabbit' else int(ear_x1)
            draw.polygon([(ear_x1, ear_y1), (ear_x2, ear_y2), (int(ear_x1 - ear_size), ear_y1)],
                        fill=animal_color, outline=None)
            
            # Eyes
            eye_size = head_size // 8
            eye_y = head_y
            draw.ellipse([animal_center_x - head_size//3 - eye_size, eye_y - eye_size,
                        animal_center_x - head_size//3 + eye_size, eye_y + eye_size],
                       fill=(0, 0, 0), outline=None)
            draw.ellipse([animal_center_x + head_size//3 - eye_size, eye_y - eye_size,
                        animal_center_x + head_size//3 + eye_size, eye_y + eye_size],
                       fill=(0, 0, 0), outline=None)
            
            # Legs
            leg_width = animal_size // 8
            leg_height = animal_size // 2
            leg_y = body_y + body_height
            for leg_x in [animal_center_x - body_width//2, animal_center_x + body_width//2]:
                leg_x1 = max(0, min(leg_x - leg_width//2, self.width - 1))
                leg_x2 = max(0, min(leg_x + leg_width//2, self.width - 1))
                leg_y1 = max(0, min(leg_y, self.height - 1))
                leg_y2 = max(0, min(leg_y + leg_height, self.height - 1))
                if leg_x1 > leg_x2:
                    leg_x1, leg_x2 = leg_x2, leg_x1
                if leg_y1 > leg_y2:
                    leg_y1, leg_y2 = leg_y2, leg_y1
                draw.rectangle([leg_x1, leg_y1, leg_x2, leg_y2],
                             fill=animal_color, outline=None)
        
        elif animal_type in ['bear', 'elephant']:
            # Large animals
            body_width = animal_size * 1.3
            body_height = animal_size * 1.1
            body_y = animal_center_y + animal_size // 4
            
            draw.ellipse([animal_center_x - body_width, body_y - body_height,
                        animal_center_x + body_width, body_y + body_height],
                       fill=animal_color, outline=None)
            
            # Head
            head_size = animal_size // 1.5
            head_y = body_y - body_height - head_size // 3
            
            draw.ellipse([animal_center_x - head_size, head_y - head_size,
                        animal_center_x + head_size, head_y + head_size],
                       fill=animal_color, outline=None)
            
            # Ears (large for elephant, small for bear)
            if animal_type == 'elephant':
                ear_size = head_size
                # Left ear
                ear_x1 = max(0, min(animal_center_x - head_size - ear_size//2, self.width - 1))
                ear_x2 = max(0, min(animal_center_x - head_size + ear_size//2, self.width - 1))
                ear_y1 = max(0, min(head_y - ear_size//2, self.height - 1))
                ear_y2 = max(0, min(head_y + ear_size//2, self.height - 1))
                if ear_x1 > ear_x2:
                    ear_x1, ear_x2 = ear_x2, ear_x1
                if ear_y1 > ear_y2:
                    ear_y1, ear_y2 = ear_y2, ear_y1
                draw.ellipse([ear_x1, ear_y1, ear_x2, ear_y2],
                           fill=animal_color, outline=None)
                # Right ear
                ear_x1 = max(0, min(animal_center_x + head_size - ear_size//2, self.width - 1))
                ear_x2 = max(0, min(animal_center_x + head_size + ear_size//2, self.width - 1))
                if ear_x1 > ear_x2:
                    ear_x1, ear_x2 = ear_x2, ear_x1
                draw.ellipse([ear_x1, ear_y1, ear_x2, ear_y2],
                           fill=animal_color, outline=None)
            
            # Trunk (elephant) or snout (bear)
            if animal_type == 'elephant':
                trunk_length = head_size
                trunk_y1 = max(0, min(head_y + head_size // 2, self.height - 1))
                trunk_y2 = max(0, min(trunk_y1 + trunk_length, self.height - 1))
                trunk_width = head_size // 4
                trunk_x1 = max(0, min(animal_center_x - trunk_width, self.width - 1))
                trunk_x2 = max(0, min(animal_center_x + trunk_width, self.width - 1))
                if trunk_x1 > trunk_x2:
                    trunk_x1, trunk_x2 = trunk_x2, trunk_x1
                if trunk_y1 > trunk_y2:
                    trunk_y1, trunk_y2 = trunk_y2, trunk_y1
                draw.ellipse([trunk_x1, trunk_y1, trunk_x2, trunk_y2],
                           fill=animal_color, outline=None)
            
            # Legs (4 legs, thick)
            leg_width = animal_size // 6
            leg_height = animal_size
            leg_y = body_y + body_height
            for leg_x in [animal_center_x - body_width*0.6, animal_center_x - body_width*0.2,
                         animal_center_x + body_width*0.2, animal_center_x + body_width*0.6]:
                leg_x1 = max(0, min(leg_x - leg_width//2, self.width - 1))
                leg_x2 = max(0, min(leg_x + leg_width//2, self.width - 1))
                leg_y1 = max(0, min(leg_y, self.height - 1))
                leg_y2 = max(0, min(leg_y + leg_height, self.height - 1))
                if leg_x1 > leg_x2:
                    leg_x1, leg_x2 = leg_x2, leg_x1
                if leg_y1 > leg_y2:
                    leg_y1, leg_y2 = leg_y2, leg_y1
                draw.rectangle([leg_x1, leg_y1, leg_x2, leg_y2],
                             fill=animal_color, outline=None)
        
        elif animal_type in ['lion', 'tiger']:
            # Big cats
            body_width = animal_size * 1.1
            body_height = animal_size * 1.3
            body_y = animal_center_y + animal_size // 4
            
            draw.ellipse([animal_center_x - body_width, body_y - body_height,
                        animal_center_x + body_width, body_y + body_height],
                       fill=animal_color, outline=None)
            
            # Head with mane (lion) or stripes (tiger)
            head_size = animal_size // 1.8
            head_y = body_y - body_height - head_size // 2
            
            # Mane for lion
            if animal_type == 'lion':
                mane_size = int(head_size * 1.3)
                mane_color = (min(255, animal_color[0] + 30), min(255, animal_color[1] + 20), animal_color[2])
                mane_x1 = int(max(0, min(animal_center_x - mane_size, self.width - 1)))
                mane_x2 = int(max(0, min(animal_center_x + mane_size, self.width - 1)))
                mane_y1 = int(max(0, min(head_y - mane_size, self.height - 1)))
                mane_y2 = int(max(0, min(head_y + mane_size, self.height - 1)))
                if mane_x1 > mane_x2:
                    mane_x1, mane_x2 = mane_x2, mane_x1
                if mane_y1 > mane_y2:
                    mane_y1, mane_y2 = mane_y2, mane_y1
                draw.ellipse([mane_x1, mane_y1, mane_x2, mane_y2],
                           fill=mane_color, outline=None)
            
            head_x1 = max(0, min(animal_center_x - head_size, self.width - 1))
            head_x2 = max(0, min(animal_center_x + head_size, self.width - 1))
            head_y1 = max(0, min(head_y - head_size, self.height - 1))
            head_y2 = max(0, min(head_y + head_size, self.height - 1))
            if head_x1 > head_x2:
                head_x1, head_x2 = head_x2, head_x1
            if head_y1 > head_y2:
                head_y1, head_y2 = head_y2, head_y1
            draw.ellipse([head_x1, head_y1, head_x2, head_y2],
                       fill=animal_color, outline=None)
            
            # Stripes for tiger
            if animal_type == 'tiger':
                stripe_color = (0, 0, 0)
                for _ in range(5):
                    stripe_x = random.randint(max(0, animal_center_x - body_width), 
                                            min(self.width - 1, animal_center_x + body_width))
                    stripe_y1 = max(0, min(body_y - body_height, self.height - 1))
                    stripe_y2 = max(0, min(body_y + body_height, self.height - 1))
                    if stripe_y1 > stripe_y2:
                        stripe_y1, stripe_y2 = stripe_y2, stripe_y1
                    draw.line([(stripe_x, stripe_y1), (stripe_x, stripe_y2)],
                             fill=stripe_color, width=3)
            
            # Eyes
            eye_size = head_size // 6
            eye_y = head_y
            eye_x1 = max(0, min(animal_center_x - head_size//3 - eye_size, self.width - 1))
            eye_x2 = max(0, min(animal_center_x - head_size//3 + eye_size, self.width - 1))
            eye_y1 = max(0, min(eye_y - eye_size, self.height - 1))
            eye_y2 = max(0, min(eye_y + eye_size, self.height - 1))
            if eye_x1 > eye_x2:
                eye_x1, eye_x2 = eye_x2, eye_x1
            if eye_y1 > eye_y2:
                eye_y1, eye_y2 = eye_y2, eye_y1
            draw.ellipse([eye_x1, eye_y1, eye_x2, eye_y2],
                       fill=(255, 200, 0), outline=(0, 0, 0), width=2)
            eye_x1 = max(0, min(animal_center_x + head_size//3 - eye_size, self.width - 1))
            eye_x2 = max(0, min(animal_center_x + head_size//3 + eye_size, self.width - 1))
            if eye_x1 > eye_x2:
                eye_x1, eye_x2 = eye_x2, eye_x1
            draw.ellipse([eye_x1, eye_y1, eye_x2, eye_y2],
                       fill=(255, 200, 0), outline=(0, 0, 0), width=2)
            
            # Legs
            leg_width = animal_size // 7
            leg_height = animal_size // 1.5
            leg_y = body_y + body_height
            for leg_x in [animal_center_x - body_width//2, animal_center_x + body_width//2]:
                leg_x1 = max(0, min(leg_x - leg_width//2, self.width - 1))
                leg_x2 = max(0, min(leg_x + leg_width//2, self.width - 1))
                leg_y1 = max(0, min(leg_y, self.height - 1))
                leg_y2 = max(0, min(leg_y + leg_height, self.height - 1))
                if leg_x1 > leg_x2:
                    leg_x1, leg_x2 = leg_x2, leg_x1
                if leg_y1 > leg_y2:
                    leg_y1, leg_y2 = leg_y2, leg_y1
                draw.rectangle([leg_x1, leg_y1, leg_x2, leg_y2],
                             fill=animal_color, outline=None)
        
        else:  # abstract animal
            # Abstract animal form
            num_parts = random.randint(3, 6)
            for i in range(num_parts):
                part_color = random.choice(palette)
                part_x = animal_center_x + random.randint(-animal_size, animal_size)
                part_y = animal_center_y + random.randint(-animal_size, animal_size)
                part_size = random.randint(animal_size // 4, animal_size // 2)
                
                shape = random.choice(['circle', 'ellipse', 'organic'])
                if shape == 'circle':
                    draw.ellipse([part_x - part_size, part_y - part_size,
                                part_x + part_size, part_y + part_size],
                               fill=part_color, outline=None)
                elif shape == 'ellipse':
                    w = part_size
                    h = int(part_size * random.uniform(0.7, 1.3))
                    draw.ellipse([part_x - w, part_y - h, part_x + w, part_y + h],
                               fill=part_color, outline=None)
                else:  # organic
                    points = []
                    for j in range(8):
                        angle = 2 * math.pi * j / 8
                        r = part_size * random.uniform(0.7, 1.1)
                        px = int(part_x + r * math.cos(angle))
                        py = int(part_y + r * math.sin(angle))
                        points.append((px, py))
                    draw.polygon(points, fill=part_color, outline=None)
        
        return image
    
    def _create_interior(self, image: Image.Image, palette: List[Tuple[int, int, int]]) -> Image.Image:
        """
        Create interior: room, furniture, architectural elements, perspective.
        """
        draw = ImageDraw.Draw(image)
        
        # Room perspective (one-point perspective)
        vanishing_point_x = self.center_x
        vanishing_point_y = self.height // 3
        
        # Floor
        floor_color = random.choice(palette)
        # Darken for floor
        r, g, b = floor_color
        r = max(0, int(r * 0.7))
        g = max(0, int(g * 0.7))
        b = max(0, int(b * 0.7))
        floor_color = (r, g, b)
        
        floor_y = int(self.height * 2 // 3)
        floor_points = [
            (0, floor_y),
            (self.width, floor_y),
            (self.width, self.height),
            (0, self.height)
        ]
        draw.polygon(floor_points, fill=floor_color, outline=None)
        
        # Walls
        wall_color = random.choice(palette)
        # Lighten for walls
        r, g, b = wall_color
        r = min(255, int(r + (255 - r) * 0.2))
        g = min(255, int(g + (255 - g) * 0.2))
        b = min(255, int(b + (255 - b) * 0.2))
        wall_color = (r, g, b)
        
        # Left wall
        left_wall_points = [
            (0, 0),
            (0, self.height),
            (vanishing_point_x, floor_y),
            (vanishing_point_x, vanishing_point_y)
        ]
        draw.polygon(left_wall_points, fill=wall_color, outline=None)
        
        # Right wall
        right_wall_points = [
            (self.width, 0),
            (self.width, self.height),
            (vanishing_point_x, floor_y),
            (vanishing_point_x, vanishing_point_y)
        ]
        draw.polygon(right_wall_points, fill=wall_color, outline=None)
        
        # Ceiling
        ceiling_color = random.choice(palette)
        # Lighten for ceiling
        r, g, b = ceiling_color
        r = min(255, int(r + (255 - r) * 0.3))
        g = min(255, int(g + (255 - g) * 0.3))
        b = min(255, int(b + (255 - b) * 0.3))
        ceiling_color = (r, g, b)
        
        ceiling_points = [
            (0, 0),
            (self.width, 0),
            (vanishing_point_x, vanishing_point_y)
        ]
        draw.polygon(ceiling_points, fill=ceiling_color, outline=None)
        
        # Furniture and elements
        # Window
        if random.random() < 0.7:
            window_color = random.choice(palette)
            # Lighten for window (light coming through)
            r, g, b = window_color
            r = min(255, int(r + (255 - r) * 0.5))
            g = min(255, int(g + (255 - g) * 0.5))
            b = min(255, int(b + (255 - b) * 0.5))
            window_color = (r, g, b)
            
            window_x = random.choice([self.width // 4, 3 * self.width // 4])
            window_y = self.height // 4
            window_width = self.width // 6
            window_height = self.height // 4
            
            # Window frame
            draw.rectangle([window_x - window_width, window_y - window_height,
                          window_x + window_width, window_y + window_height],
                         fill=window_color, outline=None)
            
            # Window cross (panes)
            draw.line([(window_x, window_y - window_height), (window_x, window_y + window_height)],
                     fill=(0, 0, 0), width=2)
            draw.line([(window_x - window_width, window_y), (window_x + window_width, window_y)],
                     fill=(0, 0, 0), width=2)
        
        # Table
        if random.random() < 0.6:
            table_color = random.choice(palette)
            table_y = floor_y - self.height // 8
            table_width = self.width // 3
            table_depth = self.height // 6
            
            # Table top (trapezoid in perspective)
            table_top_points = [
                (vanishing_point_x - table_width, table_y),
                (vanishing_point_x + table_width, table_y),
                (vanishing_point_x + table_width//2, table_y - table_depth),
                (vanishing_point_x - table_width//2, table_y - table_depth)
            ]
            draw.polygon(table_top_points, fill=table_color, outline=None)
            
            # Table legs
            leg_width = self.width // 40
            leg_positions = [
                (vanishing_point_x - table_width * 0.7, table_y),
                (vanishing_point_x + table_width * 0.7, table_y),
                (vanishing_point_x - table_width * 0.3, table_y - table_depth),
                (vanishing_point_x + table_width * 0.3, table_y - table_depth)
            ]
            
            for leg_x, leg_y in leg_positions:
                leg_height = floor_y - leg_y
                draw.rectangle([leg_x - leg_width//2, leg_y,
                              leg_x + leg_width//2, leg_y + leg_height],
                             fill=table_color, outline=None)
        
        # Chair
        if random.random() < 0.5:
            chair_color = random.choice(palette)
            chair_x = vanishing_point_x + random.randint(-self.width//4, self.width//4)
            chair_y = floor_y - self.height // 12
            chair_width = self.width // 8
            chair_height = self.height // 6
            
            # Chair back
            draw.rectangle([chair_x - chair_width//2, chair_y - chair_height,
                          chair_x + chair_width//2, chair_y],
                         fill=chair_color, outline=None)
            
            # Chair seat
            seat_depth = self.height // 12
            seat_points = [
                (chair_x - chair_width//2, chair_y),
                (chair_x + chair_width//2, chair_y),
                (chair_x + chair_width//3, chair_y - seat_depth),
                (chair_x - chair_width//3, chair_y - seat_depth)
            ]
            draw.polygon(seat_points, fill=chair_color, outline=None)
            
            # Chair legs
            leg_width = self.width // 50
            leg_x_positions = [
                chair_x - chair_width//3,
                chair_x + chair_width//3
            ]
            
            for leg_x in leg_x_positions:
                leg_height = floor_y - chair_y
                draw.rectangle([leg_x - leg_width//2, chair_y,
                              leg_x + leg_width//2, chair_y + leg_height],
                             fill=chair_color, outline=None)
        
        # Decorative elements
        # Picture on wall
        if random.random() < 0.4:
            picture_color = random.choice(palette)
            picture_x = random.choice([self.width // 6, 5 * self.width // 6])
            picture_y = self.height // 3
            picture_width = self.width // 10
            picture_height = self.height // 8
            
            draw.rectangle([picture_x - picture_width, picture_y - picture_height,
                          picture_x + picture_width, picture_y + picture_height],
                         fill=picture_color, outline=(0, 0, 0), width=2)
        
        # Door
        if random.random() < 0.5:
            door_color = random.choice(palette)
            door_x = random.choice([self.width // 8, 7 * self.width // 8])
            door_width = self.width // 8
            door_height = floor_y - self.height // 4
            
            draw.rectangle([door_x - door_width//2, self.height // 4,
                          door_x + door_width//2, self.height // 4 + door_height],
                         fill=door_color, outline=None)
            
            # Door handle
            handle_x = door_x + door_width//3
            handle_y = self.height // 4 + door_height // 2
            draw.ellipse([handle_x - 3, handle_y - 3, handle_x + 3, handle_y + 3],
                       fill=(0, 0, 0), outline=None)
        
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
            'impressionism': 1.1,  # Slightly enhanced for light effects
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
        elif style == 'impressionism':
            # Soft blur already applied in _create_impressionism, but ensure it's maintained
            pass  # Blur already applied in creation method
        
        # Sharpening for precision
        if style in ['precisionism', 'op_art', 'constructivism', 'de_stijl']:
            image = image.filter(ImageFilter.SHARPEN)
        
        return image

