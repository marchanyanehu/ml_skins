from contextlib import contextmanager
from .db_singleton import db

@contextmanager
def get_db():
    session = db.get_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()