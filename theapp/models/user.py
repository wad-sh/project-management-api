from sqlalchemy import *
from database import Base
from sqlalchemy.orm import relationship

class User (Base) :
    
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
    )

    username = Column(
        String,
        index =True,
        unique = True,
        nullable=False
    )

    email = Column (
        String,
        index = True,
        unique = True,
        nullable=False
    )

    hashed_password = Column(
        String,
        nullable=False
    )

    projects = relationship(
        "Project",
        back_populates= "owner"
    )