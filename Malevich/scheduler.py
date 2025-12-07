"""
Scheduler for automatic Instagram post publishing.
All documentation in English.
"""
import schedule
import time
import logging
from datetime import datetime
from typing import Optional, Callable
from pathlib import Path

logger = logging.getLogger(__name__)


class PostScheduler:
    """Scheduler for Instagram posts."""
    
    def __init__(self, post_function: Callable, 
                 times: Optional[list] = None,
                 interval_hours: Optional[int] = None):
        """
        Initialize scheduler.
        
        Args:
            post_function: Function to execute for posting (should take 0 arguments)
            times: List of posting times (format "HH:MM"), e.g., ["09:00", "18:00"]
            interval_hours: Interval between posts in hours (if times not provided)
        """
        self.post_function = post_function
        self.times = times or []
        self.interval_hours = interval_hours
        self.running = False
        
        self._setup_schedule()
    
    def _setup_schedule(self):
        """Set up schedule."""
        if self.times:
            for time_str in self.times:
                schedule.every().day.at(time_str).do(self._safe_post)
                logger.info(f"Scheduled post at {time_str}")
        elif self.interval_hours:
            schedule.every(self.interval_hours).hours.do(self._safe_post)
            logger.info(f"Scheduled post every {self.interval_hours} hours")
        else:
            # Default: 2 times per day at 10:00 and 20:00
            schedule.every().day.at("10:00").do(self._safe_post)
            schedule.every().day.at("20:00").do(self._safe_post)
            logger.info("Using default schedule: 10:00 and 20:00")
    
    def _safe_post(self):
        """Safely execute post function with error handling."""
        try:
            logger.info(f"Running scheduled post at {datetime.now()}")
            self.post_function()
            logger.info("Post successfully published")
        except Exception as e:
            logger.error(f"Error publishing post: {e}")
    
    def start(self, check_interval: int = 60):
        """
        Start scheduler.
        
        Args:
            check_interval: Schedule check interval in seconds
        """
        self.running = True
        logger.info("Scheduler started")
        
        while self.running:
            schedule.run_pending()
            time.sleep(check_interval)
    
    def stop(self):
        """Stop scheduler."""
        self.running = False
        logger.info("Scheduler stopped")
    
    def run_once(self):
        """Run one post immediately (for testing)."""
        self._safe_post()


def create_scheduler_from_config(post_function: Callable, config: dict) -> PostScheduler:
    """
    Create scheduler from configuration dictionary.
    
    Args:
        post_function: Function for posting
        config: Dictionary with settings:
            - times: list of times
            - interval_hours: interval in hours
    
    Returns:
        PostScheduler object
    """
    return PostScheduler(
        post_function=post_function,
        times=config.get('times'),
        interval_hours=config.get('interval_hours')
    )
