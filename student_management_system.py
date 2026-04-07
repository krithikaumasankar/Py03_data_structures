students = ()
n = int(input("Enter number of students: "))
# storing student records
for i in range(n):
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: ")
    s = (sid, name, marks)
    students = students + (s,)	using (s,) -> ((1, "Ram", 90), (2, "Sam", 85))
				using (s)  -> (1, "Ram", 90, 2, "Sam", 85)
print("\nAll Student Records:")
for r in students:
    print("ID:", r[0], "Name:", r[1], "Marks:", r[2])

# search student by ID
search_id = int(input("\nEnter Student ID to search: "))
found = False

for s in students:
    if s[0] == search_id:
        print("Student Found:", s)
        found = True
        break

if not found:
    print("Student not found")

# highest marks
max_student = students[0]
for s in students:
    if s[2] > max_student[2]:
        max_student = s
print("\nStudent with Highest Marks:", max_student)

# students with marks less than 40
print("\nStudents scoring less than 40:")
for s in students:
    if s[2] < 40:
        print(s)

# average marks 
total = 0
for s in students:
    total += s[2] 
avg = total / len(students)
print("\nAverage Marks:", avg)
