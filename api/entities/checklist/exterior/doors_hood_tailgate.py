from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class DoorsHoodTailgate(db.Model):
    __tablename__ = "tb_doors_hood_tailgate"
    

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    doors_alignmet = db.Column(db.SmallInteger(), nullable=False)
    doors_hinges = db.Column(db.SmallInteger(), nullable=False)
    roof_inspection = db.Column(db.SmallInteger(), nullable=False)
    hood_alignment = db.Column(db.SmallInteger(), nullable=False)
    hood_release = db.Column(db.SmallInteger(), nullable=False)
    hood_hinges = db.Column(db.SmallInteger(), nullable=False)
    hood_gass_struts = db.Column(db.SmallInteger(), nullable=False)
    tailgate_alignment = db.Column(db.SmallInteger(), nullable=False)
    trunk_gass_struts = db.Column(db.SmallInteger(), nullable=False)
    power_lift_gate_operation = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    __table_args__ = {"schema": "checklist_app"}


    def __repr__(self):
        return f"""Exterior lights [id = {self.id},
                                  doors_alignmet = {self.doors_alignmet},
                                  doors_hinges= {self.doors_hinges},
                                  roof_inspection = {self.roof_inspection},
                                  hood_alignment = {self.hood_alignment},
                                  hood_release = {self.hood_release},
                                  hood_hinges = {self.hood_hinges},
                                  hood_gass_struts= {self.hood_gass_struts},
                                  tailgate_alignment = {self.tailgate_alignment},
                                  trunk_gass_struts = {self.trunk_gass_struts},
                                  power_lift_gate_operation = {self.power_lift_gate_operation}]"""

    def to_json(self):
        return {
            "id": self.id,
            "doors_alignmet": self.doors_alignmet,
            "doors_hinges": self.doors_hinges,
            "roof_inspection": self.roof_inspection,
            "hood_alignment": self.hood_alignment,
            "hood_release": self.hood_release,
            "hood_hinges": self.hood_hinges,
            "hood_gass_struts": self.hood_gass_struts,
            "tailgate_alignment": self.tailgate_alignment,
            "trunk_gass_struts": self.trunk_gass_struts,
            "power_lift_gate_operation": self.power_lift_gate_operation,
        }
