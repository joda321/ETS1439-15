text = "hello world"
print(text.startswith("hello"))     # True
print(text.startswith("world"))     # False
print(text.startswith("lo", 3))     # True (starts checking at index 3)
