from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class ExteriorLights(db.Model):
    __tablename__ = "tb_exterior_lights"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    front_end_lights = db.Column(db.SmallInteger(), nullable=False)
    back_end_lights = db.Column(db.SmallInteger(), nullable=False)
    side_exterior_lights = db.Column(db.SmallInteger(), nullable=False)
    hazard_lights = db.Column(db.SmallInteger(), nullable=False)
    auto_on_off_lightning = db.Column(db.SmallInteger(), nullable=False)
    trailer_lamp_connector = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    def __repr__(self):
        return f"""Exterior lights [id= {self.id}, front_end_lights = {self.front_end_lights},
                                  back_end_lights = {self.back_end_lights},
                                  side_exterior_lights= {self.side_exterior_lights},
                                  hazard_lights= {self.hazard_lights},
                                  auto_on_off_lightning= {self.auto_on_off_lightning},
                                  trailer_lamp_connector= {self.trailer_lamp_connector}]"""

    def to_json(self):
        return {
            "id": self.id,
            "front_end_lights": self.front_end_lights,
            "back_end_lights": self.back_end_lights,
            "side_exterior_lights": self.side_exterior_lights,
            "hazard_lights": self.hazard_lights,
            "auto_on_off_lightning": self.auto_on_off_lightning,
            "trailer_lamp_connector": self.trailer_lamp_connector
        }
