"""
Advanced Animal Generator - Uses art knowledge base to create realistic animals
in various artistic styles based on world art movements.
All documentation in English.
"""
import random
import math
from typing import Tuple, List, Optional
from PIL import Image, ImageDraw
from Malevich.generators.art_knowledge_base import ArtKnowledgeBase


class AdvancedAnimalGenerator:
    """
    Advanced animal generator that uses art knowledge base to create
    anatomically correct and stylistically appropriate animals.
    """
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
    
    def generate_animal(self, image: Image.Image, palette: List[Tuple[int, int, int]], 
                        style: str = 'realism', animal_type: Optional[str] = None) -> Image.Image:
        """
        Generate an animal using art knowledge base for accurate anatomy and style.
        
        Args:
            image: PIL Image to draw on
            palette: Color palette
            style: Art style (affects proportions, detail, etc.)
            animal_type: Specific animal type, or None for random
            
        Returns:
            Modified PIL Image
        """
        draw = ImageDraw.Draw(image)
        
        # Get style characteristics
        style_chars = ArtKnowledgeBase.get_style_characteristics(style)
        
        # Choose animal type
        if animal_type is None:
            animal_type = random.choice(list(ArtKnowledgeBase.ANIMAL_ANATOMY.keys()))
        
        # Get anatomical reference
        anatomy = ArtKnowledgeBase.get_animal_anatomy(animal_type)
        
        # Base size
        animal_size = min(self.width, self.height) // 3
        
        # Apply style to proportions
        body_ratio = anatomy['body_ratio']
        body_ratio = ArtKnowledgeBase.apply_style_to_proportions(body_ratio, style)
        
        # Calculate body dimensions
        body_width = int(animal_size * body_ratio[0])
        body_height = int(animal_size * body_ratio[1])
        
        # Position animal
        animal_center_x = self.center_x
        animal_center_y = self.center_y + animal_size // 6  # Slightly below center
        body_y = animal_center_y
        
        # Get base color
        animal_color = random.choice(palette)
        
        # Apply style to color
        if style_chars['color_usage'] == 'wild_unrealistic':
            # Fauvism: wild colors
            animal_color = (
                min(255, random.randint(200, 255)),
                min(255, random.randint(100, 255)),
                min(255, random.randint(100, 255))
            )
        elif style_chars['color_usage'] == 'bold_saturated':
            # Pop art: bold colors
            r, g, b = animal_color
            animal_color = (
                min(255, int(r * 1.3)),
                min(255, int(g * 1.3)),
                min(255, int(b * 1.3))
            )
        
        # Draw body with style-appropriate technique
        if style_chars['anatomy'] == 'fragmented':
            # Cubism: fragmented body
            self._draw_fragmented_body(draw, animal_center_x, body_y, body_width, body_height, animal_color)
        elif style_chars['brushwork'] == 'visible_strokes':
            # Impressionism: visible brushstrokes
            self._draw_impressionist_body(draw, animal_center_x, body_y, body_width, body_height, animal_color, palette)
        else:
            # Realism/Hyperrealism: smooth body
            self._draw_realistic_body(draw, animal_center_x, body_y, body_width, body_height, animal_color, style)
        
        # Draw head
        head_size = int(animal_size * anatomy.get('head_ratio', 0.4))
        head_y = body_y - body_height - head_size // 2
        
        if style_chars['detail_level'] in ['high', 'extreme']:
            # Detailed head
            self._draw_detailed_head(draw, animal_type, animal_center_x, head_y, head_size, 
                                    animal_color, palette, anatomy, style_chars)
        else:
            # Simplified head
            self._draw_simplified_head(draw, animal_type, animal_center_x, head_y, head_size,
                                     animal_color, anatomy, style_chars)
        
        # Draw legs
        leg_props = anatomy.get('leg_proportions', (0.15, 0.5))
        leg_width = int(animal_size * leg_props[0])
        leg_height = int(animal_size * leg_props[1])
        leg_y = body_y + body_height
        
        if style_chars['detail_level'] in ['high', 'extreme']:
            self._draw_detailed_legs(draw, animal_type, animal_center_x, body_width, leg_y,
                                   leg_width, leg_height, animal_color, style_chars)
        else:
            self._draw_simplified_legs(draw, animal_center_x, body_width, leg_y,
                                     leg_width, leg_height, animal_color)
        
        # Draw tail if applicable
        if 'tail_length' in anatomy and random.random() < 0.7:
            tail_length = int(animal_size * anatomy['tail_length'])
            self._draw_tail(draw, animal_type, animal_center_x, body_y, body_width,
                          tail_length, animal_color, style_chars)
        
        # Add style-specific details
        if style_chars['detail_level'] == 'extreme':
            self._add_micro_details(draw, animal_center_x, body_y, body_width, body_height,
                                  animal_color, palette)
        
        return image
    
    def _draw_realistic_body(self, draw: ImageDraw.Draw, center_x: int, center_y: int,
                           width: int, height: int, color: Tuple[int, int, int], style: str):
        """Draw realistic body with volume and shading."""
        # Main body
        x1 = max(0, min(center_x - width, self.width - 1))
        x2 = max(0, min(center_x + width, self.width - 1))
        y1 = max(0, min(center_y - height, self.height - 1))
        y2 = max(0, min(center_y + height, self.height - 1))
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        
        draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
        
        # Add shading for volume
        if style in ['realism', 'hyperrealism']:
            # Light source from top-left
            shade_color = (
                max(0, int(color[0] * 0.7)),
                max(0, int(color[1] * 0.7)),
                max(0, int(color[2] * 0.7))
            )
            shade_x1 = max(0, min(center_x - width//2, self.width - 1))
            shade_x2 = max(0, min(center_x + width//3, self.width - 1))
            shade_y1 = max(0, min(center_y - height//3, self.height - 1))
            shade_y2 = max(0, min(center_y + height//2, self.height - 1))
            if shade_x1 > shade_x2:
                shade_x1, shade_x2 = shade_x2, shade_x1
            if shade_y1 > shade_y2:
                shade_y1, shade_y2 = shade_y2, shade_y1
            draw.ellipse([shade_x1, shade_y1, shade_x2, shade_y2], fill=shade_color, outline=None)
    
    def _draw_impressionist_body(self, draw: ImageDraw.Draw, center_x: int, center_y: int,
                               width: int, height: int, color: Tuple[int, int, int],
                               palette: List[Tuple[int, int, int]]):
        """Draw body with visible brushstrokes (Impressionism)."""
        # Multiple overlapping strokes
        for _ in range(15):
            stroke_color = random.choice(palette)
            stroke_x = center_x + random.randint(-width, width)
            stroke_y = center_y + random.randint(-height, height)
            stroke_w = random.randint(20, 40)
            stroke_h = random.randint(30, 50)
            x1 = max(0, min(stroke_x - stroke_w//2, self.width - 1))
            x2 = max(0, min(stroke_x + stroke_w//2, self.width - 1))
            y1 = max(0, min(stroke_y - stroke_h//2, self.height - 1))
            y2 = max(0, min(stroke_y + stroke_h//2, self.height - 1))
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            draw.ellipse([x1, y1, x2, y2], fill=stroke_color, outline=None)
    
    def _draw_fragmented_body(self, draw: ImageDraw.Draw, center_x: int, center_y: int,
                            width: int, height: int, color: Tuple[int, int, int]):
        """Draw fragmented body (Cubism)."""
        # Break body into geometric fragments
        fragments = [
            (center_x - width//2, center_y - height//2, center_x, center_y),
            (center_x, center_y - height//2, center_x + width//2, center_y),
            (center_x - width//2, center_y, center_x, center_y + height//2),
            (center_x, center_y, center_x + width//2, center_y + height//2),
        ]
        for frag in fragments:
            x1, y1, x2, y2 = frag
            x1 = max(0, min(x1, self.width - 1))
            x2 = max(0, min(x2, self.width - 1))
            y1 = max(0, min(y1, self.height - 1))
            y2 = max(0, min(y2, self.height - 1))
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
    
    def _draw_detailed_head(self, draw: ImageDraw.Draw, animal_type: str, center_x: int, head_y: int,
                           head_size: int, color: Tuple[int, int, int], palette: List[Tuple[int, int, int]],
                           anatomy: dict, style_chars: dict):
        """Draw detailed head with features."""
        # Head base
        x1 = max(0, min(center_x - head_size, self.width - 1))
        x2 = max(0, min(center_x + head_size, self.width - 1))
        y1 = max(0, min(head_y - head_size, self.height - 1))
        y2 = max(0, min(head_y + head_size, self.height - 1))
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
        
        # Eyes
        eye_pos = anatomy.get('eye_position', (0.3, 0.4))
        eye_size = head_size // 8
        eye_y = int(head_y + head_size * eye_pos[1])
        
        # Left eye
        left_eye_x = int(center_x - head_size * eye_pos[0])
        eye_x1 = max(0, min(left_eye_x - eye_size, self.width - 1))
        eye_x2 = max(0, min(left_eye_x + eye_size, self.width - 1))
        eye_y1 = max(0, min(eye_y - eye_size, self.height - 1))
        eye_y2 = max(0, min(eye_y + eye_size, self.height - 1))
        if eye_x1 > eye_x2:
            eye_x1, eye_x2 = eye_x2, eye_x1
        if eye_y1 > eye_y2:
            eye_y1, eye_y2 = eye_y2, eye_y1
        
        eye_color = anatomy.get('eye_color', (0, 0, 0))
        draw.ellipse([eye_x1, eye_y1, eye_x2, eye_y2], fill=eye_color, outline=None)
        
        # Right eye
        right_eye_x = int(center_x + head_size * eye_pos[0])
        eye_x1 = max(0, min(right_eye_x - eye_size, self.width - 1))
        eye_x2 = max(0, min(right_eye_x + eye_size, self.width - 1))
        if eye_x1 > eye_x2:
            eye_x1, eye_x2 = eye_x2, eye_x1
        draw.ellipse([eye_x1, eye_y1, eye_x2, eye_y2], fill=eye_color, outline=None)
        
        # Ears
        if 'ear_size' in anatomy:
            ear_size = int(head_size * anatomy['ear_size'])
            ear_shape = anatomy.get('ear_shape', 'triangular')
            
            if ear_shape == 'triangular':
                # Left ear
                ear_x = int(center_x - head_size * 0.4)
                ear_y = int(head_y - head_size * 0.3)
                ear_points = [
                    (ear_x, ear_y),
                    (ear_x - ear_size//2, ear_y - ear_size),
                    (ear_x + ear_size//2, ear_y - ear_size)
                ]
                draw.polygon(ear_points, fill=color, outline=None)
                
                # Right ear
                ear_x = int(center_x + head_size * 0.4)
                ear_points = [
                    (ear_x, ear_y),
                    (ear_x - ear_size//2, ear_y - ear_size),
                    (ear_x + ear_size//2, ear_y - ear_size)
                ]
                draw.polygon(ear_points, fill=color, outline=None)
    
    def _draw_simplified_head(self, draw: ImageDraw.Draw, animal_type: str, center_x: int, head_y: int,
                            head_size: int, color: Tuple[int, int, int], anatomy: dict, style_chars: dict):
        """Draw simplified head (for styles like Pop Art, Fauvism)."""
        x1 = max(0, min(center_x - head_size, self.width - 1))
        x2 = max(0, min(center_x + head_size, self.width - 1))
        y1 = max(0, min(head_y - head_size, self.height - 1))
        y2 = max(0, min(head_y + head_size, self.height - 1))
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
        
        # Simple eyes
        eye_size = head_size // 6
        eye_y = head_y
        eye_x1 = max(0, min(center_x - head_size//3 - eye_size, self.width - 1))
        eye_x2 = max(0, min(center_x - head_size//3 + eye_size, self.width - 1))
        eye_y1 = max(0, min(eye_y - eye_size, self.height - 1))
        eye_y2 = max(0, min(eye_y + eye_size, self.height - 1))
        if eye_x1 > eye_x2:
            eye_x1, eye_x2 = eye_x2, eye_x1
        if eye_y1 > eye_y2:
            eye_y1, eye_y2 = eye_y2, eye_y1
        draw.ellipse([eye_x1, eye_y1, eye_x2, eye_y2], fill=(0, 0, 0), outline=None)
        
        eye_x1 = max(0, min(center_x + head_size//3 - eye_size, self.width - 1))
        eye_x2 = max(0, min(center_x + head_size//3 + eye_size, self.width - 1))
        if eye_x1 > eye_x2:
            eye_x1, eye_x2 = eye_x2, eye_x1
        draw.ellipse([eye_x1, eye_y1, eye_x2, eye_y2], fill=(0, 0, 0), outline=None)
    
    def _draw_detailed_legs(self, draw: ImageDraw.Draw, animal_type: str, center_x: int, body_width: int,
                          leg_y: int, leg_width: int, leg_height: int, color: Tuple[int, int, int],
                          style_chars: dict):
        """Draw detailed legs with joints."""
        leg_positions = [
            center_x - body_width * 0.6,
            center_x - body_width * 0.2,
            center_x + body_width * 0.2,
            center_x + body_width * 0.6
        ]
        
        for leg_x in leg_positions:
            # Upper leg
            x1 = max(0, min(int(leg_x - leg_width//2), self.width - 1))
            x2 = max(0, min(int(leg_x + leg_width//2), self.width - 1))
            y1 = max(0, min(leg_y, self.height - 1))
            y2 = max(0, min(leg_y + leg_height//2, self.height - 1))
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
            
            # Lower leg (paw)
            paw_width = int(leg_width * 1.2)
            y1 = max(0, min(leg_y + leg_height//2, self.height - 1))
            y2 = max(0, min(leg_y + leg_height, self.height - 1))
            x1 = max(0, min(int(leg_x - paw_width//2), self.width - 1))
            x2 = max(0, min(int(leg_x + paw_width//2), self.width - 1))
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
    
    def _draw_simplified_legs(self, draw: ImageDraw.Draw, center_x: int, body_width: int,
                            leg_y: int, leg_width: int, leg_height: int, color: Tuple[int, int, int]):
        """Draw simplified legs."""
        leg_positions = [
            center_x - body_width//2,
            center_x + body_width//2
        ]
        
        for leg_x in leg_positions:
            x1 = max(0, min(leg_x - leg_width//2, self.width - 1))
            x2 = max(0, min(leg_x + leg_width//2, self.width - 1))
            y1 = max(0, min(leg_y, self.height - 1))
            y2 = max(0, min(leg_y + leg_height, self.height - 1))
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
    
    def _draw_tail(self, draw: ImageDraw.Draw, animal_type: str, center_x: int, body_y: int,
                  body_width: int, tail_length: int, color: Tuple[int, int, int], style_chars: dict):
        """Draw tail with style-appropriate technique."""
        tail_x = center_x + body_width
        tail_y = body_y
        tail_angle = random.uniform(-math.pi/4, math.pi/4)
        tail_end_x = int(tail_x + tail_length * math.cos(tail_angle))
        tail_end_y = int(tail_y + tail_length * math.sin(tail_angle))
        
        tail_width = tail_length // 4
        
        if style_chars['brushwork'] == 'visible_strokes':
            # Impressionism: broken tail
            for i in range(5):
                seg_x = int(tail_x + (tail_end_x - tail_x) * i / 5)
                seg_y = int(tail_y + (tail_end_y - tail_y) * i / 5)
                x1 = max(0, min(seg_x - tail_width//2, self.width - 1))
                x2 = max(0, min(seg_x + tail_width//2, self.width - 1))
                y1 = max(0, min(seg_y - tail_width//2, self.height - 1))
                y2 = max(0, min(seg_y + tail_width//2, self.height - 1))
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 > y2:
                    y1, y2 = y2, y1
                draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
        else:
            # Smooth tail
            tail_x1 = min(tail_x - tail_width, tail_end_x - tail_width)
            tail_x2 = max(tail_x + tail_width, tail_end_x + tail_width)
            tail_y1 = min(tail_y - tail_width, tail_end_y - tail_width)
            tail_y2 = max(tail_y + tail_width, tail_end_y + tail_width)
            
            tail_x1 = max(0, min(tail_x1, self.width - 1))
            tail_x2 = max(0, min(tail_x2, self.width - 1))
            tail_y1 = max(0, min(tail_y1, self.height - 1))
            tail_y2 = max(0, min(tail_y2, self.height - 1))
            
            if tail_x1 > tail_x2:
                tail_x1, tail_x2 = tail_x2, tail_x1
            if tail_y1 > tail_y2:
                tail_y1, tail_y2 = tail_y2, tail_y1
            
            draw.ellipse([tail_x1, tail_y1, tail_x2, tail_y2], fill=color, outline=None)
    
    def _add_micro_details(self, draw: ImageDraw.Draw, center_x: int, center_y: int,
                         width: int, height: int, color: Tuple[int, int, int], palette: List[Tuple[int, int, int]]):
        """Add micro-details for hyperrealism."""
        # Add texture points
        for _ in range(50):
            detail_x = center_x + random.randint(-width, width)
            detail_y = center_y + random.randint(-height, height)
            detail_color = random.choice(palette)
            detail_size = random.randint(1, 3)
            
            x1 = max(0, min(detail_x - detail_size, self.width - 1))
            x2 = max(0, min(detail_x + detail_size, self.width - 1))
            y1 = max(0, min(detail_y - detail_size, self.height - 1))
            y2 = max(0, min(detail_y + detail_size, self.height - 1))
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            draw.ellipse([x1, y1, x2, y2], fill=detail_color, outline=None)

