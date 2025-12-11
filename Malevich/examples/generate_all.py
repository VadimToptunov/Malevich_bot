"""
Unified script to generate example images for all art styles and generators.
All documentation in English.
"""
import logging
import random
from pathlib import Path
from typing import Optional

from Malevich.generators import ComprehensiveStyleGenerator, InterdisciplinaryGenerator
from Malevich.generators import Magnet, AvantGuard

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# All available styles from ComprehensiveStyleGenerator
COMPREHENSIVE_STYLES = [
    'hyperrealism', 'photorealism', 'minimalism', 'pop_art', 'op_art',
    'fauvism', 'futurism', 'dadaism', 'constructivism', 'de_stijl',
    'art_deco', 'art_nouveau', 'neoclassicism', 'romanticism', 'realism',
    'naturalism', 'mannerism', 'rococo', 'classicism', 'symbolism',
    'precisionism'
]


def generate_comprehensive_examples(output_dir: Path, count_per_style: int = 3):
    """Generate examples using ComprehensiveStyleGenerator."""
    generator = ComprehensiveStyleGenerator(width=1080, height=1080)
    
    logger.info(f"Generating comprehensive style examples...")
    total = 0
    
    for style in COMPREHENSIVE_STYLES:
        for i in range(count_per_style):
            try:
                image = generator.generate(style=style)
                filename = f"comprehensive_{style}_{i+1:02d}.jpg"
                filepath = output_dir / filename
                image.save(filepath, 'JPEG', quality=95)
                total += 1
                logger.info(f"  ✓ {filename}")
            except Exception as e:
                logger.error(f"  ✗ Error generating {style}: {e}")
    
    logger.info(f"Generated {total} comprehensive style images")


def generate_interdisciplinary_examples(output_dir: Path, count: int = 10):
    """Generate examples using InterdisciplinaryGenerator."""
    generator = InterdisciplinaryGenerator(width=1080, height=1080)
    
    logger.info(f"Generating interdisciplinary examples...")
    total = 0
    
    emotions = ['gratitude', 'anger', 'joy', 'fear', 'love', 'sadness', 'calm', 'energy', 'mystery']
    psychiatric = ['schizophrenia', 'synesthesia', 'hallucination', None]
    physiological = ['protanopia', 'deuteranopia', 'tritanopia', 'achromatopsia', 'agnosia', None]
    math_patterns = ['mandelbrot', 'julia', 'penrose', 'chaos', None]
    physics = ['quantum', 'interference', 'diffraction', 'relativity', None]
    chemistry = ['molecule', 'crystal', 'reaction', 'fluorescence', None]
    
    for i in range(count):
        try:
            image = generator.generate(
                emotion=random.choice(emotions) if random.random() < 0.5 else None,
                psychiatric_filter=random.choice(psychiatric),
                physiological_filter=random.choice(physiological),
                math_pattern=random.choice(math_patterns),
                physics_concept=random.choice(physics),
                chemistry_concept=random.choice(chemistry),
                use_marketing=random.random() < 0.7,
                complexity=random.uniform(0.3, 0.9)
            )
            filename = f"interdisciplinary_{i+1:03d}.jpg"
            filepath = output_dir / filename
            image.save(filepath, 'JPEG', quality=95)
            total += 1
            logger.info(f"  ✓ {filename}")
        except Exception as e:
            logger.error(f"  ✗ Error generating interdisciplinary {i+1}: {e}")
    
    logger.info(f"Generated {total} interdisciplinary images")


def generate_legacy_examples(output_dir: Path, count: int = 5):
    """Generate examples using legacy generators (Magnet, AvantGuard)."""
    logger.info(f"Generating legacy examples...")
    total = 0
    
    # Magnet examples
    magnet = Magnet(1080, 1080)
    for i in range(count):
        try:
            filepath = magnet.create_image()
            # Move to output directory
            from pathlib import Path as PathLib
            src = PathLib(filepath)
            dst = output_dir / f"magnet_{i+1:02d}.jpg"
            if src.exists():
                import shutil
                shutil.move(str(src), str(dst))
                total += 1
                logger.info(f"  ✓ magnet_{i+1:02d}.jpg")
        except Exception as e:
            logger.error(f"  ✗ Error generating magnet {i+1}: {e}")
    
    # AvantGuard examples
    ag = AvantGuard()
    for i in range(count):
        try:
            image = ag.generate_image(1080, 1080, 
                                    random.choice([True, False]),
                                    random.choice([True, False]),
                                    random.choice([True, False]),
                                    random.choice([True, False]),
                                    random.choice([True, False]))
            filename = f"avantguard_{i+1:02d}.jpg"
            filepath = output_dir / filename
            image.save(filepath, 'JPEG', quality=95)
            total += 1
            logger.info(f"  ✓ {filename}")
        except Exception as e:
            logger.error(f"  ✗ Error generating avantguard {i+1}: {e}")
    
    logger.info(f"Generated {total} legacy images")


def generate_all_examples(output_dir: Optional[Path] = None,
                         comprehensive: bool = True,
                         interdisciplinary: bool = True,
                         legacy: bool = False,
                         count_per_style: int = 3,
                         interdisciplinary_count: int = 10,
                         legacy_count: int = 5):
    """
    Generate all example images.
    
    Args:
        output_dir: Output directory (default: examples/)
        comprehensive: Generate comprehensive style examples
        interdisciplinary: Generate interdisciplinary examples
        legacy: Generate legacy generator examples
        count_per_style: Number of images per comprehensive style
        interdisciplinary_count: Number of interdisciplinary images
        legacy_count: Number of legacy images
    """
    if output_dir is None:
        output_dir = Path('examples')
    output_dir.mkdir(exist_ok=True)
    
    logger.info(f"Starting example generation...")
    logger.info(f"Output directory: {output_dir.absolute()}")
    
    if comprehensive:
        generate_comprehensive_examples(output_dir, count_per_style)
    
    if interdisciplinary:
        generate_interdisciplinary_examples(output_dir, interdisciplinary_count)
    
    if legacy:
        generate_legacy_examples(output_dir, legacy_count)
    
    logger.info(f"\n{'='*60}")
    logger.info(f"Example generation complete!")
    logger.info(f"Location: {output_dir.absolute()}")


if __name__ == "__main__":
    import sys
    
    # Parse command line arguments
    comprehensive = '--no-comprehensive' not in sys.argv
    interdisciplinary = '--no-interdisciplinary' not in sys.argv
    legacy = '--legacy' in sys.argv
    
    generate_all_examples(
        comprehensive=comprehensive,
        interdisciplinary=interdisciplinary,
        legacy=legacy
    )

