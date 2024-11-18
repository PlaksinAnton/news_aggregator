from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    telephone = Column(String(15))
    preferences = relationship("Preference", secondary="User_Preferences")

class Preference(Base):
    __tablename__ = 'Preference'
    id = Column(Integer, primary_key=True)
    preference = Column(String(100), unique=True, nullable=False)

class UserPreference(Base):
    __tablename__ = 'User_Preferences'
    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    preference_id = Column(Integer, ForeignKey('Preference.id'), primary_key=True)
