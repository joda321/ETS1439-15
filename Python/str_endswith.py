text = "hello world"

print(text.endswith("world"))       # True
print(text.endswith("hello"))       # False
print(text.endswith("lo", 3, 5))    # True (text[3:5] == "lo")
print(text.endswith(("world", "planet")))  # True
