text = "banana"
try:
    pos = text.index("a")
    print(f"'a' found at index {pos}")
except ValueError:
    print("Not found!")
