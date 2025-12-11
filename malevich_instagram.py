"""
Main script for generating avant-garde images and posting them to Instagram.
Supports multiple art styles: cubism, expressionism, surrealism, and more.
All documentation in English.
"""
import os
import logging
import random
from pathlib import Path
from typing import Optional

from Malevich.generators import ComprehensiveStyleGenerator
from Malevich.social import CaptionGenerator, InstagramPoster, PostScheduler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration from environment variables
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
SESSION_FILE = os.getenv('INSTAGRAM_SESSION_FILE', '.instagram_session.json')

# Create output directory for images
OUTPUT_DIR = Path('generated_images')
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_and_post(style: Optional[str] = None,
                      palette: Optional[str] = None,
                      format: str = 'square',
                      auto_post: bool = False) -> str:
    """
    Generate an avant-garde image and optionally post it to Instagram.
    
    Args:
        style: Art style ('cubism', 'expressionism', 'surrealism', 
               'fragmented', 'intense', 'hybrid', 'auto')
        palette: Palette name from ART_PALETTES
        format: Instagram format ('square', 'portrait', 'landscape', 'story')
        auto_post: Automatically post to Instagram
        
    Returns:
        Path to generated image file
    """
    # Generate image
    logger.info(f"Generating image (style: {style or 'auto'}, palette: {palette or 'auto'})")
    generator = ComprehensiveStyleGenerator(width=1080, height=1080)
    image = generator.generate(style=style or 'auto', palette_name=palette)
    
    # Save image
    filename = f"avantgarde_{random.randint(10000, 99999)}.jpg"
    filepath = OUTPUT_DIR / filename
    image.save(filepath, 'JPEG', quality=95)
    logger.info(f"Image saved: {filepath}")
    
    if auto_post:
        # Post to Instagram
        if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
            logger.warning("Instagram credentials not configured. Skipping post.")
            return str(filepath)
        
        try:
            poster = InstagramPoster(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
            
            # Login to Instagram
            if not poster.is_logged_in:
                poster.login(session_file=SESSION_FILE)
            
            # Prepare image for Instagram
            instagram_path = poster.prepare_image_for_instagram(str(filepath), format)
            
            # Generate caption and hashtags using caption generator
            caption_gen = CaptionGenerator()
            caption, hashtags = caption_gen.generate_full_post(style=style)
            
            # Post to Instagram
            poster.post_image(instagram_path, caption, hashtags)
            logger.info("Image successfully posted to Instagram")
            
        except Exception as e:
            logger.error(f"Error posting to Instagram: {e}")
            raise
    
    return str(filepath)


def setup_auto_posting(times: Optional[list] = None, 
                      interval_hours: Optional[int] = None):
    """
    Set up automatic posting schedule.
    
    Args:
        times: List of posting times (e.g., ["09:00", "18:00"])
        interval_hours: Interval between posts in hours
    """
    if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
        logger.error("INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD must be configured")
        return
    
    def post_job():
        """Job function for scheduler."""
        generate_and_post(auto_post=True)
    
    scheduler = PostScheduler(
        post_function=post_job,
        times=times,
        interval_hours=interval_hours
    )
    
    logger.info("Automatic posting configured. Starting scheduler...")
    scheduler.start()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "generate":
            # Generate one image
            style = sys.argv[2] if len(sys.argv) > 2 else None
            generate_and_post(style=style, auto_post=False)
        
        elif command == "post":
            # Generate and post one image
            style = sys.argv[2] if len(sys.argv) > 2 else None
            generate_and_post(style=style, auto_post=True)
        
        elif command == "schedule":
            # Start scheduler
            times = None
            if len(sys.argv) > 2:
                times = sys.argv[2].split(',')
            setup_auto_posting(times=times)
        
        else:
            print("Usage:")
            print("  python malevich_instagram.py generate [style]  - generate image")
            print("  python malevich_instagram.py post [style]       - generate and post")
            print("  python malevich_instagram.py schedule [times]    - start scheduler")
            print("\nStyles: cubism, expressionism, surrealism, fragmented, intense, hybrid, auto")
    else:
        # Default: generate one image
        generate_and_post(auto_post=False)
        print(f"\nImage saved to {OUTPUT_DIR}")
