from ma import ma
from models.transaction import TransactionModel
from models.student import StudentModel


class TransactionSchema(ma.ModelSchema):
    class Meta:
        model = TransactionModel
        load_only = ("student",)
        dump_only = ("id",)
        include_fk = True
