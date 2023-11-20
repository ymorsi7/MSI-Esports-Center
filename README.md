<img src = "https://cdn.dribbble.com/users/3144264/screenshots/16080159/media/76c03dd932c1e3f797c3fb5869826de9.png"  height = "75"> <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Seal_of_the_University_of_California%2C_San_Diego.svg/1200px-Seal_of_the_University_of_California%2C_San_Diego.svg.png"  height = "75">

References:
Christine Fan - EDU Program Lead (Integrated Marketing, North America Region)<br>
christinefan@msi.com

Chris Griebenow - ESports Director @ UCSD<br>
cgriebenow@ucsd.edu

# MSI Hackathon (UC San Diego)
For the 2023 MSI Hackathon, we were assigned to solve the ongoing challenge of queue management and user trackability at TEC Cafe, located at the University of California, San Diego. The challenge was to improve the efficiency of the current system they had in place, which was a scan-in-and-use methodology, and streamline it as much as possible.

We were recommended to focus on three specific features:
- Queue Management with ID Scanning
- User Metric Tracking for each PC
- Scalability of the implemented system

As these were our core, we also concluded that helper services may be of additional use such as:
- An integrated exclusive TEC AI-chat bot for student workers to ask questions related to data metrics.
- Easy-to-use user interface where the student worker can assign which computers to use.
- Custom Data Analytics, including an analysis of when students might need more time based on scan-in.
    - Archival of Daily Data which keeps track of all students that scanned in along with their playtime and expected extra time.
    - The ability to export the metrics into a PDF for each day.
    - An internal algorithm that evaluates the student's "Responsibility Score" and how credible they are.

