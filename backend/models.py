from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass



class Projects(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)

    bullets: Mapped[list["ProjectBullets"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan"      
    )

class ProjectBullets(Base):
    __tablename__ = "project_bullets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    text: Mapped[str] = mapped_column(String(150), nullable=False)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False)

    project: Mapped["Projects"] = relationship(
        back_populates="bullets"
    )



class TechnicalSkills(Base):
    __tablename__ = "technical_skills"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    bullets: Mapped[list["TechnicalBullets"]] = relationship(
        back_populates="skills",
        cascade="all, delete-orphan"      
    )

class TechnicalBullets(Base):
    __tablename__ = "technical_bullets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    skill_id: Mapped[int] = mapped_column(ForeignKey("technical_skills.id"))
    text: Mapped[str] = mapped_column(String(150), nullable=False)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False)

    skills: Mapped["TechnicalSkills"] = relationship(
        back_populates="bullets"
    )



class Experience(Base):
    __tablename__ = "experience"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role: Mapped[str] = mapped_column(String(100), nullable=False)
    company: Mapped[str] = mapped_column(String(100), nullable=False)
    # dates below are set to text so values such as "Present" may be included
    start_date: Mapped[str] = mapped_column(String(50), nullable=False)
    end_date: Mapped[str] = mapped_column(String(50), nullable=False)

    bullets: Mapped[list["ExperienceBullets"]] = relationship(
        back_populates="experience",
        cascade="all, delete-orphan"      
    )

class ExperienceBullets(Base):
    __tablename__ = "experience_bullets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    experience_id: Mapped[int] = mapped_column(ForeignKey("experience.id"))
    text: Mapped[str] = mapped_column(String(150), nullable=False)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False)

    experience: Mapped["Experience"] = relationship(
        back_populates="bullets"
    )