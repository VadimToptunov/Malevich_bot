# Project Structure

## Reorganized Modular Architecture

The project has been reorganized into a clean, modular structure:

```
Malevich/
├── generators/          # Image generation modules
│   ├── comprehensive_style_generator.py    # 21+ art styles (hyperrealism, pop art, etc.)
│   ├── interdisciplinary_generator.py      # Psychology, physics, chemistry, math integration
│   ├── magnet_image_generator.py           # Original mathematical generator
│   └── avantguard.py                       # Original avant-garde generator
│
├── utils/              # Utility modules
│   ├── tech.py                            # Random utilities, filename generation
│   └── color_systems.py                   # Advanced color theory and palettes
│
├── social/            # Social media integration
│   ├── instagram_poster.py                # Instagram posting functionality
│   ├── scheduler.py                        # Automated posting scheduler
│   └── caption_generator.py               # Creative caption generation
│
└── examples/          # Example generation scripts
    └── generate_all.py                    # Unified example generator
```

## Main Scripts

- `malevich_instagram.py` - Main Instagram posting script
- `malevich_bot.py` - Original bot script (legacy)

## Key Generators

### ComprehensiveStyleGenerator
Supports 21+ art styles:
- Hyperrealism, Photorealism
- Minimalism, Pop Art, Op Art
- Fauvism, Futurism, Dadaism
- Constructivism, De Stijl, Art Deco
- Art Nouveau, Neoclassicism, Romanticism
- Realism, Naturalism, Mannerism
- Rococo, Classicism, Symbolism, Precisionism

### InterdisciplinaryGenerator
Combines:
- Psychology & Marketing (color-emotion, visual hierarchy)
- Psychiatry (schizophrenia, synesthesia, hallucinations)
- Physiology (color blindness, visual agnosia)
- Mathematics (fractals, tessellations, chaos theory)
- Physics (quantum mechanics, wave interference, relativity)
- Chemistry (molecular structures, crystal lattices, reactions)

## Usage

### Generate Examples
```bash
python -m Malevich.examples.generate_all
```

### Generate and Post to Instagram
```bash
python malevich_instagram.py generate [style]
python malevich_instagram.py post [style]
python malevich_instagram.py schedule
```

## Removed Files

The following obsolete files have been removed:
- `advanced_generator.py` (replaced by ComprehensiveStyleGenerator)
- `refined_generator.py` (replaced by ComprehensiveStyleGenerator)
- `master_generator.py` (replaced by ComprehensiveStyleGenerator)
- `enhanced_generator.py` (replaced by ComprehensiveStyleGenerator)
- `ultra_enhanced_generator.py` (replaced by ComprehensiveStyleGenerator)
- `generate_examples.py` (replaced by examples/generate_all.py)
- `generate_enhanced_examples.py` (replaced by examples/generate_all.py)
- `generate_ultra_examples.py` (replaced by examples/generate_all.py)
- `generate_interdisciplinary_examples.py` (replaced by examples/generate_all.py)
- `generate_all_styles.py` (replaced by examples/generate_all.py)

