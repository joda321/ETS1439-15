# A list of students and their scores (unordered)
students = [
    {"name": "Amina", "score": 75},
    {"name": "Bereket", "score": 90},
    {"name": "Chala", "score": 60},
    {"name": "Dani", "score": 85},
    {"name": "Elsa", "score": 70}
]

print("Original list of students and scores:")
for s in students:
    print(f"- {s['name']}: {s['score']}")

# Sort students by their score in descending order (highest first)
students.sort(key=lambda student: student["score"], reverse=True)

print("\n🏆 Leaderboard (sorted by highest score):")
for rank, student in enumerate(students, start=1):
    print(f"{rank}. {student['name']} - {student['score']} points")
