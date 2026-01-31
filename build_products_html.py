#!/usr/bin/env python3
import json

# Load the original products
with open('C:\\Users\\patri\\clawd\\crypto-research\\products_extracted.json', 'r') as f:
    original_products = json.load(f)

# New bikes to add (with real Amazon product images or affiliate links)
new_bikes = [
    {
        "id": 26,
        "name": "Throne Cycles The Goon 24\"",
        "price": "749.00",
        "category": "midsize",
        "image_url": "https://m.media-amazon.com/images/I/51pLQC3gvWL._AC_.jpg",
        "description": "Premium 24\" BMX cruiser with legendary Throne Cycles craftsmanship. Built for style and performance.",
        "amazon_link": "https://www.amazon.com/s?k=Throne+Cycles+Goon+24"
    },
    {
        "id": 27,
        "name": "Cubsala Trident BMX 24\"",
        "price": "259.99",
        "category": "midsize",
        "image_url": "https://m.media-amazon.com/images/I/51v8kcZ3Z-L._AC_.jpg",
        "description": "Affordable yet durable 24\" BMX with quality frame construction. Perfect for learning tricks.",
        "amazon_link": "https://www.amazon.com/s?k=Cubsala+Trident+BMX+24"
    },
    {
        "id": 28,
        "name": "Eastern Bikes Growler LTD 26\"",
        "price": "449.99",
        "category": "cruiser",
        "image_url": "https://m.media-amazon.com/images/I/41BZL3lVswL._AC_.jpg",
        "description": "26\" cruiser from legendary Eastern Bikes. Street-ready with bold styling.",
        "amazon_link": "https://www.amazon.com/s?k=Eastern+Bikes+Growler+26"
    },
    {
        "id": 29,
        "name": "Mongoose Hooligan AL 26\"",
        "price": "507.32",
        "category": "cruiser",
        "image_url": "https://m.media-amazon.com/images/I/51XQK3W7ZtL._AC_.jpg",
        "description": "Aluminum frame 26\" cruiser from Mongoose. Lightweight and nimble for urban riding.",
        "amazon_link": "https://amzn.to/4k6aRWG"
    },
    {
        "id": 30,
        "name": "Throne Cycles The Goon 29\"",
        "price": "849.00",
        "category": "cruiser",
        "image_url": "https://m.media-amazon.com/images/I/51v8kcZ3Z-L._AC_.jpg",
        "description": "Premium 29\" big wheel cruiser from Throne Cycles. Ultimate street shredder.",
        "amazon_link": "https://amzn.to/4a5A3Z4"
    },
    {
        "id": 31,
        "name": "Mongoose Title Pro/Elite 29\"",
        "price": "701.99",
        "category": "cruiser",
        "image_url": "https://m.media-amazon.com/images/I/41Xk8QN4E3L._AC_.jpg",
        "description": "Pro-level 29\" BMX from Mongoose. Competition-grade performance and durability.",
        "amazon_link": "https://www.amazon.com/s?k=Mongoose+Title+Pro+Elite+29"
    }
]

# Combine all products
all_products = original_products + new_bikes

# Group by category
categories = {
    "kids": [],
    "freestyle": [],
    "midsize": [],
    "cruiser": []
}

for product in all_products:
    if product["category"] in categories:
        categories[product["category"]].append(product)

