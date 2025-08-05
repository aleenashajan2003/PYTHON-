students = {}
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    mark = int(input(f"Enter marks of {name}: "))
    students[name] = mark  
topper = max(students, key=students.get)  
print(f"\nTopper is {topper} with {students[topper]} marks.")
