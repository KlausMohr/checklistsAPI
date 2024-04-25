from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class CarpetTrimMats(db.Model):
    __tablename__ = "tb_carpet_trim_mats"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    interior_free_odor = db.Column(db.SmallInteger(), nullable=False)
    carpet = db.Column(db.SmallInteger(), nullable=False)
    floor_mats = db.Column(db.SmallInteger(), nullable=False)
    door_trim_panels = db.Column(db.SmallInteger(), nullable=False)
    headliner = db.Column(db.SmallInteger(), nullable=False)
    create_at = db.Column(TIMESTAMP(timezone=True),
                          nullable=False, server_default=text("now"))

    def __repr__(self):
        return f"""Carpet, Trim and Mats [id={self.id},
                                          interior_free_odor={self.interior_free_odor},
                                          carpet={self.carpet},
                                          floor_mats={self.floor_mats},
                                          door_trim_panels={self.door_trim_panels},
                                          headliner={self.headliner}]"""

    def to_json(self):
        return {
            "id": self.id,
            "interior_free_odor": self.interior_free_odor,
            "carpet": self.carpet,
            "floor_mats": self.floor_mats,
            "door_trim_panels": self.door_trim_panels,
            "headliner": self.headliner

        }
