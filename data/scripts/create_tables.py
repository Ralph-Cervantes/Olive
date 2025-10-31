from data.models.dogs import Dog
from data.db import Base, engine
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created.")
