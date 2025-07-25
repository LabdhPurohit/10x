from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./robot.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Trajectory(Base):
    __tablename__ = "trajectories"
    id = Column(Integer, primary_key=True, index=True)
    x = Column(Float, index=True)
    y = Column(Float, index=True)
    timestamp = Column(String)

Base.metadata.create_all(bind=engine)
