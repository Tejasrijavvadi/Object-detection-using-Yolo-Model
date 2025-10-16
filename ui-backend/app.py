from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

AI_BACKEND_URL = "http://localhost:8001/detect"

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    files = {"file": (file.filename, await file.read(), file.content_type)}
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(AI_BACKEND_URL, files=files)
    return JSONResponse(response.json())
