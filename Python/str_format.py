# Example: Using str.format() to format strings

student = "Marta"
subjects = ["Biology", "Math", "History"]
grades = [88, 92, 79]

# Print header
print("Student Name: {}".format(student))
print("Subjects and Grades:")

# Loop through subjects and grades
for i in range(len(subjects)):
    print("{}: {}%".format(subjects[i], grades[i]))

# Calculate average
average = sum(grades) / len(grades)
print("Average Grade: {:.2f}%".format(average))
