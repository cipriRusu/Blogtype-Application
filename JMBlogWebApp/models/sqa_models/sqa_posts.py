from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime, ForeignKey
from models.sqa_models.sqa_users import Base

class Posts(Base):
    __tablename__ = 'posts'
    posts_id = Column(UUID, primary_key=True)
    creation_date = Column(DateTime)
    edit_date = Column(DateTime)
    author = Column(String, ForeignKey('users.user_name'))
    title = Column(String)
    post_content = Column(String)
    parent = relationship("Users", back_populates='children')
