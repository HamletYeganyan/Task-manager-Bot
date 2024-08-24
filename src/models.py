from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, TIMESTAMP
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime

class UserORM(Base):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, nullable=False)
    updated_at: Mapped[str] = mapped_column(TIMESTAMP)
    task_count: Mapped[str]
    completed_task_count: Mapped[str]
    incomplete_task_count: Mapped[str]
    last_task_created: Mapped[str] = mapped_column(TIMESTAMP)
    last_task_updated: Mapped[str] = mapped_column(TIMESTAMP)

class TaskORM(Base):
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}
    user_id: Mapped[str]
    task_id: Mapped[str] = mapped_column(primary_key=True)
    description: Mapped[str]
    deadline: Mapped[str]
    is_completed: Mapped[str]
    created_at: Mapped[str]
    updated_at: Mapped[str]