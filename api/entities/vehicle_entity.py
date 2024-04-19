from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()


class Vehicle(db.Model):
    __tablename__ = "tb_vehicle"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    make = db.Column(db.String(), nullable=False)
    model = db.Column(db.String(), nullable=False)
    year = db.Column(db.String(), nullable=False)
    color = db.Column(db.String(), nullable=False)
    vin = db.Column(db.String(), nullable=False)
    mileage = db.Column(db.String(), nullable=False)
    licenseplt = db.Column(db.String(), nullable=False)
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    __table_args__ = {"schema": "checklist_app"}

    def __repr__(self):
        return f"Vehicle [make={self.make}, model={self.model}, year={self.year}, color={self.color}, vin={self.vin}, mileage={self.mileage}, licenseplt={self.licenseplt}]"

    def to_json(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "vin": self.vin,
            "mileage": self.mileage,
            "licenseplt": self.licenseplt,
        }
