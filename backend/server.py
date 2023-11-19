# Necessary Imports
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response, FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import time
from utilities.Tester import Tester
from utilities.PDF import PDF
import uvicorn      
import os

## make sure to import your student and computer object files

app = FastAPI()             
app.mount("/src", StaticFiles(directory="src/"), name="src")
total_users = []
users = {}
queue = {}

## Should actually return users for this as well
@app.get('/', response_class=HTMLResponse)
def get_home(request: Request) -> HTMLResponse:
    with open("src/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

## For assigning a computer to a user
## Duration is useful again here so the internal algorithm can have a clock and count down.
@app.post('/user')
def add_student(position: str, duration: str):
    aPerson = Tester.createPerson() ## PID , NAME, TIME IN , DURATION, EXTRA MINUTES, SEVERE TALLY, MODERATE TALLY, LIGHT TALLY
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

@app.get('/pdf/{pdf_path}', response_class=HTMLResponse)
def get_home(pdf_path: str) -> FileResponse:
    headers = {
        "Content-Disposition": "inline; filename=sample.pdf"
    }  
    
    location = os.getcwd() + "/backend/PDF/" + pdf_path
    response = FileResponse(location, media_type="application/pdf", headers=headers)
    return response


@app.post('/export_pdf')
def get_pdf():
    date = PDF.createPDF()
    return date

@app.post('/current_users')
def get_users():
    ## The front end should have an event listener that sends a request to this route when the student worker presses user dashboard.
    return users

@app.post('/current_queue')
def get_queue():
    return queue

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)