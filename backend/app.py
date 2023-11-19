# Solution to track/manage (user session) times at each PC
# Goal: improve (queue time) and streamline organization of (TEC usage).

# Recommendation
# 1. Queue management with PID
# 2. Track (user session) for each PC
# 3. Make layout/status of PC managable, for scalibility.
from Student import make_student
import Comp

from flask import Flask

app = Flask(__name__)
@app.route("/")         # Runs when root is reached
def main():
    computers = {}
    queue = []
    for alp, num in zip(["A","B","C","D","E"], [5,5,6,6,4]):
        for i in range(1,num+1):
            computers[alp+str(i)] = Comp.Comp(alp+str(i))

    # for comp in computers.values(): print(comp.cid)        # list all computers.

    def assign(cid, pid, desired_time):
        if computers[cid].open:
            computers[cid].start(pid, desired_time)

    def enqueue(pid):
        queue.insert(pid)

if __name__ == "__main__":
    app.run("localhost", 6969)
