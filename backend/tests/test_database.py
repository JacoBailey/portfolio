from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session
from app.database import get_db

def test_get_db_returns_session():
    db = next(get_db())
    try:
        assert isinstance(db, Session)
    finally:
        db.close()

def test_get_db_closes_session():
    mock_session = MagicMock()

    with patch("app.database.SessionLocal", return_value=mock_session):
        # Create db session
        gen = get_db()

        # Skip to first yeild statement
        session = next(gen)

        # Close session
        gen.close()

        # Assert statement
        mock_session.close.assert_called_once()