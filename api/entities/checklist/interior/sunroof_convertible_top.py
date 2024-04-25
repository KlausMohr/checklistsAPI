from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class SunroofConvertibleTop(db.Model):
    __tablename__ = "tb_sunroof_convertible_top"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    sunroof = db.Column(db.SmallInteger(), nullable=False)
    convertible_top = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    def __repr__(self):
        return f"""Sunroof and Convertible Top [id={self.id},
                                                sunroof={self.sunroof},
                                                convertible_top={self.convertible_top}]"""

    def to_json(self):
        return {
            "id": self.id,
            "sunroof": self.sunroof,
            "convertible_top": self.convertible_top
        }
