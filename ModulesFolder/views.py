from ModulesFolder import app, db
from flask import jsonify, request
from datetime import datetime
from marshmallow import ValidationError
from ModulesFolder.models import User, Category, Record
from ModulesFolder.schemas import UserSchema, CategorySchema, RecordSchema

@app.route('/healthcheck')
def healthcheck():
    return jsonify(status="ok")

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user_schema = UserSchema()
        user = user_schema.load(data)
        new_user = User(name=user['name'])
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return user_schema.jsonify(users), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user_schema = UserSchema()
    return user_schema.jsonify(user), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return '', 204

@app.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()
    try:
        category_schema = CategorySchema()
        category = category_schema.load(data)
        new_category = Category(name=category['name'])
        db.session.add(new_category)
        db.session.commit()
        return category_schema.jsonify(new_category), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@app.route('/category', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    category_schema = CategorySchema(many=True)
    return category_schema.jsonify(categories), 200

@app.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    db.session.delete(category)
    db.session.commit()
    return '', 204

@app.route('/record', methods=['POST'])
def create_record():
    data = request.get_json()
    try:
        record_schema = RecordSchema()
        record = record_schema.load(data)

        user = User.query.get(record['user_id'])
        category = Category.query.get(record['category_id'])
        if not user or not category:
            return jsonify({"error": "Invalid user_id or category_id"}), 400

        new_record = Record(
            user_id=record['user_id'],
            category_id=record['category_id'],
            amount=record['amount'],
            timestamp=datetime.utcnow()
        )
        db.session.add(new_record)
        db.session.commit()
        return record_schema.jsonify(new_record), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@app.route('/record', methods=['GET'])
def get_records():
    records = Record.query.all()
    record_schema = RecordSchema(many=True)
    return record_schema.jsonify(records), 200

@app.route('/record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    record = Record.query.get(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404
    db.session.delete(record)
    db.session.commit()
    return '', 204

@app.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = Record.query.get(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404
    record_schema = RecordSchema()
    return record_schema.jsonify(record), 200

@app.errorhandler(404)
def not_found(error):
    return {"message": "Resource not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return {"message": "Internal server error"}, 500
