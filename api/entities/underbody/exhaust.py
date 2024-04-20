from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db


class Exhaust(db.Model):
    __tablename__ = "tb_exhaust"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    exhaust_system_condition = db.Column(db.SmallInteger(), nullable=False)
    emissions_control = db.Column(db.SmallInteger(), nullable=False)

    def __repr__(self):
        return f"Exhaust [id={self.id}, exhaust_system={self.exhaust_system_condition}, emissions_control={self.emissions_control}]"

    def to_json(self):
        return {
            "id": self.id,
            "exhaust_system_condition": self.exhaust_system_condition,
            "emissions_control": self.emissions_control,
        }
