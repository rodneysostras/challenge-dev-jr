# Copyright 2022 the author Rodney Sostras. All rights reserved.

from typing import List
from pydantic import BaseModel

class DataGraph(BaseModel):
    source: str
    target: str
    distance: str

class GraphBase(BaseModel):
    data: List[DataGraph]

class GraphCreate(GraphBase):
    pass

class GraphUpdate(GraphBase):
    pass

class Graph(GraphBase):
    id: int
        
    class Config:
        orm_mode = True