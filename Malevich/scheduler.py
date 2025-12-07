"""
Планировщик для автоматической публикации постов в Instagram.
"""
import schedule
import time
import logging
from datetime import datetime
from typing import Optional, Callable
from pathlib import Path

logger = logging.getLogger(__name__)


class PostScheduler:
    """Планировщик постов в Instagram."""
    
    def __init__(self, post_function: Callable, 
                 times: Optional[list] = None,
                 interval_hours: Optional[int] = None):
        """
        Инициализация планировщика.
        
        Args:
            post_function: Функция для публикации поста (должна принимать 0 аргументов)
            times: Список времени для публикации (формат "HH:MM"), например ["09:00", "18:00"]
            interval_hours: Интервал между постами в часах (если не указаны times)
        """
        self.post_function = post_function
        self.times = times or []
        self.interval_hours = interval_hours
        self.running = False
        
        self._setup_schedule()
    
    def _setup_schedule(self):
        """Настраивает расписание."""
        if self.times:
            for time_str in self.times:
                schedule.every().day.at(time_str).do(self._safe_post)
                logger.info(f"Запланирован пост на {time_str}")
        elif self.interval_hours:
            schedule.every(self.interval_hours).hours.do(self._safe_post)
            logger.info(f"Запланирован пост каждые {self.interval_hours} часов")
        else:
            # По умолчанию: 2 раза в день в 10:00 и 20:00
            schedule.every().day.at("10:00").do(self._safe_post)
            schedule.every().day.at("20:00").do(self._safe_post)
            logger.info("Используется расписание по умолчанию: 10:00 и 20:00")
    
    def _safe_post(self):
        """Безопасный вызов функции постинга с обработкой ошибок."""
        try:
            logger.info(f"Запуск запланированного поста в {datetime.now()}")
            self.post_function()
            logger.info("Пост успешно опубликован")
        except Exception as e:
            logger.error(f"Ошибка при публикации поста: {e}")
    
    def start(self, check_interval: int = 60):
        """
        Запускает планировщик.
        
        Args:
            check_interval: Интервал проверки расписания в секундах
        """
        self.running = True
        logger.info("Планировщик запущен")
        
        while self.running:
            schedule.run_pending()
            time.sleep(check_interval)
    
    def stop(self):
        """Останавливает планировщик."""
        self.running = False
        logger.info("Планировщик остановлен")
    
    def run_once(self):
        """Запускает один пост немедленно (для тестирования)."""
        self._safe_post()


def create_scheduler_from_config(post_function: Callable, config: dict) -> PostScheduler:
    """
    Создает планировщик из конфигурационного словаря.
    
    Args:
        post_function: Функция для публикации
        config: Словарь с настройками:
            - times: список времени
            - interval_hours: интервал в часах
    
    Returns:
        PostScheduler объект
    """
    return PostScheduler(
        post_function=post_function,
        times=config.get('times'),
        interval_hours=config.get('interval_hours')
    )

