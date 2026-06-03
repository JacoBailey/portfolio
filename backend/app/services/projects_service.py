from sqlalchemy.orm import Session
from app.models import Project
from app.core.logger import logger
from time import time

def get_projects_service(db: Session):    
    start = time()
    projects = db.query(Project).all()
    duration = time() - start
    logger.info("projects fetched", extra={"rows": len(projects), "duration": round(duration, 4)})
    return projects