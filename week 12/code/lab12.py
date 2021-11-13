## CS 101 Lab
## week 12
## John Chirpich
## jwcgnq@umkc.edu
import csv
import operator
#final = []
dictionary = {}
third = []
#function to get the test file
def get_inputtxt():
    while True:
        try:
            txt_file = input("Enter the name of the input file => ")
            file_txt = txt_file
            txt_file = open(txt_file, "r")
            return file_txt
            close(txt_file)
            break
        except FileNotFoundError:
            print("Could not open", txt_file)
#this function takes the txt file and makes it into a list of all the word in it, then filters them so they are all more than 3 and takes out punctuation 
def create_list(inny):
    #this converts the file to a csv and then reads it line by line
    first = []
    with open(inny, newline = '') as cars:    
        txt_file_write = open(inny, "a")                                                                                      
        car_reader = csv.reader(cars, delimiter=' ')
        for car in car_reader:
            first += car
    second = []
    for word in first:
        if len(word) > 3:
            if "." in word or "!" in word or "?" in word or "," in word:
                second.append(word[:-1].lower())
            else:
                second.append(word.lower())
    return second
#converts the list into a dictionary
def create_dict(lst):
    for word in lst:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    


#runs functions
inny = get_inputtxt()
secondlist = create_list(inny)
create_dict(secondlist)
sorted_d = dict( sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))
list_of_keys = list(sorted_d)
#prints all the info, its kinda messy :)
print("Most frequently used words")
print("#       word         freq")
print("==========================")
print("1", "     ", list_of_keys[0], "        ", sorted_d[list_of_keys[1]])
number =0
try:
    number += 1
    print(number, "     ", list_of_keys[number], "        ", sorted_d[list_of_keys[number]])
except IndexError:
    pass
try:
    number += 1
    print(number, "     ", list_of_keys[number], "        ", sorted_d[list_of_keys[number]])
except IndexError:
    pass
try:
    number += 1
    print(number, "     ", list_of_keys[number], "        ", sorted_d[list_of_keys[number]])
except IndexError:
    pass
try:
    number += 1
    print(number, "     ", list_of_keys[number], "        ", sorted_d[list_of_keys[number]])
except IndexError:
    pass
try:
    number += 1
    print(number, "     ", list_of_keys[number], "        ", sorted_d[list_of_keys[number]])
except IndexError:
    pass
try:
    number += 1
    print(number, "     ", list_of_keys[number], "        ", sorted_d[list_of_keys[number]])
except IndexError:
    pass
try:
    number += 1
    print(number, "     ", list_of_keys[number], "        ", sorted_d[list_of_keys[number]])
except IndexError:
    pass
try:
    number += 1
    print(number, "     ", list_of_keys[number], "        ", sorted_d[list_of_keys[number]])
except IndexError:
    pass
try:
    number += 1
    print(number, "     ", list_of_keys[number], "        ", sorted_d[list_of_keys[number]])
except IndexError:
    pass
#this while loop will get the numebr of words that only show up once
count = 0
once = 0
while count < len(list_of_keys):
    if dictionary[list_of_keys[count]] == 1:
        once +=1
    count +=1
print("\nThere are", once, "words that occur only once")
print("There are", len(list_of_keys), "unique words in this document")
