"""
Malevich Bot - Advanced art generation system.
All documentation in English.
"""
from Malevich.generators import (
    ComprehensiveStyleGenerator,
    InterdisciplinaryGenerator,
    Magnet,
    AvantGuard
)
from Malevich.social import (
    CaptionGenerator,
    InstagramPoster,
    InstagramImagePreparer,
    PostScheduler,
    create_scheduler_from_config
)
from Malevich.utils import Tech, AdvancedColorSystem

__all__ = [
    # Generators
    'ComprehensiveStyleGenerator',
    'InterdisciplinaryGenerator',
    'Magnet',
    'AvantGuard',
    # Social
    'CaptionGenerator',
    'InstagramPoster',
    'InstagramImagePreparer',
    'PostScheduler',
    'create_scheduler_from_config',
    # Utils
    'Tech',
    'AdvancedColorSystem',
]

__version__ = '2.0.0'