We also have an [added feature](https://tecguest.netlify.app/) for future scalability where students will have to input how long they'll play for and automatically lock them if they exceed them. 

## Flow
### Layout
When a student walks into the TEC Cafe, they are expected to scan in. This initial scan is saved on the student workers' laptop and is assumed to store their PID, Name, and Time Stamp in. If this scan is valid, the student worker is allowed to choose from the available computers listed on their interface. A computer with no color indicates availability, green represents in use, and red represents overdue. The student worker must input how long they are going to play when they choose a computer position for that student.

### User Dashboard
When the student worker inputs the number of hours the student will play, the information will show up on the User Dashboard. The User Dashboard is a collection of all the students currently playing within TEC Cafe and displays their PID, Name, Scan in Time, Hours they'll play, and the position of their computers. This allows the student worker to easily see which student is at where and easy access to their information.

### Analytics
The Analytics section is a helper service dedicated to helping TEC Cafe run much more smoothly. It features a time series analysis that shows when students are more likely to need more time relative to when they scan in. Below the graph, student workers have the ability to export the previous day's PDF, which generates a table consisting of all the PIDs, names of the students, Total Hours they played, Extra Time they took, and different severity of warnings they received on that time.

You will also see that on all sections, there is a blue icon on the bottom right, which is a custom-built AI chatbot built exclusively for TEC Cafe. Student workers have the freedom to ask questions as it is trained on all the previous CSV data our service has generated. A question could be, how many students came on November 9th, or which student came to our cafe the most during November? Using this, student workers can figure out who's the most frequent visitor as well as who's the frequent troublemaker.

You can generate a custom PDF. Here is the PDF:
![image](https://github.com/ymorsi7/MSI-Esports-Center/assets/85778372/ae6ecc9a-1242-4c33-86e2-a7b4e9accb20)


### Queue
The queue is designed to showcase all students who scan in but computer positions are taken. The queue displays the PID, the name, and the hours they're going to play. The expected hours are critical as the student worker can advise that they are closing in an hour when the student wants to play for more than an hour. When TEC Cafe is filled, students are still responsible for scanning in. When a seat opens up, it will go from green to a noncolor on the computer layout. The student worker can then see who's the first student on the queue, and call their name.

It is also very flexible. The reason why we didn't have it so that you're in the queue only when the cafe is full is because what if you want to grab lunch first but be next in line. You can register for your spot but this is up to the student worker. If the person is taking too long, the student worker can remove them from the queue.
### Custom TEC AI Chatbox
Our custom TEC AI Chatbox is trained on previous data depending on the specifications. This means that if you want it on one day, on a month, or even on a year, you can do so. This tool is very powerful as it allows analytics of data using AI. For example, you can ask various questions about the data without having to do work on the data.

Here are working examples of the Chat AI Bot.
![image](https://github.com/ymorsi7/MSI-Esports-Center/assets/85778372/1b99bc3e-7e4c-4bfc-9ead-136b3bd2ee66)

As shown, if you have custom metrics you keep track of, the AI can answer based on the data provided.

## Technical Documentation
### RESTFful System Design
In our system design, we're adhering to a principle called RESTful which stands for representation state transfer and allows for the simple interaction between web services without intense processing.

There are 4 components to a RESTful system.
```python
@app.get() # Associated with retrieving information
@app.post() # Associated with adding information
@app.put() # Associated with updating information
@app.delete() # Associated with deleting information
```

These 'routes' allow for the web browser to communicate with our system and request different information based on the activity.

### Data Analytics
There is a custom Test generator that generates fake mock data in which we can test our internal responsibility metric evaluation.

There are 6 methods that are static, meaning they do not require an object to use.
```python
class Tester:
    @staticmethod
    def createTest(number):
        month = datetime.datetime.now().strftime("%B")
        if not os.path.exists(os.getcwd() + "\\data\\"):
            os.makedirs(os.getcwd() + "\\data\\")
        if not os.path.exists(os.getcwd() + "\\data\\" + month):
                os.makedirs(os.getcwd() + "\\data\\" + month)
        File = os.path.join(os.getcwd() + "\\data\\" + month, str(datetime.date.today()) + "_TestData.csv")     
        with open(File, 'w', newline='') as file:
            writer = csv.writer(file)   
            field = ["PID", "Name", "Time In", "Total Hours (H)", "Extra Time (Minutes)", "Severe", "Moderate", "Light"]
            writer.writerow(field)

            for _ in range (number):
               writer.writerow([Tester.__generatePID(), Tester.__generateName(), Tester.__generateTimeIn(), Tester.__generateNumber(0,4), Tester.__generateNumber(0,60), Tester.__generateNumber(0,1), Tester.__generateNumber(0,2), Tester.__generateNumber(0,3)])

    @staticmethod
    def createPerson():
        return [Tester.__generatePID(), Tester.__generateName(), Tester.__generateTimeIn(), Tester.__generateNumber(0,60), 0, 0, 0]
    
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
```

Our custom evaluator is not static though as it is meant to be ran every month.
```python
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
```

Our built in PDF features several core helper libraries and is shown below:
```python
import csv
from datetime import timedelta
import datetime
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
import os
class PDF:
    @staticmethod
    def createPDF():
        file = os.path.join(os.getcwd() + "\\backend\\utilities/", "TestData.csv")     
        with open(file, "r") as csvfile:
            data = list(csv.reader(csvfile))

        elements = []

        styles = getSampleStyleSheet()
        styleNormal = styles['Normal']

        line1 = 'UC San Diego TEC Center Daily User Report'
        line2 = 'Date: {}'.format(datetime.datetime.now().strftime("%m-%d-%Y"))
        elements.append(Paragraph(line1, styleNormal))
        elements.append(Paragraph(line2, styleNormal))
        elements.append(Spacer(inch, .25 * inch))


        all_cells = [(0, 0), (-1, -1)]
        header = [(0, 0), (-1, 0)]
        column0 = [(0, 0), (0, -1)]
        column1 = [(1, 0), (1, -1)]
        column2 = [(2, 0), (2, -1)]
        column3 = [(3, 0), (3, -1)]
        column4 = [(4, 0), (4, -1)]
        column5 = [(5, 0), (5, -1)]
        column6 = [(6, 0), (6, -1)]
        table_style = TableStyle([
            ('VALIGN', all_cells[0], all_cells[1], 'TOP'),
            ('LINEBELOW', header[0], header[1], 1, colors.black),
            ('ALIGN', column0[0], column0[1], 'LEFT'),
            ('ALIGN', column1[0], column1[1], 'LEFT'),
            ('ALIGN', column2[0], column2[1], 'LEFT'),
            ('ALIGN', column3[0], column3[1], 'RIGHT'),
            ('ALIGN', column4[0], column4[1], 'RIGHT'),
            ('ALIGN', column5[0], column5[1], 'LEFT'),
            ('ALIGN', column6[0], column6[1], 'RIGHT'),
        ])

        colWidths = [
            2.2 * cm, 
            3.6 * cm,  
            4.2 * cm,  
            2 * cm,  
            3.6 * cm,  
            1.7 * cm,  
            1.5 * cm, 
            1.5 * cm
        ]

        for index, row in enumerate(data):
            for col, val in enumerate(row):
                if col != 5 or index == 0:
                    data[index][col] = val.strip("'[]()")
                else:
                    data[index][col] = Paragraph(val, styles['Normal'])

        t = Table(data, colWidths=colWidths)
        t.setStyle(table_style)
        elements.append(t)
        if not os.path.exists(os.getcwd() + "/backend/PDF/"):
            os.makedirs(os.getcwd() + "/backend/PDF/")
        archivo_pdf = SimpleDocTemplate(
            'backend/PDF/TEC_{}.pdf'.format((datetime.datetime.now() - timedelta(1)).strftime('%Y-%m-%d')),
            pagesize=letter,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=28)
        archivo_pdf.build(elements)
        return 'TEC_{}.pdf'.format((datetime.datetime.now() - timedelta(1)).strftime('%Y-%m-%d'))
```
