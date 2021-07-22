"""
Module contains Employee model definition
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


# pylint: disable=too-few-public-methods
class Employee(Base):
    """Employee DB Model."""
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String)
