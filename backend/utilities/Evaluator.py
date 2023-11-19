from csv import reader
import glob
import os
import datetime
import csv

class Evaluator:
    students = {}

    def __init__(self, filePath):
        files = glob.glob(filePath)
        for file in files:
            Reader = reader(open(file))
            header = next(Reader) # if there is a header
            for PID, Name, Time_In, Total_Time, Extra_Time, S_Tally, M_Tally, L_Tally in Reader:
                count = 0
                if PID in Evaluator.students:
                    count += 1
                    data = Evaluator.students[PID]
                    Evaluator.students[PID].update({PID: [Name, str(data[1] + Total_Time), str(count + data[2]), str(int(data[3]) + int(Extra_Time)), [data[4] + S_Tally, data[5] + M_Tally, data[6] + L_Tally]]})
                else:
                    Evaluator.students[PID] = [Name, str(Total_Time), str(count), str(Extra_Time), [S_Tally, M_Tally, L_Tally]]
    
    def evaluate(self, month):
        if not os.path.exists(os.getcwd() + "\\scores\\"):
                os.makedirs(os.getcwd() + "\\scores\\")
        File = os.path.join(os.getcwd() + "\\scores\\", month + "_ScoreData.csv")     
        with open(File, 'w', newline='') as file:
            writer = csv.writer(file)   
            field = ["PID", "Name", "Total Time", "Counts", "Extra Time", "Responsibility Score Deduction", "Tallies (Severe, Moderate, Light)"]
            writer.writerow(field)

            for PID in Evaluator.students:
                score = (2) * float(Evaluator.students[PID][2]) * (float(Evaluator.students[PID][3])/10) + (1.5) * float(Evaluator.students[PID][3])
                data = Evaluator.students[PID]
                writer.writerow([PID, data[0], data[1], data[2], data[3], score, [data[4][0], data[4][1], data[4][2]]])

if __name__ == "__main__": 
    list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = input("Enter the month you want to evaluate:")
    month = month.title()
    while month not in list:
        print("Not a valid month")
        month = input("Enter the month you want to evaluate:")

    while not os.path.exists(os.getcwd() + "\\data\\" + month):
        print("There is no data for that month.")
        month = input("Enter the month you want to evaluate:")

    filePath = os.getcwd() + "\\data\\" + month + "\\*.csv"
    anEvaluator = Evaluator(filePath)
    anEvaluator.evaluate(month)
    #print(anEvaluator.students)