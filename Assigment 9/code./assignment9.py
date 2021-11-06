## CS 101 Lab
## week 9
## John Chirpich
## jwcgnq@umkc.edu
import calendar
import csv
big_list = []
dates = {}
months = {}
offense = {}
byzip = {}
#function to turn the numebr of the month to the actual month
def month_from_number(number):
    return calendar.month_name[number]
#reads the file and creates a list of the contents
def read_in_line(filename):
    file = open(filename, encoding="utf-8")
    file_csv = csv.reader(file)
    for line in file_csv:
        big_list.append(line)
    big_list.pop(0)
#function to get a valid input filename
def get_inputtxt():
    check = True
    while check:
        try:
            txt_file = input("Enter the name of the crime data file => ")
            file_txt = txt_file
            txt_file = open(txt_file, "r")
            return file_txt
            close(txt_file)
            check = False
            break
        except FileNotFoundError:
            print("Could not open", txt_file)
#makes a dictionary of dates in which cromes were commited
def create_reported_date_dict(list):
    for key in list:
        try:
            if key[1] not in dates:
                dates[key[1]] = 1
            else:
                dates[key[1]] = dates[key[1]] + 1
        except:
            pass

#creates a dictionary of crimes by month
def create_reported_month_dict(list):
    for key in list:
        try:
            if key[1][:2] not in months:
                months[key[1][:2]] = 1
            else:
                months[key[1][:2]] = months[key[1][:2]] + 1
        except:
            pass

#creates a dictonary of what type and how many 
def create_offense_dict(list):
    for key in list:
        try:
            if key[7] not in offense:
                offense[key[7]] = 1
            else:
                offense[key[7]] = offense[key[7]] + 1
        except:
            pass
#creates a dictionary of offenses and what zip codes they were in
def create_offense_by_zip(list):
    for key in list:
        #print(key[7])
        #print(byzip[key[7][13]])
        #try:
        
        if key[7] not in byzip:
            #print("1")
            #print(key[7])
            #print(key[13])
            #print(key[13])
            byzip[key[7]] = {key[13] : 1 }
            #print(byzip)
            #byzip[key[7]][key[13]]
    
        elif key[13] in byzip[key[7]]:
            #print("2")
            #print(key)
                #print(byzip[key[7][13]])
            byzip[key[7]][key[13]] += 1
                    
        elif key[13] not in byzip[key[7]]:
            #print("3")
               # print(byzip[key[7][13]])
            byzip[key[7]][key[13]] = 1

        else:
            print("Error")
        #except:
            #print(byzip[key[7]])
            #pass
        #print(byzip)

            
#runs all the functions
inny = get_inputtxt()
read_in_line(inny)
create_reported_date_dict(big_list)
by_month = create_reported_month_dict(big_list)
create_offense_dict(big_list)
create_offense_by_zip(big_list)
#gives the user the info
large_month = max_key = max(months, key=months.get)
print("The month with the higest # of crimes is", month_from_number(int(large_month)), "with", months[large_month], "offenses.")
large_offense = max_key = max(offense, key=offense.get)
print("The offense with the highest # of crimes is", large_offense, "With", offense[large_offense], "Offenses.")
while True:
    search = input("Enter an offense => ")
    if search in offense:
        break
    else:
        print("Not a valid offense found, please try again")
print(search, "offenses by zip code")
print("Zip code     # of offenses")
print("==========================")
print("             ", offense[search])
for zip in byzip[search]:
    if zip == "":
        print("Unknown zips:", byzip[search][zip])
    else:
        print(zip,"       ", byzip[search][zip])
