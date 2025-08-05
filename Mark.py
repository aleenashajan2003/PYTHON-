# Program to store and display marks of 5 students
marks = []
for i in range(1, 6):  # from 1 to 5
    mark = int(input(f"Enter marks of student {i}: "))
    marks.append(mark)  # Add mark to the list
print("\nMarks of 5 students:")
for i in range(5):
    print(f"Student {i + 1}: {marks[i]}")
