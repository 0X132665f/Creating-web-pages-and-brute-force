from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'admin' and password == 'apple':
        return jsonify(message='Login successful'), 201
    else:
        return jsonify(message='Invalid username or password'), 401

if __name__ == '__main__':
    app.run(debug=True, port=5001)