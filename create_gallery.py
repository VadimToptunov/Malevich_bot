"""
Script to create an HTML gallery from generated images.
All documentation in English.
"""
import os
from pathlib import Path
from typing import List, Tuple


def create_gallery_html(images_dir: str = 'examples', output_file: str = 'gallery.html'):
    """
    Create an HTML gallery from images in the specified directory.
    
    Args:
        images_dir: Directory containing images
        output_file: Output HTML file name
    """
    images_path = Path(images_dir)
    if not images_path.exists():
        print(f"Error: Directory '{images_dir}' not found")
        return
    
    # Find all image files
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
    image_files = []
    
    for file in sorted(images_path.iterdir()):
        if file.suffix.lower() in image_extensions:
            # Determine category from filename
            filename = file.name
            if filename.startswith('comprehensive_'):
                category = 'comprehensive'
            elif filename.startswith('interdisciplinary_'):
                category = 'interdisciplinary'
            elif filename.startswith('magnet_') or filename.startswith('avantguard_'):
                category = 'legacy'
            else:
                category = 'other'
            
            # Use relative path for HTML
            rel_path = os.path.join(images_dir, file.name)
            image_files.append({
                'path': rel_path,
                'name': file.stem.replace('_', ' ').title(),
                'category': category
            })
    
    if not image_files:
        print(f"No images found in '{images_dir}'")
        return
    
    # Read the HTML template
    html_template = Path('view_gallery.html').read_text(encoding='utf-8')
    
    # Generate JavaScript array of images
    images_js = 'const images = [\n'
    for img in image_files:
        images_js += f"    {{path: '{img['path']}', name: '{img['name']}', category: '{img['category']}'}},\n"
    images_js += '];\n'
    
    # Replace placeholder in template
    html_content = html_template.replace('// Image data will be inserted here\n        const images = [];', images_js)
    
    # Write output file
    output_path = Path(output_file)
    output_path.write_text(html_content, encoding='utf-8')
    
    print(f"✓ Gallery created: {output_file}")
    print(f"  Found {len(image_files)} images")
    print(f"  Open in browser: open {output_file}")


if __name__ == "__main__":
    create_gallery_html()
    print("\nTo view the gallery:")
    print("  open gallery.html")

