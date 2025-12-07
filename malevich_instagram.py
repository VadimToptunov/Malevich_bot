"""
Основной скрипт для генерации и публикации авангардных изображений в Instagram.
"""
import os
import logging
import random
from pathlib import Path
from typing import Optional

from Malevich.refined_generator import RefinedGenerator
from Malevich.instagram_poster import InstagramPoster, InstagramImagePreparer
from Malevich.scheduler import PostScheduler

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Конфигурация
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
SESSION_FILE = os.getenv('INSTAGRAM_SESSION_FILE', '.instagram_session.json')

# Создаем директорию для изображений
OUTPUT_DIR = Path('generated_images')
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_and_post(style: Optional[str] = None, 
                      palette: Optional[str] = None,
                      format: str = 'square',
                      auto_post: bool = False) -> str:
    """
    Генерирует изображение и опционально публикует его в Instagram.
    
    Args:
        style: Стиль генерации ('geometric', 'organic', 'gradient', 'hybrid', 'auto')
        palette: Название палитры
        format: Формат для Instagram ('square', 'portrait', 'landscape')
        auto_post: Автоматически опубликовать в Instagram
        
    Returns:
        Путь к сгенерированному изображению
    """
    # Генерируем изображение
    logger.info(f"Генерация изображения (стиль: {style or 'auto'}, палитра: {palette or 'auto'})")
    generator = RefinedGenerator(width=1080, height=1080)
    image = generator.generate(style=style or 'auto', palette_name=palette)
    
    # Сохраняем изображение
    filename = f"malevich_{random.randint(1000, 9999)}.jpg"
    filepath = OUTPUT_DIR / filename
    image.save(filepath, 'JPEG', quality=95)
    logger.info(f"Изображение сохранено: {filepath}")
    
    if auto_post:
        # Публикуем в Instagram
        if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
            logger.warning("Instagram credentials не настроены. Пропускаем публикацию.")
            return str(filepath)
        
        try:
            poster = InstagramPoster(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
            
            # Входим в Instagram
            if not poster.is_logged_in:
                poster.login(session_file=SESSION_FILE)
            
            # Подготавливаем изображение
            instagram_path = poster.prepare_image_for_instagram(str(filepath), format)
            
            # Генерируем подпись и хештеги
            captions = [
                "Абстрактная композиция в стиле авангарда",
                "Геометрические формы и чистые цвета",
                "Современная интерпретация супрематизма",
                "Минималистичная абстракция",
                "Игра форм и цветов"
            ]
            caption = random.choice(captions)
            hashtags = poster.generate_hashtags(style or 'avantgarde')
            
            # Публикуем
            poster.post_image(instagram_path, caption, hashtags)
            logger.info("Изображение успешно опубликовано в Instagram")
            
        except Exception as e:
            logger.error(f"Ошибка при публикации в Instagram: {e}")
    
    return str(filepath)


def setup_auto_posting(times: Optional[list] = None, interval_hours: Optional[int] = None):
    """
    Настраивает автоматическую публикацию постов.
    
    Args:
        times: Список времени для публикации (например, ["09:00", "18:00"])
        interval_hours: Интервал между постами в часах
    """
    if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
        logger.error("Необходимо настроить INSTAGRAM_USERNAME и INSTAGRAM_PASSWORD")
        return
    
    def post_job():
        """Задача для планировщика."""
        generate_and_post(auto_post=True)
    
    scheduler = PostScheduler(
        post_function=post_job,
        times=times,
        interval_hours=interval_hours
    )
    
    logger.info("Автоматическая публикация настроена. Запуск планировщика...")
    scheduler.start()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "generate":
            # Генерируем одно изображение
            style = sys.argv[2] if len(sys.argv) > 2 else None
            generate_and_post(style=style, auto_post=False)
        
        elif command == "post":
            # Генерируем и публикуем одно изображение
            style = sys.argv[2] if len(sys.argv) > 2 else None
            generate_and_post(style=style, auto_post=True)
        
        elif command == "schedule":
            # Запускаем планировщик
            times = None
            if len(sys.argv) > 2:
                times = sys.argv[2].split(',')
            setup_auto_posting(times=times)
        
        else:
            print("Использование:")
            print("  python malevich_instagram.py generate [style]  - сгенерировать изображение")
            print("  python malevich_instagram.py post [style]      - сгенерировать и опубликовать")
            print("  python malevich_instagram.py schedule [times]   - запустить планировщик")
            print("\nСтили: geometric, organic, gradient, hybrid, auto")
    else:
        # По умолчанию генерируем одно изображение
        generate_and_post(auto_post=False)
        print(f"\nИзображение сохранено в {OUTPUT_DIR}")

