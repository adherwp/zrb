from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel
from core.repo.search_filter import SearchFilter
from abc import ABC, abstractmethod

Schema = TypeVar('Schema', bound=BaseModel)
SchemaData = TypeVar('SchemaData', bound=BaseModel)
SchemaResult = TypeVar('SchemaResult', bound=BaseModel)


class Model(Generic[Schema, SchemaData, SchemaResult], ABC):

    @abstractmethod
    async def get_by_id(self, id: str) -> Schema:
        pass

    @abstractmethod
    async def get_all(self) -> List[Schema]:
        pass

    @abstractmethod
    async def get(
        self, search_filter: Optional[SearchFilter] = None,
        limit: int = 100, offset: int = 0
    ) -> SchemaResult:
        pass

    @abstractmethod
    async def count(self, search_filter: Optional[SearchFilter] = None) -> int:
        pass

    @abstractmethod
    async def insert(self, data: SchemaData) -> Schema:
        pass

    @abstractmethod
    async def update(self, id: str, data: SchemaData) -> Schema:
        pass

    @abstractmethod
    async def delete(self, id: str) -> Schema:
        pass