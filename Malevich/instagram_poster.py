"""
Модуль для постинга изображений в Instagram.
Использует instagrapi для работы с Instagram API.
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
    """Класс для постинга изображений в Instagram."""
    
    # Рекомендуемые размеры для Instagram
    INSTAGRAM_SIZES = {
        'square': (1080, 1080),      # Квадрат
        'portrait': (1080, 1350),    # Вертикаль (4:5)
        'landscape': (1080, 566),    # Горизонталь (1.91:1)
        'story': (1080, 1920),       # Stories (9:16)
    }
    
    def __init__(self, username: Optional[str] = None, password: Optional[str] = None):
        """
        Инициализация Instagram клиента.
        
        Args:
            username: Имя пользователя Instagram
            password: Пароль Instagram
        """
        if Client is None:
            raise ImportError(
                "instagrapi не установлен. Установите его: pip install instagrapi"
            )
        
        self.client = Client()
        self.username = username
        self.password = password
        self.is_logged_in = False
        
    def login(self, username: Optional[str] = None, password: Optional[str] = None,
              session_file: Optional[str] = None) -> bool:
        """
        Вход в Instagram.
        
        Args:
            username: Имя пользователя (если не указано при инициализации)
            password: Пароль (если не указан при инициализации)
            session_file: Путь к файлу сессии для сохранения
            
        Returns:
            True если вход успешен
        """
        username = username or self.username
        password = password or self.password
        
        if not username or not password:
            raise ValueError("Необходимо указать username и password")
        
        try:
            # Пытаемся загрузить сессию из файла
            if session_file and os.path.exists(session_file):
                try:
                    self.client.load_settings(session_file)
                    self.client.login(username, password)
                    logger.info("Вход выполнен с использованием сохраненной сессии")
                except Exception as e:
                    logger.warning(f"Не удалось загрузить сессию: {e}")
                    self.client.login(username, password)
            else:
                self.client.login(username, password)
            
            # Сохраняем сессию
            if session_file:
                self.client.dump_settings(session_file)
            
            self.is_logged_in = True
            self.username = username
            return True
            
        except ChallengeRequired:
            logger.error("Требуется двухфакторная аутентификация")
            raise
        except LoginRequired:
            logger.error("Ошибка входа. Проверьте логин и пароль")
            raise
        except Exception as e:
            logger.error(f"Ошибка при входе: {e}")
            raise
    
    def prepare_image_for_instagram(self, image_path: str, 
                                   format: str = 'square') -> str:
        """
        Подготавливает изображение для Instagram (изменяет размер).
        
        Args:
            image_path: Путь к исходному изображению
            format: Формат ('square', 'portrait', 'landscape', 'story')
            
        Returns:
            Путь к подготовленному изображению
        """
        if format not in self.INSTAGRAM_SIZES:
            raise ValueError(f"Неизвестный формат: {format}")
        
        target_size = self.INSTAGRAM_SIZES[format]
        
        # Открываем изображение
        image = Image.open(image_path)
        
        # Изменяем размер с сохранением пропорций и центрированием
        image.thumbnail(target_size, Image.Resampling.LANCZOS)
        
        # Создаем новое изображение нужного размера
        new_image = Image.new('RGB', target_size, (255, 255, 255))
        
        # Вставляем изображение по центру
        x = (target_size[0] - image.size[0]) // 2
        y = (target_size[1] - image.size[1]) // 2
        new_image.paste(image, (x, y))
        
        # Сохраняем подготовленное изображение
        output_path = image_path.replace('.jpg', f'_instagram_{format}.jpg')
        new_image.save(output_path, 'JPEG', quality=95)
        
        return output_path
    
    def post_image(self, image_path: str, caption: str = "", 
                   hashtags: Optional[List[str]] = None) -> bool:
        """
        Публикует изображение в Instagram.
        
        Args:
            image_path: Путь к изображению
            caption: Подпись к посту
            hashtags: Список хештегов
            
        Returns:
            True если публикация успешна
        """
        if not self.is_logged_in:
            raise RuntimeError("Необходимо войти в Instagram. Вызовите login()")
        
        # Добавляем хештеги к подписи
        if hashtags:
            hashtag_string = " ".join([f"#{tag}" for tag in hashtags])
            caption = f"{caption}\n\n{hashtag_string}" if caption else hashtag_string
        
        try:
            self.client.photo_upload(image_path, caption)
            logger.info(f"Изображение успешно опубликовано: {image_path}")
            return True
        except Exception as e:
            logger.error(f"Ошибка при публикации: {e}")
            raise
    
    def generate_hashtags(self, style: str = 'avantgarde') -> List[str]:
        """
        Генерирует релевантные хештеги для авангардного искусства.
        
        Args:
            style: Стиль изображения
            
        Returns:
            Список хештегов
        """
        base_hashtags = [
            'abstractart', 'contemporaryart', 'digitalart', 'modernart',
            'artwork', 'art', 'abstract', 'geometric', 'minimalist'
        ]
        
        style_hashtags = {
            'avantgarde': ['avantgarde', 'suprematism', 'constructivism', 'abstractexpressionism'],
            'geometric': ['geometricart', 'geometric', 'minimalism', 'lines'],
            'organic': ['organic', 'flow', 'fluid', 'nature'],
            'gradient': ['gradient', 'colorful', 'vibrant', 'color']
        }
        
        hashtags = base_hashtags.copy()
        if style in style_hashtags:
            hashtags.extend(style_hashtags[style])
        
        # Добавляем случайные дополнительные
        additional = [
            'artdaily', 'instaart', 'artgallery', 'artlovers',
            'creative', 'design', 'visualart', 'artistic'
        ]
        hashtags.extend(random.sample(additional, 3))
        
        return hashtags[:20]  # Instagram ограничивает до 30 хештегов, берем 20


# Утилита для работы без авторизации (только подготовка изображений)
class InstagramImagePreparer:
    """Утилита для подготовки изображений без авторизации в Instagram."""
    
    def __init__(self):
        self.sizes = InstagramPoster.INSTAGRAM_SIZES
    
    def prepare(self, image_path: str, format: str = 'square') -> str:
        """Подготавливает изображение для Instagram."""
        poster = InstagramPoster()
        return poster.prepare_image_for_instagram(image_path, format)

