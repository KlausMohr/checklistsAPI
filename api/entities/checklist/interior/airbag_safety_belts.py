from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.aplication.config import db


class AirbagSafetyBelts(db.Model):
    __tablename__ = "tb_airbag_safety_belts"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    airbags = db.Column(db.SmallInteger(), nullable=False)
    safety_belts = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"Airbgas and Safety Belts [id={self.id}, airbags={self.airbags}, safety_belts={self.safety_belts}]"

    def to_json(self):
        return {
            "id": self.id,
            "airbags": self.airbags,
            "safety_belts": self.safety_belts
        }
