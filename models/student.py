from datetime import datetime
from typing import List
from db import db


class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.now)

    transactions = db.relationship("TransactionModel",
                                   backref='transactor',
                                   lazy="dynamic")

    @classmethod
    def find_by_name(cls, name) -> "StudentModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["StudentModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
