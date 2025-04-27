sentences = [
    "HELLO WORLD",
    "Python is Fun",
    "WELCOME TO THE PARTY",
    "good morning",
    "HAVE A NICE DAY"
]

for sentence in sentences:
    if sentence.isupper():
        print(f"Shouting detected: {sentence}")
    else:
        print(f"Normal speaking: {sentence}")
