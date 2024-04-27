from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db

from api.entities.checklist.diagnosis_entity import Diagnosis
from api.entities.checklist.underhood_entity import Underhood
from api.entities.checklist.underbody_entity import Underbody
from api.entities.checklist.exterior_entity import Exterior
from api.entities.checklist.interior_entity import Interior
from api.entities.checklist.hybrid_entity import Hybrid
from api.entities.checklist.roadtest_enitity import RoadTest


class Checklist(db.Model):
    __tablename__ = "tb_checklist"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    diagnostic_id = db.Column(
        db.Integer(), db.ForeignKey("checklist_app.tb_diagnostic.id", ondelete="CASCADE")
    )
    underhood_id = db.Column(
        db.Integer(), db.ForeignKey("checklist_app.tb_underhood.id", ondelete="CASCADE")
    )
    underbody_id = db.Column(
        db.Integer(), db.ForeignKey("checklist_app.tb_underbody.id", ondelete="CASCADE")
    )
    exterior_id = db.Column(
        db.Integer(), db.ForeignKey("checklist_app.tb_exterior.id", ondelete="CASCADE")
    )
    interior_id = db.Column(
        db.Integer(), db.ForeignKey("checklist_app.tb_interior.id", ondelete="CASCADE")
    )
    hybrid_id = db.Column(
        db.Integer(), db.ForeignKey("checklist_app.tb_hybrid.id", ondelete="CASCADE")
    )
    roadtest_id = db.Column(
        db.Integer(), db.ForeignKey("checklist_app.tb_roadtest.id", ondelete="CASCADE")
    )
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    diagnostic = db.relationship(Diagnosis)
    underhood = db.relationship(Underhood)
    underbody = db.relationship(Underbody)
    exterior = db.relationship(Exterior)
    interior = db.relationship(Interior)
    hybrid = db.relationship(Hybrid)
    roadtest = db.relationship(RoadTest)

    def __repr__(self):
        return f"""Checklist [id={self.id},
                            diagnostic_id={self.diagnostic_id},
                            underhood={self.underhood_id},
                            underbody={self.underbody_id},
                            exterior={self.exterior_id},
                            interior={self.interior_id},
                            hybrid={self.hybrid_id},
                            roadtest={self.roadtest_id}
                            ]"""

    def to_json(self):
        return {
            "id": self.id,
            "diagnostic_id": self.diagnostic_id,
            "underhood": self.underhood_id,
            "underbody": self.underbody_id,
            "exterior": self.exterior_id,
            "interior": self.interior_id,
            "hybrid": self.hybrid_id,
            "roadtest": self.roadtest_id
        }
