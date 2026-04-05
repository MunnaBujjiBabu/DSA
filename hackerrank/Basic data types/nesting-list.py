


no_students = int(input("number of students: "))
students = []
for i in range(no_students):
    name = input("enter name: ")
    mark = float(input("enter marks: "))
    students.append([name, mark])


print(students)


grades = []
for i in range(no_students):
    grades.append(students[i][1])

# grades = set(grades)
# print(grades)

sorted_grades = []

for i in range(len(grades)):
    if grades[i] not in sorted_grades:
        sorted_grades.append(grades[i])
print(sorted_grades)
sorted_grades.sort()
print(sorted_grades)

second_lowest = sorted_grades[1]
print(second_lowest)

low_name = []
for i in range(no_students):
    if students[i][1] == second_lowest:
        low_name.append(students[i][0])
        
        
print(low_name)