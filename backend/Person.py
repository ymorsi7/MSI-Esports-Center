class Person:
    pid = ""
    name = ""
    time_in = None
    total_hours = None      # timedelta format
    overage_hours = None    # credit score
    overage_severity = None

    def __init__(self, pid, name):
        self.name = name
        self.major = major


    def update_usage(self, elapsed):
        total_usage += elapsed

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
               writer.writerow([Person.__generatePID(), Person.__generateName(), Person.__generateTimeIn(), Person.__generateNumber(0,4), Person.__generateNumber(0,60), Person.__generateNumber(0,1), Person.__generateNumber(0,2), Person.__generateNumber(0,3)])

    @staticmethod
    def createPerson():
        return [Person.__generatePID(), Person.__generateName(), Person.__generateTimeIn(), Person.__generateNumber(0,60), 0, 0, 0]
    
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


