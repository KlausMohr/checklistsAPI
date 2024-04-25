from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class Seats(db.Model):
    __tablename__ = "tb_seats"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    upholstery = db.Column(db.SmallInteger(), nullable=False)
    seat_head_restraint = db.Column(db.SmallInteger(), nullable=False)
    folding_seats = db.Column(db.SmallInteger(), nullable=False)
    heated_seats = db.Column(db.SmallInteger(), nullable=False)
    cooled_seats = db.Column(db.SmallInteger(), nullable=False)
    integrated_child_safety = db.Column(db.SmallInteger(), nullable=False)
    create_at = db.Column(TIMESTAMP(timezone=True),
                          nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Seats [id={self.id},
                          upholstery={self.upholstery},
                          folding_seats={self.folding_seats},
                          heated_seats={self.heated_seats},
                          cooled_seats={self.cooled_seats},
                          integrated_child_safety={self.integrated_child_safety}]"""

    def to_json(self):
        return {
            "id": self.id,
            "upholstery": self.upholstery,
            "seat_head_restraint": self.seat_head_restraint,
            "folding_seats": self.folding_seats,
            "heated_seats": self.heated_seats,
            "cooled_seats": self.cooled_seats,
            "integrated_child_safety": self.integrated_child_safety
        }
