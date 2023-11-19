# Necessary Imports
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from starlette.responses import JSONResponse
from datetime import time
import uvicorn      

## make sure to import your student and computer object files


app = FastAPI()             

total_users = {} 
users = {} 
queue = {}

@app.get('/', response_class=HTMLResponse)
def get_home(request: Request) -> HTMLResponse:
    with open("index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

## For assigning a computer to a user
## Duration is useful again here so the internal algorithm can have a clock and count down.
@app.post('/user')
def add_student(duration: str):
    #add algorithms here
    return False

## For adding a student to a queue
## Duration is useful so that when the cafe is about to close, student worker can tell them their hours (like hey we close ta 10 when they're here at 8 pm and wanna play for 4 hours)
@app.post('/queue')
def add_queue(duration: str):
  #add algorithms here
  ## This route should be called when all the seats are taken. So in the front end, just query select all, check if they're occupied and if they are,
  # call this route with the duration, ill create the fake student data.
  return False

@app.post('/current_users')
def get_users():
    ## The front end should have an event listener that sends a request to this route when the student worker presses user dashboard.
    return users

@app.post('/current_queue')
def get_queue():
    return queue
if __name__ == "__main__":
  # total_users = {} # total users that came today, dynamically populated
   # users = {} # current users in tec cafe using computers
    #fake_users = [] # fake users container
   # for _ in range (15):
     #   fake_users.append([Tester.createPerson()]) ## [PID (AXXXXXXXX), Name, Time In (YYYY-MM-DD HH:M:S), Duration, Tally (severe), Tally (moderate), Tally (light)]
    
    #print(fake_users)

    ## Test Algorithms
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)