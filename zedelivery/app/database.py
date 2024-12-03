from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:810502@localhost:3306/ze_delivery"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    
    Base.metadata.create_all(bind=engine)

    
    with engine.connect() as conn:
        try:
            
            conn.execute(text("ALTER TABLE partners AUTO_INCREMENT = 1"))
        except Exception as e:
            print(f"Erro ao tentar alterar o auto_increment: {e}")


create_tables()
