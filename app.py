from flask import Flask, jsonify
from Model import Database
from Controller import UserController

app = Flask(__name__)
session = Database.UserBase()

@app.route('/user', methods=['GET'])
def get_user_route():
    user = UserController.get_user(session.session(), 1)
    
    if user:
        return jsonify({
            'name': user.name,
            'id': user.id,
            'raw': user.raw,
            'result': user.result,
            'probability': user.probability,
            'tag': user.tag
        })
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == "__main__":
    app.run()