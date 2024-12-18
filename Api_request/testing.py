from app.database import engine
from app.models import Base

# Create all tables defined in models
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
