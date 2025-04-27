messages = [
    "hello",
    "good morning",
    "python is fun",
    "እንኳን ደህና መጡ",
]

for message in messages:
    encoded_message = message.encode('utf-8')
    print(f"Original: {message}")
    print(f"Encoded : {encoded_message}\n")
