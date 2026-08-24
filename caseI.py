# Create an empty list to store marks
marks = []

# Take marks of 5 students
for i in range(1, 6):
    score = float(input(f"Enter marks of student {i}: "))
    marks.append(score)

# Display the list of marks
print("\nMarks List:", marks)

# Calculate Total and Average
total = sum(marks)
average = total / len(marks)

print("Total Marks   =", total)
print("Average Marks =", average)

# Find Highest and Lowest marks
print("Highest Marks =", max(marks))
print("Lowest Marks  =", min(marks))

# Count categories
excellent = 0
average_count = 0
fail = 0

for score in marks:
    if score >= 90:
        excellent += 1
    elif score >= 50:
        average_count += 1
    else:
        fail += 1

print("\nExcellent (90+) :", excellent, "student(s)")
print("Average (50-89) :", average_count, "student(s)")
print("Fail (Below 50) :", fail, "student(s)")