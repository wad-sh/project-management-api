from sqlalchemy import Column,Integer,ForeignKey,String,Enum as SQLEnum
from database import Base
from sqlalchemy.orm import relationship
from enums import TaskStatus


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


    status =Column(
        SQLEnum(TaskStatus),
        default= TaskStatus.pending,
        nullable= False
    )

    project = relationship(
        "Project",
        back_populates="tasks"
    )