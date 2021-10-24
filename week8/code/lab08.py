## CS 101 Lab
## week 8
## John Chirpich
## jwcgnq@umkc.edu
import csv
#promts the user for the mpg and checks if it is within reason
def get_minmpg():
    while True:
        try:
            min_mpg = int(input("Enter minimum mpg => "))
            if min_mpg > 100:
                print("Fuel economy must be less than 100")
            elif min_mpg < 0:
                print("Fuel economy must be more than 0")
            else:
                return min_mpg
                break
        except ValueError:
            print("You must enter a number for fuel economy.")
        
#promts user for the input text and it makes sure it exists
def get_inputtxt():
    check = True
    while check:
        try:
            txt_file = input("Enter the name of the input vechile file => ")
            file_txt = txt_file
            txt_file = open(txt_file, "r")
            return file_txt
            close(txt_file)
            check = False
            break
        except FileNotFoundError:
            print("Could not open", txt_file)
#promts user for the output text and it makes sure it exists
def get_outputtxt():
    check = True
    while check:
        try:
            txt_file = input("Enter the name of file to outout to => ")
            file_txt = txt_file
            txt_file = open(txt_file, "r")
            return file_txt
            close(txt_file)
            check = False
            break
        except FileNotFoundError:
            print("Could not open", txt_file)
        except OSError:
            print('There was an os error, please try again')
#this is the main function for finding the cars within the given mpg
def crawl(min_mpg, inny, outty):
    #this prepares to open all the files and writes the key for the output text
    txt_file = open(inny, "r")
    txt_file_write = open(outty, "a")
    txt_file_write.write("year  make    model	cylinders	trany	VClass	displ	combinedmpg	citympg	highwaympg\n")
    #this converts the file to a casv and then reads it line by line to get the average mpg
    with open(inny, newline = '') as cars:    
        txt_file_write = open(outty, "a")                                                                                      
        car_reader = csv.reader(cars, delimiter='\t')
        for car in car_reader:
            try:
                avg_mpg = int(car[-2])
                if min_mpg < avg_mpg:
                    final = "   ".join(car)
                    final = final + "\n"
                    txt_file_write = open(outty, "a") 
                    txt_file_write.write(final)
            except:
                print("There was an error resulting from this line: ", car)
    return "Done"


#runs functions
min_mpg = get_minmpg()
inny = get_inputtxt()
outty = get_outputtxt()
print(crawl(min_mpg, inny, outty))



