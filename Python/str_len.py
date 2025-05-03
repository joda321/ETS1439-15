# Example: Using len() with different data types

name = "Engineering"
numbers = [10, 20, 30, 40, 50]
grades = {"Math": 95, "Physics": 88, "Chemistry": 91}

# Using len() with a string
print("Length of name:", len(name))

# Using len() with a list
print("Number of items in numbers list:", len(numbers))

# Using len() with a dictionary
print("Number of subjects:", len(grades))

# Checking if the list has more than 3 items
if len(numbers) > 3:
    
    print("The list has more than 3 items.")

# Display all subjects if dictionary is not empty
if len(grades) > 0:
    print("Subjects:", list(grades.keys()))
