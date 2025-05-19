# Initial product dictionary
product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000
}

print("🛒 Original Product Info:")
for key, value in product.items():
    print(f"{key}: {value}")

# Use update() to change price and add new data
product.update({
    "price": 72000,            # Update price
    "stock": 25,               # Add stock info
    "warranty": "1 year"       # Add warranty info
})

print("\n📦 Updated Product Info:")
for key, value in product.items():
    print(f"{key}: {value}")
