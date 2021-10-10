
#CS 101 Lab
#Program 5
#John Chirpich
#jwcgnq@umkc.edu



import string
ident = []
#changes letter to number
def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    return string.ascii_uppercase.index(char)
#This function converts the id to either a list of integars or a string
def convert_int(card_num, alist):
    ident = []
    card = ""
    count = 0
    while count < len(card_num):
        num = ""
        if card_num[count].isalpha() == True:
            num = str(character_value(card_num[count]))
        else:
            num = card_num[count]
        ident.append(str(num))
        count += 1

    if alist == False:
        return "".join(ident)
    else:
        count = 0
        card = []
        while count < len(ident):
            card.append(int(ident[count]))
            count += 1
        return card
        
#makes a check digit     
def get_check_digit(idnumber : str) -> int:
    card_num = convert_int(card_num, True)
    count = 0
    total = 0
    while count <= 8:
        total = total + ((count+1) * card_num[count])
        count += 1
    return total % 10

#finds errors in the id
def is_valid(card_num : str) -> tuple:
    error = []
    orig = card_num
    count = 0
    if len(card_num) < 9:
        error.append("The length of the number given must be 10.")
        return error
    while count < 5:

        if card_num[count].isnumeric() == True:
            two = ("The first 5 characters must be A-Z, the invalid character is a", card_num[count], "at", count)
            error.append(two)
            return error
        count += 1

    count =7
    while count < 9:
        if type(card_num[count]) == int:
            three = "The last 3 characters must be 0-9, the invalid character is a", card_num[count], "at", count
            error.append(three)
            return error
        count += 1
    card_num = convert_int(card_num, True)
    count = 0


    count = 0
    if card_num[5] != 1 and card_num[5] != 2 and card_num[5] != 3:
        error.append("The sixth character must be 1 2 or 3")
    if card_num[6] != 1 and card_num[6] != 2 and card_num[6] != 3 and card_num[6] != 4:
        error.append("The seventh character must be 1 2 3 or 4")
    one = verify_check_digit(orig)
    if one == False:
        error.append("Check Digit does not match calculated value.")
    if error == []:
        return True
    else:
        return error

#verifys first of the id os valid, then if the check digit is good
def verify_check_digit(card_num : str) -> tuple:
    #one = is_valid(card_num)
    card_num = convert_int(card_num, True)
    count = 0
    total = 0
    while count <= 8:
        total = total + ((count+1) * card_num[count])
        count += 1
    if (total % 10) == card_num[9]:
        return True
    else:
        return False
    
    #''' returns True if the check digit is valid, False if not '''
    


def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    if idnumber[5] == "1":
        return "School of Computing and Engineering SCE"
    elif idnumber[5] == "2":
        return "School of law"
    elif idnumber[5] == "3":
        return "College of Arts and Sciences"
  

def get_grade(idnumber : str) -> str:
    #Returns the grade for index 6'''
    if idnumber[6] == '1':
       return "Freshsman"
    elif idnumber[6] == '2':
        return "Sophmore"
    elif idnumber[6] == '3':
        return "Junior"
    elif idnumber[6] == '4':
        return "Senior"
    else:
        return "Invalid grade"

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result = is_valid(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            error = []
            print(is_valid(card_num))
