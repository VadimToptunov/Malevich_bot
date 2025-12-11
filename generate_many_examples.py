"""
Generate a large number of examples in all available styles.
All documentation in English.
"""
import logging
from pathlib import Path
from Malevich.examples.generate_all import (
    generate_comprehensive_examples,
    generate_interdisciplinary_examples,
    generate_legacy_examples
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def generate_many_examples():
    """Generate many examples in all styles."""
    output_dir = Path('examples')
    output_dir.mkdir(exist_ok=True)
    
    logger.info("=" * 60)
    logger.info("Generating MANY examples in all styles...")
    logger.info("=" * 60)
    
    # Generate comprehensive styles - 10 examples per style (21 styles = 210 images)
    logger.info("\n📸 Generating Comprehensive Style Examples (10 per style)...")
    generate_comprehensive_examples(output_dir, count_per_style=10)
    
    # Generate interdisciplinary - 50 examples with various combinations
    logger.info("\n🔬 Generating Interdisciplinary Examples (50 examples)...")
    generate_interdisciplinary_examples(output_dir, count=50)
    
    # Generate legacy - 20 examples each
    logger.info("\n🎨 Generating Legacy Examples (20 each)...")
    generate_legacy_examples(output_dir, count=20)
    
    logger.info("\n" + "=" * 60)
    logger.info("✅ Generation complete!")
    logger.info(f"📁 All images saved to: {output_dir.absolute()}")
    logger.info("=" * 60)


if __name__ == "__main__":
    generate_many_examples()

