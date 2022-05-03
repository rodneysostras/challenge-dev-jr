# Copyright 2022 the author Rodney Sostras. All rights reserved.

## Crud base
## Possui os recursos necessarios para
## manipulação de dados no banco de dados

from typing import Any, Generic, List, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import select

from fastapi.encoders import jsonable_encoder

from appconfig.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    model = None

    def __init__(self, session: Session):
        self.session = session

    def list(self, skip: int = 0,  limit: int = 100,) -> List[ModelType]:
        """ Listar quantidade de graph informados """
        stmt = select(self.model).offset(skip).limit(limit)
        result = self.session.execute(stmt).scalars().all()

        return result

    def retrieve(self, id: Any) -> ModelType:
        """ Encontra o registro especifico """
        stmt = select(self.model).where(self.model.id == id)
        result = self.session.execute(stmt).scalars().first()

        return result

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        """ Cria um novo registro """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)

        self.session.add(db_obj)
        self.session.commit()

        return db_obj

    def update(self, id: Any, obj_in: UpdateSchemaType) -> ModelType:
        """ Atualiza um registro especifico """
        db_obj = self.retrieve(id)

        if not db_obj: return None

        update_data = obj_in.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_obj, key, value)
        
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
            
        return db_obj

    def destroy(self, id: Any) -> ModelType:
        """ Apaga um registro especifico"""
        db_obj = self.retrieve(id)

        if not db_obj: return None
        
        self.session.delete(db_obj)
        self.session.commit()
        
        return db_obj