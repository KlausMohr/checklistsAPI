from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.database.database import db

from api.entities.checklist.underhood.fluids import Fluids
from api.entities.checklist.underhood.engine import Engine
from api.entities.checklist.underhood.cooling_system import CoolingSystem
from api.entities.checklist.underhood.fuel_system import FuelSystem
from api.entities.checklist.underhood.engine_electrical_system import EngineElectricalSystem


class Underhood(db.Model):
    __tablename__ = "tb_underhood"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    fluids_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_fluids.id", ondelete="CASCADE"))
    engine_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_engine.id", ondelete="CASCADE"))
    cooling_system_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_cooling_system.id", ondelete="CASCADE"))
    fuel_system_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_fuel_system.id", ondelete="CASCADE"))
    engine_electrical_system_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_engine_electrical_system.id", ondelete="CASCADE"))
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    fluids = db.relationship(Fluids)
    engine = db.relationship(Engine)
    cooling_system = db.relationship(CoolingSystem)
    fuel_system = db.relationship(FuelSystem)
    engine_electrical_system = db.relationship(EngineElectricalSystem)

    def __repr__(self):
        return f"""Underhood [id={self.id},
                              fluids_id={self.fluids_id},
                              engine_id={self.engine_id},
                              cooling_system_id={self.cooling_system_id},
                              fuel_system_id={self.fuel_system_id},
                              engine_electrical_system_id={self.engine_electrical_system_id}
                              ]"""

    def to_json(self):
        return {
            "id": self.id,
            "fluids_id": self.fluids_id,
            "engine_id": self.engine_id,
            "cooling_system_id": self.cooling_system_id,
            "fuel_system_id": self.fuel_system_id,
            "engine_electrical_system_id": self.engine_electrical_system_id
        }
