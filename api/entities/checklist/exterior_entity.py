from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db
from api.entities.checklist.exterior.body_bumpers import BodyPanelsBumper
from api.entities.checklist.exterior.doors_hood_tailgate import DoorsHoodTailgate
from api.entities.checklist.exterior.grille_trim_roof_rack import GrilleTrimRoofRack
from api.entities.checklist.exterior.glass_outside_mirrors import GlassOutsideMirrors
from api.entities.checklist.exterior.exterior_lights import ExteriorLights


class Exterior(db.Model):
    __tablename__ = "tb_exterior"

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    body_panels_bumper_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_body_bumper.id", ondelete="CASCADE"))
    doors_hood_tailgate_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_doors_hood_tailgate.id", ondelete="CASCADE"))
    grille_trim_roof_rack_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_grille_trim_roof_rack.id", ondelete="CASCADE"))
    glass_outside_mirrors_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_glass_outside_mirrors.id", ondelete="CASCADE"))
    exterior_lights_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_exterior_lights.id", ondelete="CASCADE"))
    create_at = db.Column(TIMESTAMP(timezone=True),
                          nullable=False, server_default=text("now()"))

    body_panels_bumper = db.relationship(BodyPanelsBumper)
    doors_hood_tailgate = db.relationship(DoorsHoodTailgate)
    grille_trim_roof_rack = db.relationship(GrilleTrimRoofRack)
    glass_outside_mirrors = db.relationship(GlassOutsideMirrors)
    exterior_lights = db.relationship(ExteriorLights)

    __table_args__ = {"schema": "checklist_app"}

    def __repr__(self):
        return f"""Exterior [id= {self.id},
                           body_panels_bumper_id= {self.body_panels_bumper_id},
                           doors_hood_tailgate_id= {self.doors_hood_tailgate_id},
                           grille_trim_roof_rack_id= {self.grille_trim_roof_rack_id},
                           glass_outside_mirrors_id= {self.glass_outside_mirrors_id},
                           exterior_lights_id = {self.exterior_lights_id}]"""

    def to_json(self):
        return {
            "id": self.id,
            "body_panels_bumper_id": self.body_panels_bumper_id,
            "doors_hood_tailgate_id": self.doors_hood_tailgate_id,
            "grille_trim_roof_rack_id": self.grille_trim_roof_rack_id,
            "glass_outside_mirrors_id": self.glass_outside_mirrors_id,
            "exterior_lights_id": self.exterior_lights_id

        }
