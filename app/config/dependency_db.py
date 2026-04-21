from app.infrastructure.database.connection import SessionLocal

class Dependencies:
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()