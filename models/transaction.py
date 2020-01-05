from typing import List
from db import db


class TransactionModel(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    amt = db.Column(db.Integer, nullable=False)
    from_date = db.Column(db.DateTime, nullable=False)
    to_date = db.Column(db.DateTime, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('students.id'),
                           nullable=False)
    student = db.relationship('StudentModel')

    @classmethod
    def find_by_amt(cls, amt) -> List["TransactionModel"]:
        return cls.query.filter_by(amt=amt).all()

    @classmethod
    def find_all(cls) -> List['TransactionModel']:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
