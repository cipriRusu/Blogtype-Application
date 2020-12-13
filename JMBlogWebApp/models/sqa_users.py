from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(UUID)
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    user_created_at = Column(DateTime)
    user_modified_at = Column(DateTime)
