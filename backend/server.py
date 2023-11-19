# Necessary Imports
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from starlette.responses import JSONResponse
from datetime import time
from utilities.Tester import Tester
import uvicorn      

## make sure to import your student and computer object files


app = FastAPI()             

total_users = []
users = {}
queue = {}

## Should actually return users for this as well
@app.get('/', response_class=HTMLResponse)
def get_home(request: Request) -> HTMLResponse:
    with open("index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

## For assigning a computer to a user
## Duration is useful again here so the internal algorithm can have a clock and count down.
@app.post('/user')
def add_student(position: str, duration: str):
    #add algorithms here
    aPerson = Tester.createPerson() ## PID , NAME, TIME IN , DURATION, EXTRA MINUTES, SEVERE TALLY, MODERATE TALLY, LIGHT TALLY
    ## Associate aPerson with a computer and add it to users and total users
    return #.append([str(aPerson[0]), str(aPerson[1]), duration])

@app.delete("/user/{PID}")
def delete_user(PID: str):
    if users[PID]: 
        del users[PID]
    return True
## For adding a student to a queue
## Duration is useful so that when the cafe is about to close, student worker can tell them their hours (like hey we close ta 10 when they're here at 8 pm and wanna play for 4 hours)
@app.post('/queue')
def add_queue(duration: str):
  #add algorithms here
  ## This route should be called when all the seats are taken. So in the front end, just query select all, check if they're occupied and if they are,
  # call this route with the duration, ill create the fake student data.
  aPerson = Tester.createPerson()
  queue[str(aPerson[0])] = [str(aPerson[1]), duration] ## Key: PID, Value: Name, Duration
  return True

@app.delete("/queue/{PID}")
def delete_user(PID: str):
    if queue[PID]:
        del queue[PID]
    return True

@app.post("/export_pdf")
def create_pdf():
    ## Algorithms
    return False

@app.post('/current_users')
def get_users():
    ## The front end should have an event listener that sends a request to this route when the student worker presses user dashboard.
    return users

@app.post('/current_queue')
def get_queue():
    return queue
if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)