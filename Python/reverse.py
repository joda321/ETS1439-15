# A user goes through steps in a learning app
user_steps = []

# User starts the tutorial
user_steps.append("Opened app")
user_steps.append("Selected 'Learn Python'")
user_steps.append("Started Lesson 1")
user_steps.append("Watched Intro Video")
user_steps.append("Tried Coding Exercise")
user_steps.append("Checked Hints")
user_steps.append("Submitted Answer")
user_steps.append("Passed Quiz")

# Print the steps in the order they happened
print("Steps in normal order:")
for step in user_steps:
    print("-", step)

print("\nNow let's see the steps in reverse (like going back):")
# Reverse the steps in place
user_steps.reverse()

# Print the reversed steps
for step in user_steps:
    print("-", step)
