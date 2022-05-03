# Copyright 2022 the author Rodney Sostras. All rights reserved.

## Router
## Rotas url do sistemas 

from fastapi import APIRouter

from ping.router import ping_router
from graph.router import graph_router

app_router = APIRouter()

app_router.include_router(ping_router)
app_router.include_router(graph_router)
