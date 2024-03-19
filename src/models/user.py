from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from conf.db_conf import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    password = Column(String)