from flask import Flask, jsonify
from flask_restful import Api

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5000, debug=True)