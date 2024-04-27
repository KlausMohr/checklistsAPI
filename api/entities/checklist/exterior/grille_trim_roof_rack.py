from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class GrilleTrimRoofRack(db.Model):
    __tablename__ = "tb_grille_trim_roof_rack"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    grille_inspection = db.Column(db.SmallInteger(), nullable=False)
    trim_inspection = db.Column(db.SmallInteger(), nullable=False)
    roof_rack_inspection = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Grille, Trim, Roof and Rack [id = {self.id},
                                              grille_inspection= {self.grille_inspection},
                                              trim_inspection= {self.trim_inspection},
                                              roof_rack_inspection = {self.roof_rack_inspection}]"""

    def to_json(self):
        return {
            "id": self.id,
            "grille_inspection": self.grille_inspection,
            "trim_inspection": self.trim_inspection,
            "roof_rack_inspection": self.roof_rack_inspection
        }
