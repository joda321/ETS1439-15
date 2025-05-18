# Dictionary representing a user profile
user = {
    "username": "zelalem99",
    "email": "zelalem@example.com",
    "password": "secret123",
    "last_login": "2025-05-17"
}

print("👤 Original User Profile:")
for key, value in user.items():
    print(f"{key}: {value}")

# Remove the password field for display
user.pop("password")

print("\n🔐 Safe User Profile (for display):")
for key, value in user.items():
    print(f"{key}: {value}")
