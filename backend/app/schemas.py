from pydantic import BaseModel, ConfigDict


# Establish base classes

class ORMBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class BulletRead(ORMBaseModel):
    id: int
    text: str
    order_index: int


# Technical Skills

class TechnicalBulletRead(BulletRead):
    pass

class TechnicalSkillRead(ORMBaseModel):
    name: str
    id: int
    bullets: list[TechnicalBulletRead]


# Projects

class ProjectBulletRead(BulletRead):
    project_id: int

class ProjectRead(ORMBaseModel):
    id: int
    name: str
    description: str
    bullets: list[ProjectBulletRead]


# Experience

class ExperienceBulletRead(BulletRead):
    experience_id: int

class ExperienceRead(ORMBaseModel):
    id: int
    role: str
    company: str
    start_date: str
    end_date: str
    bullets: list[ExperienceBulletRead]