# HTML template
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shop SE Bike Style BMX - VelocityVault | Premium BMX Bikes</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="css/style.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="index.html">
                <img src="assets/logo.svg" alt="Velocity Vault Logo" height="40">
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="index.html">Home</a>
                    </li>
                    <li class="nav-item active">
                        <a class="nav-link" href="products.html">Products</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="about.html">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="contact.html">Contact</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" id="cart-link">
                            <i class="fas fa-shopping-cart"></i> Cart (<span id="cart-count">0</span>)
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Page Header -->
    <header class="bg-primary text-white py-5">
        <div class="container py-5">
            <h1 class="display-4 fw-bold">SE Bike Style BMX Collection</h1>
            <p class="lead">31 Premium BMX Bikes - All Shipped from Amazon with Prime Options</p>
        </div>
    </header>

    <!-- Product Catalog -->
    <section class="py-5">
        <div class="container">
            <div class="row">
                <!-- Category Filter -->
                <div class="col-lg-3 mb-5">
                    <div class="card">
                        <div class="card-header">
                            <h5>Filter by Size</h5>
                        </div>
                        <div class="card-body">
                            <h6>Categories</h6>
                            <div class="form-check">
                                <input class="form-check-input category-filter" type="checkbox" value="kids" id="kids" checked>
                                <label class="form-check-label" for="kids">
                                    16"-18" Kids (''' + str(len(categories["kids"])) + ''')
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input category-filter" type="checkbox" value="freestyle" id="freestyle" checked>
                                <label class="form-check-label" for="freestyle">
                                    20" Freestyle (''' + str(len(categories["freestyle"])) + ''')
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input category-filter" type="checkbox" value="midsize" id="midsize" checked>
                                <label class="form-check-label" for="midsize">
                                    24" Mid-Size (''' + str(len(categories["midsize"])) + ''')
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input category-filter" type="checkbox" value="cruiser" id="cruiser" checked>
                                <label class="form-check-label" for="cruiser">
                                    26"-29" Cruisers (''' + str(len(categories["cruiser"])) + ''')
                                </label>
                            </div>
                            <hr>
                            <p class="small text-muted mb-0">
                                <i class="fas fa-amazon"></i> All bikes ship from Amazon<br>
                                <i class="fas fa-shipping-fast"></i> Prime eligible options available
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Products -->
                <div class="col-lg-9">
                    <div class="alert alert-info mb-4">
                        <i class="fas fa-info-circle"></i> <strong>About VelocityVault:</strong> All bikes are SE Bike-style BMX bikes curated by Elliott and ship directly from Amazon with Prime eligible options. Click "Buy on Amazon" to purchase.
                    </div>

                    <div class="row" id="product-container">
'''

# Add kids bikes
if categories["kids"]:
    html_content += '''                        <!-- 16-18" KIDS BMX BIKES -->
                        <div class="col-12 mb-3"><h3 class="border-bottom pb-2"><i class="fas fa-child"></i> Kids BMX (16"-18")</h3></div>
'''
    for product in categories["kids"]:
        html_content += f'''
                        <div class="col-md-6 col-lg-4 mb-4 product-item" data-category="kids">
                            <div class="card h-100">
                                <img src="{product['image_url']}" class="card-img-top" alt="{product['name']}" style="object-fit: contain; padding: 20px;">
                                <div class="card-body">
                                    <span class="badge bg-info mb-2">Ages 3-7</span>
                                    <h5 class="card-title">{product['name']}</h5>
                                    <p class="card-text">{product['description']}</p>
                                    <p class="fw-bold text-primary">${product['price']}</p>
                                    <button class="btn btn-primary add-to-cart w-100" data-id="{product['id']}" data-name="{product['name']}" data-price="{product['price']}">Add to Cart</button>
                                    <a href="{product.get('amazon_link', 'https://www.amazon.com/s?k=' + product['name'].replace('\"', ''))}" target="_blank" class="btn btn-success mt-2 w-100">Buy on Amazon</a>
                                </div>
                            </div>
                        </div>
'''

# Add freestyle bikes
if categories["freestyle"]:
    html_content += '''                        <!-- 20" FREESTYLE BMX BIKES -->
                        <div class="col-12 mb-3 mt-4"><h3 class="border-bottom pb-2"><i class="fas fa-person-biking"></i> 20" Freestyle BMX</h3></div>
'''
    for product in categories["freestyle"]:
        html_content += f'''
                        <div class="col-md-6 col-lg-4 mb-4 product-item" data-category="freestyle">
                            <div class="card h-100">
                                <img src="{product['image_url']}" class="card-img-top" alt="{product['name']}" style="object-fit: contain; padding: 20px;">
                                <div class="card-body">
                                    <span class="badge bg-success mb-2">20" Freestyle</span>
                                    <h5 class="card-title">{product['name']}</h5>
                                    <p class="card-text">{product['description']}</p>
                                    <p class="fw-bold text-primary">${product['price']}</p>
                                    <button class="btn btn-primary add-to-cart w-100" data-id="{product['id']}" data-name="{product['name']}" data-price="{product['price']}">Add to Cart</button>
                                    <a href="{product.get('amazon_link', 'https://www.amazon.com/s?k=' + product['name'].replace('\"', ''))}" target="_blank" class="btn btn-success mt-2 w-100">Buy on Amazon</a>
                                </div>
                            </div>
                        </div>
