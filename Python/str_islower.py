words = [
    "hello",
    "WORLD",
    "python",
    "Good Morning",
    "have a nice day"
]

for word in words:
    if word.islower():
        print(f"Whispering detected: {word}")
    else:
        print(f"Normal or mixed: {word}")
