from datetime import datetime

class PC(object):

    def __init__(self, id):
        self.id = id
        self.open = True
        self.session_id = ""
        self.session_time = None


    def start(self, id):
        self.session_time = datetime.now()
        self.session_id = id
        self.open = False

    
    def end(self):
        self.session_time = None
        self.session_id = ""
        self.open = True


    def elapsed(self):
        if (self.open): return datetime.now() - datetime.now()
        return datetime.now() - self.time
    

    
        

    
