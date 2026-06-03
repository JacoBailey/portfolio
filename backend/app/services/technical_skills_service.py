from sqlalchemy.orm import Session
from app.models import TechnicalSkill
from app.core.logger import logger
from time import time

def get_skills_service(db: Session):    
    start = time()
    skills = db.query(TechnicalSkill).all()
    duration = time() - start
    logger.info("skills fetched", extra={"rows": len(skills), "duration": round(duration, 4)})
    return skills