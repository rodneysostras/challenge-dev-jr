# Copyright 2022 the author Rodney Sostras. All rights reserved.
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from appconfig.database import Base, get_session

DATABASE_URL_TEST = os.getenv('DATABASE_URL_TEST')

engine = create_engine(DATABASE_URL_TEST, pool_pre_ping=True)
testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_session():
    with testing_session_local() as session:
        yield session

def dependency_overrides(app):
    app.dependency_overrides[get_session] = override_get_session

    return app