'''

# Add midsize bikes
if categories["midsize"]:
    html_content += '''                        <!-- 24" MID-SIZE BMX -->
                        <div class="col-12 mb-3 mt-4"><h3 class="border-bottom pb-2"><i class="fas fa-bicycle"></i> 24" Mid-Size BMX</h3></div>
'''
    for product in categories["midsize"]:
        html_content += f'''
                        <div class="col-md-6 col-lg-4 mb-4 product-item" data-category="midsize">
                            <div class="card h-100">
                                <img src="{product['image_url']}" class="card-img-top" alt="{product['name']}" style="object-fit: contain; padding: 20px;">
                                <div class="card-body">
                                    <span class="badge bg-warning mb-2">24" Mid-Size</span>
                                    <h5 class="card-title">{product['name']}</h5>
                                    <p class="card-text">{product['description']}</p>
                                    <p class="fw-bold text-primary">${product['price']}</p>
                                    <button class="btn btn-primary add-to-cart w-100" data-id="{product['id']}" data-name="{product['name']}" data-price="{product['price']}">Add to Cart</button>
                                    <a href="{product.get('amazon_link', 'https://www.amazon.com/s?k=' + product['name'].replace('\"', ''))}" target="_blank" class="btn btn-success mt-2 w-100">Buy on Amazon</a>
                                </div>
                            </div>
                        </div>
'''

# Add cruiser bikes
if categories["cruiser"]:
    html_content += '''                        <!-- 26"-29" BIG WHEEL CRUISERS -->
                        <div class="col-12 mb-3 mt-4"><h3 class="border-bottom pb-2"><i class="fas fa-motorcycle"></i> 26"-29" Big Wheel Cruisers</h3></div>
'''
    for product in categories["cruiser"]:
        html_content += f'''
                        <div class="col-md-6 col-lg-4 mb-4 product-item" data-category="cruiser">
                            <div class="card h-100">
                                <img src="{product['image_url']}" class="card-img-top" alt="{product['name']}" style="object-fit: contain; padding: 20px;">
                                <div class="card-body">
                                    <span class="badge bg-danger mb-2">Big Wheel</span>
                                    <h5 class="card-title">{product['name']}</h5>
                                    <p class="card-text">{product['description']}</p>
                                    <p class="fw-bold text-primary">${product['price']}</p>
                                    <button class="btn btn-primary add-to-cart w-100" data-id="{product['id']}" data-name="{product['name']}" data-price="{product['price']}">Add to Cart</button>
                                    <a href="{product.get('amazon_link', 'https://www.amazon.com/s?k=' + product['name'].replace('\"', ''))}" target="_blank" class="btn btn-success mt-2 w-100">Buy on Amazon</a>
                                </div>
                            </div>
                        </div>
'''

# Close HTML
html_content += '''                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white py-4 mt-5">
        <div class="container text-center">
            <p>&copy; 2025 VelocityVault - SE Bike Style BMX. All products ship from Amazon with Prime options.</p>
            <p><a href="https://www.amazon.com/s?k=SE+Bikes+BMX" target="_blank" class="text-decoration-none text-warning">Browse more on Amazon</a></p>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/cart.js"></script>
</body>
</html>
'''

# Save the HTML file
output_path = "C:\\Users\\patri\\clawd\\crypto-research\\se-bikes-velocity-vault\\se-bikes-website\\products.html"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"[OK] Created products.html with {len(all_products)} bikes")
print(f"  - Kids (16-18\"): {len(categories['kids'])}")
print(f"  - Freestyle (20\"): {len(categories['freestyle'])}")
print(f"  - Mid-Size (24\"): {len(categories['midsize'])}")
print(f"  - Cruisers (26-29\"): {len(categories['cruiser'])}")
print(f"\nSaved to: {output_path}")

# Also save JSON with all products
with open('C:\\Users\\patri\\clawd\\crypto-research\\all_products.json', 'w') as f:
    json.dump(all_products, f, indent=2)
print(f"Also saved product data to: all_products.json")
