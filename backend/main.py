from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pathlib import Path
from loguru import logger
from time import time
from sqladmin import Admin, ModelView
import os
from database import get_db, engine
from models import Project, ProjectBullet, Experience, ExperienceBullet, TechnicalSkill, TechnicalBullet
from schemas import TechnicalSkillRead, ProjectRead, ExperienceRead


# Establish FastAPI application object instance
app = FastAPI()
logger.info("Portfolio API started.")


# SQLAdmin Config (dev only)
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


# SQLAdmin Activation
environment = os.getenv('ENVIRONMENT')
if environment is None:
    raise EnvironmentError("No environment env variable found")
logger.info(f"Environment: {environment}")
if environment == 'development':
    try:
        admin = Admin(app, engine)
        logger.info("SQLAdmin enabled (development mode)")
        admin.add_view(TechnicalSkillAdmin)
        admin.add_view(TechnicalBulletAdmin)
        admin.add_view(ProjectAdmin)
        admin.add_view(ProjectBulletAdmin)
        admin.add_view(ExperienceAdmin)
        admin.add_view(ExperienceBulletAdmin)
    except Exception:
        logger.exception("Failed to initialize SQLAdmin")
        raise


# Save program root dir path to var
ROOT_DIR = Path(__file__).resolve().parent.parent


# Mount directory site files
app.mount("/static", StaticFiles(directory=str(ROOT_DIR / 'frontend')), name="static")
logger.info(f"Static files mounted at /static from {ROOT_DIR / 'frontend'}")


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
    start = time()
    try:
        skills = db.query(TechnicalSkill).all()
        duration = time() - start
        logger.info(f"GET /api/skills/ returned {len(skills)} rows in {duration:.4f}s")
        return skills
    except Exception:
        logger.exception("GET /api/skills/ failed")
        raise

@app.get("/api/projects/", response_model=list[ProjectRead])
def get_projects(db:Session = Depends(get_db)):
    start = time()
    try:
        projects = db.query(Project).all()
        duration = time() - start
        logger.info(f"GET /api/projects/ returned {len(projects)} rows in {duration:.4f}s")
        return projects
    except Exception:
        logger.exception("GET /api/projects/ failed")
        raise

@app.get("/api/experience/", response_model=list[ExperienceRead])
def get_experience(db:Session = Depends(get_db)):
    start = time()
    try:
        experience = db.query(Experience).all()
        duration = time() - start
        logger.info(f"GET /api/experience/ returned {len(experience)} rows in {duration:.4f}s")
        return experience
    except Exception:
        logger.exception("GET /api/experience/ failed")
        raise