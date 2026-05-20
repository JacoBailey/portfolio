from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pathlib import Path

from .database import get_db
from .models import TechnicalSkills, Projects, Experience
from .schemas import TechnicalSkillsRead, ProjectsRead, ExperienceRead



# Establish FastAPI application object instance
app = FastAPI()

# Save program root dir path to var
ROOT_DIR = Path(__file__).resolve().parent.parent

# Mount directory site files
app.mount("/static", StaticFiles(directory=str(ROOT_DIR / "frontend")), name="static")



# Webpage routing: returns static (or dynamic) webpages

# decarator (@...) uses an external function (i.e. the wrapper, called by the decarator) that adds logic to function beneath
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



# Database connection routing: returns JSON from db for each request

@app.get("/api/skills/", response_model=list[TechnicalSkillsRead])
def get_skills(db:Session = Depends(get_db)):
    skills = db.query(TechnicalSkills).all()
    return skills

@app.get("/api/projects/", response_model=list[ProjectsRead])
def get_projects(db:Session = Depends(get_db)):
    projects = db.query(Projects).all()
    return projects

@app.get("/api/experience/", response_model=list[ExperienceRead])
def get_experience(db:Session = Depends(get_db)):
    experience = db.query(Experience).all()
    return experience