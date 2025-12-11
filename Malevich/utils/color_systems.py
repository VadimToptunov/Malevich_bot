"""
Advanced color system with sophisticated palettes and complex harmonies.
Extracted from interdisciplinary_generator for reuse across all generators.
All documentation in English.
"""
import random
import math
from typing import Tuple, List
from colorsys import hsv_to_rgb, rgb_to_hsv


class AdvancedColorSystem:
    """Advanced color system with sophisticated palettes and complex harmonies."""
    
    # Sophisticated color palettes with complex, nuanced colors
    # Using desaturated, tinted, shaded, and toned colors
    SOPHISTICATED_PALETTES = {
        'luxury': [
            (45, 45, 65),      # Deep charcoal blue
            (120, 100, 80),    # Muted taupe
            (180, 150, 120),   # Warm beige
            (200, 180, 160),   # Cream
            (85, 65, 95),      # Dusty plum
            (140, 120, 100),   # Sage taupe
            (220, 200, 180),   # Soft ivory
            (95, 85, 110),     # Lavender gray
        ],
        'vibrant_sophisticated': [
            (220, 50, 80),     # Deep rose
            (180, 70, 120),    # Muted magenta
            (100, 150, 200),   # Soft periwinkle
            (250, 180, 100),   # Warm peach
            (160, 200, 180),   # Mint sage
            (200, 150, 180),   # Dusty rose
            (140, 120, 200),   # Lavender
            (220, 160, 140),   # Terracotta
        ],
        'moody_dark': [
            (25, 30, 45),      # Deep navy
            (60, 45, 55),      # Dark burgundy
            (45, 55, 65),      # Slate blue
            (80, 60, 50),      # Burnt sienna
            (55, 65, 75),      # Charcoal blue
            (70, 50, 60),      # Deep mauve
            (40, 50, 60),      # Storm gray
            (90, 70, 55),      # Dark rust
        ],
        'pastel_sophisticated': [
            (240, 230, 220),   # Warm white
            (220, 210, 200),   # Soft beige
            (200, 220, 240),   # Powder blue
            (240, 220, 200),   # Peach cream
            (220, 240, 220),   # Mint cream
            (240, 220, 240),   # Lavender cream
            (240, 240, 220),   # Vanilla
            (220, 220, 240),   # Periwinkle cream
        ],
        'earth_rich': [
            (95, 75, 55),      # Rich brown
            (120, 100, 80),    # Taupe
            (140, 120, 100),   # Warm gray
            (110, 90, 70),     # Coffee
            (85, 95, 75),      # Olive brown
            (100, 85, 70),     # Umber
            (130, 110, 90),    # Sandstone
            (75, 85, 95),      # Slate
        ],
        'jewel_tones': [
            (100, 50, 120),    # Deep amethyst
            (50, 100, 150),    # Sapphire
            (150, 100, 50),    # Amber
            (120, 50, 100),    # Ruby
            (50, 150, 100),    # Emerald
            (150, 120, 50),    # Topaz
            (100, 120, 150),   # Aquamarine
            (120, 100, 150),   # Tanzanite
        ],
        'sunset_complex': [
            (255, 120, 80),    # Coral
            (255, 160, 100),   # Peach
            (200, 100, 120),   # Rose
            (180, 140, 160),   # Dusty rose
            (220, 180, 140),   # Apricot
            (160, 120, 140),   # Mauve
            (240, 200, 160),   # Cream
            (200, 160, 180),   # Blush
        ],
        'ocean_depth': [
            (20, 40, 60),      # Deep ocean
            (40, 70, 90),      # Ocean blue
            (60, 100, 120),    # Teal
            (80, 120, 140),    # Aqua
            (100, 140, 160),   # Sky blue
            (50, 80, 100),     # Steel blue
            (70, 90, 110),     # Slate blue
            (30, 50, 70),      # Navy
        ],
        'forest_mystery': [
            (30, 50, 40),      # Deep forest
            (50, 70, 60),      # Forest green
            (70, 90, 80),      # Sage
            (90, 110, 100),    # Moss
            (40, 60, 50),      # Pine
            (60, 80, 70),      # Olive
            (80, 100, 90),     # Mint
            (50, 70, 55),      # Emerald
        ],
        'metallic_sophisticated': [
            (180, 170, 160),   # Pewter
            (200, 190, 180),   # Silver
            (220, 200, 150),   # Gold
            (160, 150, 140),   # Bronze
            (190, 180, 170),   # Platinum
            (170, 160, 150),   # Steel
            (210, 190, 160),   # Brass
            (150, 140, 130),   # Iron
        ],
    }
    
    @staticmethod
    def rgb_to_lab(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
        """Convert RGB to LAB color space for better color manipulation."""
        # Simplified RGB to LAB conversion
        r, g, b = [c / 255.0 for c in rgb]
        
        # Gamma correction
        r = r / 12.92 if r <= 0.04045 else ((r + 0.055) / 1.055) ** 2.4
        g = g / 12.92 if g <= 0.04045 else ((g + 0.055) / 1.055) ** 2.4
        b = b / 12.92 if b <= 0.04045 else ((b + 0.055) / 1.055) ** 2.4
        
        # Convert to XYZ (simplified)
        x = r * 0.4124 + g * 0.3576 + b * 0.1805
        y = r * 0.2126 + g * 0.7152 + b * 0.0722
        z = r * 0.0193 + g * 0.1192 + b * 0.9505
        
        # Convert to LAB (simplified)
        x /= 0.95047
        z /= 1.08883
        
        fx = x ** (1/3) if x > 0.008856 else (7.787 * x + 16/116)
        fy = y ** (1/3) if y > 0.008856 else (7.787 * y + 16/116)
        fz = z ** (1/3) if z > 0.008856 else (7.787 * z + 16/116)
        
        L = 116 * fy - 16
        a = 500 * (fx - fy)
        b = 200 * (fy - fz)
        
        return (L, a, b)
    
    @staticmethod
    def create_tinted_color(color: Tuple[int, int, int], white_amount: float = 0.3) -> Tuple[int, int, int]:
        """Create tinted color (add white, desaturate)."""
        r, g, b = color
        r = int(r + (255 - r) * white_amount)
        g = int(g + (255 - g) * white_amount)
        b = int(b + (255 - b) * white_amount)
        return (min(255, r), min(255, g), min(255, b))
    
    @staticmethod
    def create_shaded_color(color: Tuple[int, int, int], black_amount: float = 0.3) -> Tuple[int, int, int]:
        """Create shaded color (add black, darken)."""
        r, g, b = color
        r = int(r * (1 - black_amount))
        g = int(g * (1 - black_amount))
        b = int(b * (1 - black_amount))
        return (max(0, r), max(0, g), max(0, b))
    
    @staticmethod
    def create_toned_color(color: Tuple[int, int, int], gray_amount: float = 0.3) -> Tuple[int, int, int]:
        """Create toned color (add gray, reduce saturation)."""
        r, g, b = color
        gray = int((r + g + b) / 3)
        r = int(r * (1 - gray_amount) + gray * gray_amount)
        g = int(g * (1 - gray_amount) + gray * gray_amount)
        b = int(b * (1 - gray_amount) + gray * gray_amount)
        return (min(255, max(0, r)), min(255, max(0, g)), min(255, max(0, b)))
    
    @staticmethod
    def generate_complex_harmony(base_color: Tuple[int, int, int], harmony_type: str = 'tetradic',
                                variations: int = 8) -> List[Tuple[int, int, int]]:
        """Generate complex color harmony with variations."""
        r, g, b = [c / 255.0 for c in base_color]
        h, s, v = rgb_to_hsv(r, g, b)
        hue = h * 360.0
        
        palette = []
        
        if harmony_type == 'tetradic':
            # Four colors forming rectangle on color wheel
            hues = [hue, (hue + 60) % 360, (hue + 180) % 360, (hue + 240) % 360]
        elif harmony_type == 'split_triadic':
            # Base + two colors adjacent to complement
            comp_hue = (hue + 180) % 360
            hues = [hue, (comp_hue - 30) % 360, (comp_hue + 30) % 360]
        elif harmony_type == 'analogous_extended':
            # Five adjacent colors
            hues = [(hue + i * 15) % 360 for i in range(5)]
        elif harmony_type == 'double_complementary':
            # Two complementary pairs
            hues = [hue, (hue + 180) % 360, (hue + 30) % 360, (hue + 210) % 360]
        else:  # complex_triadic
            # Three colors with variations
            hues = [hue, (hue + 120) % 360, (hue + 240) % 360]
        
        for h_val in hues:
            # Base color
            rgb = AdvancedColorSystem.hue_to_rgb(h_val, s, v)
            palette.append(rgb)
            
            # Create variations: tinted, shaded, toned
            palette.append(AdvancedColorSystem.create_tinted_color(rgb, 0.2))
            palette.append(AdvancedColorSystem.create_shaded_color(rgb, 0.2))
            palette.append(AdvancedColorSystem.create_toned_color(rgb, 0.2))
        
        return palette[:variations]
    
    @staticmethod
    def hue_to_rgb(hue: float, saturation: float, value: float) -> Tuple[int, int, int]:
        """Convert HSV to RGB."""
        r, g, b = hsv_to_rgb(hue / 360.0, saturation, value)
        return (int(r * 255), int(g * 255), int(b * 255))
    
    @staticmethod
    def create_sophisticated_gradient(color1: Tuple[int, int, int], color2: Tuple[int, int, int],
                                     steps: int = 100, curve: str = 'ease_in_out') -> List[Tuple[int, int, int]]:
        """Create sophisticated gradient with easing curves."""
        gradient = []
        
        for i in range(steps):
            t = i / (steps - 1)
            
            # Apply easing curve
            if curve == 'ease_in_out':
                t = t * t * (3 - 2 * t)  # Smoothstep
            elif curve == 'ease_in':
                t = t * t
            elif curve == 'ease_out':
                t = 1 - (1 - t) * (1 - t)
            elif curve == 'sine':
                t = (1 - math.cos(t * math.pi)) / 2
            
            # Interpolate colors
            r = int(color1[0] * (1 - t) + color2[0] * t)
            g = int(color1[1] * (1 - t) + color2[1] * t)
            b = int(color1[2] * (1 - t) + color2[2] * t)
            
            gradient.append((r, g, b))
        
        return gradient

