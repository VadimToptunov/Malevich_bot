"""
Script to generate example images for all art styles.
All documentation in English.
"""
import logging
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


def generate_all_examples():
    """Generate example images for all art styles."""
    generator = MasterGenerator(width=1080, height=1080)
    
    logger.info("Starting generation of example images for all styles...")
    
    for style in STYLES:
        logger.info(f"Generating {style} style image...")
        try:
            image = generator.generate(style=style, palette_name=None)
            filename = f"example_{style}.jpg"
            filepath = OUTPUT_DIR / filename
            image.save(filepath, 'JPEG', quality=95)
            logger.info(f"✓ Saved: {filepath}")
        except Exception as e:
            logger.error(f"✗ Error generating {style}: {e}")
    
    logger.info(f"\nAll examples generated in: {OUTPUT_DIR.absolute()}")
    logger.info(f"Generated {len(STYLES)} example images")


if __name__ == "__main__":
    generate_all_examples()

