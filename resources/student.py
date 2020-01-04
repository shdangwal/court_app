from flask_restful import Resource, reqparse
from models.student import StudentModel


class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument()
    def get(self, name):
        student = StudentModel.find_by_name(name)
        pass

    def post(self, name):
        pass

    def put(self, name):
        pass

    def delete(self, name):
        pass


class StudentList(Resource):
    def get(self):
        pass