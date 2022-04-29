# Copyright 2022 the author Rodney Sostras. All rights reserved.

from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime, JSON, Integer

from appconfig.database import Base

class GraphModel(Base):
    __tablename__ = 'graph'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)