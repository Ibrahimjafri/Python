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
percentage = (total * 100) // 500
print("                                  ")
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 50:
    grade = "E"
else:
    grade = ("F")
print("                                  ")
print("          SCROLL DOWN             ")
print("                                  ")
print("-----MARK SHEET-----")
print("Name:", name)
print("Total Marks:", total,"/500")
print("Percentage:", percentage,"%")
print("Grade:", grade)
print("-------------------")
