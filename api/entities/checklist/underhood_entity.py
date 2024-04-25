from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.database.database import db

from api.entities.checklist.underhood.fluids import Fluids
from api.entities.checklist.underhood.engine import Engine
from api.entities.checklist.underhood.cooling_system import CoolingSystem
from api.entities.checklist.underhood.fuel_system import FuelSystem
from api.entities.checklist.underhood.electrical_system import ElectricalSystem


class Underhood(db.Model):
    __tablename__ = "tb_underhood"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)

    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f""""""
    
    def to_json(self):
        return{
            
        }