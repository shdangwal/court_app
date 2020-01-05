from ma import ma
from models.student import StudentModel
from models.transaction import TransactionModel
from schemas.transaction import TransactionSchema


class StudentSchema(ma.ModelSchema):
    students = ma.Nested(TransactionSchema, many=True)

    class Meta:
        model = StudentModel
        dump_only = ("id",)
        include_fk = True
