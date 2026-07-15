from sqlalchemy import *
from database import Base
from sqlalchemy.orm import relationship

class Project (Base) :
    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key= True
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable= False
    )

    title = Column(
        String,
        nullable= False
    )

    description = Column(
        String
    )

    owner = relationship(
        "User",
        back_populates= "projects"
    )

    tasks = relationship(
        "Task",
        back_populates="project"
        cascade="all, delete-orphan"
    )

    