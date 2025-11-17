name = input("Enter Student Name: ")
print("                                  ")
print("Total Marks are: 500")
print("                                  ")
print("Enter Subjects Marks (out of 100):")
print("                                  ")
maths = int(input("Maths: "))
urdu = int(input("Urdu: "))
english = int(input("English: "))
islamiat = int(input("Islamiat: "))
computer = int(input("Computer: "))
print("                                  ")
print("         SCROLL DOWN               ")
print("                                  ")
total = maths + urdu + english + islamiat + computer
percentage = total / 500 * 100
print("                                  ")
if percentage >= 90:
    grade = "A+"
    remarks = f"Outstanding! Excellent performance, {name}!"
elif percentage >= 80:
    grade = "A"
    remarks = f"Excellent! Keep up the good work, {name}!"
elif percentage >= 70:
    grade = "B"
    remarks = f"Very Good! You're doing great, {name}!"
elif percentage >= 60:
    grade = "C"
    remarks = f"Good! There's room for improvement, {name}."
elif percentage >= 50:
    grade = "D"
    remarks = f"Satisfactory. Need to work harder, {name}."
else:
    grade = "F"
    remarks = f"Needs Improvement. Please focus on your studies, {name}."

print("                                  ")
print("          SCROLL DOWN             ")
print("                                  ")
print("-----MARK SHEET-----")
print("Name:", name)
print("Total Marks: 500")
print("Obtained Marks:", total)
print("Percentage:", percentage,"%")
print("Grade:", grade)
print("Remarks:", remarks)
print("-------------------")
