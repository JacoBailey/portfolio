from sqlalchemy.orm import Session
from app.models import Experience
from app.core.logger import logger
from time import time

def get_experiences_service(db: Session):    
    start = time()
    experiences = db.query(Experience).all()
    duration = time() - start
    logger.info("experiences fetched", extra={"rows": len(experiences), "duration": round(duration, 4)})
    return experiences