from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api
from config import Config
import os
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

import ModulesFolder.views

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)