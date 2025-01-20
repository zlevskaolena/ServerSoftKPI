from ModulesFolder import app, db
from flask import jsonify, request
from datetime import datetime

users = {}
user_id_counter = 1
categories = {}
category_id_counter = 1
records = {}
record_id_counter = 1

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





@app.route('/category', methods=['POST'])
def create_category():
    global category_id_counter
    data = request.get_json()
    category_id = category_id_counter
    categories[category_id] = {"name": data['name'], "id": category_id}
    category_id_counter += 1
    return jsonify(categories[category_id]), 201

@app.route('/category', methods=['GET'])
def get_categories():
    return jsonify(list(categories.values())), 200

@app.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    if category_id in categories:
        del categories[category_id]
        return '', 204
    return jsonify({"error": "Category not found"}), 404




@app.route('/record', methods=['POST'])
def create_record():
    global record_id_counter
    data = request.get_json()

    print(f"Received data: {data}")

    if data.get('user_id') not in users or data.get('category_id') not in categories:
        return jsonify({"error": "Invalid user_id or category_id"}), 400

    timestamp = datetime.utcnow().isoformat()

    record_id = record_id_counter
    records[record_id] = {
        "user_id": data['user_id'],
        "category_id": data['category_id'],
        "amount": data['amount'],
        "timestamp": timestamp,
        "id": record_id
    }
    record_id_counter += 1
    return jsonify(records[record_id]), 201

@app.route('/record', methods=['GET'])
def get_records():
    filtered_records = list(records.values())
    return jsonify(filtered_records), 200

@app.route('/record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    if record_id in records:
        del records[record_id]
        return '', 204
    return jsonify({"error": "Record not found"}), 404

@app.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = records.get(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404
    return jsonify(record), 200



@app.errorhandler(404)
def not_found(error):
    return {"message": "Resource not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return {"message": "Internal server error"}, 500


