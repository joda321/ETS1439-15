# Example: Filtering user input with isalnum()

user_inputs = ["user123", "hello_world", "abc!", "Welcome", "2025", ""]

print("Valid alphanumeric inputs:")
for item in user_inputs:
    if item.isalnum():
        print(f"'{item}' is valid.")
    else:
        print(f"'{item}' is NOT valid (non-alphanumeric characters found).")
