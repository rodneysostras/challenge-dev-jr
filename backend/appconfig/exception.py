# Copyright 2022 the author Rodney Sostras. All rights reserved.

## Exception
## Utilitario de erros personalizados da aplicação

from fastapi import HTTPException, status

class ConfigException(Exception):
    pass

class E404Exception(HTTPException):
    def __init__(self, detail='Not found'):
        self.status_code=status.HTTP_404_NOT_FOUND
        self.detail = detail