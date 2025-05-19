# 1. fromkeys() — create dictionary with default values
genres = ["Fiction", "Science", "History"]
book_stock = dict.fromkeys(genres, 0)  # Start with 0 books in each genre

print("📦 Initial book stock by genre:")
for genre, stock in book_stock.items():
    print(f"{genre}: {stock} books")

# 2. setdefault() — safely add a new key if it doesn't exist
new_genre = "Fantasy"
book_stock.setdefault(new_genre, 5)  # If Fantasy doesn't exist, add it with 5 books

# 3. popitem() — remove the last inserted item (Fantasy in this case)
last_removed = book_stock.popitem()

print("\n📚 After adding Fantasy and removing last genre:")
for genre, stock in book_stock.items():
    print(f"{genre}: {stock} books")

print(f"\n🗑️ Removed genre: {last_removed[0]}, stock was: {last_removed[1]} books")
