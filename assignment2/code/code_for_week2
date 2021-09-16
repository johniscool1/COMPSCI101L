#CS 101 Lab
#Program 2
#John Chirpich
#jwcgnq@umkc.edu

print("**** WElcome to the grade calculator ****")
#grabs inputs from users
name = input("\nWho are we calculating the grade for? ==> ")
labgrade = int(input("\nEnter Labs grade? ==> "))
#checks if value is out of range
if labgrade > 100:
    print("The value entered should have been 100 or less. It has been changed to 100.")
    labgrade = 100
if labgrade < 0:
    print("The value entered should have been zero or greator. It has been changed to zero.")
    labgrade = 0
exams = int(input("\nEnter the Exams grade ==> "))
#checks if value is out of range
if exams > 100:
    print("The value entered should have been 100 or less. It has been changed to 100.")
    exams = 100
if exams < 0:
    print("The value entered should have been zero or greator. It has been changed to zero.")
    exams = 0
att = int(input("\nEnter the attendence grade ==> "))
#checks if value is out of range
if att > 100:
    print("The value entered should have been 100 or less. It has been changed to 100.")
    att = 100
if att < 0:
    print("The value entered should have been zero or greator. It has been changed to zero.")
    att = 0
finalgrade = ((labgrade * .7) + (exams * .2) + (att * .1))
print("\nThe weighted grade for",name, "is",finalgrade)
#Decides the letter grade
if finalgrade >= 90:
    letgrade = "A"
elif finalgrade >=80:
    letgrade = "B"
elif finalgrade >=70:
    letgrade = "C"
elif finalgrade >= 60:
    letgrade = "D"
else:
    letgrade = "F"
#prints letter grade
print(name, "has a letter grade of", letgrade)
print("Thank you for using the Lab Grade Calculator")
