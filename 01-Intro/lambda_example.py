students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 95},
    {"name": "Charlie", "grade": 82}
]

print(students[0]['grade'])

# Sort by grade instead of name
#sorted_students = sorted(students, key=lambda x: x["grade"])

sorted_students = sorted(students, key=lambda x: x['name'], reverse=True)
print(sorted_students)
