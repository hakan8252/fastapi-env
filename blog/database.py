from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker


# engine = create_engine("sqlite:///./blog.db", echo=True, connect_args={"check_same_thread": False})
engine = create_engine("mysql+pymysql://root:hitman1.@localhost:3306/blogapplication")

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a base class for your models
Base: DeclarativeMeta = declarative_base()


def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()
