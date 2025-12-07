"""
Module for posting images to Instagram.
Uses instagrapi for Instagram API interaction.
All documentation in English.
"""
import os
import logging
from typing import Optional, List
from pathlib import Path
from PIL import Image

try:
    from instagrapi import Client
    from instagrapi.exceptions import LoginRequired, ChallengeRequired
except ImportError:
    Client = None
    ChallengeRequired = None
    LoginRequired = None

logger = logging.getLogger(__name__)


class InstagramPoster:
    """Class for posting images to Instagram."""
    
    # Recommended sizes for Instagram
    INSTAGRAM_SIZES = {
        'square': (1080, 1080),      # Square
        'portrait': (1080, 1350),    # Vertical (4:5)
        'landscape': (1080, 566),    # Horizontal (1.91:1)
        'story': (1080, 1920),       # Stories (9:16)
    }
    
    def __init__(self, username: Optional[str] = None, password: Optional[str] = None):
        """
        Initialize Instagram client.
        
        Args:
            username: Instagram username
            password: Instagram password
        """
        if Client is None:
            raise ImportError(
                "instagrapi is not installed. Install it: pip install instagrapi"
            )
        
        self.client = Client()
        self.username = username
        self.password = password
        self.is_logged_in = False
        
    def login(self, username: Optional[str] = None, password: Optional[str] = None,
              session_file: Optional[str] = None) -> bool:
        """
        Login to Instagram.
        
        Args:
            username: Username (if not provided during initialization)
            password: Password (if not provided during initialization)
            session_file: Path to session file for saving
            
        Returns:
            True if login successful
        """
        username = username or self.username
        password = password or self.password
        
        if not username or not password:
            raise ValueError("Username and password must be provided")
        
        try:
            # Try to load session from file
            if session_file and os.path.exists(session_file):
                try:
                    self.client.load_settings(session_file)
                    self.client.login(username, password)
                    logger.info("Logged in using saved session")
                except Exception as e:
                    logger.warning(f"Failed to load session: {e}")
                    self.client.login(username, password)
            else:
                self.client.login(username, password)
            
            # Save session
            if session_file:
                self.client.dump_settings(session_file)
            
            self.is_logged_in = True
            self.username = username
            return True
            
        except ChallengeRequired:
            logger.error("Two-factor authentication required")
            raise
        except LoginRequired:
            logger.error("Login error. Check username and password")
            raise
        except Exception as e:
            logger.error(f"Error during login: {e}")
            raise
    
    def prepare_image_for_instagram(self, image_path: str, 
                                   format: str = 'square') -> str:
        """
        Prepare image for Instagram (resize to appropriate dimensions).
        
        Args:
            image_path: Path to source image
            format: Format ('square', 'portrait', 'landscape', 'story')
            
        Returns:
            Path to prepared image
        """
        if format not in self.INSTAGRAM_SIZES:
            raise ValueError(f"Unknown format: {format}")
        
        target_size = self.INSTAGRAM_SIZES[format]
        
        # Open image
        image = Image.open(image_path)
        
        # Resize with aspect ratio preservation and centering
        image.thumbnail(target_size, Image.Resampling.LANCZOS)
        
        # Create new image with target size
        new_image = Image.new('RGB', target_size, (255, 255, 255))
        
        # Paste image centered
        x = (target_size[0] - image.size[0]) // 2
        y = (target_size[1] - image.size[1]) // 2
        new_image.paste(image, (x, y))
        
        # Save prepared image
        output_path = image_path.replace('.jpg', f'_instagram_{format}.jpg')
        new_image.save(output_path, 'JPEG', quality=95)
        
        return output_path
    
    def post_image(self, image_path: str, caption: str = "", 
                   hashtags: Optional[List[str]] = None) -> bool:
        """
        Post image to Instagram.
        
        Args:
            image_path: Path to image
            caption: Post caption
            hashtags: List of hashtags
            
        Returns:
            True if post successful
        """
        if not self.is_logged_in:
            raise RuntimeError("Must login to Instagram. Call login()")
        
        # Add hashtags to caption
        if hashtags:
            hashtag_string = " ".join([f"#{tag}" for tag in hashtags])
            caption = f"{caption}\n\n{hashtag_string}" if caption else hashtag_string
        
        try:
            self.client.photo_upload(image_path, caption)
            logger.info(f"Image successfully posted: {image_path}")
            return True
        except Exception as e:
            logger.error(f"Error posting image: {e}")
            raise


# Utility for working without authentication (image preparation only)
class InstagramImagePreparer:
    """Utility for preparing images without Instagram authentication."""
    
    def __init__(self):
        self.sizes = InstagramPoster.INSTAGRAM_SIZES
    
    def prepare(self, image_path: str, format: str = 'square') -> str:
        """Prepare image for Instagram."""
        poster = InstagramPoster()
        return poster.prepare_image_for_instagram(image_path, format)
