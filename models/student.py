from db import db


class c(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    
    trans_id = db.Column(db.Integer, db.ForeignKey('transactions.id'))
    trans = db.relationship('TransactionModel')
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'transaction_id': self.trans_id
        }
        
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    