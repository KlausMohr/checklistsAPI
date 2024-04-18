from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:@dmin1234@localhost:5432/checklist_app"
    db.init_app(app)
    migrate.init_app(app, db)
    return app