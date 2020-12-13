from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Posts(Base):
    __tablename__= 'posts'
    posts_id = Column(UUID)
    creation_date = Column(DateTime)
    edit_date = Column(DateTime)
    author = Column(UUID)
    title = Column(String)
    post_content = Column(String)
