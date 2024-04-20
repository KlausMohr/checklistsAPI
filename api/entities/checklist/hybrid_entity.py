from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.database.database import db


class Hybrid(db.Model):
    __tablename__ = "tb_hybrid"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    hybrid_cooling_system = db.Column(db.SmallInteger(), nullable=False)
    switchable_powertrain_mount = db.Column(db.SmallInteger(), nullable=False)
    hybrid_entertainment_information_display = db.Column(
        db.SmallInteger(), nullable=False)
    power_outlet_low_voltage = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    def __repr__(self):
        return f"""Hybrid System [id = {self.id},
                                 hybrid_cooling_system = {self.hybrid_cooling_system},
                                 switchable_powertrain_mount= {self.switchable_powertrain_mount},
                                 hybrid_entertainment_information_display= {self.hybrid_entertainment_information_display},
                                 power_outlet_low_voltage= {self.power_outlet_low_voltage}]"""

    def to_json(self):
        return {
            "id": self.id,
            "hybrid_cooling_system": self.hybrid_cooling_system,
            "switchable_powertrain_mount": self.switchable_powertrain_mount,
            "hybrid_entertainment_information_display": self.hybrid_entertainment_information_display,
            "power_outlet_low_voltage": self.power_outlet_low_voltage
        }
