from abc import ABC, abstractmethod
from typing import Any, List, Dict

class ETLStep(ABC):
    @abstractmethod
    async def process(self, data: Any) -> Any:
        pass

class ETLPipeline(ABC):
    @abstractmethod
    async def run(self) -> None:
        pass