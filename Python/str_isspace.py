# Example: Checking for empty or whitespace-only lines in text

lines = ["Hello", "   ", "\t", "World", "", "\n"]
print("Lines with only whitespace:")

for i, line in enumerate(lines):
    if line.isspace():
        print("Line {} is only whitespace.".format(i))
    elif line == "":
        print("Line {} is empty.".format(i))
    else:
        print("Line {} has content: '{}'".format(i, line))



