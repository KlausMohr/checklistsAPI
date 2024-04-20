from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class Frame(db.Model):
    __tablename__ = "tb_frame"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    frame_damage = db.Column(db.SmallInteger(), nullable=False)
    fuel_supply_system = db.Column(db.SmallInteger(), nullable=False)

    def __repr__(self):
        return f"Frame [id={self.id}, frame_damage={self.frame_damage}, fuel_supply_system={self.fuel_supply_system}]"

    def to_json(self):
        return {
            "id": self.id,
            "frame_damage": self.frame_damage,
            "fuel_supply_system": self.fuel_supply_system,
        }
