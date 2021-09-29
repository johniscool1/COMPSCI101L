#CS 101 Lab
#Program 2
#John Chirpich
#jwcgnq@umkc.edu
three = 0
count = 1
guess = []
seven = []
list1 = []
list2 = []
list3 = []
while count <= 100:
    guess.append(count)
    count +=1
print("Welcome to the Flarsheim Guesser!")
check = 1
while check == 1:
    list1 = []
    list2 = []
    list3 = [] 
    play_again = 0
    count = 0
    print("\nPlease think of a number between and including 1 and 100.\n")
    three = int(input("What is the remainder when your number is divided by 3 ?"))
    while three >= 3 or three < 0:
        print("The value entered must be less than 3 and more than 0.")
        three = int(input("What is the remainder when your number is divided by 3 ?"))
    while count < len(guess)-1:
        if (guess[count] % 3) == three:
            list1.append(guess[count])
        count += 1

    five = int(input("What is the remainder when your number is divided by 5 ?"))
    while five >= 5 or five < 0:
        print("The value entered must be less than 5 and more than 0.")
        five = int(input("What is the remainder when your number is divided by 5 ?"))
    count = 0
    while count < len(list1)-1:
        if (list1[count] % 5) == five:
            list2.append(list1[count])
        count += 1

    eight = int(input("What is the remainder when your number is divided by 7 ?"))
    while eight >= 7 or eight < 0:
        print("The value entered must be less than 7 and more than 0.")
        eight = int(input("What is the remainder when your number is divided by 7 ?"))
    count = 0
    while count < len(list2)-1:
        if (list2[count] % 7) == eight:
            list3.append(list2[count])
        count += 1
    print("Your number was", list3[0])
    print("How amazing was that?\n")
    play_again = 0
    play_again = input("Do you want to play again? Y to continue, N to quit. ")
    while play_again != "y" and play_again != "Y" and play_again != "n" and play_again != "N":
        play_again = input("Do you want to play again? Y to continue, N to quit. ")
    if play_again == "N":
        break
    elif play_again == "n":
        break
    elif play_again == "y" and play_again == "Y":
        list1 = []
        list2 = []
        list3 = []      
        pass    
