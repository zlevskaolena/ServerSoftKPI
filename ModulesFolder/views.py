from ModulesFolder import app
from flask import jsonify

@app.route('/healthcheck')
def healthcheck():
    return jsonify(status="ok")
