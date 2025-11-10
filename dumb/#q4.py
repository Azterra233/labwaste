#Q4. Assign grade to mark
mark = int(input("Enter the mark (0-100): "))
if 90 <= mark <= 100:
    grade = "A"
    print (grade, "He/She is an Excellent Student!")
elif 80 <= mark < 90:
    grade = "B"
    print (grade, "He/She is a good Student!")
elif 70<= mark <80:
    grade = "C"
    print (grade, "He/She Needs Improvement...")