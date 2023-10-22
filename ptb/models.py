import sqlalchemy as db
from sqlalchemy import orm
from sqlalchemy.orm import DeclarativeBase

from datetime import datetime


class Base(DeclarativeBase):
    created_on: orm.Mapped[datetime] = orm.mapped_column(
        db.DateTime(), server_default=db.func.now()
    )


class Person(Base):
    __tablename__ = "person"

    user_id: orm.Mapped[db.Integer] = orm.mapped_column(
        db.Integer(), primary_key=True, autoincrement=True
    )
    telegram_id: orm.Mapped[db.BigInteger] = orm.mapped_column(
        db.BigInteger(), nullable=False, unique=True
    )
    username: orm.Mapped[db.String] = orm.mapped_column(db.String(), nullable=True)
