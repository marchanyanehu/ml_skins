from abc import ABC, abstractmethod
from typing import Type, TypeVar, Dict, Any, List

T = TypeVar('T')

class InterfaceService(ABC):
    @abstractmethod
    def __init__(self, model: Type[T]):
        pass

    @abstractmethod
    def add_item(self, item: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def get_item(self, **kwargs) -> T:
        pass

    @abstractmethod
    def get_items(self, **kwargs) -> List[T]:
        pass

    @abstractmethod
    def update_item(self, item_id: int, update_data: Dict[str, Any]) -> None:
        pass