# How to View Images as Gallery on macOS

## 1. HTML Gallery (Recommended for this project)

An interactive HTML gallery has been created for your images:

```bash
# Create/update gallery
python create_gallery.py

# Open in browser
open gallery.html
```

**Advantages:**
- Beautiful interface with filtering
- Click to enlarge (lightbox)
- Grouping by categories
- Works in any browser

## 2. Finder - Gallery View

1. Open the `examples` folder in Finder
2. Press `Cmd + 4` or select **View > Gallery View**
3. Use arrows at the bottom for navigation
4. Press **Space** for Quick Look (full-screen preview)

**Keyboard shortcuts:**
- `Cmd + 1` - Icons View
- `Cmd + 2` - List View  
- `Cmd + 3` - Columns View
- `Cmd + 4` - **Gallery View** ⭐

## 3. Quick Look (Quick Preview)

1. Select multiple images in Finder
2. Press **Space**
3. Use arrow keys ← → for navigation
4. Press **Space** again to close

**Additional:**
- `Option + Space` - full-screen mode
- Can view 20+ images simultaneously

## 4. Preview (Built-in Application)

1. Select all images in Finder (`Cmd + A`)
2. Press **Enter** or double-click
3. In Preview, use the sidebar for navigation
4. `Cmd + →` / `Cmd + ←` to switch between images

## 5. Third-Party Applications

### ImageOptim (Free)
- Optimization + viewing
- `brew install --cask imageoptim`

### Xee³ (Paid, ~$5)
- Fast gallery viewing
- Support for many formats

### Lyn (Free)
- Modern image viewer
- `brew install --cask lyn`

## 6. Terminal (Quick View)

```bash
# Open all images in Preview
open examples/*.jpg

# Open in slideshow mode (if ImageMagick is installed)
# brew install imagemagick
# display examples/*.jpg
```

## Recommendation for This Project

Use the HTML gallery (`gallery.html`) - it's specifically designed for viewing your generated images with convenient navigation and filtering by styles!
