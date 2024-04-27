from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class EngineElectricalSystem(db.Model):
    __tablename__ = "tb_engine_electrical_system"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    starter = db.Column(db.SmallInteger(), nullable=False)
    ignition = db.Column(db.SmallInteger(), nullable=False)
    battery = db.Column(db.SmallInteger(), nullable=False)
    alternator_output = db.Column(db.SmallInteger(), nullable=False)
    diesel_glow_plug_system = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Engine electrical system [id={self.id},
                                             starter={self.starter},
                                             ignition={self.ignition},
                                             battery={self.battery},
                                             alternator_output={self.alternator_output},
                                             diesel_glow_plug_system={self.diesel_glow_plug_system}
                                             ]"""

    def to_json(self):
        return {
            "id": self.id,
            "starter": self.starter,
            "ignition": self.ignition,
            "battery": self.battery,
            "alternator_output": self.alternator_output,
            "diesel_glow_plug_system": self.diesel_glow_plug_system
        }
