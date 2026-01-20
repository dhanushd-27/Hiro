from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from src.db.models import user
from src.db.models import messages
from src.db.models import threads