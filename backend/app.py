# Necessary Imports
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse        
from fastapi.staticfiles import StaticFiles      
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from datetime import time
from utilities.Tester import Person
import random
import threading
import uvicorn      # Used for running the app directly through Python

#app = FastAPI()                                   
#static_files = StaticFiles(directory='public')    
#views = Jinja2Templates(directory="public/views")
#app.mount('/public', static_files, name='public') 
#app.mount("/imgs", StaticFiles(directory="public/imgs"), name="imgs")
#app.mount("/css", StaticFiles(directory="public/css"), name="css")
#app.mount("/js", StaticFiles(directory="public/js"), name="js")

#@app.get('/', response_class=HTMLResponse)
#def get_home(request: Request) -> HTMLResponse:
#    return HTMLResponse(content=views.get_template("home.html").render(), status_code=200)

#@app.post('/')

if __name__ == "__main__":
    total_users = {} # total users that came today, dynamically populated
    users = {} # current users in tec cafe using computers
    fake_users = [] # fake users container
    for _ in range (15):
        fake_users.append([Person.createPerson()]) ## [PID (AXXXXXXXX), Name, Time In (YYYY-MM-DD HH:M:S), Duration, Tally (severe), Tally (moderate), Tally (light)]
    
    print(fake_users)

    ## Test Algorithms
    
    #uvicorn.run("webServer:app", host="127.0.0.1", port=8007, reload=True)