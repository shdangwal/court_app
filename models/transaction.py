from db import db


class TransactionModel(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    amt = db.Column(db.Integer)
    from_date = db.Column(db.DateTime)
    to_date = db.column(db.DateTime)
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student_name = db.column(db.String, db.ForeignKey('students.name'))
    stud = db.relationship('StudentModel')
    
    def __init__(self, amt, from_date, to_date):
        self.amt = amt
        self.from_date = from_date
        self. to_date = to_date
        
    def json(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'student_name': self.student_name,
            'amt': self.amt,
            'from_date': self.from_date,
            'to_date': self.to_date
        }
        
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).all()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self) 
        db.session.commit()
    