# Example: Using str.join() to format list outputs

names = ["Abel", "Marta", "Selam", "Teddy"]
ids = ["101", "102", "103", "104"]

# Join names with comma
name_line = ", ".join(names)
print(f"Names: {name_line}")

# Join IDs with dash
id_line = " - ".join(ids)
print(f"Student IDs: {id_line}")

# Creating a CSV-style record
for name, id in zip(names, ids):
    print(",".join([name, id]))
