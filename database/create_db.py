from database import Base,engine
from models import Countries

print("Creating database ....")

Base.metadata.create_all(engine)