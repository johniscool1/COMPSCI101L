## CS 101 Lab
## Program 3
## John Chirpich
## jwcgnq@umkc.edu
import random
totalspins = 0
orgbank = 0
newhigh = 0
#function to get the random numebrs for the spins
def spin():
    x = random.randint(1,10)
    return x

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    answer = input("Do you want to play again?\n")
    while answer != "YES" and answer != "Y" and answer != "NO" and answer != "N" and answer != "n" and answer != "y":
        print("You must enter Y/YES/N/NO to conitnue. please try again")
        answer = input("Do you want to play again?\n")
    if answer == "n" or answer == "N" or answer == "NO":
        return False
    return True

     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wage = int(input("How many chips do you want to wager?\n"))
    while wage <= 0:
        print("Error: You can only choose 1 - 100 chips")
        wage = int(input("How many chips do you want to wager?\n"))
    while wage > bank:
        print("That is more than the amount of chips in your bank")
        print("Your current bank is", bank)
        wage = int(input("How many chips do you want to wager?\n"))
    return wage       

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    spin1 = spin()
    spin2 = spin()
    spin3 = spin()
    global totalspins
    totalspins += 1
    return spin1, spin2, spin3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc and reelc == reelb:
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0 

def get_bank() -> int:
    global orgbank
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input("Enter the amount of chips you want to start with: \n"))
    while bank <= 0 or bank > 100:
        print("Error: value must be more than 0 and less than or equal to 100.")
        bank = int(input("Enter the amount of chips you want to start with: \n"))
    orgbank = bank
    return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 2
    else:
        return wager * -1  
#function to get the highest amount you got to   
def highest_spin(bank):
    global newhigh
    if bank > newhigh:
        newhigh = bank


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            highest_spin(bank)           
        print("You lost all", orgbank, "in", totalspins, "spins")
        print("The most chips you had was", newhigh)
        playing = play_again()
