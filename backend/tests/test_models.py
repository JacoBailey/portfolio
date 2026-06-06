import os, pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from app.models import Project, ProjectBullet, Experience, ExperienceBullet, TechnicalSkill, TechnicalBullet

DATABASE_URL = os.getenv("TEST_DATABASE_URL")

engine = create_engine(DATABASE_URL)

TestingSessionLocal = sessionmaker(
    bind=engine, # Use this connection for db session
    autoflush=False, # Do not automatically push changes before queries
    autocommit=False # Do not automatically commit transactions, must be manual
)



# Bullet order index tests

def test_project_bullet_order_index_constraint():
    session = TestingSessionLocal()

    try:
        # Create data for project table and commit
        project = Project(name = "test", description="Test project")
        session.add(project)
        session.commit()
        session.refresh(project)
    
        # Create 1/2 bullet table data and commit
        bullet1 = ProjectBullet(
            project_id=project.id,
            text = "first",
            order_index = 1
        )
        session.add(bullet1)
        session.commit()

        # Create 2/2 bullet table data (with order index error)
        bullet2 = ProjectBullet(
            project_id=project.id,
            text = "second",
            order_index = 1
        )
        session.add(bullet2)

        # Check for exception raise upon commit
        with pytest.raises(IntegrityError):
            session.commit()

    # Rollback all data insertions and close table
    finally:
        session.rollback()
        session.close()

def test_experience_bullet_order_index_constraint():
    session = TestingSessionLocal()

    try:
       # Create data for project table and commit
        experience = Experience(
            role = "Role",
            company="Company Name",
            start_date="Start Date",
            end_date="End Date"
            )
        session.add(experience)
        session.commit()
        session.refresh(experience)
    
        # Create 1/2 bullet table data and commit
        bullet1 = ExperienceBullet(
            experience_id=experience.id,
            text = "first",
            order_index = 1
        )
        session.add(bullet1)
        session.commit()

        # Create 2/2 bullet table data (with order index error)
        bullet2 = ExperienceBullet(
            experience_id=experience.id,
            text = "second",
            order_index = 1
        )
        session.add(bullet2)

        # Check for exception raise upon commit
        with pytest.raises(IntegrityError):
            session.commit()

    # Rollback all data insertions and close table
    finally:
        session.rollback()
        session.close()

def test_technical_bullet_order_index_constraint():
    session = TestingSessionLocal()

    try:
        # Create data for project table and commit
        skill = TechnicalSkill(name="test")
        session.add(skill)
        session.commit()
        session.refresh(skill)
    
        # Create 1/2 bullet table data and commit
        bullet1 = TechnicalBullet(
            skill_id=skill.id,
            text = "first",
            order_index = 1
        )
        session.add(bullet1)
        session.commit()

        # Create 2/2 bullet table data (with order index error)
        bullet2 = TechnicalBullet(
            skill_id=skill.id,
            text = "second",
            order_index = 1
        )
        session.add(bullet2)

        # Check for exception raise upon commit
        with pytest.raises(IntegrityError):
            session.commit()

    # Rollback all data insertions and close table
    finally:
        session.rollback()
        session.close()



# Cascade test (ensure child data entries are deleted when parents are deleted)

def test_project_bullet_cascade_delete():
    session = TestingSessionLocal()

    try:
        # Create data for project table and commit
        project = Project(
            name="test",
            description="test")
        session.add(project)
        session.commit()
        session.refresh(project)

        # Create bullet
        bullet = ProjectBullet(
            project_id=project.id,
            text = "first",
            order_index = 1
        )
        session.add(bullet)
        session.commit()

        # Delete parent
        session.delete(project)
        session.commit()

        # Assert number of remaining bullets is equal to 0
        remaining = session.query(ProjectBullet).filter_by(project_id=project.id).all()
        assert len(remaining) == 0
    
    # Rollback all data insertions and close table
    finally:
        session.rollback()
        session.close()

