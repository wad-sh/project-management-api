from sqlalchemy import Column,Integer,ForeignKey,String,Enum as SQLEnum
from database import Base
from sqlalchemy.orm import relationship
from enum import Enum


class Task (Base) :
    __tablename__ = "tasks"

    id = Column(
        Integer,
        primary_key= True
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable= False
    )

    title=Column(
        String,
        nullable=False
    )

    description =Column(
        String
    )

    class stts (str, Enum) :
        pending = "pending"
        in_progress = "in_progress"
        completed = "completed"

    status =Column(
        SQLEnum(stts),
        default= stts.pending,
        nullable= False
    )

    project = relationship(
        "Project",
        back_populates="tasks"
    )