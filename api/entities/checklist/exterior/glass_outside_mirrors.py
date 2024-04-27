from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db


class GlassOutsideMirrors(db.Model):
    __tablename__ = "tb_glass_outside_mirrors"
    

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    windshield = db.Column(db.SmallInteger(), nullable=False)
    side_glass = db.Column(db.SmallInteger(), nullable=False)
    rear_window_tail_gate = db.Column(db.SmallInteger(), nullable=False)
    wiper_blade_replacement = db.Column(db.SmallInteger(), nullable=False)
    outside_mirror = db.Column(db.SmallInteger(), nullable=False)
    outside_mirror_folding = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))
    
    __table_args__ = {"schema": "checklist_app"}

    def __repr__(self):
        return f"""Grille, Trim, Roof and Rack [id = {self.id},
                                              windshield= {self.windshield},
                                              side_glass= {self.side_glass},
                                              rear_window_tail_gate = {self.rear_window_tail_gate},
                                              wiper_blade_replacement= {self.wiper_blade_replacement},
                                              outside_mirror= {self.outside_mirror},
                                              outside_mirror_folding= {self.outside_mirror_folding}]"""

    def to_json(self):
        return {
            "id": self.id,
            "windshield": self.windshield,
            "side_glass": self.side_glass,
            "rear_window_tail_gate": self.rear_window_tail_gate,
            "wiper_blade_replacement": self.wiper_blade_replacement,
            "outside_mirror": self.outside_mirror,
            "outside_mirror_folding": self.outside_mirror_folding

        }
