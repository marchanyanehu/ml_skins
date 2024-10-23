from abc import ABC, abstractmethod
from typing import List, Dict, Any
from etl.base import ETLStep

class BaseTransformer(ETLStep):
    @abstractmethod
    def transform(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        pass

    async def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return self.transform(data)