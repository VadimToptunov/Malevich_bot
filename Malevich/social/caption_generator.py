"""
Caption generator for Instagram posts with wordplay, surreal meanings,
and artistic references. All in English.
"""
import random
from typing import List, Optional


class CaptionGenerator:
    """
    Generates creative, surreal captions with wordplay for Instagram posts.
    Inspired by avant-garde art movements and artistic expression.
    """
    
    # Surreal, poetic phrases with unexpected combinations
    SURREAL_PHRASES = [
        "where geometry meets the void",
        "colors that dream in fragments",
        "the shape of thoughts unspoken",
        "reality folded into itself",
        "time melts in geometric patterns",
        "the space between perception and truth",
        "where lines lose their meaning",
        "a canvas of fractured memories",
        "the geometry of the impossible",
        "colors that speak in angles",
        "where form becomes feeling",
        "the mathematics of emotion",
        "shapes that remember differently",
        "the architecture of dreams",
        "where perspective breaks free",
        "colors that think in curves",
        "the geometry of silence",
        "where reality takes a different angle",
        "the shape of what could be",
        "colors that question their existence",
        # Unexpected combinations - abstract meets concrete
        "the sound of a triangle breaking",
        "where circles learn to cry",
        "squares having an existential crisis",
        "rectangles in love with infinity",
        "the taste of blue geometry",
        "where numbers feel lonely",
        "the weight of a color",
        "shapes that smell like memories",
        # Mathematical meets emotional
        "the calculus of heartbreak",
        "differential equations of desire",
        "where algebra meets anxiety",
        "the integral of all feelings",
        "fractals of forgotten conversations",
        "the logarithm of loneliness",
        "vectors pointing to nowhere",
        # Time meets space
        "yesterday's tomorrow in today's colors",
        "where past and future collide geometrically",
        "the present moment as a broken line",
        "eternity compressed into a square",
        "time zones in a single point",
        "the speed of light slowed to a crawl",
        # Physical meets metaphysical
        "gravity defying its own rules",
        "where matter becomes thought",
        "the density of a dream",
        "solid air and liquid stone",
        "the temperature of an idea",
        "where physics takes a coffee break",
        # Organic meets geometric
        "circles growing like plants",
        "where nature learns geometry",
        "the photosynthesis of shapes",
        "trees that think in straight lines",
        "flowers blooming in perfect squares",
        # Technology meets emotion
        "where algorithms feel nostalgia",
        "the pixel density of a memory",
        "code that dreams in color",
        "where binary meets the infinite",
        "the resolution of a feeling"
    ]
    
    # Wordplay and puns with unexpected twists
    WORDPLAY_PHRASES = [
        "point of view, point of you",
        "drawing conclusions",
        "a stroke of genius, or just strokes",
        "framing the unframeable",
        "coloring outside the lines of reality",
        "shaping up to be something else",
        "a different perspective on perspective",
        "lines of thought, thought of lines",
        "the art of being abstract",
        "form follows function, but what if function follows form?",
        "a square peg in a round world",
        "thinking outside the box, but the box is also outside",
        "the angle of repose, the repose of angles",
        "drawing a blank, then drawing on it",
        "a matter of perspective, or a perspective of matter",
        # Unexpected wordplay combinations
        "the right angle to a wrong question",
        "where parallel lines finally meet",
        "a circle's square root of existence",
        "the hypotenuse of a broken heart",
        "acute angles, obtuse feelings",
        "where perpendicular meets parallel",
        "the radius of reason",
        "a tangent to reality",
        "the circumference of consciousness",
        "where diameter meets destiny",
        "the area of awareness",
        "volume of void, void of volume",
        "the surface of the profound",
        "depth in two dimensions",
        "where flat meets infinite",
        "the edge of the center",
        "where inside is outside",
        "the beginning of the end of the beginning",
        "nowhere is now here",
        "the presence of absence",
        "where nothing is everything",
        "the everything of nothing",
        "full emptiness, empty fullness"
    ]
    
    # Artistic movement references with unexpected combinations
    ART_REFERENCES = [
        "in the style of fractured perception",
        "where cubism meets expressionism",
        "a surrealist's geometry",
        "suprematist dreams",
        "constructivist chaos",
        "abstract expression of the inexpressible",
        "minimalist maximalism",
        "geometric poetry",
        "the mathematics of beauty",
        "where art meets algorithm",
        # Unexpected art combinations
        "impressionism of the digital age",
        "where baroque meets minimalism",
        "renaissance in reverse",
        "romanticism without the romance",
        "classicism deconstructed",
        "where pop art meets philosophy",
        "the baroque minimalism paradox",
        "neo-classical chaos theory",
        "post-modern pre-modernism",
        "where dada meets data",
        "the realism of the unreal",
        "hyperrealism of the abstract",
        "where photorealism meets impossibility",
        "the conceptualism of the concrete",
        "where performance art stands still",
        "the installation of nothing",
        "where land art meets digital space",
        "the body art of geometric forms",
        "where street art goes indoors",
        "the graffiti of the void"
    ]
    
    # Philosophical/poetic endings with unexpected twists
    ENDINGS = [
        "what do you see?",
        "perception is reality",
        "art imitates life, or is it the other way?",
        "in the space between",
        "where meaning begins",
        "the question is the answer",
        "see what you feel",
        "feel what you see",
        "beyond the visible",
        "within the impossible",
        # Unexpected ending combinations
        "or maybe not",
        "but also yes",
        "unless it isn't",
        "which is also wrong",
        "but that's just my perspective",
        "or is it?",
        "probably",
        "definitely maybe",
        "certainly uncertain",
        "absolutely relative",
        "definitively indefinite",
        "where certainty doubts itself",
        "the answer that questions",
        "the solution that creates problems",
        "where understanding misunderstands",
        "the explanation that confuses",
        "clarity in confusion",
        "confusion in clarity",
        "the obvious hidden",
        "the hidden obvious",
        "where secrets are public",
        "the private made universal",
        "individual collective",
        "collective individual",
        "the personal impersonal",
        "impersonal personal",
        "where I becomes we becomes I",
        "the singular plural",
        "plural singular",
        "one in many, many in one"
    ]
    
    # Hashtag bases
    HASHTAG_BASES = [
        'abstractart', 'contemporaryart', 'digitalart', 'modernart',
        'artwork', 'art', 'abstract', 'geometric', 'minimalist',
        'avantgarde', 'surrealism', 'cubism', 'expressionism',
        'artdaily', 'instaart', 'artgallery', 'artlovers',
        'creative', 'design', 'visualart', 'artistic',
        'abstractexpressionism', 'geometricart', 'minimalism',
        'artoftheday', 'artistsoninstagram', 'artcollector',
        'contemporaryartist', 'abstractpainting', 'modernartist'
    ]
    
    # Style-specific hashtags
    STYLE_HASHTAGS = {
        'cubism': ['cubism', 'cubist', 'picasso', 'geometricfragmentation'],
        'expressionism': ['expressionism', 'expressionist', 'vangogh', 'emotionalart'],
        'surrealism': ['surrealism', 'surrealist', 'dali', 'dreamlike', 'surrealart'],
        'fragmented': ['fragmented', 'fragmentation', 'abstract', 'geometric'],
        'intense': ['intense', 'bold', 'highcontrast', 'emotional'],
        'suprematist': ['suprematism', 'malevich', 'constructivism']
    }
    
    def generate_caption(self, style: Optional[str] = None, 
                         include_wordplay: bool = True,
                         include_reference: bool = True,
                         max_parts: int = 4) -> str:
        """
        Generate a creative caption with wordplay and surreal meanings.
        Combines unexpected elements in an original and appropriate way.
        
        Args:
            style: Art style (for hashtag selection)
            include_wordplay: Include wordplay phrases
            include_reference: Include art movement references
            max_parts: Maximum number of parts to combine
            
        Returns:
            Generated caption string
        """
        parts = []
        
        # Start with a surreal phrase (higher chance for unexpected ones)
        if random.random() < 0.8:
            # 30% chance to pick from unexpected combinations (later in list)
            if random.random() < 0.3 and len(self.SURREAL_PHRASES) > 20:
                # Pick from the more unexpected phrases (last 30)
                unexpected_start = max(0, len(self.SURREAL_PHRASES) - 30)
                parts.append(random.choice(self.SURREAL_PHRASES[unexpected_start:]))
            else:
                parts.append(random.choice(self.SURREAL_PHRASES))
        
        # Add wordplay (60% chance, higher for more unexpected combinations)
        if include_wordplay and random.random() < 0.6:
            # 40% chance for unexpected wordplay
            if random.random() < 0.4 and len(self.WORDPLAY_PHRASES) > 15:
                unexpected_start = max(0, len(self.WORDPLAY_PHRASES) - 25)
                parts.append(random.choice(self.WORDPLAY_PHRASES[unexpected_start:]))
            else:
                parts.append(random.choice(self.WORDPLAY_PHRASES))
        
        # Add art reference (50% chance)
        if include_reference and random.random() < 0.5:
            # 35% chance for unexpected art references
            if random.random() < 0.35 and len(self.ART_REFERENCES) > 10:
                unexpected_start = max(0, len(self.ART_REFERENCES) - 20)
                parts.append(random.choice(self.ART_REFERENCES[unexpected_start:]))
            else:
                parts.append(random.choice(self.ART_REFERENCES))
        
        # Add ending (70% chance, with preference for unexpected ones)
        if random.random() < 0.7:
            # 50% chance for unexpected endings
            if random.random() < 0.5 and len(self.ENDINGS) > 10:
                unexpected_start = max(0, len(self.ENDINGS) - 30)
                parts.append(random.choice(self.ENDINGS[unexpected_start:]))
            else:
                parts.append(random.choice(self.ENDINGS))
        
        # Limit to max_parts
        if len(parts) > max_parts:
            parts = random.sample(parts, max_parts)
        
        # If no parts, use a default
        if not parts:
            parts.append(random.choice(self.SURREAL_PHRASES))
        
        # Shuffle parts for more unexpected combinations
        if len(parts) > 1 and random.random() < 0.3:
            random.shuffle(parts)
        
        # Join with creative separators (sometimes use unexpected combinations)
        separators = [' • ', ' | ', ' ~ ', ' — ', ' ... ', '\n\n', ' / ', ' × ', ' + ']
        # Sometimes use multiple different separators
        if len(parts) > 2 and random.random() < 0.2:
            caption_parts = []
            for i, part in enumerate(parts):
                caption_parts.append(part)
                if i < len(parts) - 1:
                    caption_parts.append(random.choice(separators))
            caption = ''.join(caption_parts)
        else:
            caption = random.choice(separators).join(parts)
        
        # Capitalize first letter
        caption = caption[0].upper() + caption[1:] if caption else caption
        
        return caption
    
    def generate_hashtags(self, style: Optional[str] = None, 
                         count: int = 20) -> List[str]:
        """
        Generate relevant hashtags for the post.
        
        Args:
            style: Art style
            count: Number of hashtags to generate
            
        Returns:
            List of hashtag strings
        """
        hashtags = self.HASHTAG_BASES.copy()
        
        # Add style-specific hashtags
        if style and style in self.STYLE_HASHTAGS:
            hashtags.extend(self.STYLE_HASHTAGS[style])
        
        # Shuffle and select
        random.shuffle(hashtags)
        selected = hashtags[:count]
        
        return selected
    
    def generate_full_post(self, style: Optional[str] = None) -> tuple[str, List[str]]:
        """
        Generate complete post (caption + hashtags).
        
        Args:
            style: Art style
            
        Returns:
            Tuple of (caption, hashtags_list)
        """
        caption = self.generate_caption(style=style)
        hashtags = self.generate_hashtags(style=style)
        
        return caption, hashtags
    
    def format_post(self, caption: str, hashtags: List[str]) -> str:
        """
        Format caption and hashtags for Instagram.
        
        Args:
            caption: Caption text
            hashtags: List of hashtag strings
            
        Returns:
            Formatted post string
        """
        hashtag_string = " ".join([f"#{tag}" for tag in hashtags])
        
        # Add spacing between caption and hashtags
        return f"{caption}\n\n{hashtag_string}"

