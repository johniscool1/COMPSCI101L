## CS 101 Lab
## week 13
## John Chirpich
## jwcgnq@umkc.edu
import time


class clock():
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        #self.after = after
    def tick(self):
        if self.hours == 12 and self.minutes == 59 and self.seconds == 59:
            #print("1")
            self.hours = 1
            self.seconds = 0
            self.minutes = 0
            #self.hours = "{:02}".format(self.hours)
            #self.after += 1
            #if (self.after % 2) == 0:
                #noon = "pm"
            return self.hours, self.minutes, self.seconds,
        elif self.minutes == 59 and self.seconds == 59:
            #print("2")
            self.minutes = 0
            self.seconds = 0
            self.hours += 1
            return self.hours, self.minutes, self.seconds
        elif self.seconds < 59:
            #print("3")
            self.seconds += 1
            #self.seconds = "{:02}".format(self.seconds)
            return self.hours, self.minutes, self.seconds
        elif self.seconds == 59:
            #print("4")
            self.seconds = 0
            self.minutes += 1
            return self.hours, self.minutes, self.seconds
        


while True:
    try:
        hour = int(input("Enter the current hour ==> "))
        break
    except ValueError:
        print("Invalid input")
while True:
    try:
        minute = int(input("Enter the current minute ==> "))
        break
    except ValueError:
        print("Invalid input")
while True:
    try:
        sec = int(input("Enter the current second ==> "))
        sec -= 1
        break
    except ValueError:
        print("Invalid input")

    
        

one = clock(hour,minute,sec)
#the after varialbe determines if its am or pm
after = 1
while True:
    answer = one.tick()
    if answer[0] == 12 and answer[1] == 0 and answer[2] == 0:
        after += 1
    if after % 2 == 0:
        latin = "pm"
    else:
        latin = "am"
    print("{:02}".format(answer[0]), ":", "{:02}".format(answer[1]),":", "{:02}".format(answer[2]), " ", latin, sep= "")
    time.sleep(1)
