# Imagine you are working on a student score list
original_scores = [88, 76, 92, 85]

# You want to try editing the scores without changing the original
copied_scores = original_scores.copy()

# Let's add a bonus score to the copied list
copied_scores.append(100)

# Let's also remove the lowest score from the copied list
copied_scores.remove(min(copied_scores))

# Now, print both lists to compare
print("Original scores:", original_scores)
print("Copied scores after changes:", copied_scores)

