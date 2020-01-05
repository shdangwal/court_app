from datetime import datetime
from flask_restful import Resource
from models.student import StudentModel
from schemas.pending import PendingSchema
from flask_jwt_extended import jwt_required

pending_list_schema = PendingSchema(many=True)


class PendingFees(Resource):
    @classmethod
    @jwt_required
    def get(cls):
        students = StudentModel.query.all()
        tn = datetime.now()
        pending_fees_data = []
        for student in students:
            try:
                tt = student.transactions[-1].to_date
                if tn > tt:
                    data = {
                        "student_id": student.id,
                        "student_name": student.name,
                        "valid_upto": tt.strftime("%d-%m-%Y (%H:%M:%S)"),
                        "last_transaction_id": student.transactions[-1],
                        "last_transaction_amt": student.transactions[-1].amt
                    }
                    pending_fees_data.append(data)
            except IndexError:
                data = {
                    "student_id": student.id,
                    "student_name": student.name,
                    "valid_upto": "No transactions yet.",
                    "last_transaction_id": "No transactions yet.",
                    "last_transaction_amt": 0
                }
                pending_fees_data.append(data)
        return {
            "pending": pending_list_schema.dump(pending_fees_data)
        }, 200
