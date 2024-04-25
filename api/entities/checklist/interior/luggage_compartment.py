from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class LuggageCompartment(db.Model):
    __tablename__ = "tb_luggage_compartment"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    luggage_carpet = db.Column(db.SmallInteger(), nullable=False)
    luggage_trim = db.Column(db.SmallInteger(), nullable=False)
    luggage_light = db.Column(db.SmallInteger(), nullable=False)
    jack_tool_kit = db.Column(db.SmallInteger(), nullable=False)
    spare_tire_inspection = db.Column(db.SmallInteger(), nullable=False)
    spare_tire_airpressure = db.Column(db.SmallInteger(), nullable=False)
    tire_inflator_kit = db.Column(db.SmallInteger(), nullable=False)
    emergency_trunk_lid = db.Column(db.SmallInteger(), nullable=False)
    create_at = db.Column(TIMESTAMP(timezone=True),
                          nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Luggage Compartment [id={self.id},
                                        luggage_carpet={self.luggage_carpet},
                                        luggage_trim={self.luggage_trim},
                                        luggage_light={self.luggage_light},
                                        jack_tool_kit={self.jack_tool_kit},
                                        spare_tire_inspection={self.spare_tire_inspection},
                                        spare_tire_airpressure={self.spare_tire_airpressure},
                                        tire_inflator_kit={self.tire_inflator_kit},
                                        emergency_trunk_lid={self.emergency_trunk_lid}]"""

    def to_json(self):
        return {
            "id": self.id,
            "luggage_carpet": self.luggage_carpet,
            "luggage_trim": self.luggage_trim,
            "luggage_light": self.luggage_light,
            "jack_tool_kit": self.jack_tool_kit,
            "spare_tire_inspection": self.spare_tire_inspection,
            "spare_tire_airpressure": self.spare_tire_airpressure,
            "tire_inflator_kit": self.tire_inflator_kit,
            "emergency_trunk_lid": self.emergency_trunk_lid
        }
