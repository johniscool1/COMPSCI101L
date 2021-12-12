## CS 101 Lab
## week 14
## John Chirpich
## jwcgnq@umkc.edu
import math
def total(values):
    tot = 0
    for i in values:
        tot += i
        tot = float(tot)
    return tot
def average(values):
    if values == []:
        return math.nan
    else:
        tot = float(sum(values)) / float(len(values))
        return tot
def median(values):
    if values == []:
        raise ValueError()

    else:

        if len(values) % 2 != 0:
            values.sort()
            middle = (len(values) /2) +.5
            #print("odd")
            return values[int(middle)-1]
        
        else:
            values.sort()
            medians = []
            middle_one = len(values) /2
            middle_two = middle_one + 1
            medians.append(middle_one)
            medians.append(middle_two)
            #print("even")
            return average(medians)
