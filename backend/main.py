from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

# Establish FastAPI application object instance
app = FastAPI()

# Save program root dir path to var
ROOT_DIR = Path(__file__).resolve().parent.parent

# Mount directory site files
app.mount("/static", StaticFiles(directory=str(ROOT_DIR / "frontend")), name="static")

# Webpage routing

@app.get("/")
def homepage():
    return FileResponse(ROOT_DIR / "frontend/pages/index.html")

@app.get("/contact/")
def contact():
    return FileResponse(ROOT_DIR / "frontend/pages/contact/index.html")

@app.get("/projects/")
def projects():
    return FileResponse(ROOT_DIR / "frontend/pages/projects/index.html")

@app.get("/projects/chatgpt-automation/")
def projects_chatgptautomation():
    return FileResponse(ROOT_DIR / "frontend/pages/projects/chatgpt-automation/index.html")

@app.get("/projects/text-formatter/")
def projects_textformatter():
    return FileResponse(ROOT_DIR / "frontend/pages/projects/text-formatter/index.html")

@app.get("/projects/portfolio/")
def projects_portfolio():
    return FileResponse(ROOT_DIR / "frontend/pages/projects/portfolio/index.html")