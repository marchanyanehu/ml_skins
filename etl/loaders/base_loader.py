from etl.base import ETLStep
from typing import Any, List, Dict
from abc import ABC, abstractmethod

class BaseLoader(ETLStep):
    @abstractmethod
    def load(self, data: List[Dict[str, Any]]) -> None:
        pass

    async def process(self, data: List[Dict[str, Any]]) -> None:
        self.load(data)