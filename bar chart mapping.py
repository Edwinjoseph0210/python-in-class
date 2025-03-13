import matplotlib.pyplot as plt

# Input average marks of 5 students
students = []
marks = []
grades = []

for i in range(5):
    name = input(f"Enter student {i+1} name: ")
    avg_mark = float(input(f"Enter average marks of {name}: "))
    students.append(name)
    marks.append(avg_mark)

    # Assign grades based on marks
    if avg_mark >= 90:
        grades.append("A+")
    elif avg_mark >= 80:
        grades.append("A")
    elif avg_mark >= 70:
        grades.append("B+")
    elif avg_mark >= 60:
        grades.append("B")
    elif avg_mark >= 50:
        grades.append("C")
    elif avg_mark >= 40:
        grades.append("D")
    else:
        grades.append("F")

# Plotting the bar chart
plt.figure(figsize=(8, 5))
plt.bar(students, marks, color=['green', 'blue', 'orange', 'purple', 'red'])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Students' Marks and Grades")

# Annotate each bar with grades
for i in range(5):
    plt.text(i, marks[i] + 1, grades[i], ha='center', fontsize=12, fontweight='bold')

plt.ylim(0, 100)  # Set y-axis limit
plt.show()
