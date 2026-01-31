from PIL import Image, ImageDraw, ImageFont
import os

os.chdir(r'c:\Users\Aditya\OneDrive\Desktop\Projects\TheOrdinary Clone\assets\images')

# Product specifications - more realistic
products = [
    {
        'file': 'product1.jpg',
        'name': 'Hyaluronic Acid\n2% + B5',
        'bg_color': '#F8F6F2',
        'bottle_color': '#2C2C2C',
        'label_color': '#E8D5C4',
        'accent': '#8B7355'
    },
    {
        'file': 'product2.jpg',
        'name': 'Glycolic Acid\n7% Toner',
        'bg_color': '#FBF8F3',
        'bottle_color': '#2C2C2C',
        'label_color': '#F5E6D3',
        'accent': '#C19A6B'
    },
    {
        'file': 'product3.jpg',
        'name': 'Natural\nMoisturizing\nFactors + HA',
        'bg_color': '#F5F2ED',
        'bottle_color': '#2C2C2C',
        'label_color': '#E0C9B8',
        'accent': '#A0826D'
    },
    {
        'file': 'product4.jpg',
        'name': 'Volufiline\n92% + Pal-Iso',
        'bg_color': '#FFFAF5',
        'bottle_color': '#2C2C2C',
        'label_color': '#F0DCC8',
        'accent': '#C9AE9B'
    },
    {
        'file': 'product5.jpg',
        'name': 'Multi-Peptide\nEye Serum',
        'bg_color': '#F3EFEA',
        'bottle_color': '#2C2C2C',
        'label_color': '#D4B5A0',
        'accent': '#8B6F47'
    },
    {
        'file': 'product6.jpg',
        'name': 'Niacinamide\n10% + Zinc 1%',
        'bg_color': '#F7F4F0',
        'bottle_color': '#2C2C2C',
        'label_color': '#E6D2C0',
        'accent': '#A0826D'
    }
]

for prod in products:
    # Create image with light background
    img = Image.new('RGB', (500, 700), color=prod['bg_color'])
    draw = ImageDraw.Draw(img)
    
    # Draw subtle gradient background
    for y in range(700):
        shade = int(240 + (y / 700) * 10)
        color = (shade, shade - 5, shade - 10)
        draw.line([(0, y), (500, y)], fill=color)
    
    # Draw bottle - main body (dropper bottle style)
    bottle_color_tuple = tuple(int(prod['bottle_color'][i:i+2], 16) for i in (1, 3, 5))
    label_color_tuple = tuple(int(prod['label_color'][i:i+2], 16) for i in (1, 3, 5))
    
    # Bottle cap
    draw.rectangle([210, 80, 290, 110], fill=bottle_color_tuple)
    draw.rectangle([220, 70, 280, 85], fill=bottle_color_tuple)  # pump
    
    # Main bottle body
    draw.rectangle([130, 110, 370, 520], fill=bottle_color_tuple, outline=bottle_color_tuple)
    draw.arc([130, 110, 370, 200], 0, 180, fill=bottle_color_tuple)
    
    # Label area on bottle
    label_rect = [150, 180, 350, 400]
    draw.rectangle(label_rect, fill=label_color_tuple)
    
    # Draw "THE ORDINARY" text on label
    try:
        font_title = ImageFont.truetype('arial.ttf', 32)
        font_text = ImageFont.truetype('arial.ttf', 28)
    except:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()
    
    # Title
    title = "THE\nORDINARY"
    title_bbox = draw.textbbox((0, 0), title, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((500 - title_width) // 2, 200), title, fill=bottle_color_tuple, font=font_title)
    
    # Product name on label
    prod_name_bbox = draw.textbbox((0, 0), prod['name'], font=font_text)
    prod_name_width = prod_name_bbox[2] - prod_name_bbox[0]
    draw.text(((500 - prod_name_width) // 2, 290), prod['name'], fill=bottle_color_tuple, font=font_text)
    
    # Shine effect on bottle
    draw.rectangle([140, 120, 160, 400], fill=(255, 255, 255, 50))
    
    # Highlight reflection
    draw.arc([130, 110, 250, 350], 200, 340, fill=(200, 200, 200))
    
    # Product name below bottle
    name_bbox = draw.textbbox((0, 0), prod['name'], font=font_text)
    name_width = name_bbox[2] - name_bbox[0]
    accent_color_tuple = tuple(int(prod['accent'][i:i+2], 16) for i in (1, 3, 5))
    draw.text(((500 - name_width) // 2, 550), prod['name'], fill=accent_color_tuple, font=font_text)
    
    img = img.convert('RGB')
    img.save(prod['file'], 'JPEG', quality=95)
    print(f"✓ Created {prod['file']}")

print("\n✓ All product images created successfully!")
