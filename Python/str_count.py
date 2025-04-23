# str_count_demo.py

def str_count_demo():
    text = "Hello hello HELLO heLLo world! hello again."

    print("1. Basic count (case-sensitive):")
    print(text.count("hello"))

    print("\n2. Case-insensitive count:")
    print(text.lower().count("hello"))

    print("\n3. Count of character 'l':")
    print(text.count("l"))

    print("\n4. Count of 'lo':")
    print(text.count("lo"))

    print("\n5. Count of non-existing word 'bye':")
    print(text.count("bye"))

    print("\n6. Count within a slice (indexes 0 to 20):")
    print(text.count("hello", 0, 20))

    print("\n7. Overlapping substring behavior:")
    overlap_text = "aaaa"
    print(overlap_text.count("aa"))

    print("\n8. Count of empty string:")
    print(text.count(""))

    print("\n9. Count of space characters:")
    print(text.count(" "))

    print("\n10. Count of commas in CSV line:")
    csv_line = "id,name,age,location,email"
    print(csv_line.count(","))

    print("\n11. Count of emojis:")
    emoji_text = "😀😃😄😁😃😃"
    print(emoji_text.count("😃"))

    print("\n12. Simple email format check:")
    email = "someone@example.com"
    if email.count("@") == 1 and email.count(".") >= 1:
        print("Valid format")
    else:
        print("Invalid format")


# Run the demo
if __name__ == "__main__":
    str_count_demo()
