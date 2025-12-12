"""
Art Knowledge Base - Comprehensive understanding of world art styles and techniques.
This module contains knowledge about various art movements, their characteristics,
techniques, and how to apply them in procedural generation.
All documentation in English.
"""
from typing import Dict, List, Tuple, Optional
import random
import math


class ArtKnowledgeBase:
    """
    Knowledge base containing information about world art styles, techniques,
    and characteristics for procedural art generation.
    """
    
    # Art movement characteristics
    ART_MOVEMENTS: Dict[str, Dict] = {
        'realism': {
            'proportions': 'natural',
            'anatomy': 'accurate',
            'lighting': 'natural',
            'color_usage': 'true_to_life',
            'detail_level': 'high',
            'brushwork': 'smooth',
            'perspective': 'linear',
            'texture': 'realistic'
        },
        'hyperrealism': {
            'proportions': 'photographic',
            'anatomy': 'extremely_accurate',
            'lighting': 'photographic',
            'color_usage': 'vibrant_natural',
            'detail_level': 'extreme',
            'brushwork': 'invisible',
            'perspective': 'photographic',
            'texture': 'micro_detail'
        },
        'impressionism': {
            'proportions': 'suggested',
            'anatomy': 'loose',
            'lighting': 'light_effects',
            'color_usage': 'broken_color',
            'detail_level': 'medium',
            'brushwork': 'visible_strokes',
            'perspective': 'atmospheric',
            'texture': 'brush_marks'
        },
        'expressionism': {
            'proportions': 'distorted',
            'anatomy': 'exaggerated',
            'lighting': 'dramatic',
            'color_usage': 'emotional',
            'detail_level': 'low',
            'brushwork': 'bold',
            'perspective': 'distorted',
            'texture': 'rough'
        },
        'cubism': {
            'proportions': 'geometric',
            'anatomy': 'fragmented',
            'lighting': 'multiple_angles',
            'color_usage': 'muted',
            'detail_level': 'medium',
            'brushwork': 'flat',
            'perspective': 'multiple_viewpoints',
            'texture': 'flat'
        },
        'pop_art': {
            'proportions': 'simplified',
            'anatomy': 'stylized',
            'lighting': 'flat',
            'color_usage': 'bold_saturated',
            'detail_level': 'low',
            'brushwork': 'smooth',
            'perspective': 'flat',
            'texture': 'ben_day_dots'
        },
        'fauvism': {
            'proportions': 'simplified',
            'anatomy': 'stylized',
            'lighting': 'color_based',
            'color_usage': 'wild_unrealistic',
            'detail_level': 'low',
            'brushwork': 'bold',
            'perspective': 'simplified',
            'texture': 'color_fields'
        }
    }
    
    # Animal anatomy reference - proportions based on real animals
    ANIMAL_ANATOMY: Dict[str, Dict] = {
        'cat': {
            'body_ratio': (1.0, 1.5),  # width, height
            'head_ratio': 0.4,  # head size relative to body width
            'ear_shape': 'triangular',
            'ear_size': 0.3,
            'tail_length': 1.2,
            'leg_proportions': (0.15, 0.5),  # width, height relative to body
            'eye_position': (0.3, 0.4),  # relative to head
            'nose_position': (0.5, 0.6)
        },
        'dog': {
            'body_ratio': (1.0, 1.6),
            'head_ratio': 0.45,
            'ear_shape': 'varied',
            'ear_size': 0.35,
            'tail_length': 1.0,
            'leg_proportions': (0.18, 0.55),
            'eye_position': (0.3, 0.4),
            'nose_position': (0.5, 0.65)
        },
        'bird': {
            'body_ratio': (1.5, 0.5),  # wider, flatter
            'head_ratio': 0.3,
            'wing_size': 1.2,
            'beak_size': 0.3,
            'tail_length': 0.8,
            'leg_proportions': (0.1, 0.3)
        },
        'horse': {
            'body_ratio': (1.3, 1.1),
            'head_ratio': 0.5,
            'neck_length': 0.8,
            'leg_proportions': (0.12, 1.0),  # long legs
            'mane_length': 0.6,
            'tail_length': 1.0
        },
        'lion': {
            'body_ratio': (1.2, 1.3),
            'head_ratio': 0.6,
            'mane_size': 1.4,
            'leg_proportions': (0.14, 0.7),
            'tail_length': 0.9,
            'eye_color': (255, 200, 0)
        },
        'tiger': {
            'body_ratio': (1.1, 1.3),
            'head_ratio': 0.55,
            'stripes': True,
            'leg_proportions': (0.13, 0.65),
            'tail_length': 1.0
        },
        'elephant': {
            'body_ratio': (1.4, 1.2),
            'head_ratio': 0.7,
            'ear_size': 1.0,
            'trunk_length': 0.8,
            'leg_proportions': (0.2, 1.0),  # thick, long
            'tail_length': 0.6
        },
        'bear': {
            'body_ratio': (1.3, 1.2),
            'head_ratio': 0.6,
            'ear_size': 0.25,
            'leg_proportions': (0.22, 0.8),
            'tail_length': 0.3
        },
        'rabbit': {
            'body_ratio': (0.9, 1.2),
            'head_ratio': 0.5,
            'ear_size': 0.6,  # very long ears
            'leg_proportions': (0.12, 0.4),
            'tail_length': 0.2
        },
        'fox': {
            'body_ratio': (1.0, 1.3),
            'head_ratio': 0.45,
            'ear_size': 0.4,
            'tail_length': 1.3,  # bushy tail
            'leg_proportions': (0.12, 0.5)
        },
        'wolf': {
            'body_ratio': (1.1, 1.4),
            'head_ratio': 0.5,
            'ear_size': 0.35,
            'tail_length': 1.1,
            'leg_proportions': (0.13, 0.6)
        },
        'deer': {
            'body_ratio': (1.2, 1.0),
            'head_ratio': 0.5,
            'antler_size': 0.8,
            'leg_proportions': (0.1, 1.0),
            'tail_length': 0.4
        }
    }
    
    @staticmethod
    def get_style_characteristics(style: str) -> Dict:
        """Get characteristics for a specific art style."""
        return ArtKnowledgeBase.ART_MOVEMENTS.get(style, ArtKnowledgeBase.ART_MOVEMENTS['realism'])
    
    @staticmethod
    def get_animal_anatomy(animal_type: str) -> Dict:
        """Get anatomical proportions for a specific animal."""
        return ArtKnowledgeBase.ANIMAL_ANATOMY.get(animal_type, ArtKnowledgeBase.ANIMAL_ANATOMY['cat'])
    
    @staticmethod
    def apply_style_to_proportions(proportions: Tuple[float, float], style: str) -> Tuple[float, float]:
        """Apply style characteristics to animal proportions."""
        characteristics = ArtKnowledgeBase.get_style_characteristics(style)
        
        if characteristics['proportions'] == 'distorted':
            # Expressionism: exaggerate
            return (proportions[0] * random.uniform(0.8, 1.3), proportions[1] * random.uniform(0.8, 1.3))
        elif characteristics['proportions'] == 'geometric':
            # Cubism: simplify to geometric shapes
            return (round(proportions[0]), round(proportions[1]))
        elif characteristics['proportions'] == 'simplified':
            # Pop art, Fauvism: simplify
            return (proportions[0] * 0.9, proportions[1] * 0.9)
        elif characteristics['proportions'] == 'photographic':
            # Hyperrealism: very precise
            return proportions
        else:
            # Realism, natural: keep as is
            return proportions
    
    @staticmethod
    def get_detail_level(style: str) -> str:
        """Get detail level for a style."""
        return ArtKnowledgeBase.get_style_characteristics(style).get('detail_level', 'medium')
    
    @staticmethod
    def should_use_anatomy(style: str) -> bool:
        """Determine if accurate anatomy should be used."""
        characteristics = ArtKnowledgeBase.get_style_characteristics(style)
        anatomy = characteristics.get('anatomy', 'accurate')
        return anatomy in ['accurate', 'extremely_accurate']
    
    @staticmethod
    def get_lighting_technique(style: str) -> str:
        """Get lighting technique for a style."""
        return ArtKnowledgeBase.get_style_characteristics(style).get('lighting', 'natural')

