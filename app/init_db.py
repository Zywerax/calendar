from app.database import Base, engine
from app.models import task  # 💡 WAŻNE: import modeli

def init_db():
    Base.metadata.create_all(bind=engine)