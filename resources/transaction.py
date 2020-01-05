from flask_restful import Resource
from flask import request
from models.transaction import TransactionModel
from schemas.transaction import TransactionSchema

ERROR_INSERTING = "An error occurred while inserting the transaction."
TRANSACTION_NOT_FOUND = "Transaction not found."
TRANSACTION_DELETED = "Item deleted."

transaction_schema = TransactionSchema()
transaction_list_schema = TransactionSchema(many=True)


class Transaction(Resource):
    @classmethod
    def get(cls, amt: int):
        transactions = TransactionModel.find_by_amt(amt)
        if transactions:
            return {
                "transactions": transaction_list_schema.dump(transactions)
            }, 200
        return {"message": TRANSACTION_NOT_FOUND}, 404

    @classmethod
    def post(cls, amt: int):
        transaction_json = request.get_json()
        transaction_json["amt"] = amt

        transaction = transaction_schema.load(transaction_json)
        try:
            transaction.save_to_db()
        except Exception as ex:
            return {
                "message": ERROR_INSERTING,
                "err": ex
            }, 500
        return transaction_schema.dump(transaction), 201

    @classmethod
    def delete(cls, amt: int):
        pass


class TransactionList(Resource):
    @classmethod
    def get(cls):
        return {
            "transactions": transaction_list_schema.dump(TransactionModel.find_all())
        }, 200
