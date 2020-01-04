from flask_restful import Resource, reqparse
from datetime import datetime
from models.transaction import TransactionModel


class Transaction(Resource):
    parser = reqparse.ReuestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('amt',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('from_date',
                        type=datetime.date.fromisoformat,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('to_date',
                        type=datetime.date.fromisoformat,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @classmethod
    def get_name_from_argument(cls):
        data = cls.parser.parse_args()
        name = data['name']
        return name

    def get(self):
        name = self.get_name_from_argument()
        transaction = TransactionModel.find_by_name(name)
        if transaction:
            return transaction.json()
        else:
            return {
                'message': "Transaction from user with name '{}' does not exist.".format(name)
            }, 400
                     
    def post(self):
        data = Transaction.parser.parse_args()
        trans = TransactionModel(**data)
        try:
            trans.save_to_db()
        except:
            return {'message': "An error occurred inserting the transaction."}, 500
        return trans.json(), 201

    def delete(self):
        name = self.get_name_from_argument()
        trans = TransactionModel.find_by_name(name)
        if trans:
            trans.delete_from_db()
            return {'message': "Item Deleted."}
        return {'message': 'Item not found.'}, 404


class TransactionList(Resource):
    def get(self):
        pass
