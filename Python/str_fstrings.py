# Example: Using f-strings to format output

name = "Samuel"
score = 87.5
subjects = ["Math", "Physics", "Chemistry"]
passed = True

print(f"Student Name: {name}")
print(f"Score: {score}")
print(f"Subjects taken: {', '.join(subjects)}")
print(f"Passed the exam: {'Yes' if passed else 'No'}")
print(f"Average score per subject: {score / len(subjects):.2f}")

# More formatting
print(f"{name:^20} | Score: {score:.1f}")
