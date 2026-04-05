# student = [
#     {'one': 1, 'two': 2, 'three': 44},
#     {'one': 1, 'two': 2, 'three': 44},
# ]


# student = [
#     {'one': 1, 'two': 2, 'three': {'one': 11, 'two': 12, 'three': 40}},
#     {'one': 11, 'two': 12, 'three': {'one': 11, 'two': 12, 'three': 40}},
#     {'one': 11, 'two': 12, 'three': {'one': 11, 'two': 12, 'three': 40}}
# ]

# # Sort by grade instead of name
# sorted_student = sorted(student, key=lambda x: x['three'])

# # sorted_student = sorted(student, key=lambda x: x)


# # sorted_student = sorted(student)
# print(sorted_student)


dictionary={
    "b":1,
    "c":3,
    "a":4,
    "d":2
}

print(sorted(dictionary.items(), key=lambda x:x[1]))    