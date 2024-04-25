from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.database.database import db


class Engine(db.Model):
    __tablename__ = "tb_engine"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    fluid_leaks = db.Column(db.SmallInteger(), nullable=False)
    hoses_lines = db.Column(db.SmallInteger(), nullable=False)
    belts = db.Column(db.SmallInteger(), nullable=False)
    wiring = db.Column(db.SmallInteger(), nullable=False)
    water_coolant_engine_oil = db.Column(db.SmallInteger(), nullable=False)
    oil_pressure = db.Column(db.SmallInteger(), nullable=False)
    cylinder_compression = db.Column(db.SmallInteger(), nullable=False)
    timing_belts = db.Column(db.SmallInteger(), nullable=False)
    engine_mounts = db.Column(db.SmallInteger(), nullable=False)
    turbocharger = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Engine [id={self.id},
                           fluid_leaks={self.fluid_leaks},
                           hoses_lines={self.hoses_lines},
                           belts={self.belts},
                           wiring={self.wiring},
                           water_coolant_engine_oil={self.water_coolant_engine_oil},
                           oil_pressure={self.oil_pressure},
                           cylinder_compression={self.cylinder_compression},
                           timing_belts={self.timing_belts},
                           engine_mounts={self.engine_mounts},
                           turbocharger={self.turbocharger}
                           ]"""

    def to_json(self):
        return {
            "id": self.id,
            "fluid_leaks": self.fluid_leaks,
            "hoses_lines": self.hoses_lines,
            "belts": self.belts,
            "wiring": self.wiring,
            "water_coolant_engine_oil": self.water_coolant_engine_oil,
            "oil_pressure": self.oil_pressure,
            "cylinder_compression": self.cylinder_compression,
            "timing_belts": self.timing_belts,
            "engine_mounts": self.engine_mounts,
            "turbocharger": self.turbocharger

        }
