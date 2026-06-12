from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import (
    IntegrityError,
    OperationalError,
    SQLAlchemyError,)
from pathlib import Path
from sqladmin import Admin, ModelView
import os
from app.core.logger import logger
from app.database import get_db, engine
from app.models import Project, ProjectBullet, Experience, ExperienceBullet, TechnicalSkill, TechnicalBullet
from app.schemas import TechnicalSkillRead, ProjectRead, ExperienceRead
from app.services.technical_skills_service import get_skills_service
from app.services.experiences_service import get_experiences_service
from app.services.projects_service import get_projects_service

# Save program root dir path to var
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

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


# Global exception handlers
@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    logger.exception(f"Database integrity error at {request.url.path}")
    return JSONResponse(status_code=409, content={"detail": "constraint violation"})

@app.exception_handler(OperationalError)
async def operational_error_handler(request: Request, exc: OperationalError):
    logger.exception(f"Database unavailable at {request.url.path}")
    return JSONResponse(status_code=503, content={"detail": "database unavailable"})

@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
    logger.exception(f"Database error at {request.url.path}")
    return JSONResponse(status_code=500, content={"detail": "database error"})


# Mount static assets
app.mount("/assets", StaticFiles(directory=str(ROOT_DIR / 'backend/static')), name="assets")
logger.info(f"Assets mounted at /assets from {ROOT_DIR / 'backend/static'}")


# Webpage routing: returns static (or dynamic) webpages
@app.get("/") # decorator (@...) uses an external function (i.e. the wrapper, called by the decarator) that adds logic to function beneath
def homepage():
    return FileResponse(ROOT_DIR / "frontend/pages/index.html")

@app.get("/contact/")
def contact():
    return FileResponse(ROOT_DIR / "frontend/pages/contact/index.html")

@app.get("/resume/")
def resume():
    return FileResponse(ROOT_DIR / "frontend/pages/resume/index.html")

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

@app.get("/projects/shredfinder/")
def projects_shredfinder():
    return FileResponse(ROOT_DIR / "frontend/pages/projects/shredfinder/index.html")


# Database connection routing: returns JSON from db for each request
@app.get("/api/skills/", response_model=list[TechnicalSkillRead])
def get_skills(db:Session = Depends(get_db)):
    return get_skills_service(db)

@app.get("/api/projects/", response_model=list[ProjectRead])
def get_projects(db:Session = Depends(get_db)):
    return get_projects_service(db)

@app.get("/api/experience/", response_model=list[ExperienceRead])
def get_experiences(db:Session = Depends(get_db)):
   return get_experiences_service(db)