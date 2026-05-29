from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from loguru import logger
import os

# Save database url
DATABASE_URL = os.getenv("DATABASE_URL")

# Create ORM engine for python db connections
engine = create_engine(DATABASE_URL, echo=False)
logger.info("DB engine initialized")

# Framework for db session instance
SessionLocal = sessionmaker(
    bind=engine, # Use this connection for db session
    autoflush=False, # Do not automatically push changes before queries
    autocommit=False # Do not automatically commit transactions, must be manual
)

# Dependency function for creating & closing db session instance (for each request)
def get_db():
    db = SessionLocal()
    try:
        yield db # Pause state of func/prog until yield/request is finished
    except Exception:
        logger.exception("DB session error")
        raise
    finally:
        db.close()