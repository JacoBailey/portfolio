from pydantic import BaseModel


#Technical Skills

class TechnicalBulletRead(BaseModel):
    id: int
    text: str
    order_index: int

    class Config:
        from_attributes = True

class TechnicalSkillRead(BaseModel):
    name: str
    id: int
    bullets: list[TechnicalBulletRead]

    class Config:
        from_attributes = True


# Projects

class ProjectBulletRead(BaseModel):
    id: int
    project_id: int
    text: str
    order_index: int

    class Config:
        from_attributes = True

class ProjectRead(BaseModel):
    id: int
    name: str
    description: str
    bullets: list[ProjectBulletRead]

    class Config:
        from_attributes = True


# Experience

class ExperienceBulletRead(BaseModel):
    id: int
    experience_id: int
    text: str
    order_index: int

    class Config:
        from_attributes = True

class ExperienceRead(BaseModel):
    id: int
    role: str
    company: str
    start_date: str
    end_date: str
    bullets: list[ExperienceBulletRead]

    class Config:
        from_attributes = True