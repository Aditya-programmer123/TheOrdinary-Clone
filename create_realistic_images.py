from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

os.chdir(r'c:\Users\Aditya\OneDrive\Desktop\Projects\TheOrdinary Clone\assets\images')

products = [
    {
        'file': 'product1.jpg',
        'product_name': 'Hyaluronic Acid 2% + B5',
        'subtitle': 'with Ceramides',
        'size': '30ml',
        'bg_color': '#F9F7F3',
        'label_color': '#FFFFFF',
        'text_color': '#1A1A1A'
    },
    {
        'file': 'product2.jpg',
        'product_name': 'Glycolic Acid 7%',
        'subtitle': 'Exfoliating Toner',
        'size': '240ml',
        'bg_color': '#F8F5F0',
        'label_color': '#FFFFFF',
        'text_color': '#1A1A1A'
    },
    {
        'file': 'product3.jpg',
        'product_name': 'Natural Moisturizing',
        'subtitle': 'Factors + HA',
        'size': '30ml',
        'bg_color': '#F7F4F0',
        'label_color': '#FFFFFF',
        'text_color': '#1A1A1A'
    },
    {
        'file': 'product4.jpg',
        'product_name': 'Volufiline 92%',
        'subtitle': 'Pal-Isoleucine 1%',
        'size': '15ml',
        'bg_color': '#FAFAF8',
        'label_color': '#FFFFFF',
        'text_color': '#1A1A1A'
    },
    {
        'file': 'product5.jpg',
        'product_name': 'Multi-Peptide',
        'subtitle': 'Eye Serum',
        'size': '15ml',
        'bg_color': '#F6F3F0',
        'label_color': '#FFFFFF',
        'text_color': '#1A1A1A'
    },
    {
        'file': 'product6.jpg',
        'product_name': 'Niacinamide 10%',
        'subtitle': 'Zinc 1%',
        'size': '30ml',
        'bg_color': '#F8F6F3',
        'label_color': '#FFFFFF',
        'text_color': '#1A1A1A'
    }
]

for prod in products:
    # Create high-quality image
    width, height = 600, 800
    img = Image.new('RGB', (width, height), color=prod['bg_color'])
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Load fonts
    try:
        font_large = ImageFont.truetype('arial.ttf', 40)
        font_medium = ImageFont.truetype('arial.ttf', 28)
        font_small = ImageFont.truetype('arial.ttf', 20)
        font_tiny = ImageFont.truetype('arial.ttf', 16)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_tiny = ImageFont.load_default()
    
    # Draw bottle (dropper/pump bottle)
    bottle_x1, bottle_y1 = 180, 120
    bottle_x2, bottle_y2 = 420, 500
    
    # Bottle cap/pump
    cap_color = (44, 44, 44)
    draw.rectangle([250, 90, 350, 125], fill=cap_color)
    draw.rectangle([270, 70, 330, 95], fill=cap_color)  # pump handle
    draw.ellipse([260, 60, 340, 80], fill=cap_color)  # top
    
    # Main bottle body
    draw.rectangle([bottle_x1, bottle_y1, bottle_x2, bottle_y2], fill=(220, 220, 218), outline=(180, 180, 175), width=2)
    
    # Glass shine effect (left side)
    shine_x1, shine_y1 = 190, 130
    shine_x2, shine_y2 = 210, 480
    draw.rectangle([shine_x1, shine_y1, shine_x2, shine_y2], fill=(255, 255, 255, 80))
    
    # Label on bottle
    label_x1, label_y1 = 200, 200
    label_x2, label_y2 = 400, 420
    draw.rectangle([label_x1, label_y1, label_x2, label_y2], fill=prod['label_color'], outline=(200, 200, 200), width=1)
    
    # THE ORDINARY text (centered in label)
    the_text = "THE ORDINARY"
    the_bbox = draw.textbbox((0, 0), the_text, font=font_large)
    the_width = the_bbox[2] - the_bbox[0]
    draw.text((width // 2 - the_width // 2, 215), the_text, fill=prod['text_color'], font=font_large)
    
    # Product name
    prod_name = prod['product_name']
    name_bbox = draw.textbbox((0, 0), prod_name, font=font_medium)
    name_width = name_bbox[2] - name_bbox[0]
    draw.text((width // 2 - name_width // 2, 275), prod_name, fill=prod['text_color'], font=font_medium)
    
    # Subtitle
    subtitle = prod['subtitle']
    sub_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
    sub_width = sub_bbox[2] - sub_bbox[0]
    draw.text((width // 2 - sub_width // 2, 320), subtitle, fill=(100, 100, 100), font=font_small)
    
    # Size info
    size_text = prod['size']
    size_bbox = draw.textbbox((0, 0), size_text, font=font_tiny)
    size_width = size_bbox[2] - size_bbox[0]
    draw.text((width // 2 - size_width // 2, 365), size_text, fill=(150, 150, 150), font=font_tiny)
    
    # Bottle content (liquid inside)
    liquid_y = int(bottle_y1 + (bottle_y2 - bottle_y1) * 0.4)
    draw.rectangle([bottle_x1 + 5, liquid_y, bottle_x2 - 5, bottle_y2 - 5], fill=(200, 190, 180, 200))
    
    # Bottom product info below bottle
    info_y = 540
    draw.text((width // 2 - 50, info_y), prod['product_name'], fill=prod['text_color'], font=font_medium)
    draw.text((width // 2 - 40, info_y + 50), prod['subtitle'], fill=(120, 120, 120), font=font_small)
    
    # Convert and save
    img = img.convert('RGB')
    img.save(prod['file'], 'JPEG', quality=95)
    print(f"✓ Created {prod['file']} - {prod['product_name']}")

print("\n✓ All realistic product images created!")
