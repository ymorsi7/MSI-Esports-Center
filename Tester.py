import csv
import names
from random import randint
import random as random
import datetime

class Person:
    @staticmethod
    def createTest(number):
        with open(str(datetime.date.today()) + "_TestData.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["PID", "Name", "Time In", "Total Hours", "Extra Time"]
            writer.writerow(field)

            for _ in range (number):
               writer.writerow([Person.__generatePID(), Person.__generateName(), Person.__generateTimeIn(), Person.__generateNumber(1,4), Person.__generateNumber(0,60)])

    @staticmethod
    def __generatePID():
       range_start = 10**(8-1)
       range_end = (10**8)-1
       return "A" + str(randint(range_start, range_end))
    
    @staticmethod
    def __generateName():
        rand_name = names.get_full_name(gender='male')
        return rand_name

    @staticmethod
    def __generateTimeIn():
        rtime = int(random.random()*86400)
    
        hours   = int(rtime/3600)
        minutes = int((rtime - hours*3600)/60)
        seconds = rtime - hours*3600 - minutes*60
    
        time_string = '%02d:%02d:%02d' % (hours, minutes, seconds)
        return str(datetime.date.today()) + " " + time_string
    
    @staticmethod
    def __generateNumber(min, max):
        return str(randint(min, max))

if __name__ == "__main__":
    Person.createTest(100)