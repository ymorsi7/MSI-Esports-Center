from datetime import datetime

class Comp(object):

    def __init__(self, cid):
        self.cid = cid
        self.open = True
        self.sesh_id = None
        self.sesh_start = None
        self.sesh_desired = None


    def start(self, pid, desired_time):
        self.sesh_start = datetime.now()
        self.sesh_desired = desired_time
        self.sesh_id = pid
        self.open = False

    
    def end(self):
        student[self.session_id].update_usage(self.elapsed())
        self.open = True
        self.sesh_id = None
        self.sesh_start = None
        self.sesh_desired = None


    def elapsed(self):
        if (self.open): return datetime.now() - datetime.now()
        return datetime.now() - self.sesh_start
    

    def is_over(self):
        return (datetime.now() - self.sesh_start > self.sesh_desired)

# def strfdelta(tdelta, fmt):
#     d = {}
#     d["days"] = tdelta.days
#     d["hours"], rem = divmod(tdelta.seconds, 3600)
#     d["minutes"], d["seconds"] = divmod(rem, 60)
#     return fmt.format(**d)
    
        

    
