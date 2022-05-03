# Copyright 2022 the author Rodney Sostras. All rights reserved.

from appconfig.crud import CRUDBase
from graph.model import GraphModel
from graph.schema import Graph, GraphCreate, GraphUpdate

class CRUDGraph(CRUDBase[Graph, GraphCreate, GraphUpdate]):
    model = GraphModel