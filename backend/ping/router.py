# Copyright 2022 the author Rodney Sostras. All rights reserved.

from fastapi import APIRouter

ping_router = APIRouter(
    prefix='/ping',
    tags=['ping']
)

@ping_router.get('/')
async def pong():
    return { 'message': 'pong!!!'}