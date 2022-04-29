# Copyright 2022 the author Rodney Sostras. All rights reserved.

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from graph import schema
from graph.crud import CRUDGraph
from appconfig.database import get_session
from appconfig.exception import E404Exception

graph_router = APIRouter(
    prefix='/graph',
    tags=['graph']
)

@graph_router.get('/', response_model=List[schema.Graph])
def list(
    db: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
):
    """
    Rota para lista uma quantidade de graphs
    """
    if result := CRUDGraph(db).list(skip, limit):
        return result
    
    raise E404Exception()

@graph_router.get('/{id}/', response_model=schema.Graph)
async def retrieve(
    db: Session = Depends(get_session),
    id: int = None,
):
    """
    Rota para encontrar graph especifico
    """
    if result := CRUDGraph(db).retrieve(id):
        return result

    raise E404Exception(detail=f"Graph 'ID={id}' not found.") 


@graph_router.post('/', response_model=schema.Graph, status_code=201)
async def create(
    *,
    db: Session = Depends(get_session),
    obj_in: schema.GraphCreate
):
    """
    Rota para criar um novo registro de graph
    """
    if result := CRUDGraph(db).create(obj_in):
        return result

    raise E404Exception(detail="Error") 
    