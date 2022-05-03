# Copyright 2022 the author Rodney Sostras. All rights reserved.

from typing import List
from urllib import response
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from graph import schema
from graph.crud import CRUDGraph
from appconfig.database import get_session
from appconfig.exception import E404Exception
from appconfig.utlis.graph import Graph

graph_router = APIRouter(tags=['graph'])

@graph_router.get('/graph', response_model=List[schema.Graph])
def list(
    db: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
):
    """ Lista graphs """
    if result := CRUDGraph(db).list(skip, limit):
        return result
    
    raise E404Exception()

@graph_router.get('/graph/{graphId}', response_model=schema.Graph)
async def retrieve(
    db: Session = Depends(get_session),
    graphId: int = None,
):
    """ Encontrar graph especifico """
    if result := CRUDGraph(db).retrieve(graphId):
        return result

    raise E404Exception(detail=f"Graph 'ID={graphId}' not found.") 


@graph_router.post('/graph', response_model=schema.Graph, status_code=201)
async def create(
    *,
    db: Session = Depends(get_session),
    obj_in: schema.GraphCreate
):
    """ Criar um novo registro """
    if result := CRUDGraph(db).create(obj_in):
        return result

    raise E404Exception()

@graph_router.put('/graph/{graphId}', response_model=schema.Graph)
async def update(
    *,
    db: Session = Depends(get_session),
    graphId: int = None,
    obj_in: schema.GraphCreate
):
    """ Atualiza um registro """
    if result := CRUDGraph(db).update(graphId, obj_in):
        return result

    raise E404Exception(detail=f"Graph 'ID={graphId}' not found.")  

@graph_router.delete('/graph/{graphId}', response_model=schema.Graph)
async def destroy(
    *,
    db: Session = Depends(get_session),
    graphId: int = None,
):
    """ Apaga um registro """
    if result := CRUDGraph(db).destroy(graphId):
        return result

    raise E404Exception(detail=f"Graph 'ID={graphId}' not found.")
