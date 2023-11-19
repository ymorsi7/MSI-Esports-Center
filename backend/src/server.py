# Necessary Imports
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse        
from fastapi.staticfiles import StaticFiles      
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
import random
from datetime import time
import threading
import uvicorn      # Used for running the app directly through Python

app = FastAPI()                                   
static_files = StaticFiles(directory='public')    
views = Jinja2Templates(directory="public/views")
app.mount('/public', static_files, name='public') 
app.mount("/imgs", StaticFiles(directory="public/imgs"), name="imgs")
app.mount("/css", StaticFiles(directory="public/css"), name="css")
app.mount("/js", StaticFiles(directory="public/js"), name="js")

@app.get('/', response_class=HTMLResponse)
def get_home(request: Request) -> HTMLResponse:
    return HTMLResponse(content=views.get_template("home.html").render(), status_code=200)

if __name__ == "__main__":
    uvicorn.run("webServer:app", host="127.0.0.1", port=8007, reload=True)