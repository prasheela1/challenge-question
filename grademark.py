# calculate the grade of student

# store the marks in seperate variables
sub1 = 78
sub2 = 85
sub3 = 82
sub4 = 74
sub5 = 78

# calculate total marks

total_marks = sub1 + sub2 + sub3 + sub4 + sub5

print("Total Marks = ", total_marks , "/ 500")

# calculate_percentage

max_marks = 5 * 100
percentage = (total_marks / max_marks) * 100

print("Percentage =", percentage, "%" )

# calculate the grade of sudent

if percentage >= 90:
    print('Grade A+')
elif percentage >= 80:
    print('Grade A')
elif percentage >= 70:
    print('Grade B')
elif percentage >= 60:
    print('Grade C')
elif percentage >= 50:
    print('Grade D')
else:
    print('Grade F')
