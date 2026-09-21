# Defins how rows and columns are structured inside the SQLite tasks.db table

from sqlalchemy.orm import Mapped,mapped_column
from database import Base

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(index=True)
    completed: Mapped[bool] = mapped_column(default=False)