def test_experience_bullet_cascade_delete():
    session = TestingSessionLocal()

    try:
        # Create data for project table and commit
        experience = Experience(
            role="test",
            company="test",
            start_date="start",
            end_date="end")
        session.add(experience)
        session.commit()
        session.refresh(experience)

        # Create bullet
        bullet = ExperienceBullet(
            experience_id=experience.id,
            text = "first",
            order_index = 1
        )
        session.add(bullet)
        session.commit()

        # Delete parent
        session.delete(experience)
        session.commit()

        # Assert number of remaining bullets is equal to 0
        remaining = session.query(ExperienceBullet).filter_by(experience_id=experience.id).all()
        assert len(remaining) == 0
    
    # Rollback all data insertions and close table
    finally:
        session.rollback()
        session.close()

def test_skill_bullet_cascade_delete():
    session = TestingSessionLocal()

    try:
        # Create data for project table and commit
        skill = TechnicalSkill(
            name="test"
        )
        session.add(skill)
        session.commit()
        session.refresh(skill)

        # Create bullet
        bullet = TechnicalBullet(
            skill_id=skill.id,
            text = "first",
            order_index = 1
        )
        session.add(bullet)
        session.commit()

        # Delete parent
        session.delete(skill)
        session.commit()

        # Assert number of remaining bullets is equal to 0
        remaining = session.query(TechnicalBullet).filter_by(skill_id=skill.id).all()
        assert len(remaining) == 0
    
    # Rollback all data insertions and close table
    finally:
        session.rollback()
        session.close()



# Test bullet ordering

def test_project_bullet_ordering():
    session = TestingSessionLocal()

    try:
        # Create data for project table and commit
        project = Project(
            name="test",
            description="test"
        )
        session.add(project)
        session.commit()
        session.refresh(project)

        # Create 2 bullets and commit
        bullet1 = ProjectBullet(
            project_id=project.id,
            text = "second",
            order_index = 2
        )

        bullet2 = ProjectBullet(
            project_id=project.id,
            text = "first",
            order_index = 1
        )
       
        session.add_all([bullet1, bullet2])
        session.commit()
        session.refresh(project)

        # Validate bullets ordered correctly
        bullet_order = []
        for bullet in project.bullets:
            bullet_order.append(bullet.order_index)
        assert bullet_order == [1, 2]

    finally:
        session.rollback()
        session.close()

def test_experience_bullet_ordering():
    session = TestingSessionLocal()

    try:
        # Create data for project table and commit
        experience = Experience(
            role="test",
            company="test",
            start_date="start",
            end_date="end"
        )
        session.add(experience)
        session.commit()
        session.refresh(experience)

        # Create 2 bullets and commit
        bullet1 = ExperienceBullet(
            experience_id=experience.id,
            text = "second",
            order_index = 2
        )

        bullet2 = ExperienceBullet(
            experience_id=experience.id,
            text = "first",
            order_index = 1
        )
       
        session.add_all([bullet1, bullet2])
        session.commit()
        session.refresh(experience)

        # Validate bullets ordered correctly
        bullet_order = []
        for bullet in experience.bullets:
            bullet_order.append(bullet.order_index)
        assert bullet_order == [1, 2]

    finally:
        session.rollback()
        session.close()

def test_skill_bullet_ordering():
    session = TestingSessionLocal()

    try:
        # Create data for project table and commit
        skill = TechnicalSkill(
            name="test"
        )
        session.add(skill)
        session.commit()
        session.refresh(skill)

        # Create 2 bullets and commit
        bullet1 = TechnicalBullet(
            skill_id=skill.id,
            text = "second",
            order_index = 2
        )

        bullet2 = TechnicalBullet(
            skill_id=skill.id,
            text = "first",
            order_index = 1
        )
       
        session.add_all([bullet1, bullet2])
        session.commit()
        session.refresh(skill)

        # Validate bullets ordered correctly
        bullet_order = []
        for bullet in skill.bullets:
            bullet_order.append(bullet.order_index)
        assert bullet_order == [1, 2]

    finally:
        session.rollback()
        session.close()