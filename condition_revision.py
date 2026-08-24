eco = int(input("enter marks for a student:"))
computer = int(input("enter marks for a student:"))


marks = eco + computer
if marks <0 or marks>100:
    print("Invalid marks!!Enter marks between 0 and 100.")
elif marks>=90:
    print("Grade:A+")
elif marks>=80:
    print("Grade:A")
elif marks>=70:
    print("Grade:B")
elif marks>=60:
    print("Grade:C")
elif marks>=50:
    print("Grade:D")
else:
    print("F")