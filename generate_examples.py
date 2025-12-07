"""
Script to generate example images for all art styles.
All documentation in English.
"""
import logging
import random
from pathlib import Path
from Malevich.master_generator import MasterGenerator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create output directory
OUTPUT_DIR = Path('examples')
OUTPUT_DIR.mkdir(exist_ok=True)

# All available styles based on famous artists
STYLES = [
    'renaissance', 'baroque', 'impressionist', 'post_impressionist',
    'cubist', 'surrealist', 'suprematist', 'abstract_expressionist', 'expressionist'
]


def generate_all_examples(count: int = 50):
    """
    Generate example images for all art styles.
    
    Args:
        count: Number of images to generate (default: 50)
    """
    generator = MasterGenerator(width=1080, height=1080)
    
    logger.info(f"Starting generation of {count} example images...")
    
    generated = 0
    errors = 0
    
    for i in range(count):
        # Randomly select a style
        style = random.choice(STYLES)
        logger.info(f"Generating image {i+1}/{count} ({style} style)...")
        try:
            image = generator.generate(style=style, palette_name=None)
            filename = f"example_{i+1:03d}_{style}.jpg"
            filepath = OUTPUT_DIR / filename
            image.save(filepath, 'JPEG', quality=95)
            generated += 1
            logger.info(f"✓ Saved: {filepath}")
        except Exception as e:
            errors += 1
            logger.error(f"✗ Error generating {style}: {e}")
    
    logger.info(f"\nGeneration complete!")
    logger.info(f"Generated: {generated} images")
    logger.info(f"Errors: {errors}")
    logger.info(f"Location: {OUTPUT_DIR.absolute()}")


if __name__ == "__main__":
    generate_all_examples()

