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

@app.get('/', response_class=HTMLResponse)
def get_home(request: Request) -> HTMLResponse:
    with open("index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

## For assigning a computer to a user
@app.post('/user')
def add_student(duration: str):
    #add algorithms here
    return False

## For adding a student to a queue
@app.post('/queue')
def add_person(duration: str):
  #add algorithms here
  return False

@app.post('/current_users')
def return_users():
    return users


if __name__ == "__main__":
  # total_users = {} # total users that came today, dynamically populated
   # users = {} # current users in tec cafe using computers
    #fake_users = [] # fake users container
   # for _ in range (15):
     #   fake_users.append([Person.createPerson()]) ## [PID (AXXXXXXXX), Name, Time In (YYYY-MM-DD HH:M:S), Duration, Tally (severe), Tally (moderate), Tally (light)]
    
    #print(fake_users)

    ## Test Algorithms
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)