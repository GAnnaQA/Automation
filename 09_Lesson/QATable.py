from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_email = Column(String)
    subject_id = Column(Integer)

    def __str__(self):
        return f'user_id : {self.user_id}\tuser_email : {self.user_email}\tsubject_id : {self.subject_id}'
