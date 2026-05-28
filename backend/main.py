from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pathlib import Path

from database import get_db, engine
from models import Project, ProjectBullet, Experience, ExperienceBullet, TechnicalSkill, TechnicalBullet
from schemas import TechnicalSkillRead, ProjectRead, ExperienceRead


# Establish FastAPI application object instance
app = FastAPI()


# SQLAdmin (dev only)
import os
from sqladmin import Admin, ModelView
class TechnicalSkillAdmin(ModelView, model = TechnicalSkill):
    column_list = [
        TechnicalSkill.id,
        TechnicalSkill.name
    ]
    
class TechnicalBulletAdmin(ModelView, model = TechnicalBullet):
    column_list = [
        TechnicalBullet.id,
        TechnicalBullet.skill_id,
        TechnicalBullet.text,
        TechnicalBullet.order_index
    ]

class ProjectAdmin(ModelView, model = Project):
    column_list = [
        Project.id,
        Project.name
    ]

class ProjectBulletAdmin(ModelView, model = ProjectBullet):
    column_list = [
        ProjectBullet.id,
        ProjectBullet.project_id,
        ProjectBullet.text,
        ProjectBullet.order_index
    ]

class ExperienceAdmin(ModelView, model = Experience):
    column_list = [
        Experience.id,
        Experience.role,
        Experience.company,
        Experience.start_date,
        Experience.end_date
    ]

class ExperienceBulletAdmin(ModelView, model = ExperienceBullet):
    column_list = [
        ExperienceBullet.id,
        ExperienceBullet.experience_id,
        ExperienceBullet.text,
        ExperienceBullet.order_index
    ]

if os.getenv("ENVIRONMENT") == "development":
    admin = Admin(app, engine)
    admin.add_view(TechnicalSkillAdmin)
    admin.add_view(TechnicalBulletAdmin)
    admin.add_view(ProjectAdmin)
    admin.add_view(ProjectBulletAdmin)
    admin.add_view(ExperienceAdmin)
    admin.add_view(ExperienceBulletAdmin)


# Save program root dir path to var
ROOT_DIR = Path(__file__).resolve().parent.parent


# Mount directory site files
app.mount("/static", StaticFiles(directory=str(ROOT_DIR / "frontend")), name="static")


# Webpage routing: returns static (or dynamic) webpages
@app.get("/") # decorator (@...) uses an external function (i.e. the wrapper, called by the decarator) that adds logic to function beneath
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
@app.get("/api/skills/", response_model=list[TechnicalSkillRead])
def get_skills(db:Session = Depends(get_db)):
    skills = db.query(TechnicalSkill).all()
    return skills

@app.get("/api/projects/", response_model=list[ProjectRead])
def get_projects(db:Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects

@app.get("/api/experience/", response_model=list[ExperienceRead])
def get_experience(db:Session = Depends(get_db)):
    experience = db.query(Experience).all()
    return experience