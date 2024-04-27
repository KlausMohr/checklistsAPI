from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class CoolingSystem(db.Model):
    __tablename__ = "tb_cooling_system"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    radiator = db.Column(db.SmallInteger(), nullable=False)
    pressure_test_radiator_cap = db.Column(db.SmallInteger(), nullable=False)
    cooling_fans = db.Column(db.SmallInteger(), nullable=False)
    water_pump = db.Column(db.SmallInteger(), nullable=False)
    coolant_recovery_tank = db.Column(db.SmallInteger(), nullable=False)
    cabin_air_filter = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Cooling System [id={self.id},
                                   radiator={self.radiator},
                                   pressure_test_radiator_cap={self.pressure_test_radiator_cap},
                                   cooling_fans={self.cooling_fans},
                                   water_pump={self.water_pump},
                                   coolant_recovery_tank={self.coolant_recovery_tank},
                                   cabin_air_filter={self.cabin_air_filter}
                                   ]"""

    def to_json(self):
        return {
            "id": self.id,
            "radiator": self.id,
            "pressure_test_radiator_cap": self.pressure_test_radiator_cap,
            "cooling_fans": self.cooling_fans,
            "water_pump": self.water_pump,
            "coolant_recovery_tank": self.coolant_recovery_tank,
            "cabin_air_filter": self.cabin_air_filter
        }
