# Copyright 2022 the author Rodney Sostras. All rights reserved.

## Database
## Recursos necessário pela conexão com banco de dados

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from appconfig.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Session:
    """ Retorna uma instância da conexão com banco de dados  """
    with session_local() as session:
        yield session

Base = declarative_base()