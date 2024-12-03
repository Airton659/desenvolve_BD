from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:810502@localhost:3306/ze_delivery"

# Criação do engine
engine = create_engine(DATABASE_URL)

# Criação da sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base usada para definir as classes mapeadas
Base = declarative_base()

# Função que cria uma nova sessão com o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
