from ModulesFolder import app
from flask import jsonify, request

users = {}
user_id_counter = 1

@app.route('/healthcheck')
def healthcheck():
    return jsonify(status="ok")

@app.route('/user', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.get_json()
    user_id = user_id_counter
    users[user_id] = {"name": data['name'], "id": user_id}
    user_id_counter += 1
    return jsonify(users[user_id]), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return '', 204
    return jsonify({"error": "User not found"}), 404
