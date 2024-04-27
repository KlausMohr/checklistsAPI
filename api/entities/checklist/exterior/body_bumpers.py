from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class BodyPanelsBumper(db.Model):
    __tablename__ = "tb_body_bumper"
    

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    flood_damage = db.Column(db.SmallInteger(), nullable=False)
    fire_damage = db.Column(db.SmallInteger(), nullable=False)
    major_damage = db.Column(db.SmallInteger(), nullable=False)
    body_panel = db.Column(db.SmallInteger(), nullable=False)
    bumper = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    
    __table_args__ = {"schema": "checklist_app"}

    def __repr__(self):
        return f"""Exterior lights [id={self.id},
                                  flood_damage={self.flood_damage},
                                  fire_damage={self.fire_damage},
                                  major_damage={self.major_damage},
                                  body_panel={self.body_panel},
                                  bumper={self.bumper}]"""

    def to_json(self):
        return {
            "id": self.id,
            "flood_damage": self.flood_damage,
            "fire_damage": self.fire_damage,
            "major_damage": self.major_damage,
            "body_panel": self.body_panel,
            "bumper": self.bumper
        }
