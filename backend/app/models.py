from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    
    bullets: Mapped[list["ProjectBullet"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
        order_by=lambda: ProjectBullet.order_index      
    )

class ProjectBullet(Base):
    __tablename__ = "project_bullets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    text: Mapped[str] = mapped_column(String(150), nullable=False)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False)
    
    __table_args__ = (
        UniqueConstraint(
            "project_id",
            "order_index",
            name="unique_project_bullet_order"
            ),
        )
    
    project: Mapped["Project"] = relationship(
        back_populates="bullets",
        foreign_keys=[project_id]
    )

class TechnicalSkill(Base):
    __tablename__ = "technical_skills"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    
    bullets: Mapped[list["TechnicalBullet"]] = relationship(
        back_populates="skill",
        cascade="all, delete-orphan",
        order_by=lambda: TechnicalBullet.order_index      
    )

class TechnicalBullet(Base):
    __tablename__ = "technical_bullets"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    skill_id: Mapped[int] = mapped_column(ForeignKey("technical_skills.id"))
    text: Mapped[str] = mapped_column(String(150), nullable=False)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False)
    
    __table_args__ = (
        UniqueConstraint(
            "skill_id",
            "order_index",
            name="unique_technical_bullet_order"
            ),
        )
    
    skill: Mapped["TechnicalSkill"] = relationship(
        back_populates="bullets",
        foreign_keys=[skill_id]
    )


class Experience(Base):
    __tablename__ = "experiences"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role: Mapped[str] = mapped_column(String(100), nullable=False)
    company: Mapped[str] = mapped_column(String(100), nullable=False)
    # dates below are set to text so values such as "Present" may be included
    start_date: Mapped[str] = mapped_column(String(50), nullable=False)
    end_date: Mapped[str] = mapped_column(String(50), nullable=False)
    
    bullets: Mapped[list["ExperienceBullet"]] = relationship(
        back_populates="experience",
        cascade="all, delete-orphan",
        order_by=lambda: ExperienceBullet.order_index    
    )

class ExperienceBullet(Base):
    __tablename__ = "experience_bullets"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    experience_id: Mapped[int] = mapped_column(ForeignKey("experiences.id"))
    text: Mapped[str] = mapped_column(String(150), nullable=False)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False)
    
    __table_args__ = (
        UniqueConstraint(
            "experience_id",
            "order_index",
            name="unique_experience_bullet_order"
            ),
        )
    
    experience: Mapped["Experience"] = relationship(
        back_populates="bullets",
        foreign_keys=[experience_id]
    )