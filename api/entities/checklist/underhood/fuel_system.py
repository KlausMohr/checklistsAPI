from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class FuelSystem(db.Model):
    __tablename__ = "tb_fuel_system"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    fuel_pump_noise = db.Column(db.SmallInteger(), nullable=False)
    fuel_pump_pressure = db.Column(db.SmallInteger(), nullable=False)
    fuel_filter = db.Column(db.SmallInteger(), nullable=False)
    engine_air_filter = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Fuel System [id={self.id},
                                fuel_pump_noise={self.fuel_pump_noise},
                                fuel_pump_pressure={self.fuel_pump_pressure},
                                fuel_filter={self.fuel_filter},
                                engine_air_filter={self.engine_air_filter}
                                ]"""

    def to_json(self):
        return {
            "id": self.id,
            "fuel_pump_noise": self.fuel_pump_noise,
            "fuel_pump_pressure": self.fuel_pump_pressure,
            "fuel_filter": self.fuel_filter,
            "engine_air_filter": self.engine_air_filter
        }
