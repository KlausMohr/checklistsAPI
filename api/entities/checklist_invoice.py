from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.aplication.config import db

from api.entities.vehicle_entity import Vehicle
from api.entities.checklist_entity import Checklist
from api.entities.owner_entity import Owner


class ChecklistInvoice(db.Model):
    __tablename__ = "tb_checklist_invoice"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    checklist_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_checklist.id"), nullable=False)
    vehicle_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_vehicle.id"), nullable=False)
    owner_id = db.Column(db.Integer(), db.ForeignKey(
        "checklist_app.tb_owner.id"), nullable=False)
    created_at = db.Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text("now()"))

    checklist = db.relationship(Checklist)
    vehicle = db.relationship(Vehicle)
    owner = db.relationship(Owner)

    def __repr__(self):
        return f"""Checklist Invoice [id={self.id},
                                      checklist_id={self.checklist_id},
                                      vehicle_id={self.vehicle_id},
                                      owner_id={self.owner_id}]"""

    def to_json(self):
        return {
            "id": self.id,
            "checklist_id": self.checklist_id,
            "vehicle_id": self.vehicle_id,
            "owner_id": self.owner_id
        }
