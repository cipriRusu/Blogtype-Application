from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(UUID, primary_key=True)
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    user_created_at = Column(DateTime)
    user_modified_at = Column(DateTime)
    children = relationship("Posts")
