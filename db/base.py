"""
base.py

This module defines the Base class used by SQLAlchemy for the Object-Relational Mapping (ORM).

The Base class serves as a foundation for all model classes in the application, allowing SQLAlchemy to 
map objects to rows in the corresponding database tables. Each model class defined in the application 
will inherit from this Base class.

This declarative base setup is a core part of SQLAlchemy's ORM capabilities, enabling a more Pythonic 
definition of models and their corresponding database schema.
"""

from sqlalchemy.ext.declarative import declarative_base

# Base class for all models to extend
# This class stores a catalog of classes in the Declarative system
Base = declarative_base()