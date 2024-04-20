from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from api.utils.database.database import db


class Brake(db.Model):
    __tablename__ = "tb_brake"
    __table_args__ = {"schema": "checklist_app"}

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    calipers_wheels_cylinders = db.Column(db.SmallInteger(), nullable=False)
    front_brake_pads_shoes = db.Column(db.SmallInteger(), nullable=False)
    rear_brake_pads_shoes = db.Column(db.SmallInteger(), nullable=False)
    rotor_drums = db.Column(db.SmallInteger(), nullable=False)
    brake_lines_hoses_fittings = db.Column(db.SmallInteger(), nullable=False)
    parking_brake = db.Column(db.SmallInteger(), nullable=False)
    master_cylinder_booster = db.Column(db.SmallInteger(), nullable=False)
    created_at = db.Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    def __repr__(self):
        return f"Brakes[
            id= {self.id},
            caliper_wheels_cylinders= {self.calipers_wheels_cylinders},
            front_brake_pads_shoes= {self.front_brake_pads_shoes},
            rear_brake_pads_shoes= {self.rear_brake_pads_shoes},
            rotor_drums= {self.rotor_drums},
            brake_lines_hoses_fittings= {self.brake_lines_hoses_fittings},
            parking_brake= {self.parking_brake},
            master_cylinder_booster = {self.master_cylinder_booster}]"

    def to_json(self):
        return {
            "id": self.id,
            "caliper_wheels_cylinders": self.calipers_wheels_cylinders,
            "front_brake_pads_shoes": self.front_brake_pads_shoes,
            "rear_brake_pads_shoes": self.rear_brake_pads_shoes,
            "rotor_droms": self.rotor_drums,
            "brake_lines_hoses_fittings": self.brake_lines_hoses_fittings,
            "parking_brake": self.parking_brake,
            "master_cylinder_booster": self.master_cylinder_booster
        }
