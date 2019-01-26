from flask import request
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    body = request.get_json(force=True)
    name = body['name]
    response = {'greeting': 'Hello, ' + name + '!'}
    return jsonify(response)
