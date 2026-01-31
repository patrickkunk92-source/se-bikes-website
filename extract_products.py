#!/usr/bin/env python3
import re
import urllib.request
import json

# Fetch the HTML
print("Fetching products.html from Vercel...")
content = urllib.request.urlopen('https://se-bikes-website.vercel.app/products.html').read().decode('utf-8')

# Extract all product cards
product_pattern = r'<div class="col-md-6 col-lg-4 mb-4 product-item".*?</div>\s*</div>\s*</div>'
products = re.findall(product_pattern, content, re.DOTALL)

print(f'Found {len(products)} products\n')
print("=" * 100)

# Extract key data from each product
products_data = []
for i, product in enumerate(products):
    # Extract image
    img_match = re.search(r'<img\s+src="([^"]+)"', product)
    img_url = img_match.group(1) if img_match else 'NO IMAGE'
    
    # Extract name
    name_match = re.search(r'<h5 class="card-title">([^<]+)</h5>', product)
    name = name_match.group(1) if name_match else 'NO NAME'
    
    # Extract price
    price_match = re.search(r'\$([0-9.]+)', product)
    price = price_match.group(1) if price_match else 'NO PRICE'
    
    # Extract category
    category_match = re.search(r'data-category="([^"]+)"', product)
    category = category_match.group(1) if category_match else 'NO CATEGORY'
    
    # Extract description
    desc_match = re.search(r'<p class="card-text">([^<]+)</p>', product)
    description = desc_match.group(1) if desc_match else 'NO DESC'
    
    products_data.append({
        'id': i + 1,
        'name': name.strip(),
        'price': price,
        'category': category,
        'image_url': img_url,
        'description': description.strip()
    })
    
    print(f'{i+1:2d}. {name:40s} ${price:7s} ({category:12s})')

print("=" * 100)
print(f'\nTotal products: {len(products_data)}')

# Save to JSON for reference
with open('C:\\Users\\patri\\clawd\\crypto-research\\products_extracted.json', 'w') as f:
    json.dump(products_data, f, indent=2)

print("Saved to products_extracted.json")
