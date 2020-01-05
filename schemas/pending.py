from marshmallow import Schema, fields


class PendingSchema(Schema):
    student_id = fields.Int(required=True)
    student_name = fields.String(required=True)
    valid_upto = fields.String(required=True)
    last_transaction_id = fields.String(required=True)
    last_transaction_amt = fields.Int(required=True)
