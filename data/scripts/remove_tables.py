from data.db import SessionLocal
from data.models.dogs import Dog

def clear_database():
    db = SessionLocal()
    try:
        db.query(Dog).delete()
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    clear_database()




