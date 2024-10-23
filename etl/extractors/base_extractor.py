from etl.base import ETLStep
from typing import Any, List, Dict
from abc import abstractmethod

class BaseExtractor(ETLStep):
    @abstractmethod
    async def extract(self) -> List[Dict[str, Any]]:
        pass

    async def process(self, data: Any = None) -> List[Dict[str, Any]]:
        return await self.extract()