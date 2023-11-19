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
                    Evaluator.students[PID].update({PID: [Name, str(count), str(int(Evaluator.students[PID]) + int(Extra_Time)), [S_Tally, M_Tally, L_Tally]]})
                else:
                    Evaluator.students[PID] = [Name, str(count), str(Extra_Time), [S_Tally, M_Tally, L_Tally]]
    
    def evaluate(self, month):
        if not os.path.exists(os.getcwd() + "\\scores\\"):
                os.makedirs(os.getcwd() + "\\scores\\")
        if not os.path.exists(os.getcwd() + "\\scores\\" + month):
                os.makedirs(os.getcwd() + "\\scores\\" + month)   
        File = os.path.join(os.getcwd() + "\\scores\\" + month, month + "_ScoreData.csv")     
        with open(File, 'w', newline='') as file:
            writer = csv.writer(file)   
            field = ["PID", "Name", "Responsibility Score Deduction, Tallies (Severe, Moderate, Light)"]
            writer.writerow(field)

            for PID in Evaluator.students:
                score = (2) * float(Evaluator.students[PID][1]) * (float(Evaluator.students[PID][2])/10) + (1.5) * float(Evaluator.students[PID][2])
                data = Evaluator.students[PID]
                writer.writerow([PID, data[0], score, [data[3][0], data[3][1], data[3][2]]])

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

