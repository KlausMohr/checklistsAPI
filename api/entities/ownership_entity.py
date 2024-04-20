from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from api.utils.database.database import db
from api.entities.owner_entity import Owner
from api.entities.vehicle_entity import Vehicle


class Ownership(db.Model):
    __tablename__ = "tb_ownership"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    owner_id = db.Column(
        db.Integer(), db.ForeignKey("checklist_app.tb_owner.id", ondelete="CASCADE")
    )
    vehicle_id = db.Column(
        db.Integer(), db.ForeignKey("checklist_app.tb_vehicle.id", ondelete="CASCADE")
    )
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    owner = db.relationship(Owner)
    vehicle = db.relationship(Vehicle)

    def __repr__(self):
        return f"Ownership [owner_id={Owner.name}, vehicle_id={Vehicle.model}]"

    def to_json(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "vehicle_id": self.vehicle_id,
        }
