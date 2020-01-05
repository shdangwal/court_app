from flask_restful import Resource
from flask import request
from models.student import StudentModel
from schemas.student import StudentSchema
from models.transaction import TransactionModel

NAME_ALREADY_EXISTS = "A student with name '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the student."
STUDENT_NOT_FOUND = "Student not found."
STUDENT_DELETED = "Student deleted."

student_schema = StudentSchema()
student_list_schema = StudentSchema(many=True)


class Student(Resource):
    @classmethod
    def get(cls, name: str):
        student = StudentModel.find_by_name(name)
        if student:
            return student_schema.dump(student), 200
        return {"message": STUDENT_NOT_FOUND}, 400

    @classmethod
    def post(cls, name: str):
        if StudentModel.find_by_name(name):
            return {"message": NAME_ALREADY_EXISTS.format(name)}, 400
        
        student_json = request.get_json()
        student_json["name"] = name
        
        student = student_schema.load(student_json)
                
        try:
            student.save_to_db()
        except Exception as ex:
            return {
                "message": ERROR_INSERTING,
                "err": ex
            }, 500
        return student_schema.dump(student), 201
    
    @classmethod
    def delete(cls, name: str):
        student = StudentModel.find_by_name(name)
        if student:
            student.delete_from_db()
            return {"message": STUDENT_DELETED}, 200
        return {"message": STUDENT_NOT_FOUND}, 404


class StudentList(Resource):
    @classmethod
    def get(cls):
        return {
            "students": student_list_schema.dump(StudentModel.find_all())
        }, 200
