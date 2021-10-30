## CS 101 Lab
## week 8
## John Chirpich
## jwcgnq@umkc.edu

#declare vars
test = []
programs = []
Tminum = []
Tmaxim = []
Pminum = []
Pmaxim = []

#function to calculate standard deviation
def stand(list):
    mean = sum(list) / len(list)
    variance = sum([((x - mean) ** 2) for x in list]) / len(list)
    res = variance ** 0.5
    return res
#function nto find average
def Average(lst):
    return sum(lst) / len(lst)
#function to display the menue and get what choice the user makes
def menue():
    print("\n         Grade Menu")
    print("1 - Add Test\n2 - Remove Test\n3- Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit")
    choice = input("==> ")
    check = True
    #checks if the user input is valid
    while check:
        try:
            choice = int(choice)
            if choice < 0 or choice > 6:
                print("Invalid choice")
            else:
                break
        except:
            if choice != "d" and choice != "q":
                print("Invalid choice")
            else:
                break
        choice = input("==> ")
    return choice
#prints and calculates the score table
def Display_scores():
    #find test max/min
    try:
        if min(test) == 0:
            Tminum = "n/a"
        else:
            Tminum = min(test)
        if max(test) == 0:
            Tmaxim = "n/a"
        else:
            Tmaxim = max(test)
    except ValueError:
        Tmaxim = "n/a"
        Tminum = "n/a"
    #find program max and min
    try:
        if min(programs) == 0:
            Pminum = "n/a"
        else:
            Pminum = min(programs)
        if max(programs) == 0:
            Pmaxim = "n/a"
        else:
            Pmaxim = max(programs)
    except ValueError:
        Pmaxim = "n/a"
        Pminum = "n/a"
    #get the average
    try:
        tAvg = "{:.2f}".format(Average(test))
        
    except ZeroDivisionError:
        tAvg = "n/a"

    try:
        pAvg = "{:.2f}".format(Average(programs))
    except ZeroDivisionError:
        pAvg = "n/a"
    #get standard deviation
    try:
        Pstd = "{:.2f}".format(stand(programs))
    except:
        Pstd = "n/a"
    try:
        Tstd = "{:.2f}".format(stand(test))
    except:
        Tstd = "n/a"
    #gets the weighted grade
    try:
        weight = "{:.2f}".format(((Average(test) * .6) + (Average(programs) * .4)))
    except:
        weight = "0.0"
    print("Type         #       min      max    avg    std")
    print("==================================================")
    print("Tests       ", len(test), "     ", Tminum,"   ", Tmaxim, "   ", tAvg, "   ", Tstd   )
    print("Programs    ", len(programs), "     ", Pminum,"   ", Pmaxim, "   ", pAvg,"   ", Pstd   )
    print("\n The weighted score is      ", weight)

choice = menue()
#runs the menue function and all the "simple" choices
while True:
    #display scores
    if choice == "d":
        Display_scores()
        choice = menue()
    #add test
    elif choice == 1:
        try:
            score = float(input("Enter the new Test score 0-100 ==> "))
            while score < 0:
                print("Score must be more than 0")
                score = float(input("Enter the new Test score 0-100 ==> "))
            test.append(score)
        except:
            print("INVALID SCORE")
        choice = menue()
    #remove test
    elif choice == 2:
        while True:
            try:
                score = float(input("Enter the test to remove => "))
                break
            except:
                print("Invalid input")
        try:
            test.remove(score)
        except ValueError:
            print("SCORE NOT FOUND")
        choice = menue()
    #clear tests
    elif choice == 3:
        test = []
        print("ALL TESTS DELETED")
        choice = menue()
    #Add assignment (also referenced as program)
    elif choice == 4:
        try:
            score = float(input("Enter the new program score 0-100 ==> "))
            while score < 0:
                print("Score must be more than 0")
                score = float(input("Enter the new Program score 0-100 ==> "))
            programs.append(score)
        except:
            print("INVALID SCORE")
        choice = menue()
    #remove assignment
    elif choice == 5:
        while True:
            try:
                score = float(input("Enter the program to remove => "))
                break
            except:
                print("Invalid input")
        try:
            programs.remove(score)
        except ValueError:
            print("SCORE NOT FOUND")
        choice = menue()
    #clear assignments
    elif choice == 6:
        programs = []
        print("ALL PROGRAMS DELETED")
        choice = menue()
    #because the menue all ready checks if the input is correct and the code beofre this accounts for all the choices, all this does is quit the program when q is selceted
    else:
        break
