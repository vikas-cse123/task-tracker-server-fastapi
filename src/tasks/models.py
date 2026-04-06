from sqlalchemy import Column,Integer,String,Boolean
from src.utils.db import Base

# Base is responsible for connecting my model to actual database


class TaskModel(Base):
    __tablename__ = "user_tasks"
    id = Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean,default=False)