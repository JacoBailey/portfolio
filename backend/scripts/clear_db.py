from app.database import SessionLocal
from app.models import (
    Project,
    ProjectBullet,
    TechnicalSkill,
    TechnicalBullet,
    Experience,
    ExperienceBullet,
)

db = SessionLocal()

def clear_projects():
    db.query(ProjectBullet).delete()
    db.query(Project).delete()

def clear_technical_skills():
    db.query(TechnicalBullet).delete()
    db.query(TechnicalSkill).delete()

def clear_experiences():
    db.query(ExperienceBullet).delete()
    db.query(Experience).delete()

if __name__ == "__main__":
    clear_projects()
    clear_technical_skills()
    clear_experiences()

    db.commit()
    db.close()