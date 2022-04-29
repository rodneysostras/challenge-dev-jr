# Copyright 2022 the author Rodney Sostras. All rights reserved.

## Core da aplicação
## Possui a configuração necessaria para iniciar o serviço

from fastapi import FastAPI

from appconfig.router import app_router

application = FastAPI()

application.include_router(app_router, prefix="/api")