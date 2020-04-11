from sqlalchemy import Boolean, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base, engine

# Base models:


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    pwd_hash = Column(String, nullable=False)

    notes = relationship('Note', back_populates='writer')


class Note(Base):

    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=True, default='Other')
    subject = Column(String, nullable=True, default='No Subject')
    body = Column(String(5000), nullable=False)

    writer_id = Column(Integer, ForeignKey('users.id'))
    writer = relationship('User', back_populates='notes')


# Table objects:

users_table = User.__table__
notes_table = Note.__table__
