from typing import Type, TypeVar, Dict, Any, List, Optional
from services.interface_service import InterfaceService

from database.base_model import BaseModel
from database.get_connection import get_db

from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

T = TypeVar('T', bound=BaseModel)

class BaseService(InterfaceService):
    def __init__(self, model: Type[T]):
        self.model = model

    def _query_builder(self, db: Session, filters: Optional[Dict[str, Any]] = None, 
                    sort_by: Optional[str] = None, 
                    sort_order: Optional[str] = 'desc', 
                    limit: Optional[int] = None):
        query = db.query(self.model)
        
        # Apply filters
        if filters:
            for attr, value in filters.items():
                query = query.filter(getattr(self.model, attr) == value)
        
        # Apply sorting
        if sort_by:
            if sort_order == 'desc':
                query = query.order_by(desc(getattr(self.model, sort_by)))
            if sort_order == 'asc':
                query = query.order_by(asc(getattr(self.model, sort_by)))
        
        # Apply limit
        if limit:
            query = query.limit(limit)
        
        return query

    def add_item(self, item: Dict[str, Any]) -> None:
        with get_db() as db:
            db_item = self.model(**item)
            db.add(db_item)
            db.commit()
            db.refresh(db_item)

    def get_item(self, filters: Optional[Dict[str, Any]] = None) -> Optional[T]:
        with get_db() as db:
            query = self._query_builder(db, filters=filters)
            return query.first()

    def get_items(self, filters: Optional[Dict[str, Any]] = None, 
                  sort_by: Optional[str] = None, 
                  sort_order: Optional[str] = 'asc', 
                  limit: Optional[int] = None) -> List[T]:
        with get_db() as db:
            query = self._query_builder(db, filters=filters, sort_by=sort_by, sort_order=sort_order, limit=limit)
            return query.all()

    def update_item(self, item_id: int, update_data: Dict[str, Any]) -> None:
        with get_db() as db:
            db.query(self.model).filter_by(id=item_id).update(update_data)
            db.commit()
